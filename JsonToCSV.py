from Table import Table
import Constants as const
import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--json_dir', help='Path to JSON file')
parser.add_argument('--json_file_name', help='JSON file name')
parser.add_argument('--separator', help='Separator for CSV')
parser.add_argument('--csv_dir', help='Path to save JSON')
args = parser.parse_args()

json_dir = args.json_dir
json_file_name = args.json_file_name
separator = args.separator
csv_dir = args.csv_dir
tables = []

if separator:
    const.SEPARATOR = separator
if not csv_dir:
    csv_dir = json_dir

with open(json_dir + json_file_name) as jsonFile:
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
        persons_table.add_row_column_from_dict(dict_data=person)
    tables.append(persons_table)

if data.get(const.RECOMMENDATIONS):
    recommendations = data[const.RECOMMENDATIONS]
    recommendations_table = Table(table_name=const.RECOMMENDATIONS,
                                  simple_dict=recommendations,
                                  parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(recommendations_table)

    if recommendations.get(const.AUTHORIZATION_REQUEST_DATA):
        authorizationRequestData = recommendations[const.AUTHORIZATION_REQUEST_DATA]
        authorizationRequestData__table = Table(table_name=const.AUTHORIZATION_REQUEST_DATA_NAME,
                                                parent_name_to_id={const.RECOMMENDATIONS: recommendations_table.get_last_id()})
        authorizationRequestData__table.add_columns(authorizationRequestData[const.HEADERS])
        authorizationRequestData__table.add_rows_from_value_headers_type(authorizationRequestData[const.VALUES])
        tables.append(authorizationRequestData__table)

if data.get(const.FAMILY_PARTICIPATION_IN_PROGRAM):
    tables.append(Table(table_name=const.FAMILY_PARTICIPATION_IN_PROGRAM_NAME,
                        simple_dict=data[const.FAMILY_PARTICIPATION_IN_PROGRAM],
                        parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()}))

if data.get(const.STAFF_ROLES_AND_SUPERVISION):
    tables.append(Table(table_name=const.STAFF_ROLES_AND_SUPERVISION_NAME,
                        simple_dict=data[const.STAFF_ROLES_AND_SUPERVISION],
                        parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()}))

if data.get(const.PROGRAM_DESCRIPTION):
    tables.append(Table(table_name=const.PROGRAM_DESCRIPTION_NAME,
                        simple_dict=data[const.PROGRAM_DESCRIPTION],
                        parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()}))

if data.get(const.ASSESSMENT_RESULTS):
    assessmentResults = data[const.ASSESSMENT_RESULTS]
    assessmentResults_table = Table(table_name=const.ASSESSMENT_RESULTS_NAME,
                                    simple_dict=data[const.ASSESSMENT_RESULTS],
                                    parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(assessmentResults_table)

    if assessmentResults.get(const.SERVICES):
        assessmentResults_services = assessmentResults[const.SERVICES]
        assessmentResults_services_table = Table(table_name=const.SERVICES_NAME,
                                                 parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        assessmentResults_services_table.add_columns(assessmentResults_services[const.HEADERS])
        assessmentResults_services_table.add_rows_from_value_headers_type(assessmentResults_services[const.VALUES])
        tables.append(assessmentResults_services_table)

    if assessmentResults.get(const.EDUCATIONAL_SERVICES):
        educationalServices = assessmentResults[const.EDUCATIONAL_SERVICES]
        educationalServices_table = Table(table_name=const.EDUCATIONAL_SERVICES_NAME,
                                          parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        educationalServices_table.add_columns(educationalServices[const.HEADERS])
        educationalServices_table.add_rows_from_value_headers_type(educationalServices[const.VALUES])
        tables.append(educationalServices_table)

    if assessmentResults.get(const.ACADEMIC_PERFORMANCE):
        tables.append(Table(table_name=const.ACADEMIC_PERFORMANCE_NAME,
                            simple_dict=assessmentResults[const.ACADEMIC_PERFORMANCE],
                            parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()}))

    if assessmentResults.get(const.REVIEWED_RECORDS):
        reviewedRecords_table = Table(table_name=const.REVIEWED_RECORDS,
                                      parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        reviewedRecords_table.add_columns([const.REVIEWED_RECORDS])
        reviewedRecords_table.add_string_list_rows(assessmentResults[const.REVIEWED_RECORDS])
        tables.append(reviewedRecords_table)

    if assessmentResults.get(const.VINELAND):
        vineland = assessmentResults[const.VINELAND]
        vineland_table = Table(table_name=const.VINELAND_NAME,
                               simple_dict=assessmentResults[const.VINELAND],
                               parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        tables.append(vineland_table)

        if vineland.get(const.MALADAPTIVE_BEHAVIOR_INDEX):
            maladaptiveBehaviorIndex_table = Table(table_name=const.MALADAPTIVE_BEHAVIOR_INDEX_NAME,
                                                   parent_name_to_id={const.VINELAND: vineland_table.get_last_id()})
            maladaptiveBehaviorIndex_table.add_columns(const.MALADAPTIVE_BEHAVIOR_INDEX_COLUMNS)
            maladaptiveBehaviorIndex_table.add_rows_from_data_headers_type(vineland[const.MALADAPTIVE_BEHAVIOR_INDEX],
                                                                           const.MALADAPTIVE_BEHAVIOR_INDEX_ROWS)
            tables.append(maladaptiveBehaviorIndex_table)

        if vineland.get(const.DOMAIN_DETAILS):
            domainDetails_table = Table(table_name=const.DOMAIN_DETAILS_NAME,
                                        parent_name_to_id={const.VINELAND: vineland_table.get_last_id()})
            domainDetails_table.add_columns(const.DOMAIN_DETAILS_COLUMNS)
            domainDetails_table.add_rows_from_data_headers_type(vineland[const.DOMAIN_DETAILS],
                                                                const.DOMAIN_DETAILS_ROWS)
            tables.append(domainDetails_table)

        if vineland.get(const.SCORE_SUMMARY):
            scoreSummary_table = Table(table_name=const.SCORE_SUMMARY_NAME,
                                       parent_name_to_id={const.VINELAND: vineland_table.get_last_id()})
            scoreSummary_table.add_columns(const.SCORE_SUMMARY_COLUMNS)
            scoreSummary_table.add_rows_from_data_headers_type(vineland[const.SCORE_SUMMARY], const.SCORE_SUMMARY_ROWS)
            tables.append(scoreSummary_table)

        if vineland.get(const.INFO):
            vineland_info = vineland[const.INFO]
            vineland_info_table = Table(table_name=const.VINELAND_INFO_NAME,
                                        simple_dict=vineland[const.INFO],
                                        parent_name_to_id={const.VINELAND: vineland_table.get_last_id()})
            tables.append(vineland_info_table)

            if vineland_info.get(const.DATA):
                info_data_table = Table(table_name=const.VINELAND_DATA_NAME,
                                        parent_name_to_id={const.INFO: vineland_info_table.get_last_id()})
                for info_data in vineland_info[const.DATA]:
                    info_data_table.add_columns(const.VINELAND_DATA_ROW_COLUMN)
                    info_data_table.add_exists_elements_to_row(info_data, const.VINELAND_DATA_ROW_COLUMN)
                tables.append(info_data_table)

    if assessmentResults.get(const.APPENDICES):
        appendices_table = Table(table_name=const.APPENDICES,
                                 parent_name_to_id={const.ASSESSMENT_RESULTS: assessmentResults_table.get_last_id()})
        appendices_data_table = Table(table_name=const.APPENDICES,
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
                    appendices_data_table.add_columns(const.APPENDICES_ROW_COLUMN)
                    appendices_data_table.add_exists_elements_to_row(one_data, const.APPENDICES_ROW_COLUMN)

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
    backgroundAndMethodology_table = Table(table_name=const.BACKGROUND_AND_METHODOLOGY_NAME,
                                           simple_dict=backgroundAndMethodology,
                                           parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    tables.append(backgroundAndMethodology_table)

    if backgroundAndMethodology.get(const.ASSESSMENT_RESULTS):
        assessmentResults_table = Table(table_name=const.BACKGROUND_AND_METHODOLOGY_ASSESSMENTS_RESULTS_NAME,
                                        parent_name_to_id={const.BACKGROUND_AND_METHODOLOGY: backgroundAndMethodology_table.get_last_id()})
        assessmentResults_table.add_columns([const.ASSESSMENT_RESULTS])
        assessmentResults_table.add_string_list_rows(backgroundAndMethodology[const.ASSESSMENT_RESULTS])
        tables.append(assessmentResults_table)

    if backgroundAndMethodology.get(const.ASSESSMENT_APPOINTMENTS):
        assessmentAppointments_table = Table(table_name=const.ASSESSMENT_APPOINTMENTS_NAME,
                                             parent_name_to_id={const.BACKGROUND_AND_METHODOLOGY: backgroundAndMethodology_table.get_last_id()})
        assessmentAppointments_table.add_columns(backgroundAndMethodology[const.ASSESSMENT_APPOINTMENTS][const.HEADERS])
        assessmentAppointments_table.add_rows_from_value_headers_type(backgroundAndMethodology[const.ASSESSMENT_APPOINTMENTS][const.VALUES])
        tables.append(assessmentAppointments_table)

if data.get(const.PROPOSED_OBJECTIVES):
    proposedObjectives_table = Table(table_name=const.PROPOSED_OBJECTIVES_NAME,
                                     parent_name_to_id={const.MAIN_TABLE_NAME: main_table.get_last_id()})
    strengths_table = Table(table_name=const.STRENGTHS,
                            parent_name_to_id={const.PROPOSED_OBJECTIVES: []})
    objectives_table = Table(table_name=const.OBJECTIVES,
                             parent_name_to_id={const.PROPOSED_OBJECTIVES: []})
    objectives_fields_table = Table(table_name=const.OBJECTIVE_FIELDS,
                                    parent_name_to_id={const.OBJECTIVES: []})
    phase_change_event_types_table = Table(table_name=const.PHASE_CHANGE_EVENT_TYPES_NAME,
                                           parent_name_to_id={const.OBJECTIVES: []})
    original_objective_table = Table(table_name=const.ORIGINAL_OBJECTIVE_NAME,
                                     parent_name_to_id={const.OBJECTIVES: []})
    target_groups_table = Table(table_name=const.TARGET_GROUPS_NAME,
                                parent_name_to_id={const.ORIGINAL_OBJECTIVE: []})
    targets_table = Table(table_name=const.TARGETS,
                          parent_name_to_id={const.TARGETS: []})
    objective_domain_table = Table(table_name=const.OBJECTIVE_DOMAIN_NAME,
                                   parent_name_to_id={const.ORIGINAL_OBJECTIVE: []})
    maintenance_schedule_table = Table(table_name=const.MAINTENANCE_SCHEDULE_NAME,
                                       parent_name_to_id={const.ORIGINAL_OBJECTIVE: []})
    generalization_table = Table(table_name=const.GENERALIZATION_NAME,
                                 parent_name_to_id={const.ORIGINAL_OBJECTIVE: []})
    generalization_table.add_columns(const.GENERALIZATION_COLUMNS)
    esba_crisis_plan_points_table = Table(table_name=const.ESBACrisisPlanPoints_NANE,
                                          parent_name_to_id={const.ESBACrisisPlanPoints: []})

    for proposedObjective in data[const.PROPOSED_OBJECTIVES]:
        proposedObjectives_table.add_columns(const.PROPOSED_OBJECTIVES_COLUMNS)
        proposedObjectives_table.add_exists_elements_to_row(proposedObjective, const.PROPOSED_OBJECTIVES_ROWS)

        if proposedObjective.get(const.ESBACrisisPlanPoints):
            esba_crisis_plan_points_table.add_columns([const.ESBACrisisPlanPoints])
            esba_crisis_plan_points_table.add_string_list_rows(proposedObjective[const.ESBACrisisPlanPoints])

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
                    original_objective_table.add_columns(const.ORIGINAL_OBJECTIVE_ROW_COLUMN)
                    original_objective_table.add_exists_elements_to_row(objective[const.ORIGINAL_OBJECTIVE],
                                                                        const.ORIGINAL_OBJECTIVE_ROW_COLUMN)

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.TARGET_GROUPS):
                        for target_group in objective[const.ORIGINAL_OBJECTIVE][const.TARGET_GROUPS]:
                            target_groups_table.parent_ids = [original_objective_table.get_last_id()]
                            target_groups_table.add_columns(const.TARGET_GROUPS_ROW_COLUMN)
                            target_groups_table.add_exists_elements_to_row(target_group, const.TARGET_GROUPS_ROW_COLUMN)

                            if target_group.get(const.TARGETS):
                                for target in target_group[const.TARGETS]:
                                    targets_table.parent_ids = [target_groups_table.get_last_id()]
                                    targets_table.add_columns(const.TARGETS_ROW_COLUMN)
                                    targets_table.add_exists_elements_to_row(target, const.TARGETS_ROW_COLUMN)

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.OBJECTIVE_DOMAIN):
                        objective_domain_table.parent_ids = [original_objective_table.get_last_id()]
                        objective_domain_table.add_columns(const.OBJECTIVE_DOMAIN_ROW_COLUMN)
                        objective_domain_table.add_exists_elements_to_row(objective[const.ORIGINAL_OBJECTIVE][const.OBJECTIVE_DOMAIN],
                                                                          const.OBJECTIVE_DOMAIN_ROW_COLUMN)

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.MAINTENANCE_SCHEDULE):
                        maintenance_schedule_table.parent_ids = [original_objective_table.get_last_id()]
                        maintenance_schedule_table.add_row_column_from_dict(objective[const.ORIGINAL_OBJECTIVE][const.MAINTENANCE_SCHEDULE])

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.GENERALIZATION_PERSONS):
                        for generalization_person in objective[const.ORIGINAL_OBJECTIVE][const.GENERALIZATION_PERSONS]:
                            generalization_table.parent_ids = [original_objective_table.get_last_id()]
                            generalization_table.add_exists_elements_to_row(generalization_person,
                                                                            const.GENERALIZATION_ROWS,
                                                                            [const.GENERALIZATION_PERSONS])

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.GENERALIZATION_STIMULI):
                        for generalization_slimul in objective[const.ORIGINAL_OBJECTIVE][const.GENERALIZATION_STIMULI]:
                            generalization_table.parent_ids = [original_objective_table.get_last_id()]
                            generalization_table.add_exists_elements_to_row(generalization_slimul,
                                                                            const.GENERALIZATION_ROWS,
                                                                            [const.GENERALIZATION_STIMULI])

                    if objective[const.ORIGINAL_OBJECTIVE].get(const.GENERALIZATION_SETTINGS):
                        for generalization_settings in objective[const.ORIGINAL_OBJECTIVE][const.GENERALIZATION_STIMULI]:
                            generalization_table.parent_ids = [original_objective_table.get_last_id()]
                            generalization_table.add_exists_elements_to_row(generalization_settings,
                                                                            const.GENERALIZATION_ROWS,
                                                                            [const.GENERALIZATION_SETTINGS])

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
    tables.append(generalization_table)
    tables.append(esba_crisis_plan_points_table)

path_to_save = csv_dir + json_file_name.replace('.json', '')
if not os.path.exists(path_to_save):
    os.mkdir(path_to_save)

for table in tables:
    table.show()
    table.to_csv(path_to_save + '/')

print(path_to_save)
