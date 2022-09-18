#!/bin/bash

clear
    cat<<EOF
    First install or update?:
     (0) install
     (1) update
EOF
    read -n1 -s
    case "$REPLY" in
        "0")cd
            pip3 install pyyaml
            mkdir .projectGenerator
            cd .projectGenerator
            wget https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/generator/main.py
            wget https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/generator/config.yml
            cd
            echo "alias pg='python3 .projectGenerator/main.py'" >> ~/.bashrc
            echo "alias pg='python3 .projectGenerator/main.py'" >> ~/.zshrc
            echo "please set the 'main_path' variable to your project folder in the config file"
            sleep 3
            nano .projectGenerator/config.yml
            source ~/.zshrc
            source ~/.bashrc
            ;;
        "1")cd .projectGenerator
            rm -rf *
            wget https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/generator/main.py
            wget https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/generator/config.yml
            ;;
     * )  echo "invalid option" ;;
    esac
    sleep 1
    
echo " "
echo "  __  __      ___ "
echo " /  )/  )/| )(_   "
echo "/(_/(__// |/ /__  "


