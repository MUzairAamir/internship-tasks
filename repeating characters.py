# first repeating character in a string

def repeating(text):
    # Check every character
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]:
                return text[i]

    return None



text = input("Enter a string: ")

repeat = repeating(text)

# check
if repeat:
    print("First repeating character:", repeat)
else:
    print("No repeating character found.")
