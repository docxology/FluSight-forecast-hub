# Render the technical note

First run the [archived readback](readback.md) to produce the local numeric
evidence for the table. Rendering uses the external
[docxology/template](https://github.com/docxology/template) engine. Install
uv, Python 3.14, Pandoc with a compatible `pandoc-crossref`, and XeLaTeX
with its packages.

From the root of a committed checkout named `FluSight-forecast-hub`, use an
unused path for the Template clone:

```sh
HUB_ROOT="$(pwd -P)"
TEMPLATE_ROOT="$HUB_ROOT/../flusight-render-template"
git clone https://github.com/docxology/template.git "$TEMPLATE_ROOT"
git -C "$TEMPLATE_ROOT" switch --detach 87704feae0a4490ef7dad9c931d268e8c30273c2

cd "$TEMPLATE_ROOT"
uv sync --locked --no-dev --python 3.14
mkdir -p projects/working
ln -s "$HUB_ROOT" projects/working/FluSight-forecast-hub
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/FluSight-forecast-hub --skip-manuscript-hydration
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/FluSight-forecast-hub
```

Read `output/pdf/FluSight-forecast-hub_combined.pdf` and
`output/web/index.html` in the fork checkout. The validation and provenance
receipts are under `output/reports/`.
