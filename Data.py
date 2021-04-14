import os
import xlrd

class Data:
    def __init__(self, fdy):
        self.fdy_name = fdy
        self.student_info = {}
        self.info_path = 'student_info'
        self.img_path = 'photos'

    def load_student_info(self):
        path_name = self.info_path + '/' + self.fdy_name
        if os.path.exists(path_name + '.xls'):
            path = path_name + '.xls'
        elif os.path.exists(path_name + '.xlsx'):
            path = path_name + '.xlsx'
        else:
            # TODO Error Process
            pass
        sheet = xlrd.open_workbook(path).sheet_by_index(0)
        for i in range(1, sheet.nrows):
            row = sheet.row_values(i)
            self.student_info[str(int(row[0]))] = [row[1], row[11], row[3], row[9]]
        
    def get_student_info(self, student_id):
        if student_id in self.student_info.keys():
            return self.student_info[student_id]
        else:
            return ['', '', '', '']

    def get_photo(self, student_id):
        path = self.img_path + '/' + self.fdy_name
        files = os.listdir(path)
        for file in files:
            if student_id in file:
                return path + '/' + file
        return ''
