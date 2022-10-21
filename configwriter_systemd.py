import os 
import getpass 
import configparser 
user = getpass.getuser()
Generate_path = "/usr/lib/systemd/system/" 
project_name = 'Project:RoboreactorGenFlow'
mode = 'multi-user.target' 
type = 'idle'
wanted = 'WantedBy'
execdat = 'ExecStart'
Python_exc_path = "/usr/bin/python3 "
Execute_path = "/home/"+user+"/RoboreactorGenFlow/RoboreactorGenFlow.py"
config = configparser.ConfigParser() 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
settings = ['Unit','Service','Install']
#Unit
config.add_section(settings[0]) # Getting the section added into the list topic 
config.set(settings[0],str('Description'),str(project_name)) 
config.set(settings[0],str('After'),str(mode))
#Service 
config.add_section(settings[1])
config.set(settings[1],str('type'),str(type))
config.set(settings[1],str(execdat),str(Python_exc_path+Execute_path))
#Install 
config.add_section(settings[2])
config.set(settings[2],str(wanted),str(mode))
configfile = open(Generate_path+"RoboreactorGenFlow.service",'w')
config.write(configfile)
#Enable and start service 
os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl enable RoboreactorGenFlow.service")
os.system("sudo systemctl start RoboreactorGenFlow.service")
os.system("sudo systemctl status RoboreacgorGenFlow.service")



