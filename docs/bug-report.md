# Privacy regression specification

This is an executable regression specification, not a report of an observed production incident.

ID: PRIV-01. Severity if introduced: high. Environment: isolated ClearQuestion test instance.
Reproduce: submit a synthetic named question; GET /api/questions without teacher authorization.
Expected: question text is present and the author field is absent. A teacher request to the
restricted endpoint includes the name only with a valid key. Regression checks:
test_public_response_does_not_contain_author, test_http_authorization_and_privacy, privacy.feature.
Current execution status is recorded in reports, rather than hardcoded in this specification.
