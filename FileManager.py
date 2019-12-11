import os


class FileManager:
    def save(self, file):
        fn = os.path.basename(file.filename)
        open('./files/' + fn, 'wb').write(file.file.read())

        return True

    def write(self, text, file):
        with open(file, 'w') as input_data:
            input_data.write(text)
