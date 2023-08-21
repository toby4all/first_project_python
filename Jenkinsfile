pipeline {
    agent any
options {
    buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '10'))
  }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
