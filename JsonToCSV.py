from Table import Table
import json

dirFilePath = '/home/user/Downloads/'
jsonFileName = 'dataFile.json'
tables = []


with open(dirFilePath + jsonFileName) as jsonFile:
    data = json.load(jsonFile)


main_table = Table('main_table')
main_table.add_simple_key_columns(data)
main_table.insert_simple_value_row(data)
tables.append(main_table)

if data.get('client'):
    client_table = Table('client')
    client_table.add_simple_key_columns(data['client'])
    client_table.insert_simple_value_row(data['client'])
    tables.append(client_table)

if data.get('recommendations'):
    recommendations_table = Table('recommendations')
    recommendations_table.add_simple_key_columns(data['recommendations'])
    recommendations_table.insert_simple_value_row(data['recommendations'])
    tables.append(recommendations_table)

if data.get('persons'):
    persons_table = Table('persons')
    for i in range(len(data['persons'])):
        if not persons_table.columns_added:
            persons_table.add_simple_key_columns(data['persons'][i])
        persons_table.insert_simple_value_row(data['persons'][i])
    tables.append(persons_table)

if data.get('recommendations'):
    recommendations_table = Table('recommendations')
    recommendations_table.add_simple_key_columns(data['recommendations'])
    recommendations_table.insert_simple_value_row(data['recommendations'])
    tables.append(recommendations_table)
