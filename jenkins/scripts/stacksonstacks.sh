# Removes the Project directory if exests
# Clones project directory & switches to Branch Jenkins
# Navigates to Project Directory
# Creates Fantasygens volume for the database
# removes current stack if already up
# sleeps for 10 seconds just so the network is fully removed
# fully launches the stack
ssh jenkins@projectmanager << EOF
sudo rm -rf DevOps-Practical
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins

cd DevOps-Practical

sudo docker volume create fantasygens
docker stack rm namegenstack
sleep 10
sudo env SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI} MYSQL_DATABASE=${MYSQL_DATABASE} MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} SECRET_KEY=${SECRET_KEY} docker stack deploy --compose-file docker-compose.yaml namegenstack
EOF