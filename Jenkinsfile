pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/VazirJamilCodeCraft/python-cicd-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest test_main.py
                '''
            }
        }

        stage('Run Script') {
            steps {
                input message: "Enter name for greeting", parameters: [string(name: 'USERNAME', defaultValue: 'Jammie', description: 'Enter your name')]
                sh '''
                . venv/bin/activate
                echo "$USERNAME" | python3 main.py
                '''
            }
        }
    }
}
