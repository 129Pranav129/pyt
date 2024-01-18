import subprocess

from datetime import datetime
calltype=1
loop_is_on=True
rgid=0

msisdn = int(input("Enter your msisdn : "))
time = int(input("Enter your time : "))
tester= input("Who is testing , pls enter your initials in caps and use the same one consistently !!!!! : ")


with open(f"/scratch/ri-user-1/opt/diameter_tp/scenario/{tester}.sh","w") as file3:
    file3.write('')

while(loop_is_on):
    usage = input("Enter VOICE_ONNET   :VOICE_OFFNET   :DATA_WO_CELL   :DATA_WITH_CELL   :SMS   :---- ")
    usage_quantity =  int(input("Enter the usage quantity : "))
    session_id =int(datetime.now().timestamp())

    if(usage == "VOICE_ONNET"):
        filename= "voice_onnet_usage_pj"
        calltype=1
        session_id= "VOICE_ONNET"+str(session_id)
    elif(usage == "VOICE_OFFNET"):
        calltype=0
        filename= "voice_offnet_pj"
        session_id= "VOICE_OFFNET"+str(session_id)
    elif(usage == "DATA_WO_CELL"):
        rgid=int(input("Enter the Rgid , or 20 for default : "))
        filename= "data_usage_wo_cellid_pj"  
        session_id= "DATA_WO_CELL"+str(session_id)  
    elif(usage == "DATA_WITH_CELL"):
        rgid=int(input("Enter the Rgid , or 20 for default : "))        
        filename= "data_usage_with_cellid_pj"
        session_id= "DATA_WITH_CELL"+str(session_id)
    elif(usage == "SMS"):
        filename= "sms_usage_pj"
        session_id= "SMS"+str(session_id)
    print(f"TYOUR SESSION_ID IS : {session_id} ") 
      

    with open(f"/scratch/ri-user-1/opt/diameter_tp/scenario/{filename}.xml") as file:
        new_file=file.read()
        new_file=new_file.replace("MSISDN",str(msisdn))
        new_file=new_file.replace("TIMESTAMP",str(time))
        new_file=new_file.replace("DURATION",str(usage_quantity))
        new_file=new_file.replace("CALLTYPE",str(calltype))
        new_file=new_file.replace("SESSION_ID",str(session_id))
        new_file=new_file.replace("RGID",str(rgid))

        with open(f"/scratch/ri-user-1/opt/diameter_tp/scenario/{filename}_{tester}_new.xml","w") as file2:
            file2.write(new_file)
  
    with open(f"/scratch/ri-user-1/opt/diameter_tp/scenario/{tester}.sh","a") as file3:
        file3.write(f"./run.sh {filename}_{tester}_new.xml")
        file3.write('\n')


    choice=input("Do you want to do more usages , y or n : ")
    if(choice.lower() == "n"):
        loop_is_on= False

print("##############################################################################")
print("")
print(f"YOUR RUN.SH HAS BEEN GENERATED WITH NAME {tester}.sh . Run it to get the result ")
print("")
print("##############################################################################")

# # Replace "run.sh" with the actual name of your shell script
# script_name = "/scratch/ri-user-1/opt/diameter_tp/scenario/run.sh"
# input_xml_file = "/scratch/ri-user-1/opt/diameter_tp/scenario/"+filename+"_new.xml"

# # Run the shell script
# subprocess.run(["./" + script_name, input_xml_file], shell=True)


