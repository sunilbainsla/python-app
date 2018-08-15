pipeline {
    agent { any { image 'python:3.6.6' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m py_compile D:/GitLloyds/Python/python-app/*.py'
            }
        }
		 stage('Test') {
		 steps {
                echo 'Testing....'
            }

			
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}