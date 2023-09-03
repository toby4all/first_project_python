pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
        stage('Checkout') {
            steps {
               git([url: 'https://github.com/toby4all/first_project_python.git', branch: 'main'])
            }
        }
        stage('Set Python environment variable') {
            steps {
                script {
                    env.PYTHON_PATH = 'C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311'
                    echo "Python path set to: ${env.PYTHON_PATH}"
                }
            }
        }
        stage('Install python packages') {
             steps {
                bat "${env.PYTHON_PATH}\\python.exe -m pip install --target ${env.WORKSPACE} -r requirements.txt"
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
                        bat 'python backend_test.py'
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
                        bat 'python frontend_test.py'
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
                        bat 'python combine_testing.py'
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
                        bat 'python clean_environment.py'
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




