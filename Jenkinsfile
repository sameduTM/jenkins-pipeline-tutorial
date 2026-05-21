pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
                sh 'docker build -t backend-flask .'
            }
        }
        stage('Testing') {
            steps{
                sh 'docker run -d --name backend-flask-instance -p 5500:5500 backend-flask'
                sh 'ls -al'
                sh 'curl -sI localhost:5500'
                echo 'Test passed successfully'
            }
        }
        stage('Deploy') {
            steps{
                sh 'docker push'
                echo 'Deploying...'
            }
        }
    }
    post {
        always {
            echo "This always runs"
        }
        success {
            echo "Pipeline runs successfully"
        }
        failure {
            sh 'docker-compose down'
            echo "Pipeline failed"
        }
        unstable {
            echo "Pipeline is unstable"
        }
    }
}