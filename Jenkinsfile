pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'testing' }
            steps {
                echo 'Running build on testing agent!'
            }
        }
        stage('Deploy') {
            agent { label 'deployment' }
            steps {
                echo 'Deploying app!'
            }
        }
    }
}
