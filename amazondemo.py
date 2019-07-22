def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    index = 1
    aux_states = states[:]
    for d in range(days):
        if states[1] == 0:
            aux_states[0] = 0
        else:
            aux_states[0] = 1
        if states[len(states) - 2] == 0:
            aux_states[len(states) - 1] = 0
        else:
            aux_states[len(states) - 1] = 1
        while index >= 1 and index < len(states) - 1:
            if states[index - 1] == states[index + 1]:
                aux_states[index] = 0
            else:
                aux_states[index] = 1
            index += 1
        states = aux_states[:]
    return aux_states


print(cellCompete([1, 0, 1, 0, 1, 0, 0, 1], 1))
