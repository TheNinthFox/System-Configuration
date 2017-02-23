#!/usr/bin/python3.5

import os

# Install Ansible
os.system('sudo apt-get install ansible -y')

# Copy the ansible cfg to grant access to our custom roles
os.system('cp ./config/.ansible.cfg ~/.ansible.cfg')

# Execute the setup playbook on the local machine
os.system('ansible-playbook -i ./Ansible/Inventories/local.yml ./Ansible/Playbooks/full_setup.yml')
