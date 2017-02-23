#!/usr/bin/python3.5

import os

# Install Ansible
os.system('sudo apt-get install ansible -y')
os.system('ansible-playbook ./Ansible/Playbooks/full_setup.yml')
