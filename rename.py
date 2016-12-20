import os
import time
import sys

### Renames files to their last modified timestamp ###

filepath = sys.argv[1]
if filepath[len(filepath) - 1] != "/":
	filepath = filepath + "/" # FILEPATH/
filenames = os.listdir(filepath)
renamed = []

def changename(oldname):
	# stat returns 10-member tuple: (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
	stat = os.stat(oldname)
	timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime(stat[8]))
	spl = oldname.split(".")
	if len(spl) < 2: # in case it's a folder not a file
		# print("SKIPPED FOLDER *" + oldname + "*")
		return
	ftype = "." + spl[len(spl) - 1] # .FILETYPE
	newname = filepath + timestamp + ftype

	# only proceed if name was changed
	if oldname == newname:
		# print("FILENAME *" + newname+ "* UNCHANGED")
		return

	# if a previous file name change was the same, increment the name and change
	ctr = 1
	while (timestamp + ftype) in filenames or (timestamp + ftype) in renamed:
		index = timestamp.find("_")
		if index >= 0:
			timestamp = timestamp[:index] + "_" + str(ctr)
		else:
			timestamp = timestamp + "_" + str(ctr)
		ctr += 1

	newname = filepath + timestamp + ftype
	renamed.append(timestamp + ftype)
	# print(oldname + " ==> " + newname)
	os.rename(oldname, newname)

def main():
	if (len(sys.argv) != 2):
		print("CMD ERROR: py rename.py + DIRECTORY")
		return

	for name in filenames:
		# in format FILEPATH/NAME
		changename(filepath + name)

	print("Successfully renamed files to their timestamps!")

if __name__ == "__main__":
    main()