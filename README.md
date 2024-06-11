# A "Just for fun" networkx backend

## For testing

- Install the package in editable mode:

```.sh
python -m venv envir
source envir/bin/activate

pip install -e .
pip install -e ".[developer]"
pip install -e ".[test]"
```

- Run the tests:

```.sh
NETWORKX_TEST_BACKEND=j4f \
NETWORKX_FALLBACK_TO_NX=True \
    python -m pytest --pyargs networkx
```

## Example usage

```.py
>>> import nx_j4f as j4f
>>> import networkx as nx
>>> G = j4f.J4FGraph()
>>> print(nx.number_of_isolates(G, name="x"))
Hi x
Graph with 0 nodes and 0 edges
```
