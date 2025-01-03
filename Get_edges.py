from sumolib import checkBinary, net

# Load network
net_file = "bamberg.net.xml"
network = net.readNet(net_file)

# Start and end edges
start_edge = "38033459"
end_edge = "-199523015"

# Find connected route
try:
    route_edges, _ = network.getShortestPath(network.getEdge(start_edge), network.getEdge(end_edge))
    edge_ids = [edge.getID() for edge in route_edges]
    print("Complete Route:", " -> ".join(edge_ids))
except Exception as e:
    print(f"Error finding route: {e}")
    exit()

# Save the route as a .rou.xml file
output_file = "calculated_routes.rou.xml"
with open(output_file, "w") as f:
    f.write('<routes>\n')
    f.write('<vType id="bus" accel="1.0" decel="4.0" length="12" maxSpeed="20" color="1,0,0"/>\n')
    f.write(f'<route id="calculatedRoute" edges="{" ".join(edge_ids)}"/>\n')
    f.write('<vehicle id="bus_1" type="bus" route="calculatedRoute" depart="0" color="1,0,0"/>\n')
    f.write('</routes>\n')

print(f"Route saved to {output_file}")
