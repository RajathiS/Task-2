def palindrome(string):
    return string == string[::-1]
string = "repaper"
ans = palindrome(string)
if ans:
    print("True")
else:
    print("False")

