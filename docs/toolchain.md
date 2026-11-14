# Toolchain and evidence

| Area | Implementation | Execution record |
|---|---|---|
| Selenium | Chrome/Firefox WebDriver, explicit waits and screenshot attachment | browser job / Allure artifact |
| Reporting | allure-pytest adapter + Allure CLI | Allure result JSON and generated HTML |
| BDD | features/privacy.feature + pytest-bdd steps | JUnit and Allure |
| TestNG and Apache MetaModel | java-checks, pinned Maven dependencies | Java job / Surefire XML |
| Load | 100-request Python benchmark and JMeter HTTP plan | load.json and JMeter JTL |
| API | Postman v2.1 collection | Postman assertions; Python HTTP tests run locally |
| Database | SQLite migration and integrity tests | core JUnit |
| Cloud browser | Optional Sauce Labs Selenium Remote fixture | External run only when configured |

Apache MetaModel is archived; this small compatibility exercise uses its released CSV adapter
because the syllabus names it. It is not a recommendation to adopt the project in new production systems.
BrowserStack/Grid concepts are addressed by remote WebDriver configuration and the prior course
certificates; no paid-provider run is claimed without an actual provider execution record.

Source documentation: https://www.selenium.dev/documentation/ ; https://allurereport.org/docs/pytest/ ;
https://docs.pytest.org/ ; https://github.com/apache/metamodel ; https://docs.saucelabs.com/web-apps/automated-testing/selenium/ .
