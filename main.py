import csv

with open('morse.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    morse_dict = {row[0]: row[1] for row in reader}

run = True

while run:
    input_text = input('\nEnter a sentence to convert to Morse code or type "q" to quit:\n').upper()
    if input_text == 'Q':
        run = False
    else:
        try:
            morse_code = [morse_dict[letter] for letter in input_text]
        except KeyError:
            print('Enter a sentence without special characters!')
        else:
            string_code = ''
            for code in morse_code:
                string_code += code + ' | '
            print(string_code)
