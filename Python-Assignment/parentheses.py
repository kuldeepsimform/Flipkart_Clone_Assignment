"""
    This is a program to find the correct number of brackets generation according to user input.
"""
parenthesis = []


def generate_parenthesis(open_parenthesis, close_parenthesis, output_str):
    """
    This function takes open, close, parenthesis number and bracket string as an argumetent and generate all combinations of well-formed parentheses.

    Args:
        open_parenthesis (int): open parenthesis counter
        close_parenthesis (int): close parenthesis counter
        output_str (string): bracket string
    """
    if open_parenthesis == 0 and close_parenthesis == 0:
        parenthesis.append(output_str)

    if open_parenthesis != 0:
        generate_parenthesis(
            open_parenthesis-1,
            close_parenthesis,
            output_str+'(')

    if close_parenthesis > open_parenthesis:
        generate_parenthesis(
            open_parenthesis,
            close_parenthesis-1,
            output_str+')')


n = int(input("Enter number"))
if -1 <= n <= 8:
    generate_parenthesis(n, n, '')
else:
    print("Please select range between 0 to 8")

print(parenthesis)
