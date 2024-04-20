import sys

class ExitOnError:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            if issubclass(exc_type, (AssertionError, TypeError)):
                print(f"Error: {exc_value}")
            else:
                print(f"Error: {exc_value}")
            sys.exit(1)

def sum(a, b):
    assert a == 10 and b == 20, "A is not equal to 10 and B is not equal to 20"
    print(a**2, a+b, b**2)
    return a**2, a+b, b**2

# Usage
with ExitOnError():
    # Your main code here
    # For example:
    x = 1 / 0  # This will raise a ZeroDivisionError
    sum(100, 20)
