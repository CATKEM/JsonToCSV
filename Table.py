ID = 'Id'
SEPARATOR = '*'
EMPTY_COLUMN_NAME = 'COLUMN_WITHOUT_NAME_'


class Table:
    table_name = ''
    id_counter = 1
    columns = []
    rows = []
    columns_added = False
    parent_ids = None

    def __init__(self, table_name, simple_dict=None, parent_name_to_id=None):
        self.__table_name__ = table_name
        self.columns = []
        self.rows = []
        self.columns.append(ID)
        self.columns_added = False
        if parent_name_to_id:
            self.columns.extend(parent_name_to_id.keys())
            self.parent_ids = parent_name_to_id.values()
        if simple_dict:
            self.add_row_column_from_dict(simple_dict)

    def add_row_column_from_dict(self, dict_data):
        row = []
        for key in dict_data:
            if type(dict_data[key]) is list or type(dict_data[key]) is dict or type(dict_data[key]) is tuple:
                continue
            self.add_column(key)
            row.append(dict_data[key])
        self.add_row(row)

    def add_columns(self, column_name):
        for i in range(len(column_name)):
            self.add_column(column_name[i])
        return self.columns

    def add_column(self, column_name):
        if not column_name:
            column_name = EMPTY_COLUMN_NAME + str(self.id_counter)
        column_name = column_name.lower()
        column_name = column_name.replace(' ', '_')
        self.columns.append(str(column_name))
        return self.columns

    def add_column_from_dict(self, dict_data):
        for key in dict_data:
            if type(dict_data[key]) is list or type(dict_data[key]) is dict or type(dict_data[key]) is tuple:
                continue
            self.add_column(key)
        return True

    def add_row(self, record_fields):
        if self.parent_ids:
            for parent_id in range(len(self.parent_ids)):
                record_fields.insert(0, parent_id)
        if len(record_fields) != (len(self.columns) - 1):
            print('Structure ERROR')
            return
        record_fields.insert(0, str(self.id_counter))
        self.rows.append(record_fields)
        self.id_counter += 1
        return

    def add_string_list_rows(self, rows):
        for i in range(len(rows)):
            self.add_row([rows[i]])

    def add_rows_from_dict(self, dict_data):
        fields = []
        for key in dict_data:
            if type(dict_data[key]) is list or type(dict_data[key]) is dict or type(dict_data[key]) is tuple:
                continue
            fields.append(dict_data[key])
        self.add_row(fields)

    def add_rows_from_value_headers_type(self, value_elements):
        for value_element in value_elements:
            self.add_row(value_element)

    def add_rows_from_data_headers_type(self, data, elements_name):
        for i in range(len(data['data'])):
            for j in range(len(data['data'][i])):
                row_data = []
                if len(data['data'][i]) != len(data['headers']):
                    print('Data-Header ERROR')
                row_data.append(data['headers'][j])
                for element_name in elements_name:
                    if data['data'][i][j].get(element_name):
                        row_data.append(data['data'][i][j][element_name])
                    else:
                        row_data.append(False)
                self.add_row(row_data)

    def to_csv(self, path):
        with open(path + self.__table_name__ + '.csv', 'w') as file:
            for i in range(len(self.columns)):
                if i == 0:
                    file.write(str(self.columns[i]))
                else:
                    file.write(SEPARATOR + str(self.columns[i]))
            file.write('\n')
            for i in range(len(self.rows)):
                for j in range(len(self.rows[i])):
                    if j == 0:
                        file.write(str(self.rows[i][j]))
                    else:
                        file.write(SEPARATOR + str(self.rows[i][j]))
                file.write('\n')

    def get_last_id(self):
        return self.id_counter

    def show(self):
        print('TABLE: ' + self.__table_name__)
        print(self.columns)
        for row in self.rows:
            print(row)
