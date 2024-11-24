# noinspection PyPep8Naming,SpellCheckingInspection
def Djikstra(nodes, edges, source_index=0):
    path_length = {v: float('inf') for v in nodes}
    path_length[source_index] = 0
    adjacent_nodes = {v: {} for v in nodes}
    for(u,v), w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv
        adjacent_nodes[v][u] = w_uv

if __name__ == "__main__":
    print("Test")
    Djikstra([0, 1, 2, 3, 4, 5],
             {(0, 1): 1.0, (0, 2): 1.5, (0, 3): 2.0, (1, 3): 0.5, (1, 4): 2.5, (2, 3): 1.5, (3, 5): 1.0}, 0)
