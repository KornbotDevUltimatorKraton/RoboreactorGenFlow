import os
import pwd
import time
import configparser 

user =  os.listdir("/home/")[0]
try:
   os.mkdir("/usr/lib/systemd/system",mode=0o777)
except:
    print("System directory was created")
Generate_path = "/usr/lib/systemd/system/" 
os.system("sudo chmod -R 777 "+Generate_path)
project_name = 'Project:RoboreactorGenFlow'
mode = 'multi-user.target' 
Python_exc_path = "/usr/bin/python3 "
Working_path = "/home/"+user+"/RoboreactorGenFlow"
Execute_path = "/home/"+user+"/RoboreactorGenFlow/RoboreactorGenFlow.py"   #Change username over the platform 
config = configparser.ConfigParser() 
config.optionxform = str
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
settings = ['Unit','Service','Install']
#Unit
config.add_section(settings[0]) # Getting the section added into the list topic 
config.set(settings[0],'Description',str(project_name)) 
config.set(settings[0],'After',str(mode))
#Service 
config.add_section(settings[1])
config.set(settings[1],'Type',str(type))
config.set(settings[1],'WorkingDirectory',Working_path)
config.set(settings[1],'User',str(user))
config.set(settings[1],'ExecStart',str(Python_exc_path+Execute_path))
config.set(settings[1],'WantedBy','always')
#Install 
config.add_section(settings[2])
config.set(settings[2],'WantedBy',str(mode))
configfile = open(Generate_path+"RoboreactorGenFlow.service",'w')
config.write(configfile)

