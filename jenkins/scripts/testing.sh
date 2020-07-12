sudo apt update -y
sudo apt install python3-pip python3-venv -y

pip3 install flask flask-testing pytest pytest-cov requests
pip3 install requests_mock
env SECRET_KEY=${SECRET_KEY}
env SQLALCHEMY_DATABASE_URI=${TEST_DB_URI}
python3 -m pytest ./service-one/tests/test_unit.py