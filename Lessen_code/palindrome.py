def is_palindrome(word):
    word_1 = ''
    for i in word:
        if i != ' ':
            word_1 += i
        else:
            continue

    if word_1 == word_1[::-1]:
        return True
    else:
        return False


try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")
