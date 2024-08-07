# Step 1: Define the Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

# Reverse the dictionary for decoding
MORSE_CODE_DICT_REVERSED = {v: k for k, v in MORSE_CODE_DICT.items()}

# Step 2: Implement the encoding function
def encode_to_morse(message):
    message = message.upper()
    encoded_message = ' '.join(MORSE_CODE_DICT.get(char, '') for char in message if char in MORSE_CODE_DICT or char == ' ')
    return encoded_message

# Step 3: Implement the decoding function
def decode_from_morse(morse_code):
    words = morse_code.split('   ')  # Morse code words are separated by 3 spaces
    decoded_message = ''
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(MORSE_CODE_DICT_REVERSED.get(letter, ' ') for letter in letters)
        decoded_message += decoded_word + ' '
    return decoded_message.strip()

# Example usage

message = "Titanic is in Emergency"

encoded_message = encode_to_morse(message)
print(f"Encoded: {encoded_message}")

decoded_message = decode_from_morse(encoded_message)
print(f"Decoded: {decoded_message}")
