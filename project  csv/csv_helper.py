from csv_type1 import csv_type1
from csv_type2 import csv_type2
from csv_type3 import csv_type3
from csv_type4 import csv_type4


def direct(type) :
    if type == 1 :

        obj = csv_type1()

    elif type == 2 :

        obj = csv_type2()

    elif type == 3 :

        obj =  csv_type3()

    else :

        obj = csv_type4()

    print type

    return obj

