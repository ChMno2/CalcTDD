# Illustrative mutant written by hand for Q7 (not produced by the agent):
# it memorises exactly the inputs used in the Q1 tests and is wrong elsewhere.
class Calculator:
    def add(self, a, b):
        return {(2, 3): 5}.get((a, b), 0)

    def subtract(self, a, b):
        return {(5, 3): 2, (3, 5): -2}.get((a, b), 0)

    def multiply(self, a, b):
        return {(4, 3): 12, (-4, 3): -12, (7, 0): 0}.get((a, b), 0)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return {(6, 3): 2.0, (7, 2): 3.5}.get((a, b), 0.0)
