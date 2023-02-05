import os
import shutil
from pprint import pprint
from time import gmtime


class Sort:
    def __init__(self):
        self.file_names = None
        self.dir_path = None
        self.file_path = ''
        self.array_of_files_dates = {}

    def scan_dir(self, path):
        self.dir_path = path
        for dirpath, dirnames, filenames in os.walk(self.dir_path):
            self.file_names = filenames
        print(self.file_names)
        for key in self.file_names:
            self.array_of_files_dates[key] = os.path.getmtime(os.path.join(self.dir_path, key))
        # pprint(self.array_of_files_dates)

    def path_creation(self):
        for key in self.array_of_files_dates:
            year = gmtime(self.array_of_files_dates[key]).tm_year
            mon = gmtime(self.array_of_files_dates[key]).tm_mon
            new_dir = os.path.join(os.path.normpath('d:/res'), str(year), str(mon))
            src_file = os.path.join(self.dir_path, key)
            print(f'{key:40} — {new_dir:10}')
            os.makedirs(new_dir, exist_ok=True)
            shutil.copy2(src_file, new_dir)

