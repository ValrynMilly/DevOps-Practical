ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
echo $TEST_DB_URI
cd service-one
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest service-one --cov-report term-missing
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest service-two/tests --cov-report term-missing
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest service-three/tests --cov-report term-missing
pytest ./service-four/tests/test_story.py --cov-report term-missing
EOF