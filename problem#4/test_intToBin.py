# Import student module you would like to test.
# For example:
# from main import add
from intToBin import int_to_reverse_binary
from intToBin import string_reverse

def test_passed():
    studentResultBinary = int_to_reverse_binary(19)
    correctResultBinary = "11001"
    if studentResultBinary is None:
        return False

    studentResultReverse = string_reverse(studentResultBinary)
    correctResultReverse = "10011"
    if studentResultReverse is None:
        return False

    assert studentResultBinary == correctResultBinary and studentResultReverse == correctResultReverse
def test2_passed():    
    # Test case 2
    studentResultBinary = int_to_reverse_binary(255)
    correctResultBinary = "11111111"
    if studentResultBinary is None:
        return False

    studentResultReverse = string_reverse(studentResultBinary)
    correctResultReverse = "11111111"
    if studentResultReverse is None:
        return False

    assert studentResultBinary == correctResultBinary and studentResultReverse == correctResultReverse
    
    # Test case 3
def test3_passed(): 
    studentResultBinary = int_to_reverse_binary(122)
    correctResultBinary = "0101111"
    if studentResultBinary is None:
        return False

    studentResultReverse = string_reverse(studentResultBinary)
    correctResultReverse = "1111010"
    if studentResultReverse is None:
        return False

    assert studentResultBinary == correctResultBinary and studentResultReverse == correctResultReverse

