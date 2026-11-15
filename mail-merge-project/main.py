# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names = []

with open("Input/Names/invited_names.txt") as names:
    for name in names:
        invited_names.append(name.strip())

print(invited_names)

with open("Input/Letters/starting_letter.txt", "r") as invitation_letter:
    letter = invitation_letter.read()
    first_name = invited_names[0]
    first_invitation = letter.replace("[name]", first_name)
    print(first_invitation)