def read_input(filename):
    cases = []
    with open(filename, 'r') as f:
        num_cases = int(f.readline().strip())
        for _ in range(num_cases):
            n = int(f.readline().strip())
            board = []
            for _ in range(n):
                board.append(f.readline().strip())
            cases.append({'board': board, 'n': n})
    return cases


def solve(case):
    lanes = []
    board, n = case['board'], case['n']
    for row in board:
        lanes.append(row)
    for i in range(n):
        lanes.append(''.join([x[i] for x in board]))

    xs_count = 1 << 31
    dots_count = []

    for lane in lanes:
        if 'O' in lane:
            dots_count.append(-100)
            continue
        dot_count = lane.count('.')
        dots_count.append(dot_count)
        xs_count = min(xs_count, dot_count)

    if xs_count == 1 << 31:
        return -1, -1

    if xs_count > 1:
        options_count = dots_count.count(xs_count)
    else:
        for i in range(n):
            if dots_count[i] == xs_count:
                j = lanes[i].index('.')
                dots_count[n + j] = -1
        options_count = dots_count.count(xs_count)

    return xs_count, options_count


def test():
    cases = read_input("xs_and_os_input.txt")
    with open('result.txt', 'w') as f:
        for i, case in enumerate(cases):
            xs_count, options_count = solve(case)
            print('Case #{}: {} {}'.format(i + 1, xs_count, options_count)
                  if xs_count >= 0 else
                  'Case #{}: Impossible'.format(i + 1), file=f)
