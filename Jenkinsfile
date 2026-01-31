pipeline {
    agent any
    environment {
        USERNAME = 'Ken Wekesa'
        COUNTRY = 'Kenya'
    }
    stages {
        stage('Deploy') {
            steps {
                echo "Hello ${USERNAME}, welcome to ${COUNTRY}"
                sh 'printenv'
            }
        }
    }
}