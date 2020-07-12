ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
echo $TEST_DB_URI
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-one/application --cov-report term-missing
cd
cd service-two/tests
pytest test_story.py --cov
EOF