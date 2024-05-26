# A "Just for fun" networkx backend

## For testing

- Install the package in editable mode:

```sh
pip install -e ".[developer]"
pip install -e ".[test]"
```

- Run the tests:

```.sh
NETWORKX_TEST_BACKEND=j4f \
NETWORKX_FALLBACK_TO_NX=True \
    python -m pytest --pyargs networkx
```
