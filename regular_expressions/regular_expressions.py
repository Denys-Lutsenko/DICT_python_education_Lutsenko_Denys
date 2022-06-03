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


def regex_v3(regex: str, string):
    if regex.startswith("^"):
        regex = regex.replace("^", "")
        temp_regex = regex.replace("$", "")
        for i in range(len(temp_regex)):
            if temp_regex[i] != "." and temp_regex[i] != string[i]:
                return False

    if regex.endswith("$"):
        regex = regex.replace("$", "")
        for i in range(-1, -1 - len(regex), -1):
            if regex[i] != "." and regex[i] != string[i]:
                return False

    return unequal_len_regex(regex, string)


print(regex_v3(regex_string, input_string))
