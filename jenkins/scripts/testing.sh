ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
echo $TEST_DB_URI
cd service-one
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest ./service-one/tests/test_unit.py
EOF