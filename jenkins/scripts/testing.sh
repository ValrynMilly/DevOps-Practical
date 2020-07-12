ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
echo $TEST_DB_URI
cd service-one
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-one --cov-report term-missing
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-two/tests --cov-report term-missing
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-three/tests --cov-report term-missing
EOF