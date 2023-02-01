def run_iteration(commands):
    commands[1] = noun
    commands[2] = verb

    for position in range(0, len(commands), 4):
        instruction = commands[position]

        if instruction == 1:
            commands[commands[position + 3]] = commands[commands[position + 1]] + commands[commands[position + 2]]
        elif instruction == 2:
            commands[commands[position + 3]] = commands[commands[position + 1]] * commands[commands[position + 2]]
        elif instruction == 99:
            break

    return commands[0]


with open('input.txt', 'r') as f:
    inputs = list(map(int, f.read().replace('/n', '').split(',')))

for noun in range(0, 100, 1):
    for verb in range(0, 100, 1):

        iteration = run_iteration(inputs.copy())

        if iteration == 19690720:
            print(100 * noun + verb)
            exit
