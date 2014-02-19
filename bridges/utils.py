def get_bridges(vertexes, full_return=False):
    used = set()
    tin = {}
    fup = {}
    bridges = []

    def dfs(vertex, parent=None, timer=0):
        used.add(vertex)
        tin[vertex] = timer
        fup[vertex] = timer
        timer += 1
        for target in vertexes[vertex]:
            if target == parent:
                continue
            if target in used:
                fup[vertex] = min(fup[vertex], tin[target])
            else:
                dfs(target, vertex, timer)
                fup[vertex] = min(fup[vertex], fup[target])
                if fup[target] > tin[vertex]:
                    bridges.append((vertex, target))

    dfs(vertexes.keys()[0])

    if full_return:
        return {'bridges': bridges, 'tin': tin, 'fup': fup}
    else:
        return bridges


def get_cut_vertexes(vertexes):
    used = set()
    tin = {}
    fup = {}

    cut_vertexes = []

    def dfs(vertex, parent=None, timer=0):
        used.add(vertex)
        tin[vertex] = timer
        fup[vertex] = timer
        timer += 1
        children = 0
        for target in vertexes[vertex]:
            if target == parent:
                continue
            if target in used:
                fup[vertex] = min(fup[vertex], tin[target])
            else:
                dfs(target, vertex, timer)
                fup[vertex] = min(fup[vertex], fup[target])
                if fup[target] >= tin[vertex] and parent is not None:
                    cut_vertexes.append(vertex)
                children += 1

        if parent is None and children > 1:
            cut_vertexes.append(vertex)

    dfs(vertexes.keys()[0])

    return cut_vertexes


if __name__ == '__main__':
    # vertexes = {
    #     1: [2, 3],
    #     2: [1, 3],
    #     3: [1, 2, 4, 5],
    #     4: [3, 5],
    #     5: [3, 4]
    # }

    vertexes = {
        1: [2],
        2: [1, 3, 4],
        3: [2, 4],
        4: [2, 3, 5],
        5: [4, 6],
        6: [5]
    }

    print get_bridges(vertexes)
