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
        sh 'cd Assignment-2 ; cd node-js-orchestrator ; sudo bash run.sh'
      }
    }
  }
}