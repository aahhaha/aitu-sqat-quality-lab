# ClearQuestion quality engineering laboratory

**Subject:** Software Quality Assurance and Testing  
**Portfolio owner:** Aibyn Samat

This repository contains an executable demonstration, design or research artifacts, automated
checks and reproducible execution reports. It was prepared as new portfolio work in November 2026.

## Run

```sh
python -m venv .venv
# Activate .venv using your platform's normal command.
python -m pip install -r requirements-dev.txt
python -m pytest -m "not browser and not external" --alluredir=reports/allure-results
python tools/evidence.py
```

Reports: [execution record](reports/execution.json), [test output](reports/test-output.txt).
[GitHub Actions](https://github.com/aahhaha/aitu-sqat-quality-lab/actions) runs the independent Linux checks.
The report records timestamps, environment, test counts and source hashes.

## Read the portfolio

[docs/test-plan.md](docs/test-plan.md)  [docs/strategies.md](docs/strategies.md)  [docs/toolchain.md](docs/toolchain.md)

[Preparation and attribution](PROVENANCE.md). Do not publish private keys, real student records or raw interview recordings.
