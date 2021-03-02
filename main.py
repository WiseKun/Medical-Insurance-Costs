import csv
import random

# Create new class to convert each piece of data to a more useable format
class InsuranceRecord:
  def __init__(self, age, sex, bmi, children, smoker, region, charges):
    self.age = int(age)
    self.sex = 0 if sex=='female' else 1
    self.bmi = float(bmi)
    self.children = int(children)
    self.smoker = True if smoker=='yes' else False
    self.region = region
    self.charges = round(float(charges), 2)

  # Returns the newly made dictionary
  def return_record(self):
    return {'Age': self.age, 'Sex': self.sex, 'BMI': self.bmi, 'Children': self.children, 'Smoker': self.smoker, 'Region': self.region, 'Charges': self.charges}

def analyse_smoker(dataset):
  dataset_length = len(dataset)
  # Finds the average cost
  smoker_total = 0
  non_smoker_total = 0
  # Loop through every record in the dataset
  for record in dataset:
    if record['Smoker']:
      smoker_total += float(record['Charges'])
    else:
      non_smoker_total += float(record['Charges'])
  # Calculates the average cost
  smoker_average = round(smoker_total/dataset_length, 2)
  non_smoker_average = round(non_smoker_total/dataset_length, 2)

  return smoker_average, non_smoker_average

# Opens the 'insurance.csv' file in read mode as 'dataset'
with open('insurance.csv', 'r') as dataset:
  dataset_dict = list(csv.DictReader(dataset))
  dataset_length = len(dataset_dict)

  # Convert records to instances of the class 'InsuranceRecord'
  new_dataset = []
  for i in range(dataset_length):
    cur = dataset_dict[i]
    new_dataset.append(InsuranceRecord(cur['age'], cur['sex'], cur['bmi'], cur['children'], cur['smoker'], cur['region'], cur['charges']).return_record())

  # Prints a random record from the dataset
  print('Here is a random record: {}\n'.format(new_dataset[random.randint(0, dataset_length)]))

  # Prints the average cost for smokers and non-smokers
  smoker_average, non_smoker_average = analyse_smoker(new_dataset)
  print('Average cost for a smoker: ${}\nAverage cost for a non-smoker: ${}\n'.format(smoker_average, non_smoker_average))
