import os
import random

# 负责加载辅导员的所有学生照片路径，
# 滚动时随机访问路径，停止时获取当前选中学生的学号
class roll_photo:
    def __init__(self):
        self.fdy_selected = ""
        self.all_fdy_student = []
        self.current_selected_student = 0
        self.img_path = 'photos'

    # 每次换辅导员的所有预加载动作
    def reset(self, fdy):
        self.all_fdy_student = []
        self.fdy_selected = fdy
        if self.fdy_selected:
            path = self.img_path + '/' + self.fdy_selected
            files = os.listdir(path)
            if files:
                self.all_fdy_student = [path + '/' + item for item in files]
                self.current_selected_student = 0
                self.fdy_selected = fdy
                return True
            
            else:
                return False
    

    # 随机访问图片
    def display_photo(self):
        if self.all_fdy_student:
            # 考虑其他随机方式
            self.current_selected_student = random.randint(0, len(self.all_fdy_student) - 1)
            return self.all_fdy_student[self.current_selected_student]

    # 返回当前选中的学生学号(str) 
    def get_current_selected_student_id(self):
       
        selected_path = self.all_fdy_student[self.current_selected_student]
        self.all_fdy_student.remove(selected_path)
        photo_name = selected_path.split('/')[-1]
        student_id = photo_name.split('.')[0]
        return student_id