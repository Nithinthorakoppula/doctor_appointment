# """
# 1.hospital
# 2.login
# 3.location-destination
# 4.slots availablity
# 5.date and time
# 6.op fee
# 7.user details -name,mobile,address,desease
# """
s="""
1.patient details
2.hospital and doctor
3.doctor slots
4.fee for op
5.book slot 
"""

doc={("wellness","nuero"):[{"Dr.Akhilesh":101},{"Dr.Ravindra":102},{"Dr.Arman":103}],
        ("Navodhaya","nuero"):[{"Dr.Amarsingh":789},{"Dr.Shamkumar":890},{"Dr.Raju":891}]} 

patients={"Nick": 123,"shashi": 234}
patients_details=[]
patient=input("enter the name: ")
if patient in patients.keys():
    passward=int(input("enter the passward: "))
    if passward == patients[patient]:
            print(s)
            option=int(input("enter your option: "))
            if option==1:
                name=input("enter your name: ")
                mobile=int(input("enter your mobile number:"))
                age=int(input("enter your age:"))
                gender=input("enter your gender:")
                desease=input("enter your desease: ")
                l=[name,mobile,age,gender,desease]
                patients_details.append(l)
            elif option==2:
                hospital=input("enter the hospital name : ")
                desease=input("enter your desease : ")
                print("Available Doctors :")
                if hospital in ("wellness","nuero"):
                    if desease in ("wellness","nuero"):
                        print(doc["wellness","nuero"])
                elif hospital in ("Navodhaya","nuero"):
                    if desease in ("Navodhaya","nuero"):
                        print(doc["Navodhaya","nuero"])
                else:
                    print("no doctor Available")

    else:
        print("inavalid")
else:
    print("enter valid name!")