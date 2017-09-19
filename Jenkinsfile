pipeline {
  agent {
    node {
      label 'jenkins'
    }
    
  }
  stages {
    stage('steps') {
      steps {
        git(url: 'https://github.com/airavata-courses/MethkupalliVasanth', branch: 'Assignment-2')
        sh '''cd Assignment-2 ; cd node-js-orchestrator ;   
sudo apt-get update;  sudo apt-get install apt-transport-https ca-certificates curl software-properties-common;  $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -; sudo apt-get update; sudo apt-get install docker-ce

;



sudo bash run.sh'''
      }
    }
  }
}