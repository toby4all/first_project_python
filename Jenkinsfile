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
                sh 'nohup python rest_app.py &'
            }
        }
        stage('Run frontend') {
            steps {
                sh 'nohup python web_rest.py &'
            }
        }
        stage('Run backend tests') {
            steps {
                sh 'python3 backend_test.py &'
            }
        }
        stage('Run frontend tests') {
            steps {
                sh 'python3 frontend_test.py &'
            }
        }
        stage('Run combined tests') {
            steps {
                sh 'python combined_testing.py &'
            }
        }
        stage('Clean environment') {
            steps {
                sh 'python clean_environment.py'
            }
        }
    }

}

