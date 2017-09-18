pipeline {
  agent {
    node {
      label 'jenkins'
    }
    
  }
  stages {
    stage('') {
      steps {
        sh '''cd Assignment-2/node-js-orchestrator/

| ./run.sh'''
        git(url: 'https://github.com/airavata-courses/MethkupalliVasanth', branch: 'Assignment-2')
      }
    }
  }
}