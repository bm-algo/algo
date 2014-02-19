from math import factorial

from utils import get_bridges



def my_algo(array):

    # to vertexes
    vertexes = {}
    for (first, second) in array:
        if first not in vertexes:
            vertexes[first] = set([second])
        else:
            vertexes[first].add(second)
        if second not in vertexes:
            vertexes[second] = set([first])
        else:
            vertexes[second].add(first)

    # getting subgraphs
    def init_subgraph(vertex):
        graph = [vertex]
        for vertex in graph:
            for child in vertexes[vertex]:
                if child not in graph:
                    graph.append(child)
        return graph

    graphs = []
    vertexes_in_graphs_count = 0
    while vertexes_in_graphs_count < len(vertexes.keys()):
        current_graph = init_subgraph(vertexes.keys()[0])
        graphs.append(current_graph)
        vertexes_in_graphs_count += len(current_graph) 

    global_result = 0

    if len(graphs) == 1:
        graph = vertexes
        result = get_bridges(graph, full_return=True)
        fup = result['fup']
        bridges_values = [(fup[v1] + fup[v2]) / 2. for v1, v2 in result['bridges']]
        for value in bridges_values:
            before = len([v for v in fup.values() if v < value])
            after = len([v for v in fup.values() if v >= value])
            global_result += before * after

        non_bridges_count = len([e for e in array if tuple(e) not in result['bridges']])
        possible_edges_count = factorial(len(graph.keys()) - 1) - len(array)

        global_result += possible_edges_count*non_bridges_count

        return global_result

    if len(graphs) == 2:
        non_bridges_count = 0
        for graph in graphs:
            edges = [e for e in array if e[0] in graph or e[1] in graph]
            graph_vertexes = dict((k, v) for k, v in vertexes.items() if k in graph)
            bridges = get_bridges(graph_vertexes)
            non_bridges_count += len([e for e in edges if tuple(e) not in bridges])

        global_result = non_bridges_count * (len(graphs[0]) + len(graphs[1]))

    return global_result




# examples:

# graph = [[1, 2], [2, 3], [3, 4], [1, 4]]
# print my_algo(graph)

graph = [[1, 2], [1, 3], [2, 3], [3, 4], [4, 5]]
print my_algo(graph)
