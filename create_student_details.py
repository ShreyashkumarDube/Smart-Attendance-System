import os
import pandas as pd

# Ensure the StudentDetails directory exists
if not os.path.exists("StudentDetails"):
    os.makedirs("StudentDetails")

# Create a sample StudentDetails.csv file
data = {
    "Id": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
}
df = pd.DataFrame(data)
df.to_csv("StudentDetails" + os.sep + "StudentDetails.csv", index=False)
print("StudentDetails.csv file created successfully.")