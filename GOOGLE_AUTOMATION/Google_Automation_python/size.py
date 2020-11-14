import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w+') as f:
      abspath = os.path.join(os.getcwd(), filename)
      timestamp = os.path.getmtime(abspath)
  # Convert the timestamp into a readable format, then into a string
      time_new = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format((str(time_new.year)+"-"+str(time_new.month)+"-"+str(time_new.day))))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

