from ...wall.parser import parse
import pytest
from parsimonious import IncompleteParseError

def test_quoted_string():
  parse('''foo = "bar"
''')

def test_ticked_string():
  parse('''foo = 'bar
''')

def test_backticked_string():
  parse('''foo = `bar ${hi} hello`
''')

def test_bad_quoted_string():
  with pytest.raises(IncompleteParseError):
    parse('''foo = "bar ${hi} hello
''')

def test_bad_backticked_string():
  with pytest.raises(IncompleteParseError):
    parse('''foo = `bar ${hi} hello
''')