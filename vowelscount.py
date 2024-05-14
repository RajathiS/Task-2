def vowels(string):
    vowel_a = 0
    vowel_e = 0
    vowel_i = 0
    vowel_o = 0
    vowel_u = 0
    string = string.lower()
    for char in string:
        if char == 'a':
            vowel_a += 1
        elif char == 'e':
            vowel_e += 1
        elif char == 'i':
            vowel_i += 1
        elif char == 'o':
            vowel_o += 1
        elif char == 'u':
            vowel_u += 1
            # total_vowels += 1
    total_vowels = vowel_a+vowel_e+vowel_i+vowel_o+vowel_u
    print("Number of Vowels:", total_vowels)
    print("Vowels A:", vowel_a)
    print("Vowels E:", vowel_e)
    print("Vowels I:", vowel_i)
    print("Vowels O:", vowel_o)
    print("Vowels U:", vowel_u)
vowels("Guvi Geeks Network Private Limited?")




