from sumolib import checkBinary, net

# Load the network file
net_file = "bamberg.net.xml"
network = net.readNet(net_file)

# Define the edges for your specific route
route_edges = ["edge1", "edge2", "edge3", "edge4"]

# Print details of the selected route
for edge_id in route_edges:
    edge = network.getEdge(edge_id)
    print(f"Edge: {edge_id}, Length: {edge.getLength()}")

# Save route to a file
with open("selected_routes.rou.xml", "w") as f:
    f.write('<routes>\n')
    f.write('<vType id="bus" accel="1.0" decel="4.0" length="12" maxSpeed="20" color="1,0,0"/>\n')
    f.write(f'<route id="selectedRoute" edges="{" ".join(route_edges)}"/>\n')
    f.write('<vehicle id="bus_1" type="bus" route="selectedRoute" depart="0" color="1,0,0"/>\n')
    f.write('</routes>')
