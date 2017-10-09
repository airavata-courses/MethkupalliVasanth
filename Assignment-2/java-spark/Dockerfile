FROM openjdk:8
ADD target/demo-0.0.1-SNAPSHOT.jar demo-0.0.1-SNAPSHOT.jar
EXPOSE 4567
ENTRYPONT["mvn", "clean", "install", "package"]
ENTRYPOINT ["java","-jar","demo-0.0.1-SNAPSHOT.jar",">logs_java.txt"]
