
name = str(input("Enter Name:\n"));
section = str(input("Enter class:\n"));
marks = int(input("Enter marks obtained:"));
maxmarks = int(500);
minmarks = int(0);

if marks < 500 and marks  >= 400 :
    print("Excellent\n");
elif marks < 400 and marks >= 200:
    print("Good\n");
elif marks < 200 and marks >= 100 :
    print ("Fair\n");
else :
    print ("Fail\n");
     

    