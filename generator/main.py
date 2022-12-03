import yaml
from os import system
# import sys

# arguments = sys.argv #returns a list of arguments
# arguments.pop(0) #remove the first argument (the script name)
# remote = len(arguments)

system('echo "\x1b[31m"') # Red
system('clear')

print("  __              __                ")
print(" /__)_   '_ __/  / _ _   _ _ __/  _ ")
print("/   / ()/(-( /  (__)(-/)(-/ (//()/  ")
print("      _/                            ")
system('echo "\x1b[39m"')

print('What is the name of the project?')
pro_name = str(input('> '))

#get project types and path from yaml file

# if remote == 0:
with open('.projectGenerator/config.yml', 'r') as file:
    config = yaml.safe_load(file)
    projects = config['projects']
    main_path = config['main_path']
# elif remote == 1:
#     with open('https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/generator/config.yml', 'r') as file:
#         config = yaml.safe_load(file)
#         projects = config['projects']
#         main_path = arguments[0]


#project types
keys = list(projects.keys()) #array of dict keys

for item in keys:
    print(str(keys.index(item)) + ') ' + item)


print('What kind of project do you want to create?')
pro_type = int(input('> '))
pro_type = keys[pro_type]
pro_type = projects.get(pro_type) 


path = main_path + pro_type['path']
create_cmd = pro_type['cmd']
create_cmd = create_cmd.replace('pro_name', pro_name)

system('echo "\x1b[35m"') # Magenta
system('cd '+path+' && '+create_cmd)

if 'github' in create_cmd:
    system('rm -rf '+path+pro_name+'/LICENSE') #remove license file

system('code ' +path+pro_name) #open in VS Code

system('echo "\x1b[32m"') # Green
print("  __  __      ___ ")
print(" /  )/  )/| )(_   ")
print("/(_/(__// |/ /__  ")
system('echo "\x1b[39m"') # default color
