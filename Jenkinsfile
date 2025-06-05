pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/VazirJamilCodeCraft/flask-cicd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                pkill -f app.py || true
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
