"""
Name: Henry Holman
Lab Time: Thursday 2pm

"""

def int_to_reverse_binary(num1):
    
    revbinary_val = ''
    while num1 > 0:
        revbinary_val += str(num1 % 2)
        num1 = int(num1 / 2) 
    return revbinary_val


def string_reverse(revbinary_val): 
    reverse_input = ''
    for i in revbinary_val:
        reverse_input = i + reverse_input
    
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    revbinary_val = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(revbinary_val))
    print(binary_string)
