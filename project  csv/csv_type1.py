import csv

class csv_type1:
    def parse(self, fsource):
        sending_array = []

        read_file = csv.reader(file(fsource))

        for row in read_file:
            dictn = {'email': row[0], 'city': row[1]}

            sending_array.append(dictn)

        return sending_array