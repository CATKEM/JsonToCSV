import json
ID_COUNTERS = {}
TRUE = 'True'
FALSE = 'False'
ID = '__id'
ROWS = 'rows'
COLUMNS = 'columns'
SEPARATOR = ','
dirFilePath = '/home/user/Downloads/'
jsonFileName = 'dataFile.json'

# removing '\n' symbols from string
remove_enters = lambda string: string.replace('\n', ' ')

# returning simple data from dict: columns + rows
get_simple_data = lambda json_element, json_element_name: get_keys_string(json_element, json_element_name) + '\n' + get_values_string(json_element, json_element_name)

# object is composite or primitive
is_composite_type = lambda element: type(element) is dict or type(element) is list


# ID counter. Need to get unique record ID
def get_record_id(table_title):
    if ID_COUNTERS.get(table_title):
        ID_COUNTERS[table_title] += 1
        return ID_COUNTERS[table_title]
    else:
        ID_COUNTERS[table_title] = 1
        return 1


# string contains dict keys with table ID column
def get_keys_string(json_element, table_name):
    columns = str(table_name) + ID
    for key in json_element:
        if is_composite_type(json_element[key]):
            continue
        columns += SEPARATOR + str(key)
    return remove_enters(columns)


# string contains dict values with table ID
def get_values_string(json_element, table_name):
    rows = str(get_record_id(table_name))
    for key in json_element:
        if is_composite_type(json_element[key]):
            continue
        rows += SEPARATOR + str(json_element[key])
    return remove_enters(rows)

# return table from list of simple dict
def get_simple_dict_list(json_element, table_name):
    columns = get_keys_string(json_element[0], table_name)
    rows = ""
    for i in range(len(json_element)):
        rows += get_values_string(json_element[i], table_name) + '\n'
    return columns + '\n' + rows


# return string contains list values
def get_list_values(data_list):
    elements_string = ''
    for element in data_list:
        elements_string += SEPARATOR + str(element)
    return remove_enters(elements_string)


# for type "value" "header" tables
def get_value_header_table(data, table_name):
    columns = table_name + ID + SEPARATOR + get_list_values(data['headers']) + '\n'
    rows = ''
    for i in range(len(data['values'])):
        rows += str(get_record_id(table_name))
        rows += get_list_values(data['values'][i]) + '\n'
    return columns + rows


def get_simple_list_data(data, table_name):
    columns = table_name + ID + ',' + table_name
    rows = ''
    for i in range(len(data)):
        rows += str(get_record_id(table_name))
        rows += SEPARATOR + str(data[i]) + '\n'
    return remove_enters(columns) + '\n' + rows


# check field exists or not. If field exists return field value. If field not exist return string "False"
def check_data_header_field(data, field_name):
    if data.get(field_name):
        return str(data[field_name])
    else:
        return FALSE


# for type "data" "header"
def get_data_header(data, table_name, additional_fields):
    columns = table_name + ID + SEPARATOR + 'header,value,' + get_list_values(additional_fields)
    rows = ''
    for i in range(len(data['data'])):
        for j in range(len(data['data'][i])):
            rows += str(get_record_id(table_name)) + SEPARATOR + str(data['headers'][j]) + SEPARATOR + str(data['data'][i][j]['value'])
            for k in range(len(additional_fields)):
                rows += SEPARATOR + check_data_header_field(data['data'][i][j], additional_fields[k])
            rows += '\n'
    return columns + '\n' + rows


def upsert_table(csv_data, table_name, columns_string):
    if not csv_data.get(table_name):
        csv_data[table_name] = {
            COLUMNS: columns_string,
            ROWS: ''
        }
    return csv_data


def get_proposedObjectives(files, data):
    PROPOSED_OBJECTIVES = 'proposedObjectives'
    STRENGTHS = 'strengths'
    OBJECTIVES = 'objectives'
    OBJECTIVES_FIELDS = 'fields'
    ORIGINAL_OBJECTIVE = 'originalObjective'
    if len(data[PROPOSED_OBJECTIVES]) == 0:
        return
    csv_data = {
        PROPOSED_OBJECTIVES: {
            COLUMNS: get_keys_string(data[PROPOSED_OBJECTIVES][0], PROPOSED_OBJECTIVES),
            ROWS: ''
        }
    }
    for proposed_objective in data[PROPOSED_OBJECTIVES]:
        csv_data[PROPOSED_OBJECTIVES][ROWS] += get_values_string(proposed_objective, PROPOSED_OBJECTIVES)
        if proposed_objective.get(STRENGTHS) and len(proposed_objective[STRENGTHS]) > 0:
            upsert_table(csv_data, STRENGTHS, STRENGTHS + ID + SEPARATOR + STRENGTHS)
            csv_data[STRENGTHS][ROWS] += str(get_record_id(STRENGTHS)) + SEPARATOR + get_list_values(proposed_objective[STRENGTHS])

        if proposed_objective.get(OBJECTIVES) and len(proposed_objective[OBJECTIVES]) > 0:
            upsert_table(csv_data, OBJECTIVES, get_keys_string(proposed_objective[OBJECTIVES][0], OBJECTIVES))
            for objective in proposed_objective[OBJECTIVES]:
                csv_data[OBJECTIVES][ROWS] += get_values_string(objective, OBJECTIVES)
                if objective.get(OBJECTIVES_FIELDS) and len(objective[OBJECTIVES_FIELDS]) > 0:
                    upsert_table(csv_data, OBJECTIVES_FIELDS, OBJECTIVES_FIELDS + ID + SEPARATOR)
                    csv_data[OBJECTIVES_FIELDS][ROWS] += str(get_record_id(OBJECTIVES_FIELDS))
    print('+++++++++++++++++++++++++++++++')
    print(csv_data[STRENGTHS])



def json_to_csv(data):
    files = {
        'main': get_simple_data(data, 'main'),
        'client': get_simple_data(data['client'], 'client'),
        'programDescription': get_simple_data(data['programDescription'], 'programDescription'),
        'staffRolesAndSupervision': get_simple_data(data['staffRolesAndSupervision'], 'staffRolesAndSupervision'),
        'familyParticipationInProgram.': get_simple_data(data['familyParticipationInProgram'], 'familyParticipationInProgram'),
        'persons': get_simple_dict_list(data['persons'], 'persons'),
        'recommendations': get_simple_data(data['recommendations'], 'recommendations'),
        'authorizationRequestData': get_value_header_table(data['recommendations']['authorizationRequestData'], 'authorizationRequestData'),
        'assessmentResults': get_simple_data(data['assessmentResults'], 'assessmentResults'),
        'services': get_value_header_table(data['assessmentResults']['services'], 'services'),
        'vineland': get_simple_data(data['assessmentResults']['vineland'], 'vineland'),
        'info': get_simple_data(data['assessmentResults']['vineland']['info'], 'info'),
        'proposedObjectives': get_simple_dict_list(data['proposedObjectives'], 'proposedObjectives'),
        'educationalServices':get_value_header_table(data['assessmentResults']['educationalServices'], 'educationalServices'),
        'backgroundAndMethodology': get_value_header_table(data['backgroundAndMethodology']['assessmentAppointments'], 'assessmentAppointments'),
        'academicPerformance.csv': get_simple_data(data['assessmentResults']['academicPerformance'], 'academicPerformance'),
        'backgroundAndMethodology_assessmentResults': get_simple_list_data(data['backgroundAndMethodology']['assessmentResults'], 'assessmentResults'),
        'reviewedRecords': get_simple_list_data(data['assessmentResults']['reviewedRecords'], 'reviewedRecords'),
        'scoreSummary': get_data_header(data['assessmentResults']['vineland']['scoreSummary'], 'scoreSummary', ['header', 'editable']),
        'domainsDetails': get_data_header(data['assessmentResults']['vineland']['domainDetails'], 'domainDetails', ['header', 'subHeader', 'italic', 'editable']),
        'maladaptiveBehaviorIndex': get_data_header(data['assessmentResults']['vineland']['maladaptiveBehaviorIndex'], 'maladaptiveBehaviorIndex', ['type', 'placeholder', 'editable', 'header', 'subHeader']),
    }
    get_proposedObjectives(files, data)
    for key in files:
        print('-----------------------------------------------------')
        print('KEY: ' + str(key))
        print(str(files[key]))


with open(dirFilePath + jsonFileName) as jsonFile:
    jsonFileData = json.load(jsonFile)
json_to_csv(jsonFileData)