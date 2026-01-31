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
    post {
        always {
            echo 'One way or another, I have finished'
        }
        success {
            mail(to: 'wekesa884@gmail', subject: 'Success: ${currentBuild.fullDisplayName}', body: "Everything went swell!")
        }
    }
}