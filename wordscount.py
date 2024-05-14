def words(string):
    words = string.split()
    return len(words)
string = "Guvi Geeks Network Private Limited"
word_count = words(string)
print("Number of words:", word_count)