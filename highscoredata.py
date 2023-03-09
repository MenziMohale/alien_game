class HighScore:
    """ Writes and stores the high  in a file"""

    def __init__(self, file='high_score_data.txt'):
        self.file = file

    def update_high_score(self, data_to_write):
        file = open(self.file, "w")
        file.write(f"{data_to_write}")
        file.close()

    def pull_high_score(self):
        file = open(self.file, "r")
        read_file = file.read()
        convert = int(read_file)
        return convert
