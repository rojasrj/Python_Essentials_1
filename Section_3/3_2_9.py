secret_word = "chupacabra"

user_word = input("Enter a secret word: ")

while user_word != secret_word:
    user_word = input("Enter a secret word: ")

print("You\'ve successfully left the loop.")