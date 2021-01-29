import pickle
#pickling means priserving=======
# cars=["Audi","BMW","Harryti Tuzuki"]
# file = "Mycar.pkl"                          #pickling=========
# fileobj= open(file,'wb')    #wb == write binary
# pickle.dump(cars,fileobj)
# fileobj.close()

#=====depickling
file="Mycar.pkl"
fileobj=open(file,"rb")       #rb==read binary
mycar=pickle.load(fileobj)
print(type(mycar))

