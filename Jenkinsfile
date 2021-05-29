pipeline {
    agent any

    stages {
        stage('prebuild') {
            steps {
                sh 'chmod +x scripts/prebuild.sh'
                sh 'scripts/prebuild.sh'
            }
        }
        stage('build') {
            steps {
                sh 'chmod +x scripts/build.sh'
                sh 'scripts/build.sh'
                sh 'python3 scripts/pybuild.py'
            }
        }
        stage('test') {
            steps {
                sh 'chmod +x scripts/test.sh'
                sh 'scripts/test.sh'
            }
        }
        stage('tablecreate') {
            steps {
               sh 'python3 scripts/tablecreate.py'
            }
        }   
    }
}    

