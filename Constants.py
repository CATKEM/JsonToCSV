CLIENT = 'client'
PERSONS = 'persons'
RECOMMENDATIONS = 'recommendations'
AUTHORIZATION_REQUEST_DATA = 'authorizationRequestData'
FAMILY_PARTICIPATION_IN_PROGRAM = 'familyParticipationInProgram'
STAFF_ROLES_AND_SUPERVISION = 'staffRolesAndSupervision'
PROGRAM_DESCRIPTION = 'programDescription'
ASSESSMENT_RESULTS = 'assessmentResults'
SERVICES = 'services'
EDUCATIONAL_SERVICES = 'educationalServices'
ACADEMIC_PERFORMANCE = 'academicPerformance'
REVIEWED_RECORDS = 'reviewedRecords'
VINELAND = 'vineland'
MALADAPTIVE_BEHAVIOR_INDEX = 'maladaptiveBehaviorIndex'
MALADAPTIVE_BEHAVIOR_INDEX_COLUMNS = ['header', 'value', 'type', 'placeholder', 'is_header', 'is_sub_header',
                                      'is_editable']
MALADAPTIVE_BEHAVIOR_INDEX_ROWS = ['value', 'type', 'placeholder', 'header', 'subHeader', 'editable']
DOMAIN_DETAILS = 'domainDetails'
DOMAIN_DETAILS_COLUMNS = ['header', 'value', 'is_header', 'is_sub_header', 'is_italic', 'is_editable', 'is_optional']
DOMAIN_DETAILS_ROWS = ['value', 'header', 'subHeader', 'italic', 'editable', 'optional']
SCORE_SUMMARY = 'scoreSummary'
SCORE_SUMMARY_COLUMNS = ['header', 'value', 'is_header', 'is_editable']
SCORE_SUMMARY_ROWS = ['value', 'header', 'editable']
VINELAND_DATA_ROW_COLUMN = ['name', 'type', 'value', 'placeholder']
INFO = 'info'
DATA = 'data'
APPENDICES = 'appendices'
APPENDICES_ROW_COLUMN = ['name', 'type', 'value']
ATTACHMENTS = 'attachments'
IMAGES = 'images'
BACKGROUND_AND_METHODOLOGY = 'backgroundAndMethodology'
ASSESSMENT_APPOINTMENTS = 'assessmentAppointments'
PROPOSED_OBJECTIVES = 'proposedObjectives'
PROPOSED_OBJECTIVES_COLUMNS = ['name', 'dbName', 'description', 'additionalInfo', 'hasESBACrisisPlan',
                               'behaviorAssessmentStatement']
PROPOSED_OBJECTIVES_ROWS = ['name', 'dbName', 'description', 'additionalInfo', 'hasESBACrisisPlan',
                            'behaviorAssessmentStatement']
STRENGTHS = 'strengths'
OBJECTIVES = 'objectives'
FIELDS = 'fields'
PHASE_CHANGE_EVENT_TYPES = 'phaseChangeEventTypes'
PHASE_CHANGE_EVENT_TYPES_COLUMNS = ['name', 'value']
ORIGINAL_OBJECTIVE = 'originalObjective'
ORIGINAL_OBJECTIVE_ROW_COLUMN = ['rate', 'type', 'field', 'order', 'status', 'deleted', 'variety', 'baseline',
                                 'response', 'createdAt', 'updatedAt', 'objectType', 'promptOrder', 'isIncomplete',
                                 'reinforcement', 'originalStatus', 'longDescription', 'masteryCriteria',
                                 'promptHierarchy', 'treatmentPlanId', 'shortDescription', 'maxTeachingTrials',
                                 'objectiveDomainId', 'protocolMaterials', 'assessmentToolSource',
                                 'discriminativeStimuli', 'originPromptHierarchy', 'generalizationCriteria',
                                 'protocolClientAttention', 'errorCorrectionProcedure', 'lastCollectedActivityDate',
                                 'protocolTeachingEnvironment']
TARGET_GROUPS = 'targetGroups'
TARGET_GROUPS_ROW_COLUMN = ['name', 'deleted']
TARGETS = 'targets'
TARGETS_ROW_COLUMN = ['name', 'active', 'status', 'deleted', 'originalStatus', 'hasCollectedActivities']
OBJECTIVE_DOMAIN = 'objectiveDomain'
OBJECTIVE_DOMAIN_ROW_COLUMN = ['description']
MAINTENANCE_SCHEDULE = 'maintenanceSchedule'
GENERALIZATION_PERSONS = 'generalizationPersons'
GENERALIZATION_STIMULI = 'generalizationStimuli'
GENERALIZATION_SETTINGS = 'generalizationSettings'
GENERALIZATION_COLUMNS = ['deleted', 'createdAt', 'createdBy', 'updatedAt', 'updatedBy', 'description', 'reviewStatus',
                          'addedDuringSession', 'type']
GENERALIZATION_ROWS = ['deleted', 'createdAt', 'createdBy', 'updatedAt', 'updatedBy', 'description', 'reviewStatus',
                                                          'addedDuringSession']
ESBACrisisPlanPoints = 'ESBACrisisPlanPoints'
HEADERS = 'headers'
VALUES = 'values'
MAIN_TABLE_NAME = 'main'
AUTHORIZATION_REQUEST_DATA_NAME = 'authorization_request_data'
FAMILY_PARTICIPATION_IN_PROGRAM_NAME = 'family_participation_in_program'
STAFF_ROLES_AND_SUPERVISION_NAME = 'staff_roles_and_supervision'
PROGRAM_DESCRIPTION_NAME = 'program_description'
SERVICES_NAME = 'assessment_results_services'
ASSESSMENT_RESULTS_NAME = 'assessment_results'
EDUCATIONAL_SERVICES_NAME = 'educational_services'
ACADEMIC_PERFORMANCE_NAME = 'academic_performance'
REVIEWED_RECORDS_NAME = 'reviewed_records'
VINELAND_NAME = 'vineland'
MALADAPTIVE_BEHAVIOR_INDEX_NAME = 'maladaptive_behavior_index'
DOMAIN_DETAILS_NAME = 'domain_details'
SCORE_SUMMARY_NAME = 'score_summary'
VINELAND_INFO_NAME = 'vineland_info'
VINELAND_DATA_NAME = 'vineland_info_data'
BACKGROUND_AND_METHODOLOGY_NAME = 'background_and_methodology'
BACKGROUND_AND_METHODOLOGY_ASSESSMENTS_RESULTS_NAME = 'background_and_methodology_assessment_results'
ASSESSMENT_APPOINTMENTS_NAME = 'assessment_appointments'
PROPOSED_OBJECTIVES_NAME = 'proposed_objectives'
OBJECTIVE_FIELDS = 'objective_fields'
TARGET_GROUPS_NAME = 'target_groups'
PHASE_CHANGE_EVENT_TYPES_NAME = 'phase_change_event_types'
ORIGINAL_OBJECTIVE_NAME = 'original_objective'
OBJECTIVE_DOMAIN_NAME = 'objective_domain'
MAINTENANCE_SCHEDULE_NAME = 'maintenance_schedule'
GENERALIZATION_NAME = 'generalization'
ESBACrisisPlanPoints_NANE = 'esba_crisis_plan_points'

SEPARATOR = '*'
EMPTY_COLUMN_NAME = 'COLUMN_WITHOUT_NAME_'
ID = 'Id'
PARENT_ID = '_id'
