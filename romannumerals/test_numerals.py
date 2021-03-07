from romannumerals.main import convert_numeral
from romannumerals.main import is_number_mapped
from romannumerals.main import by_power_of_ten



def test_parse_number():
    assert by_power_of_ten(345667) == [300000, 40000, 5000, 600, 60, 7]

#
# def test_harder_numerals():
#     assert convert_numeral(4) == 'IV'
#     assert convert_numeral(9) == 'IX'
#     assert convert_numeral(14) == 'XIV'
#     assert convert_numeral(99) == 'XCIX'
#
#
#
#
# def test_is_number_in_number_map():
#     assert is_number_mapped(1) == True
#     assert is_number_mapped(5) == True
#     assert is_number_mapped(10) == True
#     assert is_number_mapped(2) == False
#     assert is_number_mapped(2) == False
#     assert is_number_mapped(4) == False
#
#
# def test_simple_numeral():
#     assert convert_numeral(1) == 'I'
#     assert convert_numeral(2) == 'II'
#     assert convert_numeral(3) == 'III'
#     assert convert_numeral(5) == 'V'
#     assert convert_numeral(6) == 'VI'
#     assert convert_numeral(7) == 'VII'
#     assert convert_numeral(8) == 'VIII'
#     assert convert_numeral(10) == 'X'
#     assert convert_numeral(11) == 'XI'
#     assert convert_numeral(12) == 'XII'
#     assert convert_numeral(13) == 'XIII'
#
#
#
#
