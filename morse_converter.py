from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text_to_morse')
def text_to_morse():
    return render_template('textconv.html')

@app.route('/morse_to_text')
def morse_to_text():
    return render_template('morseconv.html')

@app.route('/convert_text_to_morse', methods=['POST'])
def convert_text_to_morse():
    text = request.form['input_text']
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')

    morse_result = ' '.join(morse_code)
    print(morse_result)  # Debugging line to check the output
    return render_template('textconv.html', result=morse_result)

@app.route('/convert_morse_to_text', methods=['POST'])
def convert_morse_to_text():
    morse = request.form['input_text']
    text = []
    for code in morse.split(' '):
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
    text_result = ''.join(text).capitalize()
    print(text_result)
    return render_template('morseconv.html', result=text_result)


if __name__ == "__main__":
    app.run(debug=True)

