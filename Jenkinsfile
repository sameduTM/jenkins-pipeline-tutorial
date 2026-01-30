pipeline {
    agent any
    stages{
        stage('Test') {
            steps {
                sh 'echo "Fail!"; exit 1'
            }
        }
    }
    post {
        always {
            echo "Pipeline Completed"
        }
        success {
            echo "Pipeline ran successfully"
        }
        failure {
            echo "Pipeline failed"
        }
        changed {
            echo "Pipeline stage changed"
        }
        unstable {
            echo "The run was unstable"
        }
    }
}