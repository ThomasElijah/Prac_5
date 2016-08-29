user_string = input("Enter a string: ")

list_strings = []
for word in user_string.split():
    if word not in list_strings:
        list_strings.append(word)

max_length = max(list_strings)

length_strings = []
for string in list_strings:
    count = 0
    for string in user_string:
        count += 1
    length_strings.append(count)

dictionary = {}
for i in range(len(list_strings)):
    dictionary[length_strings[i]] = length_strings[i]
for key in dictionary:
    print("{:{}} :{}".format(key, max_length, dictionary[key]))