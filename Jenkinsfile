pipeline {
    agent any
    triggers {
        pollSCM('*/30 * * * *')
    }
    logRotator {
        daysToKeep(5)
        numToKeep(20)
    }
    stages {
        stage('Checkout code') {
            steps {
                git url: 'https://github.com/toby4all/first_project_python.git', branch: 'Main'
            }
        }
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

