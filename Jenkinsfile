pipeline {
    agent any

    environment {
        VERSION = "1.0.${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Detect Branch') {
            steps {
                script {
                    BRANCH_NAME = bat(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    echo "Running on branch: ${BRANCH_NAME}"
                }
            }
        }

        stage('Build') {
            when {
                expression { return BRANCH_NAME == "main" }
            }
            steps {
                script {
                    def outputName = "myapp-${VERSION}.zip"
                    echo "Packaging main branch version ${VERSION}"
                    bat """
                        powershell -Command "Compress-Archive -Path * -DestinationPath build\\\\${outputName} -Force"
                    """
                }
            }
        }

        stage('Test') {
            when {
                expression { return BRANCH_NAME.startsWith("feature/") }
            }
            steps {
                echo "Running test stage for ${BRANCH_NAME}"
                // Add any test commands here
            }
        }

        stage('Archive') {
            when {
                expression { fileExists("build") }
            }
            steps {
                archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
            }
        }
    }
}
