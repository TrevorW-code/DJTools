import os, mutagen, pprint
for root, dirs, files in os.walk('.'):
	for file in files:
		no_obj = [tags for tags in mutagen.File(str(file))]
		# tags!='GEOB'
		pprint.pprint(no_obj)