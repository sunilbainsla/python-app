pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'python -m py_compile D:/GitLloyds/Python/python-app/*.py'
            }
        }
		 stage('Test') {
		 steps {
                echo 'Testing....'
				sh 'echo myCustomEnvVar=$myCustomEnvVar'
            }

			
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}