# Test plan and execution guide

System under test: the independently runnable ClearQuestion service snapshot in app.py/index.html.
Its architecture and requirements are documented in the companion SA repository. This repository
focuses on testing the same classroom product, not on claiming a separate product implementation.

## Risks and test levels

| Risk | Design technique | Check | Expected behavior |
|---|---|---|---|
| Identity disclosure | Role partitioning | HTTP privacy test, browser public queue | Author absent publicly, present for teacher |
| Invalid question | Equivalence classes / boundaries | Empty, whitespace, non-string, lengths 1/500/501 | 400 for invalid, 201 for valid |
| Retry duplicates | State/decision table | Same and conflicting request keys | Same ID or 409 |
| Concurrent votes | Integration / concurrency | 20 repeated and 20 distinct voters | 1 repeated vote, exact distinct count |
| Bad moderation transition | State transition coverage | Hide, answer-hidden, reopen | Public exclusion, 409, restored open state |
| Injection | Negative/security | SQL metacharacters and browser HTML payload | Stored as data, no script execution |
| Schema change | Migration testing | v1 rows -> v2 -> integrity check | Text/ID preserved, new default answer |
| Slow response | Performance | tools/benchmark.py and JMeter plan | Actual measured p95 retained |

## Entry and exit criteria

Entry: Python dependencies installed, temporary database per test, no production endpoints or data.
Exit for core suite: zero failures/errors in unit/integration/BDD tests; real browser jobs and Java
data checks assessed separately. External-service tests require credentials and are not silently
counted as passed. Test reports distinguish skipped tests from executed tests.

## Defect workflow

New -> Triaged -> In progress -> Fixed -> Retested -> Closed. A rejected fix returns to In progress.
Record reproduction input, environment, expected/actual outcome, severity and linked regression test.
The privacy regression sample in bug-report.md is a test-design example, not an invented production incident.

## Run

python -m pytest -m "not browser and not external" --alluredir=reports/allure-results
python -m pytest -m browser --alluredir=reports/allure-results
python tools/benchmark.py
mvn -f java-checks/pom.xml test

CI generates Allure HTML from adapter results and uploads reports/screenshots. Browser coverage
includes Chrome and Firefox on the runner. Sauce Labs requires independent secrets and deployment.
