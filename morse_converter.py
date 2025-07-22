from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

MORSE_CODE_DICT = {
    # Letters
    'A': '·−', 'B': '−···', 'C': '−·−·', 'D': '−··', 'E': '·', 'F': '··−·',
    'G': '−−·', 'H': '····', 'I': '··', 'J': '·−−−', 'K': '−·−', 'L': '·−··',
    'M': '−−', 'N': '−·', 'O': '−−−', 'P': '·−−·', 'Q': '−−·−', 'R': '·−·',
    'S': '···', 'T': '−', 'U': '··−', 'V': '···−', 'W': '·−−', 'X': '−··−',
    'Y': '−·−−', 'Z': '−−··',
    
    # Numbers
    '0': '−−−−−', '1': '·−−−−', '2': '··−−−', '3': '···−−', '4': '····−',
    '5': '·····', '6': '−····', '7': '−−···', '8': '−−−··', '9': '−−−−·',
    
    # Punctuation
    '.': '·−·−·−', ',': '−−··−−', '?': '··−−··', "'": '·−−−−·',
    '!': '−·−·−−', '/': '−··−·', '(': '−·−−·', ')': '−·−−·−',
    '&': '·−···', ':': '−−−···', ';': '−·−·−·', '=': '−···−',
    '+': '·−·−·', '-': '−····−', '_': '··−−·−', '"': '·−··−·',
    '$': '···−··−', '@': '·−−·−·',
    
    # Space
    ' ': '/'  # Using '/' to represent word separation
}

def convert_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')
    return ' '.join(morse_code)

def convert_to_text(morse_code):
    text = []
    for code in morse_code.split(' '):
        if code == '/':
            text.append(' ')
        else:
            found = False
            for char, morse in MORSE_CODE_DICT.items():
                if code == morse:
                    text.append(char.lower())
                    found = True
                    break
        # If no match is found, append a placeholder
            if not found:
                text.append('?')
    return ''.join(text)



def main():
    while True:
        user_choice = input("\n=== MORSE CODE CONVERTER ===\n"
                           "1. Convert Text to Morse Code\n"
                           "2. Convert Morse Code to Text\n"
                           "3. Exit\n"
                           "Enter your choice (1/2/3): ")
        if user_choice == '1':
            user_input = input("Enter text to convert to Morse code:\n")
            morse_code = convert_to_morse(user_input.lower())
            print("Morse Code:", morse_code)

        elif user_choice == '2':
            user_input = input("Enter Morse code to convert to text:]\n")
            text = convert_to_text(user_input.lower())
            print("Translation:", text)

        elif user_choice == '3':
            print("Exiting the Morse Code Converter. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    app.run(debug=True)
