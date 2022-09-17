#!/bin/bash

 #clear
    cat<<EOF
    First install or update?:
     (0) install
     (1) update
EOF
    read -n1 -s
    case "$REPLY" in
        "0")cd
            mkdir .projectGenerator
            cd .prjectGenerator
            wget https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/generator/main.py
            cd
            echo "alias pg='python3 .projectGenerator/main.py'" >> ~/.bashrc
            echo "alias pg='python3 .projectGenerator/main.py'" >> ~/.zshrc
            echo "please set the 'path' variable to your project folder in the main.py file"
            sleep 3
            nano .projectGenerator/main.py
            ;;
        "1")cd .prjectGenerator
            wget https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/generator/main.py
            ;;
     * )  echo "invalid option" ;;
    esac
    sleep 1


