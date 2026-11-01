pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "varshithaa777/techpulse-news"
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"
    }
    stages {
        stage('Checkout Code') { steps { checkout scm } }
        
        stage('Build Docker Image') {
            steps { 
                script { 
                    dockerImage = docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}") 
                } 
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push("${BUILD_NUMBER}")
                        dockerImage.push("latest")
                    }
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                // Using 'bat' instead of 'sh' because Jenkins is running on Windows
                bat "kubectl set image deployment/techpulse-deployment techpulse=${DOCKER_IMAGE}:${BUILD_NUMBER}"
                bat "kubectl rollout status deployment/techpulse-deployment"
            }
        }
    }
}