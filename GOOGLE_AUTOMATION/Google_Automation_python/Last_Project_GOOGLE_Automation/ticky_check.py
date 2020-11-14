#!/usr/bin/env python3

import re
import operator
import csv


diff_errors = {} #to store diff erors with freq
user_errors = {}  #to storename of users and their respective count of info and errors  

errors = []  #list to store error logs
info =[]   # .....info logs
users = []
user_name_info = []

# processing syslog.log

with open('syslog.log' , 'r') as file:
  lines =  file.readlines()
  for line in lines:
    #print(line)
    if (re.search(r"[\w ]+:[\d:]+[ \w \.]+\:\s(INFO)\s[\w ]*[\[#0-9]+\]\s\([\.\w]+\)", line.strip())) != None:
      info.append(line)
    else:
      errors.append(line)

# print(errors)
# print(info)

for error in errors:
  #find error if present in dict add else increament the key
  # extract the error
  result = re.match(r"[\w ]+:[\d:]+[ \w \.]+\:\sERROR\s([\w \']+)\(([\w\.]+)\)", error)
  try:
    if result.group(2)not in users:
      users.append(result.group(2))
    if result.group(1) not in diff_errors:
      diff_errors[result.group(1)] = 1
      #print(result.group(1))
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
# print(user_errors)

#creating the user_info dict
user_info = {}
for info_item in info:
  result = re.match(r"[\w ]+:[\d:]+[ \w \.]+\:\s(INFO)\s[\w ]*[\[#0-9]+\]\s\(([\.\w]+)\)",info_item)
  try:
    if result.group(2) not in user_name_info:
      user_name_info.append(result.group(2))
    if result.group(2) not in user_info:
      user_info[result.group(2)] = 1
    else:
      user_info[result.group(2)] = user_info[result.group(2)] + 1
  except:
    pass

# print(user_info)
sorted(user_errors.items())
#print("------------------------------\n")
sorted(user_info.items())


diff_errors_sorted = []
diff_errors_sorted = sorted(diff_errors.items(), key = operator.itemgetter(1), reverse=True)
# print(diff_errors_sorted)
# Genetating csv files from thre dictionaries
# sorted(diff_errors.items(), key = operator.itemgetter(1), reverse=True)
#--------------------------------------

csv_file = "error_message.csv"

try:
  with open(csv_file, 'w') as f:
    f.write("ERROR,COUNT \n")
    for key in diff_errors_sorted:
      f.write("%s,%s\n" %(key[0],key[1]))
except IOError:
  print("I/O error")

#----------------------------------------

sorted_errors = []
sorted_errors = sorted(user_errors.items())
sorted_info = []
sorted_info = sorted(user_info.items())

#-------------------------------------------
csv_file = "user_statistics.csv"
try:
  with open(csv_file, 'w') as f:
    f.write("Username,INFO,ERROR\n")
    for name_error in sorted_errors:
      if name_error[0] in user_name_info:
        f.write("%s,%s,%s\n"%(name_error[0].strip(),user_info[name_error[0]],name_error[1]))
      else:
        f.write("%s,%s,%s\n"%(name_error[0].strip(),0,name_error[1]))
except IOError:
  print("I/O Error")


print(f"User Error Length:-{len(sorted_errors)}")
print(f"User Error:- {sorted_errors}")
print(f"User Info:- {sorted_info}")
# print(f"Users:- {users}")
