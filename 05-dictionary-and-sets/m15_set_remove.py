from m13_prescription_data import *

# requirement is to use edoxaban drug instead of warfarin for anti-coagulant
# John and Kenny does not use warfarin drug
trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "John", "Kenny"]
for patient in trial_patients:
    prescription = patients[patient]
    print(patient, prescription)
    # this just discards and adds warfarin drug
    # what if the trial patient does not even take warfarin ?
    # then we forcefully give him the drug, that may be dangerous!!

    # prescription.discard(warfarin)
    # prescription.add(edoxaban)
    # print(patient, prescription)

    # better to use remove, so that if drug is not used it will just throw an error!
    # much better to throw error than to give wrong drug

    # prescription.remove(warfarin)
    # prescription.add(edoxaban)
    # print(patient, prescription)

    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
        print(patient, prescription)
    else:
        print(f"Patient {patient} is not taking warfarin."
              f"Please remove {patient} from the trial")

    # python way is to use exception block
    # try:
    #     prescription.remove(warfarin)
    #     prescription.add(edoxaban)
    # except KeyError:
    #     print(f"Patient {patient} is not taking warfarin."
    #           f" Please remove {patient} from the trial")

