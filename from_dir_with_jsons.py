import pandas as pd
import os
import json

# Goal:
# Traverse folders to get all JSON files
# Find the way to read them so that Pandas understands
# Try to produce identical DataFrame as for CSV

# from_records() method takes a list of tuples in which each tuple represents
# one record in the dataframe

records = [("Espresso", "5$"),("Flat White", "10$")]
pd.DataFrame.from_records(records)
pd.DataFrame.from_records(records, columns=["Coffee", "Price"])

KEYS_TO_USE = ["id", "all_artists", "title", "medium", "acquisitionYear",
               "height", "width"]

def get_record_from_file(file_path, keys_to_use):
    """ Process single json file and return a tuple containing specific
    fields."""

    with open(file_path) as artwork_file:
        content = json.load(artwork_file)

    record = []
    for field in keys_to_use:
        record.append(content[field])

    return tuple(record)

# Single file processing function demo
SAMPLE_JSON = os.path.join(".", "collection-master", "artworks", "a", "000",
                           "a00001-1035.json")

# print(SAMPLE_JSON)
# ./collection-master/artworks/a/000/a00001-1035.json

sample_record = get_record_from_file(SAMPLE_JSON, KEYS_TO_USE)
# print(sample_record)
# (1035, 'Robert Blake', 'A Figure Bowing before a Seated Old Man with his Arm
# Outstretched in Benediction. Verso: Indecipherable Sketch', 'Watercolour, ink,
# chalk and graphite on paper. Verso: graphite on paper', 1922, '419', '394')

def read_artworks_from_json(keys_to_use):
    """ Traverse the directories with JSON files.
    For first file in each directory call function
    for processing single file and go to the next
    directory
    """
    JSON_ROOT = os.path.join(".", "collection-master", "artworks", "a")

    artworks = []
    for root, _, files in os.walk(JSON_ROOT):
        for f in files:
            if f.endswith("json"):
                record = get_record_from_file(
                    os.path.join(root, f),
                    keys_to_use)
                artworks.append(record)
            break

    df = pd.DataFrame.from_records(artworks,
                                   columns=keys_to_use,
                                   index="id")
    return df

def save_for_later(df):
    # Save for later
    df.to_pickle(os.path.join(".", "data_frame_js.pickle"))

if __name__ == "__main__":
    samples = read_artworks_from_json(KEYS_TO_USE)
    print(samples)
    save_for_later(samples)