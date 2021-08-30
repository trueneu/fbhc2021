def read_input(filename):
    cases = []
    with open(filename, 'r') as f:
        num_cases = int(f.readline().strip())
        for _ in range(num_cases):
            s = f.readline().strip()
            num_edges = int(f.readline().strip())
            edges = []
            for _ in range(num_edges):
                edges.append(f.readline().strip())
            cases.append({'edges': edges, 'string': s})

    return cases


def solve(case):
    edges, s = case['edges'], case['string']
    max_dist = 1 << 31
    dist = []
    for _ in range(26):
        l = [max_dist] * 26
        dist.append(l)

    for edge in edges:
        u, w = edge
        u_index = ord(u) - ord('A')
        w_index = ord(w) - ord('A')
        dist[u_index][w_index] = 1

    for i in range(26):
        dist[i][i] = 0

    for k in range(26):
        for i in range(26):
            for j in range(26):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    result = 1 << 31

    for target_char_index in range(26):
        distance = 0
        for char in s:
            char_index = ord(char) - ord('A')
            distance += dist[char_index][target_char_index]

        result = min(result, distance)

    if result == 1 << 31:
        result = -1

    return result


def test():
    cases = read_input("consistency_chapter_2_input.txt")
    with open('result.txt', 'w') as f:
        for i, case in enumerate(cases):
            swaps_count = solve(case)
            print('Case #{}: {}'.format(i + 1, swaps_count), file=f)



