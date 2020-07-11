sudo apt update -y
sudo apt install python3-pip python3-venv -y

pip3 install flask flask-testing pytest pytest-cov requests
pip3 install requests_mock
python3 -m pytest ./service-one/tests/test_unit.py