# Profiling PolarRoute and MeshiPhi




## Results

**Tip**: Sort by `cumtime` when viewing snakeviz profile visualisations. Click a function call (line in the table) to set that as the root call. E.g. for environmental mesh building, select `build_environmental_mesh`.

### Create Environmental Mesh

#### GRF Example

Code: `scripts/meshiphi_build.py`

Config: `configs/environment/grf_example.config.json`


| MeshiPhi | Python | `build_environmental_mesh` time/s | Profile | Mesh | Optimizations |
| -------- | ------ | ---------- | ------- | ---- | ------------- |
| 2.1.15 | 3.13 | 92.4 | <a href="profiles/build_mesh_meshiphi2.1.15_python3.13.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |
| 2.2.3 | 3.13 | 88.6 | <a href="profiles/build_mesh_meshiphi2.2.3_python3.13.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |
| 2.2.3 | 3.14 | 168.0 | <a href="profiles/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |
| [2.3.0](https://github.com/bas-amop/MeshiPhi/pull/105/) | 3.13 | 74.5 | <a href="profiles/build_mesh_meshiphi2.3.0_python3.13.html" target="_blank">snakeviz</a> |  | Integer-based `.isel()` ([PR](https://github.com/bas-amop/MeshiPhi/pull/97)) |
| [2.3.0](https://github.com/bas-amop/MeshiPhi/pull/105/) | 3.14 | 55.8 | <a href="profiles/build_mesh_meshiphi2.3.0_python3.14.html" target="_blank">snakeviz</a> |  | Integer-based `.isel()` ([PR](https://github.com/bas-amop/MeshiPhi/pull/97)) |
| [2.3.0](https://github.com/bas-amop/MeshiPhi/pull/105/) | 3.14 freethreaded** | 24.2 | <a href="profiles/build_mesh_meshiphi2.3.0_python3.14_noGIL.html" target="_blank">snakeviz</a> |  | Integer-based `.isel()` ([PR](https://github.com/bas-amop/MeshiPhi/pull/97)) & GIL off |

\* _Note: these all show the same mesh output._

\** GIL (global interpreter lock) turned off using `python-freethreading` build from conda-forge; with `PYTHON_GIL=0`. Note this raises a warning as pandas is not marked as being safe without the GIL.

`trim_datapoints` for abstract scalar datasets is the function within MeshiPhi that takes up most time during both the `split_to_depth` and `aggregate` stages.

The bulk of the time is in the use of `xarray.dataset.sel`.

This is mainly due to the number of calls to this function, ~17k in this GRF example, or ~145k times in the real data example below.

Each call only takes 5E-6 seconds, but totals up to a large fraction of the overall runtime.

<s>Optimising the approach here should be the first target for speedups in mesh building.</s>

Thomas had already addressed this in ([PR #97](https://github.com/bas-amop/MeshiPhi/pull/97)), using integer-based `.isel` over `.sel`, which in addition to using python 3.14 results in a 40% speed up.

#### Real Production Data

Code: `scripts/meshiphi_build.py`

Config: `configs/environment/amsr_southern.config.json`

| MeshiPhi | Python | Total Time (s) | Profile | Mesh | Optimizations |
| -------- | ------ | ---------- | ------- | ---- | ------------- |
| 2.2.3 | 3.13 | 637 | <a href="profiles/build_mesh_amsr_southern_meshiphi2.2.3_python3.13.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_amsr_southern_meshiphi2.2.3_python3.13.html" target="_blank">geoplot</a> | None |
| 2.3.0 | 3.14 | 403 | <a href="profiles/build_mesh_amsr_southern_meshiphi2.3.0_python3.14.html" target="_blank">snakeviz</a> | - | Integer-based `.isel()` ([PR](https://github.com/bas-amop/MeshiPhi/pull/97)) |

### Add Vehicle

Code: `scripts/polarroute_add_vehicle.py`

Config: `configs/vessels/sda.json`

| PolarRoute | MeshiPhi | Python | Total Time (s) | Profile | Mesh | Optimizations |
| ---------- | -------- | ------ | ---------- | ------- | ---- | ------------- |
| 1.1.8 | 2.1.15 | 3.14 | 17.8 | <a href="profiles/add_vehicle_polarroute1.1.8_meshiphi2.1.15_python3.14.html" target="_blank">snakeviz</a> | <a href="meshplots/add_vehicle_polarroute1.1.8_meshiphi2.1.15_python3.14.html" target="_blank">geoplot</a> | None |


### Optimise Route

TODO