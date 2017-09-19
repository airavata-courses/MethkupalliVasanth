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
      }
    }
  }
}