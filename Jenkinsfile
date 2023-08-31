pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    triggers {
        pollSCM('H/30 * * * *')
    }
    stages {
        stage('Checkout') {
            steps {
               git([url: 'https://github.com/toby4all/first_project_python.git', branch: 'main'])
            }
        }
        stage{
            steps{
               bat 'pip install --user -r requirements.txt'
            }
        }
        stage('Run Backend Server') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start/min python rest_app.py'
                    } else {
                        sh 'nohup python rest_app.py &'
                    }
                }
            }
        }
        stage('Run Frontend Server') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start/min python web_rest.py'
                    } else {
                        sh 'nohup python web_rest.py &'
                    }
                }
            }
        }
        stage('Run Backend Test') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start/min python backend_test.py'
                    } else {
                        sh 'nohup python backend_test.py &'
                    }
                }
            }
        }
        stage('Run Frontend Test') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start/min python frontend_test.py'
                    } else {
                        sh 'nohup python frontend_test.py &'
                    }
                }
            }
        }
        stage('Run Combined Test') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start/min python combine_testing.py'
                    } else {
                        sh 'nohup python combine_testing.py &'
                    }
                }
            }
        }
        stage('Clear Environment') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start/min python clean_environment.py'
                    } else {
                        sh 'nohup python clean_environment.py &'
                    }
                }
            }
        }
    }
}

def checkOs() {
    if (isUnix()) {
        def uname = sh(script: 'uname', returnStdout: true)
        if (uname.startsWith("Darwin")) {
            return "Macos"
        } else {
            return "Linux"
        }
    } else {
        return "Windows"
    }
}



