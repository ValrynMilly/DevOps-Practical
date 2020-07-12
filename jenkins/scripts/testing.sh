ssh projectmanager << EOF
rm -r DevOps-Practical
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins

cd DevOps-Practical

sudo env TEST_DB_URI=${TEST_DB_URI}
sudo env SQLALCHEMY_DATABASE_URI=${TEST_DB_URI}
python3 -m pytest --cov application --cov-report term-missing
EOF