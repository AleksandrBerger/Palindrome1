#used PyCharm
def is_palindrome(phrase):
    phrase = phrase.casefold()
    list_palindrome = list(phrase.strip(""))
    list_original = list_palindrome.copy()
    # print(list_original)
    list_palindrome.reverse()

    if list_palindrome == list_original:
        print(True)
    else:
        print(False)


word: str = input("Enter a word to check whether it is a palindrome: ")
is_palindrome(word)
