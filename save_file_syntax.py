# -*- coding: utf-8 -*-
from pyparsing import *

def string_to_num(s,l,toks):
    n = toks[0]
    try:
        return int(n)
    except ValueError, ve:
        return float(n)

# Primitives
Identifier = Word(alphas+"_", alphanums+"_")
String = dblQuotedString().addParseAction(removeQuotes)
Number = Combine(Optional('-') + ( '0' | Word('123456789',nums)) +
                 Optional( '.' + Word(nums) ) +
                 Optional( Word('eE',exact=1) + Word(nums+'+-',nums)))
Number.addParseAction(string_to_num)

Date = Combine(Word(nums) + '.' +Word(nums) + '.' + Word(nums))
Yes = Literal('yes').addParseAction(lambda x: True)
No = Literal('no').addParseAction(lambda x: False)

Primitive = String | Date | Number | Yes | No | Identifier

# Little bit of text at the top of the file
Header = Identifier

# Provinces are keyed with negative ints
ProvinceKey = Combine('-' + Word(nums))

# Complex data types
Dictionary = Forward()
List = ZeroOrMore(Primitive)
CurlyList = Suppress("{") + List + Suppress("}")
CurlyDict = Suppress("{") + Dictionary + Suppress("}")

# Dictionary
Key = (Identifier | ProvinceKey | Date) + Suppress('=')
Value = CurlyDict | CurlyList | Primitive
Dictionary << dictOf(Key, Value)
Province = ProvinceKey + Suppress('=') + Dictionary

# Top level Parser
SaveFile = Header + Dictionary

