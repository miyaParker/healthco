import random


def id_generator():
    random_number = random.randint(100, 999)
    next_random_number = random.randint(1000, 9999)
    id = '323' + '-'+str(random_number) + '-'+'10'+str(next_random_number)
    return id


def bmi_calculator(weight, height):
    status = ['underweight', 'normal weight', 'overweight', 'obesity']
    bmi = int(weight)/int(height)/int(height)*10000
    if bmi == 30 or bmi > 30:
        return status[3]
    elif bmi > 25:
        return status[2]
    elif bmi > 18.5:
        return status[1]
    else:
        return status[0]

blood_types=[
    'O+',
    'O-',
    'A+',
    'A-',
    'B+',
    'B-',
    'AB+',
    'AB-'
]
disease = [
    'General',
    'Dermatology',
    'Infectious Diseases',
    'Neurology',
    'Gynecology',
    'Pediatrics',
    'Cardiology'
]
