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
                sh 'docker run -d -p 3000:3000 simple-flask-app:1.0.0'
                sh 'PID=$!'
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
            echo '$PID'
        }
        failure {
            echo 'app run failed!'
        }
    }
}