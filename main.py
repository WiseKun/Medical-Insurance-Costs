import csv
import random

# Opens the 'insurance.csv' file in read mode as 'dataset'
with open('insurance.csv', 'r') as dataset:
  dataset_dict = list(csv.DictReader(dataset))
  dataset_length = len(dataset_dict)

  # Prints a random record from the dataset
  print('Here is a random record: {}\n'.format(dataset_dict[random.randint(0, dataset_length)]))
  
  # Finds the average cost
  smoker_total = 0
  non_smoker_total = 0
  # Loop through every record in the dataset
  for record in dataset_dict:
    if record['smoker'] == 'yes':
      smoker_total += float(record['charges'])
    else:
      non_smoker_total += float(record['charges'])
  # Calculates the average cost
  smoker_average = round(smoker_total/dataset_length, 2)
  non_smoker_average = round(non_smoker_total/dataset_length, 2)

  print('Average cost for a smoker: ${}\nAverage cost for a non-smoker: ${}\n'.format(smoker_average, non_smoker_average))
