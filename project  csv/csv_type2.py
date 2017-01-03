import csv

class csv_type2:
    def parse(self, fsource):
        sending_array = []

        read_file = csv.reader(file(fsource))

        for row in read_file:
            dictn = {'name': row[0], 'email': row[1], 'category': row[2], 'city': row[3], 'address': row[4],'pin': row[5]}

            sending_array.append(dictn)
        print sending_array
        return sending_array

a = csv_type2()
a.parse("r.csv")