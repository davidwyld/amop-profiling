# Profiling PolarRoute and MeshiPhi




## Results

**Tip**: Sort by `cumtime` when viewing snakeviz profile visualisations. Click a function call (line in the table) to set that as the root call. E.g. for environmental mesh building, select `build_environmental_mesh`.

### Create Environmental Mesh

#### GRF Example

Code: `scripts/meshiphi_build.py`

Config: `configs/environment/grf_example.config.json`


| MeshiPhi | Python | Total Time (s) | Profile | Mesh | Optimizations |
| -------- | ------ | ---------- | ------- | ---- | ------------- |
| 2.1.15 | 3.13 | 92.4 | <a href="profiles/build_mesh_meshiphi2.1.15_python3.13.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |
| 2.2.3 | 3.13 | 88.6 | <a href="profiles/build_mesh_meshiphi2.2.3_python3.13.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |
| 2.2.3 | 3.14 | 168.0 | <a href="profiles/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |

\* _Note: these all show the same mesh output._


#### Real Production Data

Code: `scripts/meshiphi_build.py`

Config: `configs/environment/amsr_southern.config.json`

| MeshiPhi | Python | Total Time (s) | Profile | Mesh | Optimizations |
| -------- | ------ | ---------- | ------- | ---- | ------------- |
| 2.2.3 | 3.13 | 637 | <a href="profiles/build_mesh_amsr_southern_meshiphi2.2.3_python3.13.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_amsr_southern_meshiphi2.2.3_python3.13.html" target="_blank">geoplot</a> | None |

### Add Vehicle

Code: `scripts/polarroute_add_vehicle.py`

Config: `configs/vessels/sda.json`

| PolarRoute | MeshiPhi | Python | Total Time (s) | Profile | Mesh | Optimizations |
| ---------- | -------- | ------ | ---------- | ------- | ---- | ------------- |
| 1.1.8 | 2.1.15 | 3.14 | 17.8 | <a href="profiles/add_vehicle_polarroute1.1.8_meshiphi2.1.15_python3.14.html" target="_blank">snakeviz</a> | <a href="meshplots/add_vehicle_polarroute1.1.8_meshiphi2.1.15_python3.14.html" target="_blank">geoplot</a> | None |


### Optimise Route

TODO