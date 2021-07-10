import random as rd
import json

f = open(r"/projects/my_project/MLearning/data/student_list.json", "w+")
f.write("[")
for i in range(10000):

  fname = [chr(int(97+26*rd.random())) for i in range(5+int(rd.random()*10))]
  lname = [chr(int(97+26*rd.random())) for i in range(5+int(rd.random()%10))]
  fname[0] = fname[0].upper()
  lname[0] = lname[0].upper()
  name = "".join(fname) + " " + "".join(lname)
  std_list = ['Prep', 'LKG', 'UKG', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
  'Intermediate', 'Graduation', 'Post-Graduation', 'Ph.D.', 'Doctorate',
  ]
  std_ind = int(rd.random()*18)
  std = std_list[std_ind]
  roll = str(180000 + i)
  age = 3 + std_ind + int(rd.random()*2)
  weight = 5+std_ind**1.5 + rd.random()*10
  height = (weight/(19+5*rd.random()))**0.5
  stud_data = json.dumps({
    'Name' : name,
    'Class' : std,
    'Age' : age,
    'Height' : round(height,2),
    'Weight' : round(weight,2),

  })
  f.write(stud_data+",\n")

f.write("]")