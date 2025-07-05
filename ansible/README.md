# Part 2: Configuration Management

## Overview
Used Ansible to install Docker on the EC2 instance and ensure it starts on boot.

## Files
- hosts.ini: Inventory with EC2 IP and SSH key path
- setup-docker.yml: Ansible playbook to install and enable Docker

## Commands
ansible-playbook -i hosts.ini setup-docker.yml

## Validation
ssh -i ~/.ssh/collegeRegKey.pem ubuntu@18.201.42.31
docker --version
