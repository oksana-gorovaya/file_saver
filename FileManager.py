import os
from werkzeug.utils import secure_filename


class FileManager:
    def save(self, file, folder):
        filename = secure_filename(file.filename)
        file.save(os.path.join(folder, filename))

        return True

    def write(self, text, file):
        with open(file, 'w') as input_data:
            input_data.write(text)
