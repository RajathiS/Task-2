def most_frequent_char(string):
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    max_freq = 0
    most_frequent_char = None
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_char = char

    return most_frequent_char
string = "Guvi Geeks Network Private Limited"
result = most_frequent_char(string)
print("frequent character:", result)