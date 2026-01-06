# Profiling PolarRoute and MeshiPhi




## Results

### Create Environmental Mesh

Code: `scripts/meshiphi_build.py`

Config: `configs/environment/grf_example.config.json`

| MeshiPhi | Python | Total Time (s) | Profile | Mesh | Optimizations |
| -------- | ------ | ---------- | ------- | ---- | ------------- |
| 2.1.15 | 3.13 | 92.4 | <a href="profiles/build_mesh_meshiphi2.1.15_python3.13.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |
| 2.2.3 | 3.13 | 88.6 | <a href="profiles/build_mesh_meshiphi2.2.3_python3.13.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |
| 2.2.3 | 3.14 | 168.0 | <a href="profiles/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">snakeviz</a> | <a href="meshplots/build_mesh_meshiphi2.2.3_python3.14.html" target="_blank">geoplot</a>* | None |

\* _Note: these all show the same mesh output._

### Add Vehicle

Code: `scripts/polarroute_add_vehicle.py`

Config: `configs/vessels/sda.json`

| PolarRoute | MeshiPhi | Python | Total Time (s) | Profile | Mesh | Optimizations |
| ---------- | -------- | ------ | ---------- | ------- | ---- | ------------- |
| 1.1.8 | 2.1.15 | 3.14 | 17.8 | <a href="profiles/add_vehicle_polarroute1.1.8_meshiphi2.1.15_python3.14.html" target="_blank">snakeviz</a> | <a href="meshplots/add_vehicle_polarroute1.1.8_meshiphi2.1.15_python3.14.html" target="_blank">geoplot</a> | None |


### Optimise Route

TODO