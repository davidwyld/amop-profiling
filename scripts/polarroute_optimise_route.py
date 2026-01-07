import json
from time import time

from polar_route.route_planner.route_planner import RoutePlanner

start = time()
rp = RoutePlanner('output/grf_example.vessel.sda.json',
                  'configs/traveltime.config.json')

# Calculate optimal dijkstra path between waypoints
rp.compute_routes('configs/waypoints_example.csv')
end = time()
print(f"Compute Time: {end - start} s")

start = time()
# Smooth the dijkstra routes
rp.compute_smoothed_routes()
end = time()
print(f"Smooth Time: {end - start} s")

route_mesh = rp.to_json()

# Save to output file
with open('output/grf_example.route.json', 'w+') as f:
    json.dump(route_mesh, f, indent=4)