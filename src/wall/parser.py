from parsimonious.grammar import Grammar

grammar = Grammar(
    r"""
    expr        = (assignment / emptyline)*

    assignment  = (symbol_asgn / other_asgn)
    symbol_asgn = !evil valueseq* value? space equal space newline
    other_asgn  = !evil valueseq* value? space equal space !evil valueseq* value? space newline

    value       = (emptyset / flipper / bucks / dotbucks / paren / set / func / let / symword / word / quoted / tickquote / backticked / number)+
    evil        = (flipper / bucks / dotbucks)
    flipper     = dot space !number value
    bucks       = forcespace dollar space value
    dotbucks    = forcespace dollar space dot space value
    twovalue    = value forcespace value
    valueseq    = value forcespace
    twovalueseq = value forcespace value forcespace
    word        = ~r"[\w&/\\!@%^&*~<>,?:;|+\-_]+"
    tickquote   = ~r"'[^ \t\r\n]+"
    symword     = ~r'#(?:[^#\\]|\\.)+#'
    quoted      = ~r'"(?:[^"\\]|\\.)*"'
    backticked  = ~r'`.*`'
    equal       = "="
    dot         = "."
    number      = (float / int)
    int         = ~"[+-]?[0-9]"
    float       = ~"[+-]?[0-9]+[.][0-9]+"
    paren       = lp space valueseq* value? space rp
    set         = ls space valueseq* value? space rs
    func        = lb space valueseq* value? space rb
    let         = letlb space valueseq* value? space rb
    emptyset    = "()"
    lp          = "("
    rp          = ")"
    letlb       = "@{"
    lb          = "{"
    rb          = "}"
    ls          = "["
    rs          = "]"
    dollar      = "$"
    allws       = ~"(?:\t|\r?\n| )"
    newline     = ~"(?:\r?\n)+"
    space       = ~"(?:\t| )*"
    forcespace  = ~"(?:\t| )+"
    emptyline   = allws+
    """
)

def parse(src):
    return grammar.parse(src)