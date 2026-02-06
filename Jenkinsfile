pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
                sh 'docker-compose up -d --quiet-pull'
                sh 'docker ps'
            }
        }
        stage('Testing') {
            steps{
                sh 'pytest'
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
            echo "Pipeline failed"
        }
        unstable {
            echo "Pipeline is unstable"
        }
    }
}