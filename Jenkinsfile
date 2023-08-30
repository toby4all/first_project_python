pipeline {
    agent any
     options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
         stage('checkout now') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/toby4all/first_project_python.git'
            }
        }
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

