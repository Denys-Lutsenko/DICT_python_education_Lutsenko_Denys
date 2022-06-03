regex_string, input_string = input().split("|")


def regex_recursion(regex, string):
    if regex == "":
        return True
    elif string == "":
        return False
    elif regex[0] != "." and regex[0] != string[0]:
        return False
    else:
        return regex_recursion(regex[1:], string[1:])


def unequal_len_regex(regex, string):
    found_match = regex_recursion(regex, string)

    if found_match:
        return True
    elif string == "":
        return False
    else:
        return unequal_len_regex(regex, string[1:])


print(unequal_len_regex(regex_string, input_string))
