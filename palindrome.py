
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

words = ["программирование", "заказ", "игра", "довод"]
for word in words:
    print(f'Слово {word} является палиндромом?  {is_palindrome(word)}')
