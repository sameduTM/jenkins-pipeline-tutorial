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
                sh 'sleep 3'
                sh 'docker exec backend-flask-instance sh -c "curl localhost:5500"'
            }
        }
        stage('Deploy') {
            steps{
                echo 'Deploying...'
            }
        }
    }
    post {
        always {
            echo "This always runs"
            sh 'docker rm -f backend-flask-instance'
        }
        success {
            echo "Pipeline runs successfully"
        }
        failure {
            echo "Pipeline failed"
        }
        unstable {
            echo "Pipeline is unstable"
        }
    }
}