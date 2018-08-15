pipeline {
    agent { any { image 'python:3.6.6' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
		 stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}