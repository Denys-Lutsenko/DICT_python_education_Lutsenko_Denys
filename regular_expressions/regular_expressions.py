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


def regex_v3(regex, string):
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


def repetition(base_list, index, symbol, string_len):
    possibility = []
    if symbol in ["?", "*"]:
        empty_index = base_list[:]
        empty_index[index] = ""
        possibility.append(empty_index)
    if symbol in ["*", "+"]:
        repeated_count = 2
        current_len = len(base_list) + repeated_count - 1

        offset = 0
        if base_list[0] == "^":
            offset += 1
        if base_list[-1] == "$":
            offset += 1

        max_len = string_len + offset

        while current_len <= max_len:
            empty_index = base_list[:]
            index_char = empty_index[index]
            empty_index[index] = index_char * repeated_count
            possibility.append(empty_index)
            repeated_count += 1
            current_len += 1
    return possibility


def regex_v4_helper(base_list, idx_map, max_len):
    scenarios = [base_list]
    for index, meta in idx_map.items():
        current_scenarios = scenarios[:]
        for item in current_scenarios:
            extended_scenarios = repetition(item, index, meta, max_len)
            scenarios.extend(extended_scenarios)

    scenario_str = ["".join(scenario) for scenario in scenarios]

    return scenario_str


def regex_v4(regex, string):
    meta_count = ["?", "*", "+"]
    if all(char not in meta_count for char in regex):
        return regex_v3(regex, string)

    meta_dict = {}

    for i in range(1, len(regex)):
        if regex[i] in meta_count and regex[i - 1] != "\\":
            offset = len(meta_dict)
            meta_dict[i - 1 - offset] = regex[i]

    base_chars = [char for char in regex if char not in meta_count]

    scenarios = regex_v4_helper(base_chars, meta_dict, len(string))

    for item in scenarios:
        current_eval = regex_v3(item, string)
        if current_eval is True:
            return True

    return False


print(regex_v4(regex_string, input_string))
