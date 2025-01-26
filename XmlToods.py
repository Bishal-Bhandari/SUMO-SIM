import xml.etree.ElementTree as ET
from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableRow, TableCell
from odf.text import P


# Function to convert XML to ODS
def xml_to_ods(xml_file, ods_file, root_tag, row_tags):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Create an ODS file
    ods = OpenDocumentSpreadsheet()
    table = Table(name="Data")
    ods.spreadsheet.addElement(table)

    # Extract data and write to ODS
    header_written = False
    for element in root.findall(root_tag):
        row_data = {}

        # Collect attributes
        for attr_name, attr_value in element.attrib.items():
            row_data[attr_name] = attr_value

        # Collect sub-element data if specified
        for tag in row_tags:
            sub_element = element.find(tag)
            if sub_element is not None:
                for sub_attr, sub_value in sub_element.attrib.items():
                    row_data[f"{tag}:{sub_attr}"] = sub_value

        # Write header
        if not header_written:
            header_row = TableRow()
            for col_name in row_data.keys():
                cell = TableCell()
                cell.addElement(P(text=col_name))
                header_row.addElement(cell)
            table.addElement(header_row)
            header_written = True

        # Write data row
        data_row = TableRow()
        for col_value in row_data.values():
            cell = TableCell()
            cell.addElement(P(text=col_value))
            data_row.addElement(cell)
        table.addElement(data_row)

    # Save the ODS file
    ods.save(ods_file)
    print(f"Converted {xml_file} to {ods_file}")


# Convert each file
xml_to_ods("emission.xml", "emission.ods", "vehicle", ["emissions"])
xml_to_ods("fcd.xml", "fcd.ods", "timestep", ["vehicle"])
xml_to_ods("tripinfo.xml", "tripinfo.ods", "tripinfo", ["emissions"])

print("All files converted successfully!")
