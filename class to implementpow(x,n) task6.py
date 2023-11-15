class PowerCalculator:
    def my_pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2

        return result

# Example usage:
calculator = PowerCalculator()
result = calculator.my_pow(2, 3)
print(result)
class PowerCalculator:
    def my_pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2

        return result

# Example usage:
calculator = PowerCalculator()
result = calculator.my_pow(2, 3)
print(result)