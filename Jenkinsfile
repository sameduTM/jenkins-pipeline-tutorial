pipeline {
    agent any
    environment {
        USERNAME = 'Ken Wekesa'
        COUNTRY = 'Kenya'
    }
    stages {
        stage('Deploy - Staging') {
            steps {
                echo "Hello ${USERNAME}, welcome to ${COUNTRY}"
                sh 'printenv'
            }
        }
        stage('Deploy - Production') {
            input(message: 'Does the staging env look ok?')
        }
    }
    post {
        always {
            echo 'One way or another, I have finished'
        }
        success {
            mail(
                to: 'wanyamak884@icloud.com', 
                subject: 'Success: ${currentBuild.fullDisplayName}', 
                body: "Everything went swell!"
                )
        }
    }
}