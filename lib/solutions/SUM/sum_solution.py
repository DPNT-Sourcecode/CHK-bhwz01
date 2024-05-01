# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    
    try:
        if isinstance(x, int) or isinstance(y, int):
            raise ValueError("Parameters x and y must both be integers.")

        if x < 0 or x > 100 or y > 0 or y < 100:
            raise ValueError("Parameters x and y need to be in the range 1")

        return x + y
    
    except ValueError as e:
        print(e.args)
    except ArithmeticError as e:
        print(e.args)
    except Exception as e:
        print(e.args)




