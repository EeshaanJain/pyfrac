from pyfrac import Fraction

def test_pyfrac_negative_mixed():
    assert Fraction(41, -5).to_mixed() == "-8 1/5"
    