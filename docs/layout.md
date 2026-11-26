# Hub layout

FluSight collects forecasts of weekly influenza hospital admissions and
other optional seasonal targets. The fork retains the upstream layout.

| Location | Role |
| --- | --- |
| [`hub-config/tasks.json`](../hub-config/tasks.json) | Declared target, horizon, reference-date, location, and output-type options. |
| [`model-output/`](../model-output/README.md) | Archived forecast files organized by model identifier and reference date. |
| [Model metadata example](../model-metadata/docxology-panelqr.yml) | Identity and attribution supplied with the forecast. |
| `target-data/` | Published observed targets and reporting vintages. |
| `auxiliary-data/` | Supporting lookup data and upstream maintenance scripts. |
| `weekly-summaries/` | Retained reports organized by week. |
| `validation_result.md` | Output path used by upstream automation. |

For hospitalization quantiles, retain location codes as strings, including
leading zeroes. The reference date identifies the model's forecast round.
The target end date identifies the week whose count is predicted. The
[readback](readback.md) checks those fields for one archived group.

The [upstream season guide](upstream-season.md) explains the targets and
attribution. Use the original submission instructions for participation.
