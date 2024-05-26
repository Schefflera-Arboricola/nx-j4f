from nx_j4f.algorithms.isolate import number_of_isolates
import networkx as nx

__all__ = ["BackendInterface", "J4FGraph"]


class J4FGraph:
    """A wrapper class for networkx.Graph, networkx.DiGraph, networkx.MultiGraph,
    and networkx.MultiDiGraph."""

    __networkx_backend__ = "j4f"

    def __init__(self, graph_object=nx.Graph()):
        self.graph_object = graph_object

    def is_multigraph(self):
        return self.graph_object.is_multigraph()

    def is_directed(self):
        return self.graph_object.is_directed()


class BackendInterface:
    """BackendInterface class for parallel algorithms."""

    number_of_isolates = number_of_isolates

    @staticmethod
    def convert_from_nx(
        graph,
        edge_attrs=None,
        node_attrs=None,
        preserve_edge_attrs=False,
        preserve_node_attrs=False,
        preserve_graph_attrs=False,
        name=None,
        graph_name=None,
        *,
        weight=None,  # For nx.__version__ <= 3.1
    ):
        """Convert a networkx.Graph, networkx.DiGraph, networkx.MultiGraph,
        or networkx.MultiDiGraph to a J4FGraph."""
        if isinstance(graph, J4FGraph):
            return graph
        return J4FGraph(graph)

    @staticmethod
    def convert_to_nx(result, *, name=None):
        """Convert a J4FGraph to a networkx.Graph, networkx.DiGraph,
        networkx.MultiGraph, or networkx.MultiDiGraph."""
        return result
