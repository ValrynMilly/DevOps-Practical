# DevOps-Practical Project App: Fantasy Bio Generator 

The purpose of this project is to create a simple flask web app utilizing multiple tools that involve concepts like Software Development with Python, Continuous Integration & Cloud Fundamentals. These tools Include:  

- Kanban Board: Trello
- Version Control: Git & Github Desktop
- CI Server: Jenkins
- Configuration Management: Ansible
- Cloud server: Google Cloud Provider (GCP)
- Containerisation: Docker
- Orchestration Tool: Docker Swarm
- Reverse Proxy: NGINX
- Testing: PyTest

The app itself will be a simple Username, Title and Story Generator where a user can generate a multitude of fantasy bios. While this project wont focus too much on the app itself its the back end, development & continuous integration methodology that will shine and be focused on. 

App: [Found Here](http://35.197.211.248/)

Trello: [Found Here](https://trello.com/b/2yVzbztM)

# Table of Contents
## Navigate across Content
- [Tutorial](#Tutorial)
- [Application](#Application)
- [Cloud-Server](#Cloud-Server)
- [Docker](#Docker)
	- [Swarm](##Swarm)
	- [NginX](##NginX)
- [CI-Pipeline](#Ci-Pipeline)
	- [Jenkins](##Jenkins)
		- [Github](###Github)
		- [Ansible](###Ansible)
		- [Testing](###Testing)
		- [Stack-Setup](###Stack-Setup)
- [Documentation](#Documentation)
	- [Trello](#Trello)
	- [Risk-Assessment](#Risk-Assessment)
- [Issues-Faced](#Issues-Faced)
- [Author](#Author)

# Tutorial

The app itself is quite simple simply click **submit** on the home page and a bio will automatically be generated like so. Hitting F5 after submit or just refreshing the page will simply generate a new bio.
![picture](https://i.imgur.com/jyGEIck.png?1)

![picture](https://i.imgur.com/AR6H8YR.png)

# Application
As you can see from the above tutorial it really is a simple app! But how does it work? Well the app itself is a collection of four services, service 1-4. Service one handles communication between all services by receiving & sending requests. It is also responsible for committing to the database itself.
```python
@app.route('/', methods = ['POST'])
def namegenform_post():
    form = namegen()
    if form.validate_on_submit():
        #Upon validation of form Name is requested
        name = requests.get(servicetwo)
        #Upon validation of form Title is requested
        title = requests.get(servicethree)
        #Upon validation of form result is requested
        result = requests.get(servicefour)
        #Declaring a new variable whos values are stored for database commit
        fresh_register = Registerfantasy(fan_name=name.text, fan_title=title.text, fan_story=result.text)
        #Adding the previous variable to the session ready for commit
        db.session.add(fresh_register)
        #commiting to database
        db.session.commit()
        #returning all as text
        return result.text
```
The Database Model. I should mention that this model applies to both public database and test database.
```python
#importing database that was declared
from application import db
#Below is the database variables, simple 4 colums
class Registerfantasy(db.Model):
    #ID column for identification of each commit
    id = db.Column(db.Integer, primary_key=True)
    #Name column from generated content
    fan_name = db.Column(db.String(30), nullable=False)
    #title column from generated content
    fan_title = db.Column(db.String(30), nullable=False)
    #story column from generated content
    fan_story = db.Column(db.String(250), nullable=False)
```

The second service is a function that generates a random fantasy name.
```python
@app.route('/', methods = ['GET', 'POST'])
def namegenform_post():
    #There are three 3 lists, orcnames (not in use at the moment), midname and elvnames
    orcnames = ['uk', 'guk', 'keg', 'rag', 'kha', 'rok', 'zok', 'huk', 'rik']
    #orc names will be their own route soon
    midname = ['Aafke', 'Aaliyah', 'Ada', 'Adilya', 'Brynne', 'Britt', 'Cynthia', 'Halle', 'Ilana', 'Iris', 'Aaron', 'Adam', 'Alexander', 'Anton', 'Meldarion', 'Elijah', 'Eithelonnen']
    elvnames = ['iros', 'ilir', 'tris', 'aren', 'ana', 'ina', 'enys', 'ona', 'dir']
    #username value is set by randomly choosing one from each list
    username = (random.choice(elvnames) + random.choice(midname) + random.choice(elvnames))
    #then returns that value
    return Response(username, mimetype='type/plain')
```

The third service is a function that generates a random fantasy title.
```python
@app.route('/', methods = ['GET', 'POST'])
def titlegen_post():
    #Here we see three lists articles, descriptive & adjectives. Full of a variety of relevant values 
    articles = ['The', 'A']
    descriptive = ['Powerful', 'Dominant', 'Almighty', 'Omnipotent', 'Omniscient', 'Omnibenevolent', 'Ruling', 'Formidable', 'Divine' ,'Hero']
    objective = ['One', 'Demi-God', 'Giant', 'Berzerker', 'Hunter', 'Wizard', 'Born', 'God']
    #Title generated randomly chooses one from all three and combines them to make a title. 
    title_generated = (random.choice(articles) + " " + random.choice(descriptive) + " " + random.choice(objective)) 
    #Then returns that title
    return Response(title_generated, mimetype='type/plain')
```

And finally the fourth generates a short story for the user.
```python
@app.route('/', methods = ['GET', 'POST'])
def titlegen_post():
    #Name is defined then makes a request to service two to give it a value
    name = requests.get(servicetwo)
    #title is defined then makes a request to service thee to give it a value
    title = requests.get(servicethree)
    where = ['In a bar','On a field', 'Through the clouds', 'Under a mountain', 'Underwater', 'In a town']
    action = ['killed', 'annihilated', 'destroyed', 'Poisoned', 'Petrified', 'Saved', 'Rescued', 'Healed', 'Silenced']
    instrument = ['a pinkie', 'a pencil', 'a hammer', 'a bow', 'lightning', 'fire', 'a hunt'] 
    #short story is a combination of lists randomly picked but within the story name and title are reference so the result makes sense
    shortstory = (random.choice(where) + " " + name.text + " " + title.text +" Once " + random.choice(action)+ " " + str(random.randint(1, 3000)) + " MEN WITH " + random.choice(instrument)) 
    #then returns a response with the short story
    return Response(shortstory.upper(), mimetype='text/plain')
```
### Service Flow
![picture](https://i.imgur.com/2vpkKmX.png)

# Cloud Server
![picture](https://i.imgur.com/BnsMLlN.png)

None of this would have been possible without Google Cloud Platform (GCP). Without it the app, docker, ci server none of it would run or be available. GCP is a cloud service provider and my use of it was utilization of virtual machines that could run each of the below services.

* Jenkins (CI Server)
* Swarm Manager VM (Docker Swarm)
* 2x Swarm Worker VM's (Docker Swarm)
* VM for Development
* SQL Server for my public and test databases

# Docker

The point of this project was not to test our capabilities of development but it was of testing and deployment. To showcase this we had each service within the app put into their each separate docker containers. Each service was identified with Port numbers in my case 1:5000, 2:5001, 3:5002 & 4:5003. Now having these services all containerised is called a **stack** but it is not enough, we need to be able to manage them into some sort of collective. Enter Swarm.

## Swarm

Swarm is a group of virtual machines, in my case I had a **Swarm Manager**  and two **Swarm Workers**. Now what a swarm does it manages the **stacks** you have made into one selective network controlled by a manager. What I find amazing about swarm is that the workers share workload & can provide for downtime reliability, should one worker go down the service doesn't, you still have another. See the diagram below. 
![picture](https://i.imgur.com/qPBozUb.png)

## NginX
NginX is a web server, it can be used in a variety of ways such as mail proxy, HTTP chaching & load balancing but in my project it was used as a reverse proxy in its own container. A reverse proxy is like the doorman to special events it forwards and redirects guests to where they need to be for example a user wants to visit https://www.google.co.uk/search their own reverse proxy would redirect me to https://www.google.co.uk/webhp.

# CI-Pipeline
![picture](https://i.imgur.com/ZYm825A.png)

This is the CI Pipeline its a continuous integration/continuous development implementation I had to follow throughout this project. There are many terms people used to describe each stage but mine was **Development**, **Operations** & **Deployment**. For a Kanban I used Trello to manage tasks, Github for Version Control & Visual Studio Code to develop the app itself.

## Jenkins
![picture](https://i.imgur.com/dz3cXbh.jpg)

Jenkins is a CI Server helpful for automating the whole DevOps process. For this project I had to setup a pipeline to automate pulling from Github (Checkout SCM), install and set up Ansible, Testing & finally Stack setup. Upon implementing the CI pipeline, automating everything & about 100 builds and 200 more git commits my Jenkins Pipeline looked like this.
![picture](https://i.imgur.com/oQa6PEH.png)

### Github 
To ensure the pipeline would work into the project my first priority was to connect the pipeline to my github repo, I had to identify branch and verify on both ends (Git & Jenkins) for connection, to do this I made minor Markdown changes to see if the pipeline would build, it was a success.

### Ansible
Ansible is a configuration management tool, like a maestro to the opera it makes sure everything is where it needs to be, in this case it is installing our prerequisites like docker for us. While ansible didn't need to be my second step I thought it would be logical to implement it into each machine to install docker before I would set up the swarm. I wrote the playbook, setup an inventory & roles then I wrote a script to install ansible and run the files to setup docker on the machines. When the script is ran docker should be installed on the machines.
```
# Making sure ~/.local/bin Exists
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> .bashrc
source .bashrc

#installing prerequisites to install ansible
## python 3 & pip is needed to to install ansible
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3-pip -y

# Simply installing ansible on current user
pip3 install --user ansible

# Verifying Ansible is installed will show on logs
ansible --version

#locate to root
cd /home/jenkins/

#Running inventory & playbook
ansible-playbook -i inventory playbook.yaml
```
### Testing
Testing was done with PyTest, particularly through mock testing. Mock testing allows us the ability to test functions without them being live or in use. Much like a mock exam "its not the real one" we did this because we needed to learn to test simulated functions. if we cant access a function mock testing allows us to make simulated functions we can work on. In my case I mock tested on each function. 
``` python
class TestGenerate(TestBase):
    #Feeding and testing homeview with 'submit'
    def test_homeview(self):
        response = self.client.get('/')
        self.assertIn(b"submit", response.data)
    #Feeding and testing a name is generated with 'ilir'
    def test_generatename(self):
        with patch('requests.get') as p:
            p.return_value.text = "ilir"
            response = self.client.post('/')
            self.assertIn(b'ilir', response.data)
    #Feeding and testing a title is generated with 'A OMNIPOTENT BORN'
    def test_generatetitle(self):
        with patch('requests.get') as x:
            x.return_value.text = "A OMNIPOTENT BORN"
            response = self.client.post('/')
            self.assertIn(b'A OMNIPOTENT BORN', response.data)
```

Once tests were made I built a script that Jenkinsfile could read, much like the ansible script; the tests could be ran after ansible was installed.
```
ssh jenkins@projectmanager << EOF
cd DevOps-Practical
git pull
echo $TEST_DB_URI
cd service-one
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-one
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-two/tests
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-three/tests
sudo env TEST_DB_URI=${TEST_DB_URI} python3 -m pytest --cov service-four/tests
EOF
```

I tried using the "--cov" coverage command but Jenkins did not like the way I was calling the test. While testing works and passes each test, displaying coverage was an issue.

### Stack Setup
```
ssh projectmanager << EOF
sudo rm -rf DevOps-Practical
git clone https://github.com/ValrynMilly/DevOps-Practical.git -b Jenkins

cd DevOps-Practical

sudo docker volume create fantasygens
docker stack rm namegenstack
sleep 10
sudo env SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI} MYSQL_DATABASE=${MYSQL_DATABASE} MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} SECRET_KEY=${SECRET_KEY} docker stack deploy --compose-file docker-compose.yaml namegenstack
EOF
```

Console log after script is ran.
![picture](https://i.imgur.com/i9QYMwQ.png)

# Documentation 

## Trello

**SPRINT 1**
![picture](https://i.imgur.com/Dvedqf2.jpg)

Ok so sprint one might not look like much but it was surprisingly ambitious the original idea was to generate a name based on your own & locally that function ran fine, but when getting those form values of your name through service requests takes up two days of valuable time it seemed that I had to scale down the app. This also denied me from including other features like name based on race, currently its just elven, but I had functionality for orcish. 

**SPRINT 2**
![picture](https://i.imgur.com/wp3NUR5.jpg)

This sprint was a downscale to make everything more viable during the development stage, custom input and choice was removed & labelled as a "wont have this time colour" everything that was being finalised was either in testing or in progress. 

**SPRINT 3**
![picture](https://i.imgur.com/sE4QIRh.jpg)

This Sprint was when development had finished and was in progress of deployment. I still had many many tasks to do but most of the either was in or depended on deployment, I believe the most important tasks were the building of scripts to automate everything.

**SPRINT 4**
![picture](https://i.imgur.com/kxz5UKa.jpg)
There was a boom of acceleration once I figured out the Jenkinsfile & scripts, by the fourth sprint everything had been finished and a long list of done appeared. 

## Risk Assessment
![picture](https://i.imgur.com/NqSdHWO.png)

# Issues Faced

**Mock testing** was probably the hardest problem I came across, overcoming it took a day and a half & the end results suffice but are not good enough, the issue is how do you test random? feeding data and getting what you've fed back is fine but when your testing services that rely on random generation it could prove difficult even if you are simulating it. Another issue with testing was getting coverage reports, when running the test the best report I received were either "passed" or "failed" no coverage numbers even if parameters like --cov-report are included.

# Author 

Emiljano Kurbiba
