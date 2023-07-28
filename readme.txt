1- create a github repository and clone it
git clone https://github.com/sporhaberleri94/pythonNewVE.git

2- create a virtual environment
python -m venv fatihpython

3- activate the virtual environment
.\activate.bat 
choose command prompt not powershell

4-
pip list 
will show all the installed packages

5- create a .gitignore file and add the following lines
fatihpython

6- pip freeze > requirements.txt
if we need to install it 
pip install -r requirements.txt
7-pip install flask

8- for kubernetes environment start :
minikube start


minikube docker-env
set DOCKER_TLS_VERIFY=1
set DOCKER_HOST="http://docker:2375/v1.24/containers/json"



9-create a dockerfile
docker build -t fatihpython .
if necessary we can also delete the docker image    

create a container :
docker run -d -p 5000:5000 fatihpython

10--kubernetes commands 
minikube start
minikube status
kubectl config view
kubectl get nodes
minikube dashboard
minikube dashboard --url

