#!/bin/bash

sudo docker build -t msp .

sudo docker run -it -p 5000 --net="host" --name app_python  msp
