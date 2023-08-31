pipeline {
    agent any
    stages {
        stage('Hello world'){
             steps{
                 echo 'Hello Mark'
            }
        }
        stage('Run backend') {
            steps {
                bat 'start/min python3 rest_app.py &'
            }
        }
        stage('Run frontend') {
            steps {
                bat 'start/min python3 web_rest.py &'
            }
        }
        stage('Run backend tests') {
            steps {
                bat 'python3 backend_test.py &'
            }
        }
        stage('Run frontend tests') {
            steps {
                bat 'python3 frontend_test.py &'
            }
        }
        stage('Run combined tests') {
            steps {
                bat 'python3 combined_testing.py &'
            }
        }
        stage('Clean environment') {
            steps {
                bat 'python3 clean_environment.py'
            }
        }
    }

}

