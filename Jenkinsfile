pipeline {
    agent any
    environment {
    PATH = "${env.PATH}:/Users/Toby/AppData/Local/Programs/Python/Python311"
}

    stages {
        stage('Hello world'){
             steps{
                 echo 'Hello Oluwatobi'
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
                bat 'python backend_test.py'
            }
        }
        stage('Run frontend tests') {
            steps {
                bat 'python frontend_test.py'
            }
        }
        stage('Run combined tests') {
            steps {
                bat 'python combine_testing.py'
            }
        }
        stage('Clean environment') {
            steps {
                bat 'python clean_environment.py'
            }
        }
    }

}

