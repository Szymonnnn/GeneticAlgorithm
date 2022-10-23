class Logger:
    def __init__(self, file_name):
        self.file = open(file_name, 'w')

    def log(self, string):
        print(string, file = self.file)

    def log_array(self, array):
        print('\n'.join(' '.join(str(x) for x in row) for row in array), file = self.file)
    
    def log_population(self, population):
        i = 0
        string = ""
        for individual in population:
            string += str(i) + ". " + str(individual) + ', '
            i += 1
        print(string, file = self.file)

    def close_file(self):
        self.file.close()