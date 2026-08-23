def clean_input_string(text, max_len, allow_numbers=False):
    new_string = text.strip()
    if allow_numbers == False:
        for char in new_string:
            if char.isdigit():
                new_string.strip(char)
    x = len(new_string)
    y = max_len
    if x != y:
        final = new_string[0:y]
    return f"clean text is {final}..."

text = input("enter your text:")
length = int(input("enter maximam length:")) 
print(clean_input_string(text,length, allow_numbers=False))


