# Forecast hub design {#sec:design}

The hub stores a model's forecast rows in a file identified by its model and
reference date. Each row includes a target, location, horizon, target end
date, output type, identifier, and value. Model metadata and observed targets
live in separate directories. The task configuration declares the allowed
identifiers and the required quantile levels for a reported group.

For the weekly hospitalization target, the forecast value is a count. A
quantile level identifies a point in the submitted distribution. Quantile
representations support comparison with later observations under an explicit
evaluation protocol [@bracher2021evaluating]. This note uses the archived
values directly.
