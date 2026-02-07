pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
                sh 'docker-compose build -q'
            }
        }
        stage('Testing') {
            steps{
                sh 'docker-compose up -d'
                sh 'docker exec jenkins-pipeline-web pytest -vvv'
                sh 'docker-compose down'
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