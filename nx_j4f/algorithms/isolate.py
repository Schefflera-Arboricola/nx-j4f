import networkx as nx

__all__ = ["number_of_isolates"]


def number_of_isolates(G):
    if hasattr(G, "graph_object"):
        G = G.graph_object

    return "Hi"
