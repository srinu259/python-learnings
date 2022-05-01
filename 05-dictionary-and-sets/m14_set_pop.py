from m13_prescription_data import *

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "John", "Kenny"}

# pop() removes the item arbitarily and returns the item removed
while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)
