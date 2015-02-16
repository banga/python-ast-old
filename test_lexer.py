import lexer
import unittest
from collections import namedtuple


ExpectedToken = namedtuple('ExpectedToken', ['type', 'value'])


class LexerTest(unittest.TestCase):
    def assertEqualTokens(self, expected, text):
        tokens = list(lexer.tokenize(text))
        self.assertEquals(len(expected), len(tokens))

        for expected_token, token in zip(expected, tokens):
            self.assertEquals(expected_token.type, token.type)
            self.assertEquals(expected_token.value, token.value)


class TypeTest(LexerTest):
    def assertOfType(self, text):
        self.assertEqualTokens([ExpectedToken(self.expected_type, text)], text)


class TestOctInteger(TypeTest):
    expected_type = 'OCTINTEGER'

    def test(self):
        self.assertOfType('0o1')
        self.assertOfType('0O1')
        self.assertOfType('001')
        self.assertOfType('001234567')
        self.assertOfType('0o1l')
        self.assertOfType('0o1L')
        self.assertOfType('00')


class TestHexInteger(TypeTest):
    expected_type = 'HEXINTEGER'

    def test(self):
        self.assertOfType('0x1')
        self.assertOfType('0x1a')
        self.assertOfType('0x1abcdef')
        self.assertOfType('0X123')
        self.assertOfType('0x1L')
        self.assertOfType('0x1l')


class TestBinInteger(TypeTest):
    expected_type = 'BININTEGER'

    def test_bin(self):
        self.assertOfType('0b1')
        self.assertOfType('0b10')
        self.assertOfType('0B10')
        self.assertOfType('0b1L')
        self.assertOfType('0b1l')


class TestDecimalInteger(TypeTest):
    expected_type = 'DECIMALINTEGER'

    def test_decimal(self):
        self.assertOfType('1')
        self.assertOfType('123456789')
        self.assertOfType('123L')
        self.assertOfType('123l')
        self.assertOfType('0')


class TestFloatNumber(TypeTest):
    expected_type = 'FLOATNUMBER'

    def test(self):
        self.assertOfType('1.')
        self.assertOfType('0.1')
        self.assertOfType('01.01')

    def test_exponent(self):
        self.assertOfType('0e0')
        self.assertOfType('1e+10')
        self.assertOfType('1e-10')
