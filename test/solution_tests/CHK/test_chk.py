from lib.solutions.CHK import checkout_solution
import pytest

class TestChk():
    def test_sum(self):
        assert checkout_solution.compute("ABBBBCD") == 245

    
        

