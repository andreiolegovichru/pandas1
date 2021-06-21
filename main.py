import pandas as pd
import os
import json

# Goal:
# calculate how many different artists are in the df

df = pd.read_pickle(os.path.join(".", "data_frame_js.pickle"))

# All artists in df
artists = df["artist"]

# Unique artists in df
pd.unique(artists)

df["artist"] == "Blake, Robert"
s = df["artist"] == "Blake, Robert"
s.value_counts()

# print(s.value_counts())
# False    111
# True       4
# Name: artist, dtype: int64

artist_counts = df["artist"].value_counts()
# artist_counts
# Burne-Jones, Sir Edward Coley, Bt    54
# Blake, William                       50
# British School 18th century           6
# Blake, Robert                         4
# Richmond, George                      1
# Name: artist, dtype: int64

artist_counts["Blake, Robert"]
# 4

# df.loc[Row indexer, Column indexer]
df.loc[1035, "artist"]
# 'Blake, Robert'

# : means all the columns
df.loc[df["artist"] == "Blake, Robert", :]
#              artist  ... units
# id                   ...
# 1035  Blake, Robert  ...    mm
# 1036  Blake, Robert  ...    mm
# 1037  Blake, Robert  ...    mm
# 1038  Blake, Robert  ...    mm
# [4 rows x 8 columns]

# iloc is using indexes
df.iloc[100:300, [0,1,4]]
#                                   artist  ... acquisitionYear
# id                                        ...
# 1737   Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 1738   Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 1739   Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 20231  Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 1740   Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 1741   Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 20233  Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 1742   Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 1743   Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 1744   Burne-Jones, Sir Edward Coley, Bt  ...            1927
# 1118                      Blake, William  ...            1924
# 19411                     Blake, William  ...            1924
# 19412                     Blake, William  ...            1924
# 19413                     Blake, William  ...            1924
# 19414                     Blake, William  ...            1924
# [15 rows x 3 columns]

df.iloc[0, 0]
# 'Blake, Robert'

df.iloc[0, :]
# artist                                                 Blake, Robert
# title              A Figure Bowing before a Seated Old Man with h...
# medium             Watercolour, ink, chalk and graphite on paper....
# year                                                             NaN
# acquisitionYear                                                 1922
# width                                                          394.0
# height                                                         419.0
# units                                                             mm
# Name: 1035, dtype: object

df.iloc[0:2, 0:2]
#              artist                                              title
# id
# 1035  Blake, Robert  A Figure Bowing before a Seated Old Man with h...
# 1036  Blake, Robert  Two Drawings of Frightened Figures, Probably f...


# Goal:
# Find painting with biggest area
# Try multiplication

df["height"] * df["width"]
# id
# 1035     165086.0
# 1036      66243.0
# 1037     160181.0
# 1038     125292.0
# 1039      81405.0
#            ...
# 1118       5208.0
# 19411      2812.0
# 19412      2475.0
# 19413      2409.0
# 19414      2628.0
# Length: 115, dtype: float64

# In full df it will not work due to dirty data
df["height"] * df["width"]
# Traceback (most recent call last):
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/ops/array_ops.py", line 142, in _na_arithmetic_op
#     result = expressions.evaluate(op, left, right)
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/computation/expressions.py", line 235, in evaluate
#     return _evaluate(op, op_str, a, b)  # type: ignore[misc]
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/computation/expressions.py", line 69, in _evaluate_standard
#     return op(a, b)
# TypeError: can't multiply sequence by non-int of type 'float'
# During handling of the above exception, another exception occurred:
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/ops/common.py", line 65, in new_method
#     return method(self, other)
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/arraylike.py", line 105, in __mul__
#     return self._arith_method(other, operator.mul)
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/series.py", line 4998, in _arith_method
#     result = ops.arithmetic_op(lvalues, rvalues, op)
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/ops/array_ops.py", line 189, in arithmetic_op
#     res_values = _na_arithmetic_op(lvalues, rvalues, op)
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/ops/array_ops.py", line 149, in _na_arithmetic_op
#     result = _masked_arith_op(left, right, op)
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/ops/array_ops.py", line 91, in _masked_arith_op
#     result[mask] = op(xrav[mask], yrav[mask])
# TypeError: can't multiply sequence by non-int of type 'float'


df["width"].sort_values().head()
# id
# 20822            (1):
# 105337    (diameter):
# 98671         (each):
# 76420         (each):
# 91391        (image):
# Name: width, dtype: object

pd.to_numeric(df["width"])
# Traceback (most recent call last):
#   File "pandas/_libs/lib.pyx", line 2062, in pandas._libs.lib.maybe_convert_numeric
# ValueError: Unable to parse string "(upper):"
# During handling of the above exception, another exception occurred:
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "/home/avorotyn/gitlab/perf_test/pycharm/pandas1/myenv/lib/python3.8/site-packages/pandas/core/tools/numeric.py", line 154, in to_numeric
#     values = lib.maybe_convert_numeric(
#   File "pandas/_libs/lib.pyx", line 2099, in pandas._libs.lib.maybe_convert_numeric
# ValueError: Unable to parse string "(upper):" at position 1839

pd.to_numeric(df["width"], errors="coerce")
# id
# 1035      394.0
# 1036      311.0
# 1037      343.0
# 1038      318.0
# 1039      243.0
#           ...
# 122960    305.0
# 122961    305.0
# 121181     45.0
# 112306      NaN
# 127035    508.0
# Name: width, Length: 69201, dtype: float64

df.loc[:, "width"] = pd.to_numeric(df["width"], errors="coerce")
df.loc[:, "height"] = pd.to_numeric(df["height"], errors="coerce")
df["height"] * df["width"]
# id
# 1035      165086.0
# 1036       66243.0
# 1037      160181.0
# 1038      125292.0
# 1039       81405.0
#             ...
# 122960     93025.0
# 122961     93025.0
# 121181    108450.0
# 112306         NaN
# 127035    335280.0
# Length: 69201, dtype: float64

df["units"].value_counts()
# mm    65860
# Name: units, dtype: int64

# Assign - create new columns with size
area = df["height"] * df["width"]

df = df.assign(area=area)

df["area"].max()
# 132462000.0

df["area"].idxmax()
# 98367

df.loc[df["area"].idxmax(), :]
# artist                               Therrien, Robert
# title                No Title (Table and Four Chairs)
# medium             Aluminium, steel, wood and plastic
# year                                           2003.0
# acquisitionYear                                2008.0
# width                                          8920.0
# height                                        14850.0
# units                                              mm
# area                                      132462000.0
# Name: 98367, dtype: object

if __name__ == "__main__":
    main()
