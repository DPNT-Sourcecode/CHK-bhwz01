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

        # ensuring that we DO NOT give the free B away
        assert checkout_solution.checkout("ABBBBBBEEE") == 205

        # ensuring that we DO give the free B away
        assert checkout_solution.checkout("ABBBBBBEEE") == 205

        # # case where we have multiple pairs of Es. For every pair of E we perhaps may take away one B
        # assert checkout_solution.checkout("ABBBBBBEEEE") == 205




 


    
        


