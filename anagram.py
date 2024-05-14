def anagram(s1, s2):

    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    word_1 = sorted(s1)
    word_2 = sorted(s2)

    return word_1 == word_2

string1 = "study"
string2 = "dusty"
print(anagram(string1, string2))