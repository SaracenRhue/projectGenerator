from os import system as cmd

path = '/Users/richardkammermeier/Nextcloud/Programming/'

cmd('echo "\x1b[31m"') # Red
cmd('clear')

print("  __              __                ")
print(" /__)_   '_ __/  / _ _   _ _ __/  _ ")
print("/   / ()/(-( /  (__)(-/)(-/ (//()/  ")
print("      _/                            ")
cmd('echo "\x1b[39m"')

print('What is the name of the project?')
pro_name = str(input('> '))

#project types
projects = {\
    'static site':['Webdevelopment/', 'git clone https://github.com/SaracenRhue/HTML-boilerplate.git '+pro_name],\
    'nodejs':['Webdevelopment/','mkdir '+pro_name+' && cd '+pro_name+' && touch app.js && npm init -y'],\
    'react':['Webdevelopment/React/','npx create-react-app '+pro_name],\
    'electron':['electron/','npx create-electron-app@latest '+pro_name],\
    'docker':['docker/','cmd'],\
    'python':['Python/','mkdir '+pro_name+' && cd '+pro_name+' touch main.py'],\
    'bash':['bash/','mkdir '+pro_name+' && cd '+pro_name+' touch script.sh && echo "#!/bin/bash" >> script.sh'],\
    'cpp':['cpp/', 'git clone https://github.com/SaracenRhue/cpp-boilerplate.git '+pro_name]\
        }

keys = list(projects.keys()) #array of dict keys

for item in keys:
    print(str(keys.index(item)) + ') ' + item)


print('What kind of project do you want to create?')
pro_type = int(input('> '))
pro_type = keys[pro_type]
pro_type = projects.get(pro_type) 


path = path + pro_type[0]
create_cmd = pro_type[1]

cmd('echo "\x1b[35m"') # Magenta
cmd('cd '+path+' && '+create_cmd)

if 'github' in create_cmd:
    cmd('rm -rf '+path+pro_name+'/LICENSE') #remove license file

cmd('code ' +path+pro_name) #open in VS Code

cmd('echo "\x1b[32m"') # Green
print("  __  __      ___ ")
print(" /  )/  )/| )(_   ")
print("/(_/(__// |/ /__  ")
cmd('echo "\x1b[39m"') # default color
