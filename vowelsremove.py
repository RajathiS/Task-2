def remove_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)
remove_vowel("Guvi Geeks Network Private Limited")