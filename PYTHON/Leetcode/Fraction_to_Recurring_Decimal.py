def fractionToDecimal(numerator: int, denominator: int) -> str:
       if not numerator: return '0'
        fraction: list[str] = []
        if (numerator < 0) ^ (denominator < 0): fraction.append('-')
        dividend: int = abs(numerator)
        divisor: int = abs(denominator)
        fraction.append(str(dividend // divisor))
        remainder: int = dividend % divisor
        if not remainder: return ''.join(fraction)
        fraction.append('.')
        seen: dict[int, int] = dict()
        while remainder:
            if remainder in seen:
                fraction.insert(seen[remainder], '(')
                fraction.append(')')
                break
            else:
                seen[remainder] = len(fraction)
                remainder *= 10
                fraction.append(str(remainder // divisor))
                remainder %= divisor
        return ''.join(fraction)
