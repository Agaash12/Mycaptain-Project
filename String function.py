def most_frequent(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_dict:
        print("{} = {}".format(item[0], item[1]))
string = "Mississippi"
most_frequent(string)
