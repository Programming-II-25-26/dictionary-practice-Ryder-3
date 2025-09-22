def first(dict):
    key = input("Enter your desired key: ")
    value = input("Enter yout desired value: ")

    dict[key] = value
    return dict

def second(dict):
    key = input("Enter the key you want to check for: ")
    if key in dict:
        print(f"{key} is already in the dictionary")
    else:
        print(f"{key} is not in the dictionary")

def third(dict):
    for key in dict:
        print(f"Key = {key}")
        print(f"value = {dict[key]}")




dictionary = {}
first(dictionary)
second(dictionary)
third(dictionary)