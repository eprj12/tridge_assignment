# 2번

input으로 들어오는 특정 N진수를 원하는 원하는 output인 M진수로 변환하는 문제. 정확히는 그 기능을 하는 Transformer 클래스의 `_convert` 메서드를 구현하는 문제.

Transformer의 기본 클래스 변수가 10진수이므로 10진수에서 M진수로 변환하는 문제라고 생각했으나 `_convert` 메서드를 인코딩 메서드 `from_decimal`과 디코딩 메서드 `to_decimal` 2군데에서 모두 사용하고 있기 때문에 convert는 N진수 -> 10진수 -> M진수의 역할을 해야 한다.

 `from_decimal` 에서는 부득이하게 10진수 -> 10진수 -> M진수 변환과정을 거치게 된다. 예외사항으로 N진수가 10진수라면 10진수 변환과정을 생략할수도 있지만 그리 오래 걸리는 작업은 아니라서 그대로 두었다.



## class Transformer

```python
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
```



## N진수 -> 10진수

각 자리의 숫자와 fromdigits의 인덱스를 구한 뒤, 역순으로 순회하며 각 자리의 숫자와 진수 * 자리수만큼의 제곱을 곱해 모두 더해준다. 2진수에서 10진수를 만드는 과정을 생각하면 편하다.

예시의 base20에서 `31e`를 10진수로 변환하는데, 이를 예시로 20진수에서 10진수를 변환하는 과정을 보자. 

3 -> `0123456789abcdefghij` 의 3번째 인덱스

1 -> `0123456789abcdefghij` 의 1번째 인덱스

e -> `0123456789abcdefghij` 의 14번째 인덱스

```
3       1       14
*		    *		    *
20^2		20^1		20^0

-> (3*400) + (1*20) + (14*1) => 1234 
```





## 10진수 -> M진수

10진수를 M으로 더 이상 나누어지지 않을때까지 나눈 뒤, 나머지를 기준으로 진수에 해당하는 숫자를 찾아 M진수를 만든다.

10진수 1234를 20진수로 변환하는 과정을 보자.

```
    | 1234
20  ㅡㅡㅡㅡㅡ   
  	|	 61    14
20  ㅡㅡㅡㅡㅡ 
		|		3    1
20  ㅡㅡㅡㅡㅡ
						 3
```

3, 1, 14를 얻을 수 있고, 20진수의 기준이 되는 문자열 `0123456789abcdefghij` 의 3, 1, 14번째 인덱스에 해당하는 문자는 `31e`임을 알 수 있다.



20진수라고는 했지만 digits을 어떤 문자로 지칭하느냐에 따라 인코딩 / 암호화가 가능하다. 같은 Key를 가지고 인코딩과 디코딩를 하는 전형적인 암호방식이다.



