from PIL import Image
import os

# 将所有照片保存为450*800的缩略图
# （仅需在放入所有图片后运行一次）
class PictureResizer:
    def __init__(self, path):
        self.path = path
        self.all_folder = []

    def load_all_photo(self):
        folders = os.listdir(self.path)
        for folder in folders:
            path = self.path + '/' + folder
            photo = os.listdir(path)
            self.all_folder.append([path + '/' + item for item in photo])

    def compress_photo(self):
        if self.all_folder:
            for folder in self.all_folder:
                if folder:
                    for picture in folder:
                        try:
                            img = Image.open(picture)
                            img.thumbnail((600, 800))
                            img.save(picture)
                        except:
                            print("学生照片损坏：" + picture)
    def start(self):
        self.load_all_photo()
        self.compress_photo()
