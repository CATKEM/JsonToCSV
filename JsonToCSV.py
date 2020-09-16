from Table import Table
import json

dirFilePath = '/home/user/Downloads/'
jsonFileName = 'dataFile.json'
tables = []


with open(dirFilePath + jsonFileName) as jsonFile:
    data = json.load(jsonFile)


main_table = Table('main_table')
main_table.add_column_from_dict(data)
main_table.add_rows_from_dict(data)
tables.append(main_table)

if data.get('client'):
    client_table = Table('client')
    client_table.add_column_from_dict(data['client'])
    client_table.add_rows_from_dict(data['client'])
    tables.append(client_table)

if data.get('recommendations'):
    recommendations_table = Table('recommendations')
    recommendations_table.add_column_from_dict(data['recommendations'])
    recommendations_table.add_rows_from_dict(data['recommendations'])
    tables.append(recommendations_table)

if data.get('persons'):
    persons_table = Table('persons')
    for i in range(len(data['persons'])):
        if not persons_table.columns_added:
            persons_table.add_column_from_dict(data['persons'][i])
        persons_table.add_rows_from_dict(data['persons'][i])
    tables.append(persons_table)

if data.get('recommendations'):
    recommendations_table = Table('recommendations')
    recommendations_table.add_column_from_dict(data['recommendations'])
    recommendations_table.add_rows_from_dict(data['recommendations'])
    tables.append(recommendations_table)

    if data['recommendations'].get('authorizationRequestData'):
        authorizationRequestData__table = Table('authorizationRequestData')
        authorizationRequestData__table.add_columns(data['recommendations']['authorizationRequestData']['headers'])
        authorizationRequestData__table.add_rows_from_value_headers_type(data['recommendations']['authorizationRequestData']['values'])
        tables.append(authorizationRequestData__table)

if data.get('familyParticipationInProgram'):
    familyParticipationInProgram_table = Table('family_participation_in_program')
    familyParticipationInProgram_table.add_column_from_dict(data['familyParticipationInProgram'])
    familyParticipationInProgram_table.add_rows_from_dict(data['familyParticipationInProgram'])
    tables.append(familyParticipationInProgram_table)

if data.get('staffRolesAndSupervision'):
    staffRolesAndSupervision_table = Table('staff_roles_and_supervision')
    staffRolesAndSupervision_table.add_column_from_dict(data['staffRolesAndSupervision'])
    staffRolesAndSupervision_table.add_rows_from_dict(data['staffRolesAndSupervision'])
    tables.append(staffRolesAndSupervision_table)

if data.get('programDescription'):
    programDescription_table = Table('program_description')
    programDescription_table.add_column_from_dict(data['programDescription'])
    programDescription_table.add_rows_from_dict(data['programDescription'])
    tables.append(programDescription_table)

if data.get('assessmentResults'):
    assessmentResults = data['assessmentResults']
    assessmentResults_table = Table('assessment_results')
    assessmentResults_table.add_column_from_dict(assessmentResults)
    assessmentResults_table.add_rows_from_dict(assessmentResults)

    if assessmentResults.get('services'):
        assessmentResults_services_table = Table('assessment_results_services')
        assessmentResults_services_table.add_columns(assessmentResults['services']['headers'])
        assessmentResults_services_table.add_rows_from_value_headers_type(assessmentResults['services']['values'])
        tables.append(assessmentResults_services_table)

    if assessmentResults.get('educationalServices'):
        educationalServices_table = Table('educational_services')
        educationalServices_table.add_columns(assessmentResults['educationalServices']['headers'])
        educationalServices_table.add_rows_from_value_headers_type(assessmentResults['educationalServices']['values'])
        tables.append(educationalServices_table)

    if assessmentResults.get('academicPerformance'):
        academicPerformance_table = Table('academic_performance')
        academicPerformance_table.add_column_from_dict(assessmentResults['academicPerformance'])
        academicPerformance_table.add_rows_from_dict(assessmentResults['academicPerformance'])
        tables.append(academicPerformance_table)

    if assessmentResults.get('reviewedRecords'):
        reviewedRecords_table = Table('reviewed_records')
        reviewedRecords_table.add_column('reviewedRecord')
        reviewedRecords_table.add_string_list_rows(assessmentResults['reviewedRecords'])
        tables.append(reviewedRecords_table)

    if assessmentResults.get('vineland'):
        vineland = assessmentResults['vineland']
        vineland_table = Table('vineland')
        vineland_table.add_column_from_dict(vineland)
        vineland_table.add_rows_from_dict(vineland)
        tables.append(vineland_table)

        if vineland.get('maladaptiveBehaviorIndex'):
            maladaptiveBehaviorIndex_table = Table('maladaptive_behavior_index')
            maladaptiveBehaviorIndex_table.add_columns(['header', 'value', 'type', 'placeholder' , 'is_header',
                                                        'is_sub_header', 'is_editable'])
            maladaptiveBehaviorIndex_table.add_rows_from_data_headers_type(vineland['maladaptiveBehaviorIndex'],
                                                                           ['value', 'type', 'placeholder', 'header',
                                                                            'subHeader', 'editable'])
            tables.append(maladaptiveBehaviorIndex_table)

        if vineland.get('domainDetails'):
            domainDetails_table = Table('domain_details')
            domainDetails_table.add_columns(['header', 'value', 'is_header', 'is_sub_header', 'is_italic', 'is_editable'
                                             'is_optional', ])
            domainDetails_table.add_rows_from_data_headers_type(vineland['domainDetails'],
                                                                ['value', 'header', 'subHeader', 'italic', 'editable'
                                                                 'optional'])
            tables.append(domainDetails_table)

        if vineland.get('scoreSummary'):
            scoreSummary_table = Table('score_summary')
            scoreSummary_table.add_columns(['header', 'value', 'is_header', 'is_editable'])
            scoreSummary_table.add_rows_from_data_headers_type(vineland['scoreSummary'], ['value', 'header', 'editable'])
            tables.append(scoreSummary_table)

        if vineland.get('info'):
            vineland_info = vineland['info']
            info_table = Table('vineland_info')
            info_table.add_column_from_dict(vineland_info)
            info_table.add_rows_from_dict(vineland_info)
            tables.append(info_table)

if data.get('backgroundAndMethodology'):
    backgroundAndMethodology = data['backgroundAndMethodology']
    backgroundAndMethodology_table = Table('background_and_methodology')
    backgroundAndMethodology_table.add_column_from_dict(backgroundAndMethodology)
    backgroundAndMethodology_table.add_rows_from_dict(backgroundAndMethodology)
    tables.append(backgroundAndMethodology_table)

    if backgroundAndMethodology.get('assessmentResults'):
        assessmentResults_table = Table('background_and_methodology_assessment_results')
        assessmentResults_table.add_column('assessmentResults')
        assessmentResults_table.add_string_list_rows(backgroundAndMethodology['assessmentResults'])
        tables.append(assessmentResults_table)

    if backgroundAndMethodology.get('assessmentAppointments'):
        assessmentAppointments_table = Table('assessment_appointments')
        assessmentAppointments_table.add_columns(backgroundAndMethodology['assessmentAppointments']['headers'])
        assessmentAppointments_table.add_rows_from_value_headers_type(backgroundAndMethodology['assessmentAppointments']['values'])
        tables.append(assessmentAppointments_table)


