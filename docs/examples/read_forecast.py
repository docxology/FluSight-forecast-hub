"""Read one bounded group from the published forecast archive."""

import csv
import json
from datetime import date, timedelta
from decimal import Decimal
from itertools import islice
from pathlib import Path


SOURCE = Path("model-output/docxology-panelqr/2026-10-31-docxology-panelqr.csv")
TASKS = Path("hub-config/tasks.json")
FIELDS = (
    "reference_date", "target", "horizon", "target_end_date",
    "location", "output_type", "output_type_id", "value",
)
GROUP = {
    "reference_date": "2026-10-31",
    "target": "wk inc flu hosp",
    "horizon": "0",
    "target_end_date": "2026-10-31",
    "location": "01",
    "output_type": "quantile",
}
DISPLAY_QUANTILES = (Decimal("0.1"), Decimal("0.5"), Decimal("0.9"))


def read_group():
    schema = json.loads(TASKS.read_text(encoding="utf-8"))
    task = next(
        task
        for round_config in schema["rounds"]
        for task in round_config["model_tasks"]
        if GROUP["target"] in task["task_ids"]["target"]["optional"]
        and GROUP["output_type"] in task["output_type"]
    )
    for field in ("reference_date", "target", "horizon", "target_end_date", "location"):
        allowed = task["task_ids"][field]["optional"]
        value = int(GROUP[field]) if field == "horizon" else GROUP[field]
        if value not in allowed:
            raise ValueError(f"Archived group uses an undeclared {field}: {value}")

    quantile_options = task["output_type"]["quantile"]["output_type_id"]["required"]
    expected_quantiles = [Decimal(str(option)) for option in quantile_options]
    with SOURCE.open(encoding="utf-8", newline="") as archive:
        reader = csv.DictReader(archive)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError("Unexpected forecast columns")
        rows = list(islice(reader, len(expected_quantiles)))

    dates_match = date.fromisoformat(GROUP["target_end_date"]) == (
        date.fromisoformat(GROUP["reference_date"]) + timedelta(weeks=int(GROUP["horizon"]))
    )
    if not dates_match or any(any(row[field] != value for field, value in GROUP.items()) for row in rows):
        raise ValueError("The first archived group changed or has inconsistent dates")

    quantiles = [Decimal(row["output_type_id"]) for row in rows]
    counts = [int(row["value"]) for row in rows]
    if quantiles != expected_quantiles:
        raise ValueError("Archived quantiles differ from the declared grid or order")
    if counts != sorted(counts) or any(count < 0 for count in counts):
        raise ValueError("Expected nonnegative, nondecreasing admission counts")

    return dict(zip(quantiles, counts, strict=True))


def main():
    counts = read_group()
    destination = Path("output/data/archived-quantiles.json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    evidence = {
        "source": SOURCE.as_posix(),
        "schema": TASKS.as_posix(),
        "checked_rows": len(counts),
        "group": GROUP,
        "preview": [
            {"quantile": float(quantile), "forecast_count": counts[quantile]}
            for quantile in DISPLAY_QUANTILES
        ],
    }
    destination.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    main()
