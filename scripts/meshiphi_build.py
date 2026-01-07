import json
from time import time
from meshiphi.mesh_generation.mesh_builder import MeshBuilder

# import yappi


config_filepath = "configs/environment/grf_example.config.json"
mesh_filepath = "grf_example.mesh.json"

with open(config_filepath, 'r') as f:
    config = json.load(f)

# yappi.start()

start = time()
cg = MeshBuilder(config).build_environmental_mesh()
end = time()
print(f"Time: {end - start} s")

# yappi.stop()
# yappi.get_func_stats().print_all()
# yappi.get_thread_stats().print_all()

# mesh = cg.to_json()

# with open(mesh_filepath, 'w') as f:
#     json.dump(mesh, f, ensure_ascii=False, indent=4)
