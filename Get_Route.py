from sumolib import net

# network file
net_file = "bamberg.net.xml"
network = net.readNet(net_file)

# the edges for route
route_edges = ["edge1", "edge2", "edge3", "edge4"]

# Initialize total length
total_length = 0

# details of the selected route
# Process the route edges
print("Route Details:")
for edge_id in route_edges:
    edge = network.getEdge(edge_id)
    edge_length = edge.getLength()
    total_length += edge_length
    print(f"Edge: {edge_id}, Length: {edge_length:.2f} meters")

# Print total route length
print(f"\nTotal Route Length: {total_length:.2f} meters")

# Save route to file
with open("selected_routes.rou.xml", "w") as f:
    f.write('<routes>\n')
    f.write('<vType id="bus" accel="1.0" decel="4.0" length="12" maxSpeed="20" color="1,0,0"/>\n')
    f.write(f'<route id="selectedRoute" edges="{" ".join(route_edges)}"/>\n')
    f.write('<vehicle id="bus_1" type="bus" route="selectedRoute" depart="0" color="1,0,0"/>\n')
    f.write('</routes>')
