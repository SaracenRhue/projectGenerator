#!/bin/bash

cd
wget https://raw.githubusercontent.com/SaracenRhue/projectGenerator/main/.generator.py
echo "alias pg='python3 .generator'" >> ~/.bashrc
echo "alias pg='python3 .generator'" >> ~/.zshrc

echo "please set the 'path' variable to your project folder in the .generator.py file"

sleep 3

nano .generator.py