#dr yasmeen assignment
gmail=input("enter your gmail: ") #input

find_at=gmail.find("@")  #variable to check index of @
find_dot=gmail.find(".") #variable to check index of @

if find_at!=-1 : #check "@" exist in gmail
    print("there is @ in gmail")

if find_dot!=-1 : #check "." exist in gmail
    print("there is . in gmail")

if find_at<find_dot :#check "@" exist in gmail
    print("@ is before .")
length=len(gmail)
length= length -find_dot 
if length-1==3:  
    print ("there is 3 numbers after .")
