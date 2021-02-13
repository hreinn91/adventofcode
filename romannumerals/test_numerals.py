from romannumerals.main import get_numeral


def test_simple_numeral():
    assert get_numeral(1) == 'I'
    assert get_numeral(2) == 'II'
    assert get_numeral(3) == 'III'
