from lib.solutions.SUM import sum_solution
import pytest

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

        with pytest.raises(ValueError):
            sum_solution.compute(-1, 8)
        
        with pytest.raises(ValueError):
            sum_solution.compute(33, -5)

        with pytest.raises(ValueError):
            sum_solution.compute(-13, -5)

        with pytest.raises(ValueError):
            sum_solution.compute(101, 100)
        
        with pytest.raises(ValueError):
            sum_solution.compute(100, 101)
        

