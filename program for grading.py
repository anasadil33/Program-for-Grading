
name = str(input("Enter Name of student:\n"));
section = str(input("Enter class:\n"));
marks = int(input("Enter marks obtained:\n"));
maxmarks = int(500);
minmarks = int(0);



sub1 = str(input("Enter subject name:"));
sub2 = str(input("Enter subject name:"));          
sub3 = str(input("Enter subject name:"));
sub4 = str(input("Enter subject name:"));          
sub5 = str(input("Enter subject name:"));
marks1 = int(input("Enter marks for sub1:"));  
marks2 = int(input("Enter marks for sub2:"));
marks3 = int(input("Enter marks for sub3:"));
marks4 = int(input("Enter marks for sub4:"));
marks5 = int(input("Enter marks for sub5:"));
total = marks1 + marks2 + marks3 + marks4 +marks5 ;

                   
                   
print ("Total marks are:", total);                   
if marks < 500 and marks  >= 400 :
    print("Excellent. Keep it up.\n");
elif marks < 400 and marks >= 200:
    print("Good. Can do better.\n");
elif marks < 200 and marks >= 100 :
    print ("Fair. Need to work hard. \n");
else :
    print ("Fail. Do better next time.\n");

     

    
