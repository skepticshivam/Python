import csv
import MySQLdb


class mysqlUserDb:
    def __init__(self, root, host, pwd):
        self.root = root
        self.host = host
        self.rootpw = pwd
        print '\nChecking MySQL connection...'
        self.db = MySQLdb.connect(self.host, self.root, self.rootpw)
        self.cursor = self.db.cursor()
        print 'Connection OK, proceeding.'

    def createdb(self):
        print '\nCreating database...'

        self.cursor.execute('create database if not exists store_email')

        #  self.cursor.execute('show databases like ' + '\'' + db + '\'')

        dbs = self.cursor.fetchone()

        self.cursor.execute('use store_email')

        print 'Database created: %s' % dbs

    def createtable(self, tquery):
        self.cursor.execute(tquery)

        print '\ncreating table...\n'

    def commit(self):
        self.cursor.execute('commit')


    def write_type(self, a, b):

        temp = ""

        for i in a:

            temp = temp + i + ","

        query1 = temp.strip(',')

        temp =""



        for i in b :

            temp = temp +"'"+ i+"'" + ","

        query2 = temp.strip(",")

        sql = "insert into email_compiled1 (" + query1 + ")" +" values(" + query2 + ");"



         self.cursor.execute(sql)

