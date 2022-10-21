import os 
import getpass  
import configparser
user = getpass.getuser() 
path = "/home/"+user+"/RoboreactorGenFlow"
runpath = "/home/"+user+"/RoboreactorGenFlow/RoboreactorGenFlow_env/bin/gunicorn wsgi:app -b 0.0.0.0:8000"
supervisorpath = "/etc/supervisor/conf.d/"
topic = "program:RoboreactorGenFlow"
os.system("sudo chmod -R 777 "+supervisorpath)
os.system("sudo chmod -R 777 /var/log/")
config = configparser.ConfigParser() 
config.add_section(topic)
config.set(topic,str('directory'),str(path))
config.set(topic,str('command'),str(runpath))
config.set(topic,str('autostart'),str('true'))
config.set(topic,str('autorestart'),str('true'))
config.set(topic,str('stderr_logfile'),str('/var/log/RoboreactorGenFlow/RoboreactorGenFlow.err.log'))
config.set(topic,str('stdout_logfile'),str('/var/log/RoboreactorGenFlow/RoboreactorGenFlow.out.log'))
configfile = open(supervisorpath+"RoboreactorGenFlow.conf",'w')
config.write(configfile)
try:
   os.mkdir("/var/log/RoboreactorGenFlow",mode=0o777)
except:
     print("File is already exist")
os.system("sudo supervisorctl reread") 
os.system("sudo service supervisor restart") 
