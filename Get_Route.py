import xml.etree.ElementTree as ET

def filter_trips(input_file, output_file, edge_ids):
    """
    Filters trips from the input .xml file based on specified edge IDs
    and saves the result to a new file.

    Args:
        input_file (str): Path to the input .xml file.
        output_file (str): Path to the output .xml file.
        edge_ids (list): List of edge IDs to filter trips.
    """
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create a new root for filtered trips
    filtered_root = ET.Element(root.tag, root.attrib)

    # Find and copy trips that match the specified edges
    for trip in root.findall("trip"):
        from_edge = trip.get("from")
        to_edge = trip.get("to")
        if from_edge in edge_ids or to_edge in edge_ids:
            filtered_root.append(trip)

    # Write the filtered trips to the output file
    tree = ET.ElementTree(filtered_root)
    tree.write(output_file, encoding="UTF-8", xml_declaration=True)
    print(f"Filtered trips saved to {output_file}")

# Example usage
if __name__ == "__main__":
    # Input and output file paths
    input_file = "/mnt/data/osm.bus.trips.xml"  # Replace with your file path
    output_file = "/mnt/data/filtered_bus_trips.xml"

    # List of edge IDs to filter
    edge_ids = ["192895886", "-117351202", "-30784382#1", "-27164212"]  # Replace with desired edges

    # Call the function
    filter_trips(input_file, output_file, edge_ids)
