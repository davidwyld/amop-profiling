import json

from polar_route.vessel_performance.vessel_performance_modeller import VesselPerformanceModeller

mesh_filepath = "output/grf_example.mesh.json"
vessel_config_filepath = "configs/vessels/sda.json"
output_filepath = "output/grf_example.vessel.sda.json"

with open(mesh_filepath, 'r') as f:
    mesh_json = json.load(f)

with open(vessel_config_filepath, 'r') as f:
    vessel_config = json.load(f)

vp = VesselPerformanceModeller(mesh_json, vessel_config)
vp.model_accessibility()
vp.model_performance()

mesh = vp.to_json()

with open(output_filepath, 'w') as f:
    json.dump(mesh, f, ensure_ascii=False, indent=4)
