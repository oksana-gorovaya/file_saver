from flask import request
from FileManager import FileManager

folder = 'files'
file_name = 'user_input.txt'


class InputSaver:
    def __init__(self):
        self.text = request.form['textInput']
        self.files = request.files
        self.file_manager = FileManager()

    def save_data(self):
        try:
            self.file_manager.write(self.text, file_name)

            uploaded_files = self.files.getlist("multipleFileInput")
            uploaded_files.append(self.files['singleFileInput'])

            for uploaded_file in uploaded_files:
                self.file_manager.save(uploaded_file, folder)

            return 'Files saved'

        except Exception:

            return 'Oops something went wrong :('
