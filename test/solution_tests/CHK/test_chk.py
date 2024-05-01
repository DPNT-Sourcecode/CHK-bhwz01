from lib.solutions.CHK import checkout_solution
import pytest

class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("ABBBBBCD") == 205

        assert checkout_solution.checkout("") == 0

        assert checkout_solution.checkout("AAABBCCDD") == 245
        
        assert checkout_solution.checkout("ABcD") == -1

        assert checkout_solution.checkout(35) == -1

        assert checkout_solution.checkout(34.5) == -1


 


    
        

