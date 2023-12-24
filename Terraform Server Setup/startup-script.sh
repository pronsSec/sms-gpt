#!/bin/bash
sudo apt update
sudo apt install -y python3 python3-pip git

# Clone your application repository
git clone https://github.com/pronsSec/sms-gpt
cd sms-gpt

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Run your application
python3 app.py
