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
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg ; sudo apt-key add -

; sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"; sudo apt-get update ;  sudo apt-get install -y docker-ce;



sudo bash run.sh'''
      }
    }
  }
}