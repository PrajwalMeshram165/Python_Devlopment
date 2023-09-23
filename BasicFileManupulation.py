import shutil
f1 = open("demo1.txt","w")
text=["hellow everyone. \n", "my name is prajwal. \n","now, I am learning python "]
f1.writelines(text)
f1 = open("demo1.txt","r")
print(f1.read())
f2=open("demo2.txt","w")
shutil.copyfile("C:\\Users\\prajwal meshram\\Documents\\GuitHub\\ARCANEGIT\\demo1.txt","C:\\Users\\prajwal meshram\\Documents\\GuitHub\\ARCANEGIT\\demo2.txt")
