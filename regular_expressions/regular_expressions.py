regex, input_ = input().split("|")

if regex == "":
    print(True)
elif input_ == "":
    print(False)
elif regex == ".":
    print(True)
else:
    print(regex == input_)
