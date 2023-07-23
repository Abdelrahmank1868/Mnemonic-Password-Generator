# Random Password Generator with Mnemonic Phrases

![Termux Logo](https://termux.com/files/usr/share/termux/images/termux-icon.png)

## Purpose

The Random Password Generator with Mnemonic Phrases is a Python script designed to help users generate secure random passwords and create memorable mnemonic phrases associated with each password. This tool aims to strike a balance between security and ease of remembrance. The script utilizes a dictionary of words to generate the phrases, allowing users to create passwords that are both strong and easy to recall.

## Requirements

- [Termux](https://termux.com/) - A terminal emulator for Android devices.

## How to Use

1. Install Termux: 
   - Download and install [Termux](https://termux.com/) from the Google Play Store if you haven't already.

2. Install Python:
   - Open Termux and install Python by running the following command:
     ```
     pkg install python
     ```

3. Get the Password Generator Script:
   - Copy the contents of the provided Python script named `password_generator.py`.

4. Create a Dictionary File:
   - Create a text file named `word_dictionary.txt` in the same directory as the script.
   - Add one random word per line to this file. The words in this dictionary will be used to generate mnemonic phrases.

5. Run the Script:
   - Open Termux and navigate to the directory where you saved the script and the dictionary file.
   - Run the script using the following command:
     ```
     python password_generator.py
     ```

6. Using the Script:
   - Upon running the script, you will be presented with a menu with the following options:
     - `1`: Generate a random password
     - `2`: Generate a mnemonic phrase
     - `0`: Exit the script

7. Generate Random Passwords:
   - Choose option `1` from the menu and specify the desired password length when prompted.
   - The script will generate a random password consisting of alphanumeric characters and symbols.

8. Generate Mnemonic Phrases:
   - Choose option `2` from the menu and enter the desired number of words for the phrase when prompted.
   - The script will create a mnemonic phrase using random words from the dictionary file.

9. Exit the Script:
   - To exit the script, choose option `0` from the menu.

## Security Note

While mnemonic phrases can be easier to remember than random passwords, they might be more susceptible to dictionary-based attacks. It is essential to use a strong word dictionary and consider increasing the number of words in the mnemonic phrase to enhance security.

## Disclaimer

The Random Password Generator with Mnemonic Phrases script is provided for educational and personal use only. The authors do not assume any responsibility for the misuse or consequences resulting from the use of this tool.