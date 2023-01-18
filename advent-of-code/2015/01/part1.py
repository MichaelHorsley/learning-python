with open('01.txt', 'r') as f:
    instructions = f.read().replace('/n', '')

story = 0

for character in instructions:
    if character == '(':
        story += 1
    else:
        story -= 1

print(story)
