import csv
import random

# Function that converts data to more useable format
def change_data(data):
  age = int(data['age'])
  sex = 0 if data['sex'] == 'female' else 1
  bmi = float(data['bmi'])
  children = int(data['children'])
  smoker = True if data['smoker'] == 'yes' else False
  charges = round(float(data['charges']), 2)
  return {'Age': age, 'Sex': sex, 'BMI': bmi, 'Children': children, 'Smoker': smoker, 'Region': data['region'], 'Charges': charges}

def analyse_smoker(dataset):
  # Finds the average cost
  smoker_total, num_of_smoker, non_smoker_total, num_of_non_smoker = 0, 0, 0, 0
  # Loop through every record in the dataset
  for record in dataset:
    smoker = record['Smoker']
    charges = record['Charges']
    if smoker:
      smoker_total += charges
      num_of_smoker += 1
    else:
      non_smoker_total += charges
      num_of_non_smoker += 1
  # Calculates the average cost
  smoker_average = round(smoker_total/num_of_smoker, 2)
  non_smoker_average = round(non_smoker_total/num_of_non_smoker, 2)

  return smoker_average, non_smoker_average

def analyze_bmi(dataset):
  # Finds the average cost
  underweight_total, num_of_underweight, healthy_total, num_of_healthy, overweight_total, num_of_overweight, obese_total, num_of_obese = 0, 0, 0, 0, 0, 0, 0, 0
  # Loop through every record in the dataset
  for record in dataset:
    bmi = record['BMI']
    charges = record['Charges']
    # If the person is underweight
    if bmi < 18.5:
      underweight_total += charges
      num_of_underweight += 1
    # Else if the person is healthy weight
    elif bmi < 24.9:
      healthy_total += charges
      num_of_healthy += 1
    # Else if the person is overweight
    elif bmi < 29.9:
      overweight_total += charges
      num_of_overweight += 1
    # Else the person is obese
    else:
      obese_total += charges
      num_of_obese += 1
  # Calculate the average cost
  underweight_average = round(underweight_total/num_of_underweight, 2)
  healthy_average = round(healthy_total/num_of_healthy, 2)
  overweight_average = round(overweight_total/num_of_overweight, 2)
  obese_average = round(obese_total/num_of_obese, 2)

  # Return the calculated averages
  return underweight_average, healthy_average, overweight_average, obese_average

# Opens the 'insurance.csv' file in read mode as dataset
with open('insurance.csv', 'r') as dataset:
  dataset_dict = list(csv.DictReader(dataset))
  dataset_length = len(dataset_dict)

  # Convert records a more useable format
  new_dataset = []
  for i in range(dataset_length):
    cur = dataset_dict[i]
    new_cur = change_data(cur)
    new_dataset.append(new_cur)

  # Prints a random record from the dataset
  print('Here is a random record: {}\n'.format(new_dataset[random.randint(0, dataset_length)]))

  # Prints the average cost for smokers and non-smokers
  smoker_average, non_smoker_average = analyse_smoker(new_dataset)
  print('Average cost for a smoker: ${}\nAverage cost for a non-smoker: ${}\n'.format(smoker_average, non_smoker_average))
  # We can see that whether or not someone smokes has a VERY BIG role in determining medical insurance cost.

  # Prints the average cost for underweight, healthy, overweight and obese records
  underweight_average, healthy_average, overweight_average, obese_average = analyze_bmi(new_dataset)
  print('Average cost for underweight: ${}\nAverage cost for healthy: ${}\nAverage cost for overweight: ${}\nAverage cost for obese: ${}\n'.format(underweight_average, healthy_average, overweight_average, obese_average))
  # This shows us that weight has a very big role in determining medical insurance cost. The lower the weight, the lower the cost.
