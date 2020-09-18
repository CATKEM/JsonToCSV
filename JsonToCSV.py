from Table import Table
import Constants as const
import json
import os

dirFilePath = '/home/user/Downloads/'
jsonFileName = 'dataFile.json'
tables = []


with open(dirFilePath + jsonFileName) as jsonFile:
    data = json.load(jsonFile)

main_table = Table(table_name=const.MAIN_TABLE_NAME,
                   simple_dict=data)
tables.append(main_table)

if data.get(const.CLIENT):
    tables.append(Table(table_name=const.CLIENT,
                        simple_dict=data[const.CLIENT],
                        parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()}))

if data.get(const.PERSONS):
    persons_table = Table(table_name=const.PERSONS,
                          parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    for person in data[const.PERSONS]:
        persons_table.add_row_column_from_dict(person)
    tables.append(persons_table)

if data.get(const.RECOMMENDATIONS):
    recommendations = data[const.RECOMMENDATIONS]
    recommendations_table = Table(table_name=const.RECOMMENDATIONS,
                                  simple_dict=recommendations,
                                  parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(recommendations_table)

    if recommendations.get(const.AUTHORIZATION_REQUEST_DATA):
        authorizationRequestData = recommendations[const.AUTHORIZATION_REQUEST_DATA]
        authorizationRequestData__table = Table(table_name='authorization_request_data',
                                                parent_name_to_id={const.RECOMMENDATIONS: recommendations_table.get_last_id()})
        authorizationRequestData__table.add_columns(authorizationRequestData['headers'])
        authorizationRequestData__table.add_rows_from_value_headers_type(authorizationRequestData['values'])
        tables.append(authorizationRequestData__table)

if data.get(const.FAMILY_PARTICIPATION_IN_PROGRAM):
    tables.append(Table(table_name='family_participation_in_program',
                        simple_dict=data[const.FAMILY_PARTICIPATION_IN_PROGRAM],
                        parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()}))

if data.get(const.STAFF_ROLES_AND_SUPERVISION):
    tables.append(Table(table_name='staff_roles_and_supervision',
                        simple_dict=data[const.STAFF_ROLES_AND_SUPERVISION],
                        parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()}))

if data.get(const.PROGRAM_DESCRIPTION):
    tables.append(Table(table_name='program_description',
                        simple_dict=data['programDescription'],
                        parent_name_to_id={const.MAIN_TABLE_NAME:main_table.get_last_id()}))

if data.get(const.ASSESSMENT_RESULTS):
    assessmentResults = data[const.ASSESSMENT_RESULTS]
    assessmentResults_table = Table(table_name='assessment_results',
                                    simple_dict=data[const.ASSESSMENT_RESULTS],
                                    parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(assessmentResults_table)

    if assessmentResults.get(const.SERVICES):
        assessmentResults_services = assessmentResults[const.SERVICES]
        assessmentResults_services_table = Table(table_name='assessment_results_services',
                                                 parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        assessmentResults_services_table.add_columns(assessmentResults_services['headers'])
        assessmentResults_services_table.add_rows_from_value_headers_type(assessmentResults_services['values'])
        tables.append(assessmentResults_services_table)

    if assessmentResults.get('educationalServices'):
        educationalServices = assessmentResults[const.EDUCATIONAL_SERVICES]
        educationalServices_table = Table(table_name='educational_services',
                                          parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        educationalServices_table.add_columns(educationalServices['headers'])
        educationalServices_table.add_rows_from_value_headers_type(educationalServices['values'])
        tables.append(educationalServices_table)

    if assessmentResults.get(const.ACADEMIC_PERFORMANCE):
        tables.append(Table(table_name='academic_performance',
                            simple_dict=assessmentResults[const.ACADEMIC_PERFORMANCE],
                            parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()}))

    if assessmentResults.get(const.REVIEWED_RECORDS):
        reviewedRecords_table = Table(table_name='reviewed_records',
                                      parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        reviewedRecords_table.add_columns([const.REVIEWED_RECORDS])
        reviewedRecords_table.add_string_list_rows(assessmentResults[const.REVIEWED_RECORDS])
        tables.append(reviewedRecords_table)

    if assessmentResults.get(const.VINELAND):
        vineland = assessmentResults[const.VINELAND]
        vineland_table = Table(table_name='vineland',
                               simple_dict=assessmentResults['vineland'],
                               parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        tables.append(vineland_table)

        if vineland.get(const.MALADAPTIVE_BEHAVIOR_INDEX):
            maladaptiveBehaviorIndex_table = Table(table_name='maladaptive_behavior_index',
                                                   parent_name_to_id={const.VINELAND: vineland_table.get_last_id()})
            maladaptiveBehaviorIndex_table.add_columns(['header', 'value', 'type', 'placeholder' , 'is_header',
                                                        'is_sub_header', 'is_editable'])
            maladaptiveBehaviorIndex_table.add_rows_from_data_headers_type(vineland['maladaptiveBehaviorIndex'],
                                                                           ['value', 'type', 'placeholder', 'header',
                                                                            'subHeader', 'editable'])
            tables.append(maladaptiveBehaviorIndex_table)

        if vineland.get(const.DOMAIN_DETAILS):
            domainDetails_table = Table(table_name='domain_details',
                                        parent_name_to_id={const.VINELAND: vineland_table.get_last_id()})
            domainDetails_table.add_columns(['header', 'value', 'is_header', 'is_sub_header', 'is_italic', 'is_editable'
                                             'is_optional', ])
            domainDetails_table.add_rows_from_data_headers_type(vineland[const.DOMAIN_DETAILS],
                                                                ['value', 'header', 'subHeader', 'italic', 'editable'
                                                                 'optional'])
            tables.append(domainDetails_table)

        if vineland.get(const.SCORE_SUMMARY):
            scoreSummary_table = Table(table_name='score_summary',
                                       parent_name_to_id={const.VINELAND: vineland_table.get_last_id()})
            scoreSummary_table.add_columns(['header', 'value', 'is_header', 'is_editable'])
            scoreSummary_table.add_rows_from_data_headers_type(vineland[const.SCORE_SUMMARY], ['value', 'header', 'editable'])
            tables.append(scoreSummary_table)

        if vineland.get(const.INFO):
            vineland_info = vineland[const.INFO]
            vineland_info_table = Table(table_name='vineland_info',
                                        simple_dict=vineland[const.INFO],
                                        parent_name_to_id={const.VINELAND: vineland_table.get_last_id()})
            tables.append(vineland_info_table)

            if vineland_info.get(const.DATA):
                info_data_table = Table(table_name='vineland_info_data',
                                        parent_name_to_id={const.INFO: vineland_info_table.get_last_id()})
                for info_data in vineland_info[const.DATA]:
                    info_data_table.add_columns(['name', 'type', 'value', 'placeholder'])
                    info_data_table.add_exists_elements_to_row(info_data, ['name', 'type', 'value', 'placeholder'])
                tables.append(info_data_table)

    if assessmentResults.get(const.APPENDICES):
        appendices_table = Table(table_name=const.APPENDICES,
                                 parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        appendices_data_table = Table(table_name='appendices_data',
                                      parent_name_to_id={const.APPENDICES: appendices_table.get_last_id()})
        attachments_table = Table(table_name=const.ATTACHMENTS,
                                  parent_name_to_id={const.APPENDICES: []})
        images_table = Table(table_name=const.IMAGES,
                             parent_name_to_id={const.ATTACHMENTS: []})
        for one_appendices in assessmentResults[const.APPENDICES]:
            appendices_table.add_row_column_from_dict(one_appendices)

            if one_appendices.get(const.DATA):
                for one_data in one_appendices[const.DATA]:
                    appendices_table.parent_ids = [appendices_table.get_last_id()]
                    appendices_data_table.add_columns(['name', 'type', 'value'])
                    appendices_data_table.add_exists_elements_to_row(one_data, ['name', 'type', 'value'])

            if one_appendices.get(const.ATTACHMENTS):
                for one_attachment in one_appendices[const.ATTACHMENTS]:
                    appendices_table.parent_ids = [appendices_table.get_last_id()]
                    attachments_table.add_row_column_from_dict(one_attachment)

                    if one_attachment.get(const.IMAGES):
                        for image in one_attachment[const.IMAGES]:
                            images_table.parent_ids = [appendices_table.get_last_id()]
                            images_table.add_row_column_from_dict(image)

        tables.append(appendices_table)
        tables.append(appendices_data_table)
        tables.append(images_table)

if data.get(const.BACKGROUND_AND_METHODOLOGY):
    backgroundAndMethodology = data[const.BACKGROUND_AND_METHODOLOGY]
    backgroundAndMethodology_table = Table(table_name='background_and_methodology',
                                           simple_dict=backgroundAndMethodology,
                                           parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(backgroundAndMethodology_table)

    if backgroundAndMethodology.get(const.ASSESSMENT_RESULTS):
        assessmentResults_table = Table(table_name='background_and_methodology_assessment_results',
                                        parent_name_to_id={const.BACKGROUND_AND_METHODOLOGY: backgroundAndMethodology_table.get_last_id()})
        assessmentResults_table.add_columns([const.ASSESSMENT_RESULTS])
        assessmentResults_table.add_string_list_rows(backgroundAndMethodology[const.ASSESSMENT_RESULTS])
        tables.append(assessmentResults_table)

    if backgroundAndMethodology.get(const.ASSESSMENT_APPOINTMENTS):
        assessmentAppointments_table = Table(table_name='assessment_appointments',
                                             parent_name_to_id={const.BACKGROUND_AND_METHODOLOGY: backgroundAndMethodology_table.get_last_id()})
        assessmentAppointments_table.add_columns(backgroundAndMethodology[const.ASSESSMENT_APPOINTMENTS]['headers'])
        assessmentAppointments_table.add_rows_from_value_headers_type(backgroundAndMethodology[const.ASSESSMENT_APPOINTMENTS]['values'])
        tables.append(assessmentAppointments_table)

if data.get(const.PROPOSED_OBJECTIVES):
    proposedObjectives_table = Table(table_name='proposed_objectives',
                                     parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    strengths_table = Table(table_name=const.STRENGTHS,
                            parent_name_to_id={const.PROPOSED_OBJECTIVES: []})
    objectives_table = Table(table_name=const.OBJECTIVES,
                             parent_name_to_id={const.PROPOSED_OBJECTIVES: []})
    objectives_fields_table = Table(table_name='objective_fields',
                                    parent_name_to_id={const.OBJECTIVES: []})
    phase_change_event_types_table = Table(table_name='phase_change_event_types',
                                           parent_name_to_id={const.OBJECTIVES: []})
    original_objective_table = Table(table_name='original_objective',
                                     parent_name_to_id={const.OBJECTIVES: []})
    target_groups_table = Table(table_name='target_groups',
                                parent_name_to_id={const.ORIGINAL_OBJECTIVE: []})
    targets_table = Table(table_name='targets',
                          parent_name_to_id={const.TAGRETS: []})
    objective_domain_table = Table(table_name='objective_domain',
                                   parent_name_to_id={const.ORIGINAL_OBJECTIVE: []})
    maintenance_schedule_table = Table(table_name='maintenance_schedule',
                                       parent_name_to_id={const.ORIGINAL_OBJECTIVE: []})
    generalization_table = Table(table_name='generalization',
                                 parent_name_to_id={const.ORIGINAL_OBJECTIVE: []})

    for proposedObjective in data[const.PROPOSED_OBJECTIVES]:
        proposedObjectives_table.add_row_column_from_dict(proposedObjective)

        if proposedObjective.get(const.STRENGTHS):
            strengths_table.add_columns([const.STRENGTHS])
            strengths_table.parent_ids = [proposedObjectives_table.get_last_id()]
            strengths_table.add_string_list_rows(proposedObjective[const.STRENGTHS])

        if proposedObjective.get(const.OBJECTIVES):
            for objective in proposedObjective[const.OBJECTIVES]:
                objectives_table.parent_ids = [proposedObjectives_table.get_last_id()]
                objectives_table.add_row_column_from_dict(objective)

                if objective.get(const.FIELDS):
                    objectives_fields_table.add_columns(['name', 'value'])
                    for field in objective[const.FIELDS]:
                        objectives_fields_table.parent_ids = [objectives_table.get_last_id()]
                        objectives_fields_table.__add_row__([field['name'], field['value']])

                if objective.get(const.PHASE_CHANGE_EVENT_TYPES):
                    phase_change_event_types_table.add_columns(['type', 'value'])
                    for key in objective[const.PHASE_CHANGE_EVENT_TYPES]:
                        for event_name in objective[const.PHASE_CHANGE_EVENT_TYPES][key]:
                            phase_change_event_types_table.parent_ids = [objectives_table.get_last_id()]
                            phase_change_event_types_table.__add_row__([key, event_name])

                if objective.get(const.ORIGINAL_OBJECTIVE):
                    original_objective_table.parent_ids = [objectives_table.get_last_id()]
                    original_objective_table.add_columns(['rate', 'type', 'field', 'order', 'status', 'deleted',
                                                          'variety', 'baseline', 'response', 'createdAt', 'updatedAt',
                                                          'objectType', 'promptOrder', 'isIncomplete', 'reinforcement',
                                                          'originalStatus', 'longDescription', 'masteryCriteria',
                                                          'promptHierarchy', 'treatmentPlanId', 'shortDescription',
                                                          'maxTeachingTrials', 'objectiveDomainId', 'protocolMaterials',
                                                          'assessmentToolSource', 'discriminativeStimuli',
                                                          'originPromptHierarchy', 'generalizationCriteria',
                                                          'protocolClientAttention', 'errorCorrectionProcedure',
                                                          'lastCollectedActivityDate', 'protocolTeachingEnvironment'])
                    original_objective_table.add_exists_elements_to_row(objective[const.ORIGINAL_OBJECTIVE], ['rate', 'type', 'field', 'order', 'status', 'deleted',
                                                          'variety', 'baseline', 'response', 'createdAt', 'updatedAt',
                                                          'objectType', 'promptOrder', 'isIncomplete', 'reinforcement',
                                                          'originalStatus', 'longDescription', 'masteryCriteria',
                                                          'promptHierarchy', 'treatmentPlanId', 'shortDescription',
                                                          'maxTeachingTrials', 'objectiveDomainId', 'protocolMaterials',
                                                          'assessmentToolSource', 'discriminativeStimuli',
                                                          'originPromptHierarchy', 'generalizationCriteria',
                                                          'protocolClientAttention', 'errorCorrectionProcedure',
                                                          'lastCollectedActivityDate', 'protocolTeachingEnvironment'])

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.TARGET_GROUPS):
                        for target_group in objective[const.ORIGINAL_OBJECTIVE][const.TARGET_GROUPS]:
                            target_groups_table.parent_ids = [original_objective_table.get_last_id()]
                            target_groups_table.add_columns(['name', 'deleted'])
                            target_groups_table.add_exists_elements_to_row(target_group, ['name', 'deleted'])

                            if target_group.get(const.TAGRETS):
                                for target in target_group[const.TAGRETS]:
                                    targets_table.parent_ids = [target_groups_table.get_last_id()]
                                    targets_table.add_columns(['name', 'active', 'status', 'deleted', 'originalStatus',
                                                               'hasCollectedActivities'])
                                    targets_table.add_exists_elements_to_row(target, ['name', 'active', 'status', 'deleted',
                                                                              'originalStatus', 'hasCollectedActivities'])

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.OBJECTIVE_DOMAIN):
                        objective_domain_table.parent_ids = [original_objective_table.get_last_id()]
                        objective_domain_table.add_columns(['description'])
                        objective_domain_table.add_exists_elements_to_row(objective[const.ORIGINAL_OBJECTIVE][const.OBJECTIVE_DOMAIN],
                                                                          ['description'])

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.MAINTENANCE_SCHEDULE):
                        maintenance_schedule_table.parent_ids = [original_objective_table.get_last_id()]
                        maintenance_schedule_table.add_row_column_from_dict(objective[const.ORIGINAL_OBJECTIVE][const.MAINTENANCE_SCHEDULE])

    tables.append(proposedObjectives_table)
    tables.append(strengths_table)
    tables.append(objectives_table)
    tables.append(objectives_fields_table)
    tables.append(phase_change_event_types_table)
    tables.append(original_objective_table)
    tables.append(target_groups_table)
    tables.append(targets_table)
    tables.append(objective_domain_table)
    tables.append(maintenance_schedule_table)

for table in tables:
    table.to_csv(dirFilePath + 'Convert_Result/')


