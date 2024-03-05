import os


class Cd:
    def __init__(self, new_dir):
        try:
            if not os.path.isdir(new_dir):
                raise ValueError(f"ValueError: The path '{new_dir}' is not a directory or does not exist.")
            else:
                self.new_dir = new_dir
                self.prev_dir = os.getcwd()
        except ValueError as ve:
            print(ve)

    def __enter__(self):
        os.chdir(self.new_dir)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.prev_dir)
