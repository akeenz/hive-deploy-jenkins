pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'chmod +x scripts/build.sh'
                sh 'scripts/build.sh'
            }
        }
        stage('test') {
            steps {
                sh 'chmod +x scripts/test.sh'
                sh 'scripts/test.sh'
            }
        }
    }
}    

