from typing import Union

NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  result = None
  result = (12 * a + 25 * b) / (1 + a**(2**b))
  result = round(result, 2)
  return result


if __name__ == "__main__":
  assert some_expression_with_rounding(1, 2) == (31.0)
  assert some_expression_with_rounding(4, 3) == (0.0)

