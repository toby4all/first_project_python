pipeline {
    agent any
     options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
        stage('Run backend') {
            steps {
                bat 'python rest_app.py'
            }
        }
        stage('Run frontend') {
            steps {
                bat 'python web_rest.py'
            }
        }
        stage('Run backend tests') {
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage('Run frontend tests') {
            steps {
                bat 'python frontend_testing.py'
            }
        }
        stage('Run combined tests') {
            steps {
                bat 'python combined_testing.py'
            }
        }
        stage('Clean environment') {
            steps {
                bat 'python clean_environment.py'
            }
        }
    }

}

