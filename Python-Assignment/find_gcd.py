"""
    This program for calculating GCD of 2 numbers.    
"""
word_to_digit_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
digit_to_word_dict = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}


def word_to_num(words):
    """
    This function takes numeric words string as an argumetent and it's converted into digit value.

    Args:
        words (string): numeric words string

    Returns:
        string: converted number.
    """
    start_pos = 0
    end_pos = 0
    converted_num = ''
    while end_pos < len(words):
        if word_to_digit_dict.get(words[start_pos:end_pos+1]):
            converted_num += word_to_digit_dict.get(words[start_pos:end_pos+1])

            start_pos = end_pos + 1
        end_pos += 1
    return converted_num


def num_to_word(num):
    """
    This function takes numeric string value as an argumetent and it's converted into numeric words string.

    Args:
        nums (string): digit string

    Returns:
        string: converted numeric string.
    """

    answer = ''
    i = 0
    while i < len(num):
        answer += digit_to_word_dict.get(num[i])
        i += 1
    return answer


def find_gcd(num1, num2):
    """
    This function takes two integer value as an argumetent and calculating GCD of 2 numbers and retruning answer.

    Args:
        num1 (int): digit one for finding gcd of two number.
        num2 (int): digit two for finding gcd of two number.

    Returns:
        int: gcd of two numbers.
    """
    i = 1
    if num2 > num1:
        min_number = num1
    else:
        min_number = num1

    while i < min_number+1:
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
        i += 1
    return gcd


try:
    print("Enter numeric words zero to nine only.")
    num1 = input('Enter first value ')
    num2 = input('Enter second value ')

    converted_num1 = int(word_to_num(num1))
    converted_num2 = int(word_to_num(num2))

    print('Answer is : ', num_to_word(
        str(find_gcd(converted_num1, converted_num2))))

except ValueError as e:
    print("Please Enter valid numeric words")
