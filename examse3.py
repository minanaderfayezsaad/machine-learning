email=input("Enter your email")
print(email.find("@"))
if "@" in email :
    print("valid")
print(email.split("."))
atindex=email.find("@")
dotindex=email.find(".")
# if "@gmail.com" in email:
#     print("valid email")

if atindex< dotindex:
    print("valid email")
print(len(email))
if len(email) >= 15:
    print("valid email")
print(email[:5])
print(email[dotindex+1:])
t=email[dotindex+1:]
if t>3:
    print("invalid")
if "." not in email:
    print("ivalid no dot")
elif "@" not in email:
    print("ivalid no @")
elif atindex > dotindex:
    print("ivalid @ after .")
else:
    print("valid")
print(email.replace("@","."))
