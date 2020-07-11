sudo apt update -y
sudo apt install python3-pip python3-venv -y

pip3 install flask flask-testing pytest pytest-cov requests
python3 -m pytest ./service-one/tests/test_unit.py