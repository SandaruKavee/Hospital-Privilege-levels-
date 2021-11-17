import hashlib
import json
import sys

#validate the user name and password
def loginValidate(username, password):
    if(len(username)*len(password)==0):
        return False
    else:
        return True

#md5Hash Function
def md5Hash(password):
    return (hashlib.md5(password.encode()).hexdigest())

#check the password
def passwordCheck(pass1,pass2):

    return (md5Hash(pass1)==(pass2))

#type and previlage checking
def checkTypeAndLoggedIn(username,type):
    if (type=="doctor"):
        print("Logging in as a doctor")
        doctorView(username)
    elif (type=="nurse"):
        print("Logging in as a nurse")
        nurseView(username)
    elif(type=="patient"):
        print("Logging in as patient")
        patientView(username)
    else:
        print("invalid type")
    return
    


#login function
def login(username,password):
    if (loginValidate(username,password)):
        try:
            admin=open('admin.json','r')
            userlist=json.load(admin)['users']
            i=0
            while(i<len(userlist)):
                if(userlist[i]['username']==username):
                    
                    admin.close()
                    if (passwordCheck(password,userlist[i]['password'])):
                        checkTypeAndLoggedIn(userlist[i]['username'],userlist[i]['type'])
                        
                    return
                i+=1
            print("Enter a valid user name")
            admin.close()
            return
        except:
            print("something is error when opening")
    else:
        print("Pease enter a valid information")
        return
#view profile function
def viewMyProfille(username):
    admin=open('admin.json','r')
    userlist=json.load(admin)['users']
    i=0
    while(i<len(userlist)):
        if(userlist[i]['username']==username):
            admin.close()
            print(userlist[i]['type'])
            return {"username":username,"type":userlist[i]['type']}
        i+=1
    return


#patient view
def patientView(username):
    print("\n")
    print("================================================================================")
    print("Press 1 to see my profile")
    print("Press 2 to see my drugs")
    print("Press any key to exit")
    try:
        num=input("Enter Number :    ")
        if(num=="1"):
            print(viewMyProfille(username))
            print("\n")
            patientView(username)
            return
        elif (num=="2"):
            patientShowDrugs(username)
            print("\n")
            patientView(username)
            return
        else:
            print("Exiting")
            return
    except:
        print("error occured in patient view")
    return
#patient show drugs
def patientShowDrugs(username):
    print("\n")
    print("========================================================================================")
    print("These are the Drugs you have been given")
    data=open('deta records.json','r')
    recordList=json.load(data)['records']
    i=0
    myDrugs=[]
    while(i<len(recordList)):

        if(recordList[i]['patientName']==username):
            myDrugs.append({"Disease":recordList[i]['sickness'],"doctor":recordList[i]['docName'],"drug":recordList[i]['drug']})
            
        i+=1
    print (myDrugs)
    return 

#nurse view
def nurseView(username):
    print("\n")
    print("==========================================================================================")
    print("Press 1 to see your profile")
    print("Press 2 to see the all records of the patients that you can access")
    print("Press any key to exit")
    try:
        num=input("Enter Number :    ")
        if(num=="1"):
            print(viewMyProfille(username))
            print("\n")
            nurseView(username)
            return
        elif (num=="2"):
            nurseShowRecords()
            print("\n")
            nurseView(username)
            return
        else:
            print("Exiting")
            return
    except:
        print("error occured in patient view")
    return

   

#nurse show records
def nurseShowRecords():
    print("\n")
    print("========================================================================================")
    print("These are the Records of the patients ")
    data=open('deta records.json','r')
    recordList=json.load(data)['records']
    i=0
    records=[]
    while(i<len(recordList)):

        if(recordList[i]['sensitivity']=="low"):
            records.append({"Disease":recordList[i]['sickness'],"doctor":recordList[i]['docName'],"drug":recordList[i]['drug'],"lab report":recordList[i]['labTest']})
            
        i+=1
    print (records)
    return 

#doctor view
def doctorView(username):
    print("\n")
    print("================================================================================================")
    print("Press 1 for see your Profile")
    print("Press 2 for see all the records of the patients")
    print("Press 3 for adding a new record")
    print("press 4 for show the records you created")
    print("press any key to exit")
    try:
        num=input("Enter Number :    ")
        if(num=="1"):
            print(viewMyProfille(username))
            print("\n")
            doctorView(username)
            return
        elif (num=="2"):
            doctorShowRecords()
            print("\n")
            doctorView(username)
            return
        elif(num=="3"):
            doctorAddaRecordPage(username)
            return
        elif(num=="4"):
            doctorYourRecords(username)
            doctorView(username)
            return
        else:
            print("Exiting")
            return
    except:
        print("error occured in patient view")
    return

#doctor show records
def doctorShowRecords():
    print("\n")
    print("========================================================================================")
    print("These are the Records of the Patients")
    data=open('deta records.json','r')
    recordList=json.load(data)['records']
    i=0
    records=[]
    while(i<len(recordList)):
        records.append({"recordID":recordList[i]['recordID'],"Disease":recordList[i]['sickness'],"doctor":recordList[i]['docName'],"drug":recordList[i]['drug'],"lab report":recordList[i]['labTest']})
            
        i+=1
    print (records)
    return 

#Doctor add a record Page
def doctorAddaRecordPage(username):
    print("\n")
    print("========================================================================================")
    print("Enter the Record Details Correctly")
    data=open('deta records.json','r')
    recordList=json.load(data)['records']
    recordID=str(len(recordList)+1)
    docName=username
    patientID=input("Enter patient ID  :     ")
    patientAge=input("Enter Patient Age   :   ")
    sickness=input("Enter disease   :   ")
    drug=input("Enter the drug that is given to the Patient   :   ")
    labTest=input("Enter the Lab Test   :   ")
    sensitivity=input("Enter the Sensitivity of the data high or low   :   ")
    newRecord={"recordID":recordID,"patientName":patientID,"docName":docName,"patientAge":patientAge,"sickness":sickness,"drug":drug,"labTest":labTest,"sensitivity":sensitivity}
    recordList.append(newRecord)
    recordWrite=open('deta records.json','w')
    recordWrite.writelines(json.dumps({"records":recordList}))
    print("Successfully recorded")
    recordWrite.close()
    data.close()


    doctorView(username)
    return
#docter see my records
def doctorYourRecords(username):
    print("\n")
    print("========================================================================================")
    print("These are the Records of the Patients made by you")
    data=open('deta records.json','r')
    recordList=json.load(data)['records']
    i=0
    records=[]
    while(i<len(recordList)):
        if (recordList[i]['docName']==username):
            records.append({"recordID":recordList[i]['recordID'],"Disease":recordList[i]['sickness'],"doctor":recordList[i]['docName'],"drug":recordList[i]['drug'],"lab report":recordList[i]['labTest']})
            
        i+=1
    print (records)
    return 



#login view
def loginView():
    a=input("Username  :   ")
    b=input("Password  :   ")
    login(a,b)
    return

#sign up view
def signUpView():
    print("==================================")
    print("welcome")
    print("enter Your Details")
    username=input("Enter your username       ")
    password=input("enter your password        ")
    type=input("Enter your type nurse/doctor or a patient       ")
    print("signing in")
    if (signUpValidation(username,password,type)):
        newPw=md5Hash(password)
        signUp(username,newPw,type,password)
    return
#sign up validation
def signUpValidation(username,password,type):
    if(len(username)*len(password)*len(type)==0):
        return False

    else:
        return True

#sign up function
def signUp(username,pw,type,password):
    try:
        admin=open('admin.json','r')
        usersList=json.load(admin)['users']
        newuser={"username":username,"password":pw,"type":type}
        usersList.append(newuser)
        adminWrite=open('admin.json','w')
        adminWrite.writelines(json.dumps({"users":usersList}))
        print("Successfully Signed In")
        adminWrite.close()
        admin.close()
        login(username,password)
    except:
        print("Error When signing Up")   
    return

#main page 
print("Hospital Health Care")
print("press 1 for the sign up")
print("press 2 for the log in ")
x=input("Enter the Number :     ")
if (x=="1"):
    signUpView()
elif(x=="2"):
    loginView()
else:
    print("enter a valid number")










