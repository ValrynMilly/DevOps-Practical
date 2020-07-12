ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
echo $TEST_DB_URI
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-one/application --cov-report term-missing
cd
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-two/tests/test_name.py --cov-report term-missing
cd
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-three/tests/test_title.py --cov-report term-missing
cd
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-four/tests/test_story.py --cov-report term-missing
EOF