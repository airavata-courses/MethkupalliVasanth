sudo docker run -d --hostname rabbitmq-host --name some-rabbit --net="host" -p 5672 -p 15672 rabbitmq:3-management

sudo docker build -t msorch .

sudo docker run -it -p 20000 --net="host" --name app_node_orch  msorch
