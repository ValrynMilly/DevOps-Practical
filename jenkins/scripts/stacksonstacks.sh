ssh projectmanager << EOF
rm -r DevOps-Practical
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins

cd DevOps-Practical

sudo docker volume create fantasygens
docker stack rm namegenstack
sudo docker stack deploy -c docker-compose.yaml namegenstack env SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Le0535892@35.242.172.253/fantasygendb' MYSQL_DATABASE=mysql+pymysql://root:Le0535892@35.242.172.253/fantasygendb MYSQL_ROOT_PASSWORD=Le0535892
EOF