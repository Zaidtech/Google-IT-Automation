#!/usr/bin/env python3

import re
import operator
import csv


diff_errors = {} #to store diff erors with freq
user_errors = {}  #to storename of users and their respective count of info and errors  
errors = []  #list to store error logs
info =[]   # .....info logs

# processing syslog.log

with open('syslog.log' , 'r') as file:
  lines =  file.readlines()
  for line in lines:
    print(line)
    if (re.search(r"[\w ]+:[\d:]+[ \w \.]+\:\s(INFO)\s[\w ]*[\[#0-9]+\]\s\([\.\w]+\)", line.strip())) != None:
      #print("Info log")
     # append the info log in a list
      info.append(line)
    else:
      #print("Error Log")
      # append errors into a list
      errors.append(line)
    #if (re.search(r"[\w ]+:[\d:]+[ \w \.]+\:\s(INFO)\s[\w ]*[\[#0-9]+\]\s\([\.\w]+\)", line.strip())) != None:
     # print("Error log")
      #continue


#print(errors)
#print(info)

for error in errors:
  #find error if present in dict add else increament the key
  # extract the error
  result = re.match(r"[\w ]+:[\d:]+[ \w \.]+\:\sERROR\s([\w \']+)\(([\w\.]+)\)", error)
  try:
      if result.group(1) not in diff_errors:
        diff_errors[result.group(1)] = 1
        print(result.group(1))
      else:
        diff_errors[result.group(1)]= diff_errors[result.group(1)]+1
  except:
    pass
# Creting the user_erros dict 
    #result_info = re.match(r"[\w ]+:[\d:]+[ \w \.]+\:\s(INFO)\s[\w ]*[\[#0-9]+\]\s\([\.\w]+\)",info_count)
    try:
      if result.group(2) not in user_errors:
        user_errors[result.group(2)]=1
      else:
        user_errors[result.group(2)] = user_errors[result.group(2)]+1
    except:
      pass

#creating the user_info dict
user_info = {}
for info_item in info:
  result = re.match(r"[\w ]+:[\d:]+[ \w \.]+\:\s(INFO)\s[\w ]*[\[#0-9]+\]\s\(([\.\w]+)\)",info_item)
#print(sorted(diff_errors.items(), key = operator.itemgetter(1), reverse=True))
  try:
    if result.group(2) not in user_info:
      user_info[result.group(2)] = 1
    else:
      user_info[result.group(2)] = user_info[result.group(2)] + 1
  except:
    pass

print(sorted(user_errors.items(), key = operator.itemgetter(1),reverse=False))
print("------------------------------\n")
print(sorted(user_info.items()))




# Genetating csv files from thre dictionaries

#--------------------------------------

csv_file = "error_message.csv"

try:
  with open(csv_file, 'w') as f:
    f.write("ERROR,COUNT \n")
    for key in diff_errors.keys():
      f.write("%s,%s\n" %(key.strip(),diff_errors[key]))
except IOError:
  print("I/O error")

#----------------------------------------

csv_file = "user_statistics.csv"
try:
  with open(csv_file, 'w') as f:
    f.write("Username,INFO,ERROR")
    for key in user_errors.keys():
      #f.write("%s,%s,%s\n %d(key.strip(),tuple))
      pass
except IOError:
  print("I/O Error")



