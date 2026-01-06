```sh
pip install meshiphi
pip install snakeviz
```


To profile a run:

```sh
python -m cProfile -o profiles/<output_filename> scripts/<python_script>
```

To visualise with snakeviz:

```sh
python -m snakeviz profiles/<output_filename>
```


## Building the docs

`pip install mkdocs mkdocs-material`
