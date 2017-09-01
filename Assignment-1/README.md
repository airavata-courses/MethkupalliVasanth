# MethkupalliVasanth
 
Under Construction! Error with Python flask accessing the DB, in the process of fixing it.

## Technologies Used:

JavaScript (Node.js)
JAVA (Spark Java)
PYTHON (Flask)

## Requirements:

1. Install MongoDB, start the daemon mongod, which is essential for the microservices accessing the mongodb. Download the csv files from https://github.com/airavata-courses/MethkupalliVasanth/tree/master/Assignment-1/data-mongo. 
   Create a database named bookstore in MongoDB and run the following commands to import the collections
   > $ mongoimport -d bookstore -c  --type csv --file book.csv --headerline
   
   
   > $ mongoimport -d bookstore -c  --type csv --file genre.csv --headerline
 
2. Install Node.js
3. Install Python 2.7.x and the latest Flask version.
4. Install maven for running SparkJava Microservice.

## Testing the Architecture and the individual microservices:

1. Clone the Repository 

### Running the node.js Orchestrator service
1. Go to the node-js-orchestrator folder and run the following command
> node server.js

You can test it at http://localhost:20000/

2. Before you access the microservices from the UI, start the individual microservices first.

### Running the node.js microservice
1. Go to node-js-service folder and run the following command

> node app.js

You can test it by accessing the service from the orchestrator above.
Also, you can check this http://localhost:3000/api/books

Which shows us the database of books from the MongoDB

### Running the Spark Java microservice.

1. Go to the java spark folder in the repository and run the following maven commands
> mvn clean install package

> cd target

> java -jar demo-0.0.1-SNAPSHOT.jar

You can check the functioning of the the microservice from the orchestrator. Or use the link below
http://localhost:4567/hello/vasanth

### Running the Python Flask microservice
1. Go to the python-microservice folder and run the following commands

> python app.py

Check the functioning of the microservice from the orchestrator or use the link 
