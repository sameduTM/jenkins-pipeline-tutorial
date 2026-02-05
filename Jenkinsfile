pipeline {
    agent any
    stages {
        stage('Build-Deploy') {
            steps{
                sh 'docker-compose up -d'
                sh 'docker ps'
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