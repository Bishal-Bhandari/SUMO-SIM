import json
import xml.etree.ElementTree as ET


xml_file_ori = 'Gaustadt_with_cars906-916/Output/tripinfo.xml' # Original Stops
xml_file_gen = 'Gaustadt_with_cars906-916_updated_stops/Output/tripinfo.xml' #Gen Stops

def convertojson1(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = []

    for person in root.findall("personinfo"):
        person_data = {attr: person.get(attr) for attr in person.attrib}

        walks = person.findall("walk")
        walk1 = {key: walks[0].get(key, "") for key in ["duration", "routeLength", "timeLoss"]} if len(walks) > 0 else {}
        walk2 = {key: walks[1].get(key, "") for key in ["duration", "routeLength", "timeLoss"]} if len(walks) > 1 else {}

        ride = person.find("ride")
        ride_data = {key: ride.get(key, "") for key in ["vehicle", "duration", "routeLength", "timeLoss"]} if ride is not None else {}

        entry = {
            "PersonInfo": person_data,
            "Walk": {"Walk1": walk1, "Walk2": walk2},
            "Ride": ride_data
        }

        data.append(entry)

    # Save for original stops---------------------------------------------------
    json_file = "Output_ods/Person/personinfo_original.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Data saved")

def convertojson2(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = []

    for person in root.findall("personinfo"):
        person_data = {attr: person.get(attr) for attr in person.attrib}

        walks = person.findall("walk")
        walk1 = {key: walks[0].get(key, "") for key in ["duration", "routeLength", "timeLoss"]} if len(
            walks) > 0 else {}
        walk2 = {key: walks[1].get(key, "") for key in ["duration", "routeLength", "timeLoss"]} if len(
            walks) > 1 else {}

        ride = person.find("ride")
        ride_data = {key: ride.get(key, "") for key in
                         ["vehicle", "duration", "routeLength", "timeLoss"]} if ride is not None else {}

        entry = {
                "PersonInfo": person_data,
                "Walk": {"Walk1": walk1, "Walk2": walk2},
                "Ride": ride_data
            }

        data.append(entry)


    # Save for Gen stops---------------------------------------------------------
    json_file = "Output_ods_updated_stop/Person/personinfo_generated.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Data saved")

convertojson1(xml_file_ori)
convertojson2(xml_file_gen)