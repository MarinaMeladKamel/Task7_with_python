import csv

name = 'Name';
email = 'Email';
mobile = 'Mobile';
university = 'University';
major = 'Major';
peoples = []

while name != 'stop':
   name = ""; email = ""; mobile = ""; university = ""; major = "";
   name = input('Enter ur name: ')
   if name != 'stop':
       email = input('enter ur email: ')
   else:
       name = ""
       break
   if email != 'stop':
       mobile = input('enter ur mobile: ')
   else:
       email = ""
       break
   if mobile != 'stop':
       university = input('enter ur university: ')
   else:
       mobile = ""
       break
   if university != 'stop':
       major = input('enter ur major: ')
   else:
       university = ""
       break
   if major == 'stop':
       major = ""
       break

   peoples.append({'name': name, 'email': email, 'mobile': mobile, 'university': university, 'major': major})



with open('peopleData.csv', 'w', newline='') as csv_file:
   fieldnames = ['Name', 'Email', 'Mobile', 'University', 'Major']
   writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
   writer.writeheader()

   for people in peoples:
       writer.writerow({'Name': people['name'], 'Email': people['email'], 'Mobile': people['mobile'],
                        'University': people['university'], 'Major': people['major']})