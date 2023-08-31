pipeline {
    agent any
    stages {
        stage('Hello world'){
             steps{
                 echo 'Hello Tobby'
            }
        }
        stage('Run backend') {
            steps {
                bat 'start/min python rest_app.py'
            }
        }
        stage('Run frontend') {
            steps {
                bat 'start/min python web_rest.py'
            }
        }
        stage('Run backend tests') {
            steps {
                bat 'python3 backend_test.py'
            }
        }
        stage('Run frontend tests') {
            steps {
                bat 'python3 frontend_test.py'
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

