#!/usr/bin/python3.5

import os

# Install Ansible
os.system('sudo apt-get install ansible -y')
os.system('cp ./config/.ansible.cfg ~/.ansible.cfg')
os.system('ansible-playbook -i ./Ansible/Inventories/local.yml ./Ansible/Playbooks/full_setup.yml')
