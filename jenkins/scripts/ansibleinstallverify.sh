# Making sure ~/.local/bin Exists
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> .bashrc
source .bashrc
#installing prerequisites to install ansible
## python 3 & pip is needed to to install ansible
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3-pip -y
# Simply installing ansible on current user
pip3 install --user ansible
# Removing local project directory
rm -r DevOps-Practical
#clone project
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins
#navigate to ansible playboook location
cd DevOps-Practical/ansible
#Running inventory & playbook
ansible-playbook -i ansible/inventory ansible/playbook.yaml