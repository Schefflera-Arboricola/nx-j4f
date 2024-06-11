__all__ = ["number_of_isolates"]


def number_of_isolates(G, name=""):
    if hasattr(G, "graph_object"):
        G = G.graph_object

    return "Hi " + name + "\n" + str(G)
