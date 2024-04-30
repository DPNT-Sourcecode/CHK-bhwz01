# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):

    try:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Parameter x or y is not an integer")
        if x > 100 or x < 0 or y > 100 or y < 0:
            raise  ValueError("Parameter x or y is not in the range 0-100 inclusive")
    
        return x + y

    except ValueError as err:
        print(err.args)
    except ArithmeticError as err:
        print(err.args)
    except Exception as e:
        print(e.args)

    