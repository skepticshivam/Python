import csv

class csv_type4:
    def parse(self, fsource ):
        sending_array = []

        read_file = csv.reader(file(fsource))

        for row in read_file:
            dictn = {'name': row[0], 'mobile': row[1], 'email': row[2], 'city': row[3], 'state': row[4],'gender': row[5],'DOB': row[6]}

            sending_array.append(dictn)

        return sending_array

