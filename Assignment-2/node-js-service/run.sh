#!/bin/bash

sudo docker build -t msn .

sudo docker run -it -p 3000 --net="host" --name app_node  msn
