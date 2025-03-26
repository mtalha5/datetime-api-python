command to build image
docker build -t datetime-api-python .

command to run container

docker run -p 5000:5000 datetime-api-python
docker run -d --name python-datetime-app -p 5000:5000 datetime-api-python


endpoint of app

http://localhost:5000/datetime

HOW i will deploy this to cloud (AWS)

First, I’ll package the application as a Docker image. Once that’s ready, I’ll set up a container registry on AWS ECR and authenticate to it. Then, I’ll push the Docker image to the registry so ECS can access it.
Next, I’ll set up an ECS cluster. Depending on the requirements, I can either use EC2 instances or go with the serverless Fargate option. After that, I’ll assign the necessary IAM role to the cluster so it can pull the image from ECR.
Once the cluster is ready, I’ll create a Task Definition. This is where I’ll define container details like the image, ports, and startup command. I’ll also assign an IAM execution role to ensure the task has the right permissions.
Then, I’ll set up an ECS Service, which will manage and maintain the desired number of application instances. I’ll configure the network settings to make sure the service is accessible, and finally, I’ll find the public address or IP to access the running application.
