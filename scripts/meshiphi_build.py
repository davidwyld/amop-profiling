import json
from meshiphi.mesh_generation.mesh_builder import MeshBuilder

config_filepath = "configs/environment/grf_example.config.json"
mesh_filepath = "grf_example.mesh.json"

with open(config_filepath, 'r') as f:
    config = json.load(f)

cg = MeshBuilder(config).build_environmental_mesh()

mesh = cg.to_json()

with open(mesh_filepath, 'w') as f:
    json.dump(mesh, f, ensure_ascii=False, indent=4)
