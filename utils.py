import csv

def refresh_library(csv_file, path=path): # only for current files
  '''
  function that scans current library, reads them into csv.
  '''

  # AS: maybe use pandas here? could be a lot cleaner
  # TW: I was thinking this, but I am walking the directory so I was wondering if OS is the best
  # TW: ugly, but not sure another method

  # AS: prioritize readability over performance, the difference is gonna be so marginal it's not worth the tradeoff
  # TW: ok

  with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for _, dirs, file_names in os.walk(path):
      for file_name in file_names:
        song = file_name.split(" - ",1)
        print(song)
        try:
          writer.writerow([song[0]]+[re.sub('.mp[0-9]','',song[1])]) 
        except IndexError:
          writer.writerow(song+["__UNKNOWN__"]) # how do I add an empty column?
    print('---Done---')