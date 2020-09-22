class FileManager:

    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.links_list = None

    def read_file(self):
        with open(self.input_file_path) as f:
            self.links_list = f.readlines()
            self.links_list = [x.strip() for x in self.links_list]
            return self.links_list

    def write_line(self, link):

