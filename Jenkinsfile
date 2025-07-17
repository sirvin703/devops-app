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
                	def BRANCH_NAME = env.GIT_BRANCH?.replace('origin/', '') ?: 'unknown'
            		echo "Running on branch: ${BRANCH_NAME}"
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
                        if not exist build mkdir build
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
