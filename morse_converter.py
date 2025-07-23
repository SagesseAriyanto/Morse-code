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
    # Add your conversion logic here
    text = request.form['input_text']
    morse_result = ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)
    return render_template('textconv.html', result=morse_result)

@app.route('/convert_morse_to_text', methods=['POST'])
def convert_morse_to_text():
    # Add your conversion logic here
    morse = request.form['input_text']
    text_result = ''.join([char for code in morse.split(' ') for char, morse_code in MORSE_CODE_DICT.items() if morse_code == code])
    return render_template('morseconv.html', result=text_result)


if __name__ == "__main__":
    app.run(debug=True)
