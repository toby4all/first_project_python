pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        PATH = "${env.PATH}C:/Users/Toby/AppData/Local/Programs/Python/Python311"
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }
                git 'https://github.com/toby4all/first_project_python.git'
            }
        }
        stage('run rest app server') {
            steps {
                bat 'start/min python rest_app.py'
            }
        }
        stage('run web rest server') {
            steps {
                bat 'start/min python web_rest.py'
            }
        }
        stage('run backend testing') {
            steps {
                bat 'python backend_test.py'
            }
        }
        stage('run frontend testing') {
            steps {
                bat 'python frontend_test.py'
            }
        }
        stage('run fullstack testing') {
            steps {
                bat 'python combine_testing.py'
            }
        }
        stage('run clean environment') {
            steps {
                bat 'python clean_environment.py'
            }
        }
        stage('Hello Tobby') {
            steps {
                echo 'Hello Oluwatobi fabonmi'
            }
        }
    }
}
