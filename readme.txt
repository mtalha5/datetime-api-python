command to build image
docker build -t datetime-api-python .

command to run container

docker run -p 5000:5000 datetime-api-python
docker run -d --name python-datetime-app -p 5000:5000 datetime-api-python


endpoint of app

http://localhost:5000/datetime