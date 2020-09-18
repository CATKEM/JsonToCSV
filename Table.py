ID = 'Id'
PARENT_ID = '_id'
SEPARATOR = '*'
EMPTY_COLUMN_NAME = 'COLUMN_WITHOUT_NAME_'


class Table:
    table_name = ''
    id_counter = 1
    columns = []
    rows = []
    lock_add_columns = False
    parent_ids = None

    def __init__(self, table_name, simple_dict=None, parent_name_to_id=None):
        self.table_name = table_name
        self.columns = []
        self.rows = []
        self.columns.append(ID)
        self.columns_added = False
        if parent_name_to_id:
            columns_to_insert = []
            for key in parent_name_to_id:
                columns_to_insert.append(str(key) + PARENT_ID)
            self.columns.extend(columns_to_insert)
            self.parent_ids = parent_name_to_id.values()
        if simple_dict:
            self.add_row_column_from_dict(simple_dict)

    def __add_column__(self, column_name):
        if not column_name:
            column_name = EMPTY_COLUMN_NAME + str(self.id_counter)
        column_name = column_name.lower()
        column_name = column_name.replace(' ', '_')
        self.columns.append(str(column_name))
        return self.columns

    def __add_row__(self, fields_list):
        if self.parent_ids:
            for parent_id in self.parent_ids:
                fields_list.insert(0, parent_id)
        if len(fields_list) != (len(self.columns) - 1):
            print('Structure ERROR: ' + self.table_name)
            # return
        fields_list.insert(0, str(self.id_counter))
        self.rows.append(fields_list)
        self.id_counter += 1

    def add_row_column_from_dict(self, dict_data):
        row = []
        for key in dict_data:
            if type(dict_data[key]) is list or type(dict_data[key]) is dict or type(dict_data[key]) is tuple:
                continue
            if not self.lock_add_columns:
                self.__add_column__(key)
            row.append(dict_data[key])
        self.lock_add_columns = True
        self.__add_row__(row)

    def add_columns(self, columns_list):
        if not self.lock_add_columns:
            for i in range(len(columns_list)):
                self.__add_column__(columns_list[i])
            self.lock_add_columns = True

    def add_column_from_dict(self, dict_data):
        if not self.lock_add_columns:
            for key in dict_data:
                if type(dict_data[key]) is list or type(dict_data[key]) is dict or type(dict_data[key]) is tuple:
                    continue
                self.__add_column__(key)
            self.lock_add_columns = True

    def add_exists_elements_to_row(self, dict_data, elements_list):
        row_to_insert = []
        for element in elements_list:
            if not dict_data.get(element) == None:
                row_to_insert.append(dict_data[element])
            else:
                row_to_insert.append('null')
        self.__add_row__(row_to_insert)

    def add_string_list_rows(self, rows):
        for i in range(len(rows)):
            self.__add_row__([rows[i]])

    def add_rows_from_dict(self, dict_data):
        fields = []
        for key in dict_data:
            if type(dict_data[key]) is list or type(dict_data[key]) is dict or type(dict_data[key]) is tuple:
                continue
            fields.append(dict_data[key])
        self.__add_row__(fields)

    def add_rows_from_value_headers_type(self, value_elements):
        for value_element in value_elements:
            self.__add_row__(value_element)

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
                self.__add_row__(row_data)

    def to_csv(self, path):
        with open(path + self.table_name + '.csv', 'w') as file:
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
        print('TABLE: ' + self.table_name + ' was created!')

    def get_last_id(self):
        return self.id_counter - 1

    def show(self):
        print('TABLE: ' + self.table_name)
        print(self.columns)
        for row in self.rows:
            print(row)
