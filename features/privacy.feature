Feature: Teacher-visible authorship
  Scenario: Students see a question without the author's name
    Given a classroom question from a named student
    When the public queue is requested
    Then the question is visible without the author identity

  Scenario: Teacher can see author identity
    Given a classroom question from a named student
    When the teacher queue is requested
    Then the author identity is present
