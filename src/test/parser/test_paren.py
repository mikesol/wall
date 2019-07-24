from ...wall.parser import parse

def test_parentheses():
    parse('''(foo)=(bar)
''')
