def stack_sequence(n, sequence):

    return_array = []
    stack = []
    seq_idx = 0

    for i in range(1, n+1):
        stack.append(i)
        return_array.append('+')

        while len(sequence) > seq_idx and stack and stack[-1] == sequence[seq_idx]:
            stack.pop()
            return_array.append('-')
            seq_idx += 1

    if stack:
        print('NO')
        return

    for char in return_array:
        print(char)

sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)