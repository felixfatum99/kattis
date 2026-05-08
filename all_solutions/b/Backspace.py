#https://open.kattis.com/problems/backspace
def process_string(s):
    result = []
    for char in s:
        if char == '<':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)

input_string = input()
output_string = process_string(input_string)
print(output_string)