from varSwap import swap_values

def test_passed():
    val1 = -1
    val2 = 10
    val3 = 4
    val4 = -6
    
    student_result = swap_values(val1, val2, val3, val4)
    
    # Ensure correct return type
    if ((type(student_result) is not tuple) or (len(student_result) != 4)):
        return False

    test1, test2, test3, test4 = student_result
    
    assert test1 == 10 and test2 == -1
# Test case 2
def test_passed_2():
    val1 = 9
    val2 = 0
    val3 = 13
    val4 = -5
    
    student_result = swap_values(val1, val2, val3, val4)
    
    # Ensure correct return type
    if ((type(student_result) is not tuple) or (len(student_result) != 4)):
        return False
    
    test1, test2, test3, test4 = student_result
    
    assert test1 == 0 and test2 == 9 and test3 == -5 and test4 == 13
# Test case 3
def test_passed_3():
    val1 = 11
    val2 = 11
    val3 = 11
    val4 = 11
    
    student_result = swap_values(val1, val2, val3, val4)
    
    # Ensure correct return type
    if ((type(student_result) is not tuple) or (len(student_result) != 4)):
        return False
    
    test1, test2, test3, test4 = student_result
    
    assert test1 == 11 and test2 == 11

# Test case 4
def test_passed_4():
    val1 = 3
    val2 = 8
    val3 = 2
    val4 = 4
    
    student_result = swap_values(val1, val2, val3, val4)
    
    # Ensure correct return type
    if ((type(student_result) is not tuple) or (len(student_result) != 4)):
        return False
    
    test1, test2, test3, test4 = student_result
    
    assert test1 == 8 and test2 == 3 and test3 == 4 and test4 == 2

