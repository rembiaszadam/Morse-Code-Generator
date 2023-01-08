import csv

# Extract morse alphabet from csv file and load into dictionary.
with open('morse.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    morse_dict = {row[0]: row[1] for row in reader}

run = True

# Main loop for user input.
while run:
    # Convert user input text to upper case.
    input_text = input('\nEnter a sentence to convert to Morse code or type "q" to quit:\n').upper()

    # Allow user to quit.
    if input_text == 'Q':
        run = False

    else:
        # Go through each letter in input text and assign morse code in new list.
        try:
            morse_code = [morse_dict[letter] for letter in input_text]

        # If a character cannot be found in morse dictionary prompt user.
        except KeyError:
            print('Please use letters and numbers only, no special characters!')

        # If each letter is converted to morse,
        # assemble the morse code list into a formatted string and show the user.
        else:
            string_code = ''
            for code in morse_code:
                string_code += code + ' | '
            print(string_code)
