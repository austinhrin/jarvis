def string_after(input_string, by):
    # split string into parts
    head, sep, tail = input_string.partition(by)
    output_string = tail
    # remove space before string
    if tail[0] == ' ':
        output_string = output_string[1:]
    # remove space after string
    if tail[len(tail) - 1] == ' ':
        output_string = output_string[:-1]
    return output_string

def remove_spaces(input_string):
    output_string = input_string.split(' ')
    output_string = ''.join(output_string)
    return output_string