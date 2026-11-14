from pytest_bdd import scenarios,given,when,then
import pytest
from app import Board
scenarios('../features/privacy.feature')
@given('a classroom question from a named student',target_fixture='board')
def sample(tmp_path):
    b=Board(tmp_path/'bdd.db');b.submit(dict(room='R1',author='Synthetic Student',text='Explain this',request_id='bdd-request-01'));return b
@when('the public queue is requested',target_fixture='result')
def public(board):return board.listing()
@when('the teacher queue is requested',target_fixture='result')
def private(board):return board.listing(teacher=True)
@then("the question is visible without the author identity")
def no_author(result):assert result[0]['text']=='Explain this';assert 'author' not in result[0]
@then('the author identity is present')
def author(result):assert result[0]['author']=='Synthetic Student'
