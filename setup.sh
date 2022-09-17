#!/bin/bash

cd
mkdir .prjectGenerator
cd .prjectGenerator
wget https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/generator/main.py
cd
echo "alias pg='python3 .projectGenerator/main.py'" >> ~/.bashrc
echo "alias pg='python3 .projectGenerator/main.py'" >> ~/.zshrc

echo "please set the 'path' variable to your project folder in the main.py file"

sleep 3

nano .projectGenerator/main.py