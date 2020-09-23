class FileManager:

    def __init__(self, input_file_path: str, output_file_path: str):
        self.input_file_path: str = input_file_path
        self.output_file_path: str = output_file_path
        self.links_list = None

    def read_file(self):
        with open(self.input_file_path) as f:
            self.links_list: list = f.readlines()
            self.links_list = [x.strip() for x in self.links_list]
            return self.links_list
