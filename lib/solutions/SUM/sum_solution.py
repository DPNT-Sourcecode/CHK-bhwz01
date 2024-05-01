# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    
    try:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Parameters x and y must both be integers.")

        if x < 0 or x > 100 or y < 0 or y > 100:
            raise ValueError("Parameters x and y need to be in the range 1")

        return x + y
    
    except ValueError as e:
        print(e.args)
        raise e
    except ArithmeticError as e:
        print(e.args)
        raise e
    except Exception as e:
        print(e.args)
        raise e





