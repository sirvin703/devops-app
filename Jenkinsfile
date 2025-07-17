pipeline {
    agent any

    stages {
        stage('Branch Check') {
            steps {
                script {
                    echo "Running on branch: ${env.BRANCH_NAME}"
                }
            }
        }

        stage('Build') {
            when {
                branch 'main'
            }
            steps {
                echo 'Running main branch build stage'
                // Add production-level steps here
            }
        }

        stage('Test') {
            when {
                branch pattern: "feature/.*", comparator: "REGEXP"
            }
            steps {
                echo 'Running feature branch test stage'
                // Add dev/test steps here
            }
        }

	stage('Build and Package') {
    		steps {
        		script {
            			def version = "1.0.${env.BUILD_NUMBER}"
            			def outputName = "myapp-${version}.zip"

            			echo "Packaging app version ${version}"
           			 bat """
                			powershell -Command "Compress-Archive -Path * -DestinationPath build/${outputName} -Force"
           			 """
       			}
        		archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
    		}
	}

    }
}
