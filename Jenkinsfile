pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t simple-flask-app:1.0.0 .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -p 3000:3000 simple-flask-app'
                sh 'curl -I localhost:3000'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed'
        }
        success {
            echo 'app run successfully'
        }
        failure {
            echo 'app run failed!'
        }
    }
}