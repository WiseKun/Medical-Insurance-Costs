import csv
import random

# Opens the 'insurance.csv' file in read mode as 'dataset'
with open('insurance.csv', 'r') as dataset:
  dataset_dict = list(csv.DictReader(dataset))
  dataset_length = len(dataset_dict)

  # Prints a random record from the dataset
  print('Here is a random record: {}\n'.format(dataset_dict[random.randint(0, dataset_length)]))
