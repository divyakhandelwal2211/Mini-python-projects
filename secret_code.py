import random
import string

def encode(message):
    words = message.split(" ")
    new_words = []
    for word in words:
        if len(word) < 3:
            new_words.append(word[::-1])
        elif len(word) >= 3:
            r1 = "".join(random.choices(string.ascii_lowercase, k=3))
            r2 = "".join(random.choices(string.ascii_lowercase, k=3))
            stnew = r1 + word[1:] + word[0] + r2
            new_words.append(stnew)
            new_message = " ".join(new_words)
    print(f"Your encoded message is - {new_message}")


def decode(message):
    words = message.split(" ")
    new_words = []
    for word in words:
        if len(word) < 3:
            new_words.append(word[::-1])
        elif len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            new_words.append(stnew)
            new_message = " ".join(new_words)
    print(f"Your decoded message is - {new_message}")


print("Hey! Do you want to encode or decode?")
choice = int(input("Enter 1 for encode and 2 for decode = "))

if choice == 1:
    message = input("Enter your message for encode: ")
    encode(message)
elif choice == 2:
    message = input("Enter your message for decode: ")
    decode(message)
