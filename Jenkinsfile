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
                    def branchOutput = bat(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    def BRANCH_NAME = branchOutput.readLines().last().trim()
                    echo "Running on branch: ${BRANCH_NAME}"

                    // Set a global variable for use in other stages
                    env.ACTUAL_BRANCH = BRANCH_NAME
                }
            }
        }

        stage('Build') {
            when {
                expression { return env.ACTUAL_BRANCH == 'main' }
            }
            steps {
                script {
                    echo "Packaging main branch version ${VERSION}"
                    bat """
                        powershell -Command "Compress-Archive -Path * -DestinationPath build\\myapp-${VERSION}.zip -Force"
                    """
                }
            }
        }

        stage('Test') {
            when {
                expression { return env.ACTUAL_BRANCH.startsWith('feature/') }
            }
            steps {
                echo "Running test stage for feature branch: ${env.ACTUAL_BRANCH}"
                // Optional: run test commands
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
