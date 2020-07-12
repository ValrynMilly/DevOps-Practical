ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
echo $TEST_DB_URI
python3 -m pytest --cov service-one/application --cov-report term-missing
EOF