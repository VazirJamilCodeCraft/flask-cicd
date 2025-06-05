pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/VazirJamilCodeCraft/flask-cicd.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest test_app.py
                '''
            }
        }

        stage('Deploy App') {
            steps {
                sh '''
                pkill -f app.py || true
                nohup venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
