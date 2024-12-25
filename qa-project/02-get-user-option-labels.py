# do not remove the execute function
import json
def execute(req_uo_meta_str,req_uo_str,req_uo_prop_desc_str):
    # code goes here
    req_uo_json = json.loads(req_uo_str)

    req_uo_meta_str = req_uo_meta_str[:-1]
    req_uo_meta_str = req_uo_meta_str[1:]
    req_uo_meta_json = json.loads(req_uo_meta_str)

    req_uo_prop_desc_str = req_uo_prop_desc_str[1:-1]
    req_uo_prop_desc_str = req_uo_prop_desc_str.split(',')


    index = 0
    temp_json = ''
    temp_localized_label = ''
    error_msg = 'no error msg'

    y = convert_list_2_dict(req_uo_prop_desc_str)
    print(y)


    for key, value in req_uo_json.items():
        try:
            temp_value = str(req_uo_meta_json[key.strip()])
            temp_localized_label = str(y[temp_value])
            #temp_localized_label_key = str(y[key])
        except Exception as error:
            error_msg = error_msg + str(error)+'-->key not found'
            temp_value = ''
        try:
            temp_key = key+'.'+value.strip()
            temp_label_value = str(req_uo_meta_json[temp_key])
        except Exception as error:
            error_msg = error_msg + temp_key+' --- '+str(error)+'-->key not found\n'
            temp_label_value = ''

        #temp_json = temp_value+' --- '+temp_localized_label
        if (temp_value):
            temp_json = temp_json + '{"Code":"'+str(temp_value)+'", "Seq":"'+str(index+1)+'", "Name":"'+str(temp_value)+'", "Value":"'+temp_label_value+'"}\n'
        index = index + 1
    res = str(len(req_uo_json))
    return {"res": temp_json}

def convert_list_2_dict(my_list):
    res_dict = {}
    for i in range(0, len(my_list), 2):
        res_dict[my_list[i]] = my_list[i+1]
    return res_dict


print(execute('[{"AccessType_c.Modify_c": "Modify", "ServiceType_c": "Service Type", "user_options_metadata_messages5a96f3e8-e736-43f2-87d4-6c736e44bacc": "Access Type", "DataSensitivityLevel_c": "Data sensitivity Level", "user_options_metadata_messagesf64ab4c4-0484-4cb3-a701-53b1d02e25ed": "", "user_options_metadata_messagesa76f3bab-ee41-4816-b73b-8841645ea4b9": "", "user_options_metadata_messages467f0eca-a088-4a10-982e-cd66d6536b9d": "Start Date", "user_options_metadata_messages34f43195-0f35-4b0b-a3f5-00ac7cf63f01": "End Date should not be more than 1 year from now.", "user_options_metadata_messages_cdd58538-4688-42cb-bbaf-c98a335e716e": "UserOption625790a006f010015dcbca11c9febfa75df6_c", "Name": "Name", "user_options_metadata_messages5640f1de-8ad3-4204-9125-cfa54823c9b8": "End Date", "AccessType_c.Grant_c": "Grant", "DatasensitivityLevel_c.SensitiveOrConfidentialData_c": "Sensitive/Confidential data", "ServiceType_c.BooleBox_c": "BooleBox", "AccessType_c.Revoke_c": "Revoke", "user_options_metadata_messagesb7d1d4dc-d4d7-495f-9b1d-1052d4a8e363": "", "DatasensitivityLevel_c.InternalsharingorNonsensitive_c": "Internal sharing or Non sensitive Data", "user_options_metadata_messagese85a6d7f-ff81-4c39-9096-29375b4d1a3c": "Service Type", "user_options_metadata_messages93f08aa8-31ef-4421-b053-9547fb58f79a": "", "AccessType_c": "Access Type", "user_options_metadata_messagesb517a38b-9192-4dd2-9d2c-d4a177171e65": "Data sensitivity Level", "ServiceType_c.QBox_c": "QBox"}]',        '{"AccessType_c": "Grant_c", "DataSensitivityLevel_c": "InternalsharingorNonsensitive_c", "DurationOfAccess_c": 1723833000000, "DynamicComplexTypeRefName_c": "UserOption625790a006f010015dcbca11c9febfa75df6_c", "ServiceType_c": "QBox_c", "StartDate_c": 1723635319094, "history_Offering_Base_Price_validation_key": "wZnqEh60sOIQn0jsJ+xSiwMhfAOCWNPVQNFm1xyFyao=", "history_Offering_User_Options_Price_validation_key": "QzwhGAT3/cAJSF2me+Pg9UQf1Lgmgm4W4WFiDAUUVnk="}',        '["DataSensitivityLevel_c", "user_options_metadata_messagesb517a38b-9192-4dd2-9d2c-d4a177171e65", "ServiceType_c", "user_options_metadata_messagese85a6d7f-ff81-4c39-9096-29375b4d1a3c", "AccessType_c", "user_options_metadata_messages5a96f3e8-e736-43f2-87d4-6c736e44bacc", "StartDate_c", "user_options_metadata_messages467f0eca-a088-4a10-982e-cd66d6536b9d", "DurationOfAccess_c", "user_options_metadata_messages5640f1de-8ad3-4204-9125-cfa54823c9b8", "DynamicComplexTypeRefName_c", "Name", "DynamicComplexTypeRefName_c", "Name"]'))