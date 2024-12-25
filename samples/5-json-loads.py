import json

temp = '''
{
    "AccessType_c":"Grant_c",
    "DataSensitivityLevel_c":"InternalsharingorNonsensitive_c",
    "DurationOfAccess_c":1723833000000,
    "DynamicComplexTypeRefName_c":"UserOption625790a006f010015dcbca11c9febfa75df6_c",
    "ServiceType_c":"QBox_c",
    "StartDate_c":1723635319094,
    "changedUserOptionsForSimulation":"",
    "history_Offering_Base_Price":"",
    "history_Offering_Base_Price_validation_key":"wZnqEh60sOIQn0jsJ+xSiwMhfAOCWNPVQNFm1xyFyao=",
    "history_Offering_User_Options_Price_validation_key":"QzwhGAT3/cAJSF2me+Pg9UQf1Lgmgm4W4WFiDAUUVnk="
}'''

print(json.loads(temp))