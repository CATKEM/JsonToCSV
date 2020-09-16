ID = 'Id'
SEPARATOR = ','


class Table:
    table_name = ''
    id_counter = 1
    columns = []
    rows = []
    columns_added = False

    def __init__(self, table_name):
        self.__table_name__ = table_name
        self.columns = []
        self.rows = []
        self.columns.append(ID)
        self.columns_added = False

    def add_columns(self, *column_name):
        for i in range(len(column_name)):
            self.add_column(column_name[i])
        return self.columns

    def add_column(self, column_name):
        self.columns.append(str(column_name))
        return self.columns

    def add_simple_key_columns(self, dict_data):
        for key in dict_data:
            if type(dict_data[key]) is list or type(dict_data[key]) is dict or type(dict_data[key]) is tuple:
                continue
            self.add_column(key)
        return True

    def insert_row(self, record_fields):
        if len(record_fields) != (len(self.columns) - 1):
            return False
        record_fields.insert(0, str(self.id_counter))
        self.rows.append(record_fields)
        self.id_counter += 1
        return True

    def insert_simple_value_row(self, dict_data):
        fields = []
        for key in dict_data:
            if type(dict_data[key]) is list or type(dict_data[key]) is dict or type(dict_data[key]) is tuple:
                continue
            fields.append(dict_data[key])
        self.insert_row(fields)

    def to_csv(self, path):
        with open(path + self.__table_name__ + '.csv') as file:
            for i in range(len(self.columns)):
                file.write(str(self.columns[i]))
            file.write('\n')
            for i in range(len(self.rows)):
                file.write(str(self.rows[i] + '\n'))

    def show(self):
        print('TABLE: ' + self.__table_name__)
        print(self.columns)
        print(self.rows)
