from ...wall.parser import parse
import pytest
from parsimonious import IncompleteParseError

def test_square_brackets():
  parse('''[]=[]
''')

def test_square_brackets():
  parse('''[foo]=[bar]
''')

def test_square_brackets_error():
  with pytest.raises(IncompleteParseError):
    parse('''[foo=[bar]
''')


def test_nested_square_brackets():
  parse('''foo=[bar a b [baz c [q]]]
''')