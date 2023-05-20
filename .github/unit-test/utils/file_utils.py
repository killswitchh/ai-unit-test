from redbaron import RedBaron
import os

class FileUtils:
    def __init__(self, filename):
        self.filename = filename

    def create_directory(directory):
        # Check whether the specified path exists or not
        isExist = os.path.exists(directory)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(directory)
            print("The new directory is created!")
        return directory
    def get_file_name(filePath):
        split = filePath.split("/")
        filename = split[-1]
        return filename
    def convert_to_test(filename):
        s = filename.split(".")
        new_name = s[0] + "_ai_tests" + "." + s[1]
        return new_name
