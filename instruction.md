# Task: Generate Log Report

You are given a file `access.log`.

## Goal
Create a file named `report.json` in the working directory.

## Success Criteria

1. The file `report.json` must exist.
2. It must contain valid JSON.
3. It must include:
   - `total_requests`: total number of log lines
   - `requests_per_ip`: dictionary mapping each IP → request count
4. Counts must exactly match the contents of `access.log`.
