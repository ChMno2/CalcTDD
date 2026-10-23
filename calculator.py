class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        self._require_nonzero(b, "divide")
        return a / b

    def modulo(self, a, b):
        self._require_nonzero(b, "take modulo")
        return a % b

    def power(self, a, b):
        if b < 0:
            self._require_nonzero(a, "raise zero to a negative power, which would divide")
        return a ** b

    @staticmethod
    def _require_nonzero(b, operation):
        if b == 0:
            raise ValueError(f"Cannot {operation} by zero")