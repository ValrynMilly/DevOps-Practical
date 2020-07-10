ssh projectmanager << EOF
rm -r DevOps-Practical
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins

cd DevOps-Practical

sudo docker volume create fantasygens
docker stack rm namegenstack
sudo env password=${password} DATABASE_URI=${DATABASE_URI} docker stack deploy --compose-file docker-compose.yaml namegenstack
EOF