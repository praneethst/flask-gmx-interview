'''myfamily = [
  [{
    "name" : "Emil",
    "year" : 2004
  }],
  [{
    "name" : "Tobias",
    "year" : 2007
  }]
  ]
  
for i in myfamily[0]:
	print(i["year"])
  
    
'''
import json
import re
f = open("dict.json", "r")
x=f.read()
f.close()
y=x.replace("}{", "}  {")
#print(y)
#print(type(y.split('  ')))
z=y.split('  ')
for item in z:
    a=item.split(",")
    o=a[1].replace("}","")[10:]
    n=a[0][10:]
    #print(n + o)
    #break
    
    if "Praneeth" in n and "Kumar" in o:
        print("got it")
       
        
    
    
    







