ssh jenkins@projectmanager << EOF
rm -r DevOps-Practical
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins

cd DevOps-Practical

python3 -m pytest --cov service-one/application --cov-report term-missing
EOF