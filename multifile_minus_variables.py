"""Variables to initiate in Flow:
input_var = 6
"""

import pandas as pd
from multifile_import_from import var_from_external_file

df = pd.read_csv("multifile_materials.csv")
ally = df["Youngs (Gpa)"][3]
# input_var = 6

result = (var_from_external_file * 2) + ally + input_var
print(result)
