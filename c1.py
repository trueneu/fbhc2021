def read_input(filename):
    cases = []
    with open(filename, 'r') as f:
        t = int(f.readline().strip())
        for _ in range(t):
            edges = []
            n = int(f.readline().strip())
            cs = list(map(int, f.readline().strip().split()))
            for _ in range(n - 1):
                edge = f.readline().strip()
                v1, v2 = map(int, edge.split())
                edges.append((v1 - 1, v2 - 1))
            cases.append({'cs': cs, 'edges': edges, 'n': n})
    return cases


def solve(case):
    cs = case['cs']
    edges = case['edges']

    n = len(cs)
    adj = [[] * n for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dp = [0] * n

    seen = [False] * n

    stack = [0]

    while stack:
        node = stack[-1]
        if not seen[node]:
            seen[node] = True
            for adjacent_node in adj[node]:
                if not seen[adjacent_node]:
                    stack.append(adjacent_node)
        else:
            stack.pop()
            seen[node] = False
            child_max = 0
            for adjacent_node in adj[node]:
                if not seen[adjacent_node]:
                    child_max = max(child_max, dp[adjacent_node])
            dp[node] = child_max + cs[node]

    if len(adj[0]) <= 1:
        return dp[0]

    max1 = max2 = 0

    for adjacent_node in adj[0]:
        if dp[adjacent_node] > max2:
            if dp[adjacent_node] > max1:
                max2 = max1
                max1 = dp[adjacent_node]
            else:
                max2 = dp[adjacent_node]

    return max1 + max2 + cs[0]


def test():
    cases = read_input("gold_mine_chapter_1_input.txt")
    with open('result.txt', 'w') as f:
        for i, case in enumerate(cases):
            result = solve(case)
            print('Case #{}: {}'.format(i + 1, result), file=f)
