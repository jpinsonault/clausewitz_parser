from pyparsing import *

Identifier = Word(alphas+"_", alphanums+"_")

String = dblQuotedString().addParseAction(removeQuotes)

Number = Combine( Optional('-') + ( '0' | Word('123456789',nums) ) +
                    Optional( '.' + Word(nums) ) +
                    Optional( Word('eE',exact=1) + Word(nums+'+-',nums) ) )

Yes = Literal('yes').addParseAction(lambda x: True)
No = Literal('no').addParseAction(lambda x: False)

Primitive = String | Number | Yes | No

Header = Identifier

Hashes = Forward()

List = ZeroOrMore(Number | Identifier)

CurlyList = Suppress("{") + List + Suppress("}")

CurlyDict = Suppress("{") + Hashes + Suppress("}")

Key = Identifier() + Suppress('=')

Value = CurlyDict | Primitive | CurlyList

Hashes << dictOf(Key, Value)

SaveFile = Header + Hashes

def convertNumbers(s,l,toks):
    n = toks[0]
    try:
        return int(n)
    except ValueError, ve:
        return float(n)

Number.addParseAction(convertNumbers)