from ...wall.parser import parse
from parsimonious import IncompleteParseError
import pytest

def test_raises_on_incomplete_symbol():
  with pytest.raises(IncompleteParseError):
    parse(
r'''
foo= bar
a= #a
b= b
''')

def test_raises_on_unbackslashed_symbol():
  with pytest.raises(IncompleteParseError):
    parse(
r'''
foo= bar
a= #a##
b= b
''')

def test_properly_backslashed_symbol():
  parse(
r'''
foo= bar
a= #a\##

b= b
''')