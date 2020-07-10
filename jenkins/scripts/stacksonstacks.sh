sudo su - jenkins << EOF
rm -r mydir
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins

cd DevOps-Practical

sudo docker volume create fantasygens

sudo env password=${password} DATABASE_URI=${DATABASE_URI} docker stack deploy --compose-file docker-compose.yaml namegenstack
EOF