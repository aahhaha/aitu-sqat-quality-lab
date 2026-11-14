# Testing strategies applied to ClearQuestion

## Pyramid and ice-cream cone

Fast domain/storage tests form the base, HTTP integration and BDD scenarios occupy the middle,
and a small number of browser journeys form the top. This keeps invalid-input and concurrency
coverage broad without paying browser startup cost for every case. An inverted ice-cream cone
would place most assertions in expensive, brittle browser scripts and delay diagnosis.

## Agile testing quadrants

| Quadrant | Application |
|---|---|
| Q1 technology-facing / support team | Board boundary tests, migration and transaction tests |
| Q2 business-facing / support team | Gherkin privacy scenarios and acceptance examples |
| Q3 business-facing / critique product | Exploratory classroom workflow and accessibility review protocol |
| Q4 technology-facing / critique product | Load, privacy, injection and external browser checks |

Q3 contains a protocol rather than a fabricated completed classroom usability study.

## Honeycomb and service boundaries

The HTTP/SQLite boundary carries the important privacy and transaction behavior, so integration
checks receive substantial attention. A service-testing honeycomb emphasizes these interactions
instead of mocking every call. We still retain small unit tests for validation and state behavior.
The repository does not need microservices merely to draw a honeycomb.

## Regression, data-driven and BDD

Pytest parametrization supplies lengths, input classes and policy decisions. Concurrent integration
tests target races; before/after SQL assertions target migrations. Gherkin scenarios share the
same executable domain implementation as HTTP tests. Allure captures test steps and real browser
screenshots. Java TestNG exercises Apache MetaModel against synthetic CSV data in its actual API.
