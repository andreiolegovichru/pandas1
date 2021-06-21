import pandas as pd
import os

CSV_PATH = os.path.join(".", "collection-master", "artwork_data.csv")
print(CSV_PATH)
# pandas will create its own index column - Index
df = pd.read_csv(CSV_PATH, nrows=5)

# pandas will use existing column "id" as an index column
df = pd.read_csv(CSV_PATH, nrows=5, index_col="id")

# see only "artist" column
df = pd.read_csv(CSV_PATH, nrows=5, index_col="id", usecols=["id", "artist"])


# same result can be achieved
df = pd.read_csv(CSV_PATH, nrows=5, index_col="id", usecols=[0, 2])

COLS_TO_USE = ["id", "artist", "title", "medium", "year", "acquisitionYear",
               "height", "width", "units"]

df = pd.read_csv(CSV_PATH, nrows=5, index_col="id", usecols=COLS_TO_USE)

# Save for later
df.to_pickle(os.path.join(".", "data_frame.pickle"))