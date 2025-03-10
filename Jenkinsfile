pipeline {
    agent any  // Виконується на будь-якому доступному агенті Jenkins

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YuL1K/lab1.git'  // Заміни на свій репозиторій
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'  // Встановлюємо залежності
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=report.xml'  // Запускаємо тести та створюємо звіт
            }
        }

        stage('Publish Test Report') {
            steps {
                junit 'report.xml'  // Додаємо звіт про тести в Jenkins
            }
        }
    }
}
