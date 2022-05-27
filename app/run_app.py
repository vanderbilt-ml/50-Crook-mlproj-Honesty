import pandas as pd
import argparse

from Mach import MachEntry

app_parser = argparse.ArgumentParser()

# Parse the argument for filename
app_parser.add_argument("-f", "--file", type=str, required=True, help="Filename")

args = vars(app_parser.parse_args())

# Assign the filename
filename = args['file']

# Get the data from the provided file
data = pd.read_csv(filename, sep="\t")

# Get number of rows
rows = data.shape[0]

# Get the column names
columns = data.columns.values.tolist()

# Declare list for MachEntry instances
entries = []

# Begin iterating through the rows
for x in range(len(data.index) - 1):
  # Declare placeholder for current score
  score = 0

  # Calculate score using answers to questions 1-20
  score = score + data.iloc[x]['Q1A']
  score = score + data.iloc[x]['Q2A']
  score = score + data.iloc[x]['Q3A']
  score = score + data.iloc[x]['Q4A']
  score = score + data.iloc[x]['Q5A']
  score = score + data.iloc[x]['Q6A']
  score = score + data.iloc[x]['Q7A']
  score = score + data.iloc[x]['Q8A']
  score = score + data.iloc[x]['Q9A']
  score = score + data.iloc[x]['Q10A']
  score = score + data.iloc[x]['Q11A']
  score = score + data.iloc[x]['Q12A']
  score = score + data.iloc[x]['Q13A']
  score = score + data.iloc[x]['Q14A']
  score = score + data.iloc[x]['Q15A']
  score = score + data.iloc[x]['Q16A']
  score = score + data.iloc[x]['Q17A']
  score = score + data.iloc[x]['Q18A']
  score = score + data.iloc[x]['Q19A']
  score = score + data.iloc[x]['Q20A']
  
  q6 = data.iloc[x]['Q6A']
  q7 = data.iloc[x]['Q7A']
  religion = data.iloc[x]['religion']
  tipi1 = data.iloc[x]['TIPI1']
  tipi6 = data.iloc[x]['TIPI6']
  education = data.iloc[x]['education']
  race = data.iloc[x]['race']
  age = data.iloc[x]['age']
  gender = data.iloc[x]['gender']
  
  entries.append(MachEntry(score, q6, q7, religion, tipi1, tipi6, education, race, age, gender))
  
print(len(entries))

# Iterate through our data and start storing percentages
num_high_and_rel = 0
num_high_and_rel_christ = 0
num_high_and_rel_race_white = 0

for x in entries:
  if x.GetScore() > 59 and x.GetReligion() > 2:
    num_high_and_rel = num_high_and_rel + 1
    if x.GetReligion() == 7:
      num_high_and_rel_christ = num_high_and_rel_christ + 1
      if x.GetRace() == 60:
        num_high_and_rel_race_white = num_high_and_rel_race_white + 1
      
print("Percentage of 60+ and religious: ", (num_high_and_rel / len(data.index)) * 100)
print("Percentage of 60+ and religious that are Christian: ", (num_high_and_rel_christ / num_high_and_rel) * 100)
print("Percentage of 60+, religious, Christian, and white: ", (num_high_and_rel_race_white / num_high_and_rel) * 100)

