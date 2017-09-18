pipeline {
  agent {
    node {
      label 'jenkins'
    }
    
  }
  stages {
    stage('error') {
      steps {
        git(url: 'https://github.com/airavata-courses/MethkupalliVasanth', branch: 'Assignment-2')
        sh '''cd Assignment-2/node-js-orchestrator/

| ./run.sh'''
      }
    }
  }
}