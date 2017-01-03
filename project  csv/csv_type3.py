import csv

class csv_type3:
    def parse(self, fsource):
        sending_array = []

        read_file = csv.reader(file(fsource))

        for row in read_file:
            dictn = {'name': row[0], 'email': row[1], 'mobile': row[2], 'category': row[3], 'city': row[4],'address': row[5]}

            sending_array.append(dictn)

        return sending_array