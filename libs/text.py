def process_string(input_string):
    processed_string = input_string[:20]
    invalid_chars = r'\/:*?"<>|'
    processed_string = ''.join(char if char not in invalid_chars else '_' for char in processed_string)
    return processed_string
