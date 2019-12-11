from FileManager import FileManager

file_name = 'user_input.txt'


class InputSaver:
    def __init__(self, form):
        self.input = form
        self.file_manager = FileManager()

    def save_data(self):
        try:
            for item in self.input.list:
                if item.name == 'textInput':
                    self.file_manager.write(self.input.getlist('textInput')[0], file_name)
                    continue
                self.file_manager.save(item)

            return 'Files saved'

        except Exception:
            return 'Oops something went wrong :('
