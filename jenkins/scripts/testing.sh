ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
export TEST_DB_URI='mysql+pymysql://root:Le0535892@35.242.172.253/testfantasygendb'
echo $TEST_DB_URI
python3 -m pytest --cov service-one/application --cov-report term-missing
EOF