from romannumerals.main import convert_numeral


def test_simple_numeral():
    assert convert_numeral_simple(1) == 'I'
    assert convert_numeral_simple(2) == 'II'
    assert convert_numeral_simple(3) == 'III'

    # assert convert_numeral_simple(4) == 'IV'
    assert convert_numeral_simple(5) == 'V'
    assert convert_numeral_simple(6) == 'VI'
    assert convert_numeral_simple(7) == 'VII'
    assert convert_numeral_simple(8) == 'VIII'

    # assert convert_numeral_simple(9) == 'IX'
    assert convert_numeral_simple(10) == 'X'
    assert convert_numeral_simple(11) == 'XI'
    assert convert_numeral_simple(12) == 'XII'
    assert convert_numeral_simple(13) == 'XIII'
    # assert convert_numeral_simple(14) == 'XIV'
