import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w+') as file:
      timestamp = os.path.getmtime(file)
  # Convert the timestamp into a readable format, then into a string
      time_new = datetime.datetime.fromtimestammp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{ }".format(new_time))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
