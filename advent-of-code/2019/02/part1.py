with open('input.txt', 'r') as f:
    inputs = list(map(int, f.read().replace('/n', '').split(',')))

inputs[1] = 12
inputs[2] = 2

for position in range(0, len(inputs), 4):
    if inputs[position] == 1:
        inputs[inputs[position+3]] = inputs[inputs[position+1]] + inputs[inputs[position+2]]
    elif inputs[position] == 2:
        inputs[inputs[position+3]] = inputs[inputs[position+1]] * inputs[inputs[position+2]]
    elif inputs[position] == 99:
        break

print(inputs[0])