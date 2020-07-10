ssh -t jenkins@jenkinsvm<< EOF
git clone https://github.com/ValrynMilly/DevOps-Practical.git
cd /home/jenkins/DevOps-Practical
git checkout Jenkins
sudo docker volume create fantasygens
sudo env password=${password} DATABASE_URI=${DATABASE_URI} docker stack deploy --compose-file docker-compose.yaml namegenstack
EOF