def count_unique_characters(string):
    unique_chars = set(string)
    return len(unique_chars)
string = "Guvi Geeks Network Private Limited"
unique_count = count_unique_characters(string)
print("unique characters:", unique_count)