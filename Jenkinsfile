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
                withEnv(["PATH+C:/Users/Toby/AppData/Local/Programs/Python/Python311"]) {
                    bat 'python rest_app.py'
                }
            }
        }
        stage('Run frontend') {
            steps {
                withEnv(["PATH+C:/Users/Toby/AppData/Local/Programs/Python/Python311"]) {
                    bat 'python web_rest.py'
                }
            }
        }
        stage('Run backend tests') {
            steps {
                withEnv(["PATH+C:/Users/Toby/AppData/Local/Programs/Python/Python311"]) {
                    bat 'python3 backend_test.py'
                }
            }
        }
        stage('Run frontend tests') {
            steps {
                withEnv(["PATH+C:/Users/Toby/AppData/Local/Programs/Python/Python311"]) {
                    bat 'python3 frontend_test.py'
                }
            }
        }
        stage('Run combined tests') {
            steps {
                withEnv(["PATH+C:/Users/Toby/AppData/Local/Programs/Python/Python311"]) {
                    bat 'python combined_testing.py'
                }
            }
        }
        stage('Clean environment') {
            steps {
                withEnv(["PATH+C:/Users/Toby/AppData/Local/Programs/Python/Python311"]) {
                    bat 'python clean_environment.py'
                }
            }
        }
    }
}
