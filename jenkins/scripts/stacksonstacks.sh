# Removes the Project directory if exests
# Clones project directory & switches to Branch Jenkins
# Navigates to Project Directory
# Creates Fantasygens volume for the database
# removes current stack if already up
# sleeps for 10 seconds just so the network is fully removed
# fully launches the stack
ssh projectmanager << EOF
rm -r DevOps-Practical
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins

cd DevOps-Practical

sudo docker volume create fantasygens
docker stack rm namegenstack
sleep 10
sudo env SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Le0535892@35.242.172.253/fantasygendb' MYSQL_DATABASE=mysql+pymysql://root:Le0535892@35.242.172.253/fantasygendb MYSQL_ROOT_PASSWORD=Le0535892 SECRET_KEY=ALSkasdASdkabsdlAqwecv docker stack deploy --compose-file docker-compose.yaml namegenstack
EOF