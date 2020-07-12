ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
echo $TEST_DB_URI
cd service-one
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov application --cov-report term-missing
cd ..
cd service-two
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov tests --cov-report term-missing
cd
cd service-three
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov tests --cov-report term-missing
EOF