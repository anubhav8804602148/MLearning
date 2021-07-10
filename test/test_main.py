import random as rd
f = open(r"/projects/MLearning/data/student_list.csv")

for i in range(1000):
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
  roll = 180000 + i;
  age = 3 + std_ind + int(rd.random()*2)
  height = std_ind**1.5 + rd.random(4)
  weight = rd.random()