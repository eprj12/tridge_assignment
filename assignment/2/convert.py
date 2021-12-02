"""
Convert numbers from base 10 integers to base N strings and back again.

Sample usage:
base20 = Transformer('0123456789abcdefghij')
base20.from_decimal(1234)
'31e'
base20.to_decimal('31e')
1234
"""

'''
10진수를 n진수로 변환시키는 n transformer 구현
'''


class Transformer(object):
    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):  #
        return self._convert(i, self.decimal_digits, self.digits)  # 10진수 -> n진수

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits)) # n진수 -> 10진수

    def _convert(self, number, fromdigits, todigits): # n진수 -> m진수  # n진수 -> 10진수 -> m진수
        n, m = len(fromdigits), len(todigits)

        index_for_decimal = [fromdigits.index(d) for d in str(number)]
        decimal_digit = sum([d * (n ** idx) for idx, d in enumerate(index_for_decimal[::-1])])

        mods = []
        while decimal_digit >= m:
            mod = decimal_digit % m
            mods.append(mod)
            decimal_digit //= m
        mods.append(decimal_digit)

        base_m_digit = ''.join([todigits[mod] for mod in mods[::-1]])

        return base_m_digit



base31 = Transformer('0123456789abcdefghijklmnopqrstu')


a = base31.from_decimal(1234565787)
print(a)
print(base31.to_decimal(a))