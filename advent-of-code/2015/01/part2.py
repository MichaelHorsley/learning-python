with open('01.txt', 'r') as f:
    instructions = f.read().replace('/n', '')

story = 0

for position, character in enumerate(instructions):
    if character == '(':
        story += 1
    else:
        story -= 1
        if story == -1:
            print(position + 1)
            break
