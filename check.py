programfile = open("/t3/model1.py",'r')
code= programfile.read()
if 'keras' or 'tensorflow' in code:
    if 'Conv2D' in code:
          print("exist")
    else:
         print("not present")
else:
   print("not a NN")
         
