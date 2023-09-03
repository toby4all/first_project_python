pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
        stage('Code pull') {
            steps {
                git([url: 'https://github.com/toby4all/first_project_python.git', branch: 'main'])
            }
        }
        stage('Install python packages') {
             steps {
                bat 'pip install --user -r requirements.txt'
            }
        }
        stage('Run backend server') {
            steps {
                script {
                    bat 'start/min python rest_app.py'
                }
            }
        }
        stage('Run frontend server') {
            steps {
                script {
                    bat 'start/min python web_rest.py'
                }
            }
        }
        stage('Run backend testing') {
            steps {
                script {
                    bat 'python backend_test.py'
                }
            }
        }
        stage('Run frontend testing') {
            steps {
                script {
                    bat 'python frontend_test.py'
                }
            }
        }
        stage('Run combined testing') {
            steps {
                script {
                    bat 'python combine_testing.py'
                }
            }
        }
        stage('Run clean environment') {
            steps {
                script {
                    bat 'python clean_environment.py'
                }
            }
        }
    }
}




