import sys

class ExitOnError:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            if exc_type is AssertionError:
                print("AssertionError:", exc_value)
            else:
                print("An error occurred. Exiting...")
            sys.exit(1)

def sum(a, b):
    assert a == 10 and b == 20, "A is not equals to 10 and B is not Equals to 20"
    print(a**2, a+b, b**2)
    return a**2, a+b, b**2

# Usage
with ExitOnError():
    # Your main code here
    # For example:
    x = 1 / 1  # This will raise a ZeroDivisionError
    sum(20, 10)
