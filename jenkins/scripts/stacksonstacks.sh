sudo su - jenkins << EOF

git clone https://github.com/ValrynMilly/DevOps-Practical.git
git checkout Jenkins

cd /home/jenkins/DevOps-Practical

sudo docker volume create fantasygens

sudo env password=${password} DATABASE_URI=${DATABASE_URI} docker stack deploy --compose-file docker-compose.yaml namegenstack
EOF