#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyparsing import *

def string_to_int(s,l,toks):
    n = toks[0]
    return int(n)

def string_to_float(s,l,toks):
    n = toks[0]
    return float(n)

def make_dict(s, l, toks):
	return dict(toks)

# Primitives
# Identifier = Word(alphas + "_", alphanums + "_")
Identifier =  Regex(r"[^\"=\s{}]+")
String = dblQuotedString().addParseAction(removeQuotes)

Integer = Combine(Optional('-') + Word(nums))
Integer.addParseAction(string_to_int)

Float = Regex(r'-?\d+(\.\d*)')
Float.addParseAction(string_to_float)

Date = Combine(Word(nums) + '.' +Word(nums) + '.' + Word(nums))

# Primitive = String | Identifier | Date | Float | Integer
Primitive = (String | Identifier)

# Little bit of text at the top of the file
Header = Identifier

# Provinces are keyed with negative ints
ProvinceKey = Combine('-' + Word(nums))

# Complex data types
Dictionary = Forward()
List = ZeroOrMore(Primitive)
CurlyList = Suppress("{") + List + Suppress("}")
CurlyDict = Suppress("{") + Dictionary + Suppress("}")

# Empty Curly Braces
OptionalEmptyCurlyBraces = Optional(Suppress("{") + Suppress("}"))

Key = Identifier + Suppress('=')
Value = (CurlyDict | CurlyList | Primitive) + OptionalEmptyCurlyBraces

# Dictionary
# Key = (Identifier | ProvinceKey | Date) + Suppress('=')
# OptionalEmptyCurlyBraces is a hack to get around empty {}s in the file
Dictionary << dictOf(Key, Value)

# Top level Parser
SaveFile = Header + Dictionary
