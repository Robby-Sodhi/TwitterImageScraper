
class FileError(Exception):
    def __init__(self, file):
        super().__init__(f"{file} doesn't exist") #passing our message to the Exception parent class
