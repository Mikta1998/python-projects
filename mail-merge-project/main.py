invited_people = []

with open("Input/Names/invited_names.txt") as names:
    for name in names:
        invited_people.append(name.strip())

print(invited_people)

with open("Input/Letters/starting_letter.txt", "r") as invitation_letter:
    letter = invitation_letter.read()
    print(letter)
    for name in invited_people:
        invitation_text = letter.replace("[name]", name)
        with open(f"Output/ReadyToSend/starting_letter_{name}", "w") as invitation:
            invitation.write(invitation_text)
