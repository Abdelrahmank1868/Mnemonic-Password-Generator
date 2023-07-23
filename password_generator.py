import random
import string

def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def load_word_dictionary():
    with open('word_dictionary.txt', 'r') as file:
        return file.read().splitlines()

def generate_mnemonic_phrase(num_words=4):
    word_dictionary = load_word_dictionary()
    return ' '.join(random.choice(word_dictionary) for _ in range(num_words))

if __name__ == "__main__":
    print("Random Password Generator with Mnemonic Phrases")
    print("----------------------------------------------")
    while True:
        print("\nOptions:")
        print("1 - Generate random password")
        print("2 - Generate mnemonic phrase")
        print("0 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            password_length = int(input("Enter the password length: "))
            password = generate_random_password(password_length)
            print(f"\nGenerated Password: {password}\n")
        elif choice == '2':
            num_words = int(input("Enter the number of words in the phrase (e.g., 4): "))
            mnemonic_phrase = generate_mnemonic_phrase(num_words)
            print(f"\nGenerated Mnemonic Phrase: {mnemonic_phrase}\n")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
