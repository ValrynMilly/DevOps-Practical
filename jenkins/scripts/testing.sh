ssh jenkins@projectmanager << EOF
sudo rm -rf DevOps-Practical
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins
cd DevOps-Practical
git pull
echo $TEST_DB_URI
cd service-one
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest service-one --cov-report term-missing
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest service-two/tests --cov-report term-missing
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest service-three/tests --cov-report term-missing
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest service-four/tests --cov-report term-missing
EOF