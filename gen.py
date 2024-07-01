import pandas as pd
import random

# Define the number of rows for the dataset
num_rows = 500

# Generate random ratings from 1 to 5 for each subject for each student for 10th class
data_10th = {
    'Maths': [random.randint(1, 5) for _ in range(num_rows)],
    'Physics': [random.randint(1, 5) for _ in range(num_rows)],
    'Bio': [random.randint(1, 5) for _ in range(num_rows)],
    'Chemistry': [random.randint(1, 5) for _ in range(num_rows)]
}

# Map the ratings to the fields for 10th class
def map_field_10th(row):
    maths = row[0]
    physics = row[1]
    bio = row[2]
    chemistry = row[3]
    
    if maths >= 3 and bio >= 3 and physics >= 3 and chemistry >= 3:
        return 'PCM/PCB/PCMB'
    elif maths >= 3 and bio < 3 and (physics >= 3 or chemistry >= 3):
        return 'PCM'
    elif bio >= 3 and maths < 3 and (physics >= 3 or chemistry >= 3):
        return 'PCB'
    elif (physics >= 3 or chemistry >= 3) and maths < 3 and bio < 3:
        return 'PCM/PCB/Commerce'
    elif (physics <= 3 or chemistry <= 3) and maths > 3 and bio > 3:
        return 'PCM/PCB/Commerce'
    else:
        return 'Commerce'
    
# Add a column for the field based on the ratings for 10th class
field_data_10th = []
for i in range(num_rows):
    row = [data_10th['Maths'][i], data_10th['Physics'][i], data_10th['Bio'][i], data_10th['Chemistry'][i]]
    field_data_10th.append(map_field_10th(row))

data_10th['Fields_10th'] = field_data_10th

# Create a DataFrame for 10th class from the generated data
df_10th = pd.DataFrame(data_10th)

# Save the DataFrame for 10th class to a CSV file
df_10th.to_csv('C:\\Users\\Adarsh Pandey\\Documents\\Programs\\Career Prediction System\\generated_dataset_10th.csv', index=False)
