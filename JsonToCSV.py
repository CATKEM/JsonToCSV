from Table import Table
import json
import os

MAIN_TABLE_NAME = 'main'
dirFilePath = '/home/user/Downloads/'
jsonFileName = 'dataFile.json'
tables = []


with open(dirFilePath + jsonFileName) as jsonFile:
    data = json.load(jsonFile)

main_table = Table(table_name=MAIN_TABLE_NAME,
                   simple_dict=data)
tables.append(main_table)

CLIENT = 'client'
if data.get(CLIENT):
    tables.append(Table(table_name=CLIENT,
                        simple_dict=data[CLIENT],
                        parent_name_to_id={MAIN_TABLE_NAME: main_table.get_last_id()}))

PERSONS = 'persons'
if data.get(PERSONS):
    persons_table = Table(table_name=PERSONS,
                          parent_name_to_id={MAIN_TABLE_NAME: main_table.get_last_id()})
    for person in data[PERSONS]:
        if not persons_table.columns_added:
            persons_table.add_column_from_dict(person)
            persons_table.columns_added = True
        persons_table.add_rows_from_dict(person)
    tables.append(persons_table)

RECOMMENDATIONS = 'recommendations'
if data.get(RECOMMENDATIONS):
    recommendations = data[RECOMMENDATIONS]
    recommendations_table = Table(table_name=RECOMMENDATIONS,
                                  simple_dict=recommendations,
                                  parent_name_to_id={MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(recommendations_table)

    AUTHORIZATION_REQUEST_DATA = 'authorizationRequestData'
    if recommendations.get(AUTHORIZATION_REQUEST_DATA):
        authorizationRequestData = recommendations[AUTHORIZATION_REQUEST_DATA]
        authorizationRequestData__table = Table(table_name='authorization_request_data',
                                                parent_name_to_id={RECOMMENDATIONS: recommendations_table.get_last_id()})
        authorizationRequestData__table.add_columns(authorizationRequestData['headers'])
        authorizationRequestData__table.add_rows_from_value_headers_type(authorizationRequestData['values'])
        tables.append(authorizationRequestData__table)

FAMILY_PARTICIPATION_IN_PROGRAM = 'familyParticipationInProgram'
if data.get(FAMILY_PARTICIPATION_IN_PROGRAM):
    tables.append(Table(table_name='family_participation_in_program',
                        simple_dict=data[FAMILY_PARTICIPATION_IN_PROGRAM],
                        parent_name_to_id={MAIN_TABLE_NAME: main_table.get_last_id()}))

STAFF_ROLES_AND_SUPERVISION = 'staffRolesAndSupervision'
if data.get(STAFF_ROLES_AND_SUPERVISION):
    tables.append(Table(table_name='staff_roles_and_supervision',
                        simple_dict=data['staffRolesAndSupervision'],
                        parent_name_to_id={MAIN_TABLE_NAME: main_table.get_last_id()}))

PROGRAM_DESCRIPTION = 'programDescription'
if data.get(PROGRAM_DESCRIPTION):
    tables.append(Table(table_name='program_description',
                        simple_dict=data['programDescription'],
                        parent_name_to_id={MAIN_TABLE_NAME:main_table.get_last_id()}))

ASSESSMENT_RESULTS = 'assessmentResults'
if data.get(ASSESSMENT_RESULTS):
    assessmentResults = data[ASSESSMENT_RESULTS]
    assessmentResults_table = Table(table_name='assessment_results',
                                    simple_dict=data[ASSESSMENT_RESULTS],
                                    parent_name_to_id={MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(assessmentResults_table)

    SERVICES = 'services'
    if assessmentResults.get(SERVICES):
        assessmentResults_services = assessmentResults[SERVICES]
        assessmentResults_services_table = Table(table_name='assessment_results_services',
                                                 parent_name_to_id={ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        assessmentResults_services_table.add_columns(assessmentResults_services['headers'])
        assessmentResults_services_table.add_rows_from_value_headers_type(assessmentResults_services['values'])
        tables.append(assessmentResults_services_table)

    EDUCATIONAL_SERVICES = 'educationalServices'
    if assessmentResults.get('educationalServices'):
        educationalServices = assessmentResults[EDUCATIONAL_SERVICES]
        educationalServices_table = Table(table_name='educational_services',
                                          parent_name_to_id={ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        educationalServices_table.add_columns(educationalServices['headers'])
        educationalServices_table.add_rows_from_value_headers_type(educationalServices['values'])
        tables.append(educationalServices_table)

    ACADEMIC_PERFORMANCE = 'academicPerformance'
    if assessmentResults.get(ACADEMIC_PERFORMANCE):
        tables.append(Table(table_name='academic_performance',
                            simple_dict=assessmentResults[ACADEMIC_PERFORMANCE],
                            parent_name_to_id={ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()}))

    REVIEWED_RECORDS = 'reviewedRecords'
    if assessmentResults.get(REVIEWED_RECORDS):
        reviewedRecords_table = Table(table_name='reviewed_records',
                                      parent_name_to_id={ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        reviewedRecords_table.add_column(REVIEWED_RECORDS)
        reviewedRecords_table.add_string_list_rows(assessmentResults[REVIEWED_RECORDS])
        tables.append(reviewedRecords_table)

    VINELAND = 'vineland'
    if assessmentResults.get(VINELAND):
        vineland = assessmentResults[VINELAND]
        vineland_table = Table(table_name='vineland',
                               simple_dict=assessmentResults['vineland'],
                               parent_name_to_id={ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        tables.append(vineland_table)

        MALADAPTIVE_BEHAVIOR_INDEX = 'maladaptiveBehaviorIndex'
        if vineland.get(MALADAPTIVE_BEHAVIOR_INDEX):
            maladaptiveBehaviorIndex_table = Table(table_name='maladaptive_behavior_index',
                                                   parent_name_to_id={VINELAND: vineland_table.get_last_id()})
            maladaptiveBehaviorIndex_table.add_columns(['header', 'value', 'type', 'placeholder' , 'is_header',
                                                        'is_sub_header', 'is_editable'])
            maladaptiveBehaviorIndex_table.add_rows_from_data_headers_type(vineland['maladaptiveBehaviorIndex'],
                                                                           ['value', 'type', 'placeholder', 'header',
                                                                            'subHeader', 'editable'])
            tables.append(maladaptiveBehaviorIndex_table)

        DOMAIN_DETAILS = 'domainDetails'
        if vineland.get(DOMAIN_DETAILS):
            domainDetails_table = Table(table_name='domain_details',
                                        parent_name_to_id={VINELAND: vineland_table.get_last_id()})
            domainDetails_table.add_columns(['header', 'value', 'is_header', 'is_sub_header', 'is_italic', 'is_editable'
                                             'is_optional', ])
            domainDetails_table.add_rows_from_data_headers_type(vineland[DOMAIN_DETAILS],
                                                                ['value', 'header', 'subHeader', 'italic', 'editable'
                                                                 'optional'])
            tables.append(domainDetails_table)

        SCORE_SUMMARY = 'scoreSummary'
        if vineland.get(SCORE_SUMMARY):
            scoreSummary_table = Table(table_name='score_summary',
                                       parent_name_to_id={VINELAND: vineland_table.get_last_id()})
            scoreSummary_table.add_columns(['header', 'value', 'is_header', 'is_editable'])
            scoreSummary_table.add_rows_from_data_headers_type(vineland[SCORE_SUMMARY], ['value', 'header', 'editable'])
            tables.append(scoreSummary_table)

        INFO = 'info'
        if vineland.get(INFO):
            tables.append(Table(table_name='vineland_info',
                                simple_dict=vineland[INFO],
                                parent_name_to_id={VINELAND: vineland_table.get_last_id()}))
BACKGROUND_AND_METHODOLOGY = 'backgroundAndMethodology'
if data.get(BACKGROUND_AND_METHODOLOGY):
    backgroundAndMethodology = data[BACKGROUND_AND_METHODOLOGY]
    backgroundAndMethodology_table = Table(table_name='background_and_methodology',
                                           simple_dict=backgroundAndMethodology,
                                           parent_name_to_id={MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(backgroundAndMethodology_table)

    ASSESSMENT_RESULTS = 'assessmentResults'
    if backgroundAndMethodology.get(ASSESSMENT_RESULTS):
        assessmentResults_table = Table(table_name='background_and_methodology_assessment_results',
                                        parent_name_to_id={BACKGROUND_AND_METHODOLOGY: backgroundAndMethodology_table.get_last_id()})
        assessmentResults_table.add_column(ASSESSMENT_RESULTS)
        assessmentResults_table.add_string_list_rows(backgroundAndMethodology[ASSESSMENT_RESULTS])
        tables.append(assessmentResults_table)

    ASSESSMENT_APPOINTMENTS = 'assessmentAppointments'
    if backgroundAndMethodology.get(ASSESSMENT_APPOINTMENTS):
        assessmentAppointments_table = Table(table_name='assessment_appointments',
                                             parent_name_to_id={BACKGROUND_AND_METHODOLOGY: backgroundAndMethodology_table.get_last_id()})
        assessmentAppointments_table.add_columns(backgroundAndMethodology[ASSESSMENT_APPOINTMENTS]['headers'])
        assessmentAppointments_table.add_rows_from_value_headers_type(backgroundAndMethodology[ASSESSMENT_APPOINTMENTS]['values'])
        tables.append(assessmentAppointments_table)

PROPOSED_OBJECTIVES = 'proposedObjectives'
if data.get(PROPOSED_OBJECTIVES):
    proposedObjectives_table = Table(table_name='proposed_objectives',
                                     parent_name_to_id={MAIN_TABLE_NAME: main_table.get_last_id()})
    strengths_table = Table(table_name='strengths',
                            parent_name_to_id={PROPOSED_OBJECTIVES: []})
    for proposedObjective in data['proposedObjectives']:
        if not proposedObjectives_table.columns_added:
            proposedObjectives_table.add_column_from_dict(proposedObjective)
            proposedObjectives_table.columns_added = True
        proposedObjectives_table.add_rows_from_dict(proposedObjective)

        if proposedObjective.get('strengths'):
            if not strengths_table.columns_added:
                strengths_table.add_column('strengths')
                strengths_table.columns_added = True
            strengths_table.parent_ids = [proposedObjectives_table.get_last_id()]
            strengths_table.add_string_list_rows(proposedObjective['strengths'])

    tables.append(proposedObjectives_table)
    tables.append(strengths_table)

for table in tables:
    table.show()


