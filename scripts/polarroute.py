# import json
from polar_route.route_planner import RoutePlanner


rp = RoutePlanner('../experiments/example_data/vessel_output_file.json',
                  '../experiments/example_data/traveltime.config.json',
                  '../experiments/example_data/waypoints_example.csv')

# Calculate optimal dijkstra path between waypoints
rp.compute_routes()
# Smooth the dijkstra routes
rp.compute_smoothed_routes()

route_mesh = rp.to_json()
# Save to output file
# with open('./example.route.json', 'w+') as f:
#     json.dump(route_mesh, f, indent=4)