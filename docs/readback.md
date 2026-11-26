# Read an archived forecast group

Use Python 3.11 or newer from the repository root:

```sh
python3 docs/examples/read_forecast.py
```

The script reads [one public forecast file](../model-output/docxology-panelqr/2026-10-31-docxology-panelqr.csv)
and the [tracked task configuration](../hub-config/tasks.json). In a sparse
checkout, include those files and the `docs/` tree. The script reads the
first group for location code `01` and the reference week ending October 31,
2026. It checks the columns, task options, date alignment, the declared
quantile grid, and nonnegative integer counts in nondecreasing order.

The generated `output/data/archived-quantiles.json` records the checked
group and selected values. The script uses only local files and leaves the
archive untouched. It checks this group's structure and leaves full-file
validation, comparisons against observed values, and submission review
to their own processes.
