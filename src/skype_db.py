import sqlite3
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

success = bcolors.BOLD + bcolors.OKGREEN + "[-]" + bcolors.ENDC
fail = bcolors.BOLD + bcolors.FAIL + "[-]" + bcolors.ENDC

def skype_db_contacts(path):
	index = []
	index.append(0)
	conn = sqlite3.connect(path)
	c = conn.cursor()
	contacts = c.execute("SELECT * FROM 'Contacts'")
	for row in c.fetchall():
		sys.stdout.write("    " + success +row[3][2:])
		if len(row[3][2:]) > 24:
			sys.stdout.write(" \t: ")
		elif len(row[3][2:]) >= 16:
			sys.stdout.write(" \t\t: ")
		elif len(row[3][2:]) < 8:
			sys.stdout.write(" \t\t\t\t: ")
		else:	
			sys.stdout.write(" \t\t\t: ")
		if not row[6] is None:
			index[0] += 1
			sys.stdout.write(row[6].encode('utf-8', 'ignore'))
		if not row[15] == "" and not row[15] is None:
			sys.stdout.write(" \t\t: ")
			sys.stdout.write(str(row[15]))
		sys.stdout.write("\n")
	conn.close()
	if index[0] == 0:
		print "    " + fail + "No Skype contacts"

def skype_db_transfers(path):
	index = []
	index.append(0)
	conn = sqlite3.connect(path)
	c = conn.cursor()
	contacts = c.execute("SELECT * FROM 'Transfers'")
	for row in c.fetchall():
		index[0] += 1
		print success + row
	conn.close()
	if index[0] == 0:
		print "    " + fail + "No file transfers through Skype"

#skype_db_transfers("../main.db")