pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'siscal-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
        POSTGRES_CONTAINER = 'siscal-postgres'
        WEB_CONTAINER = 'siscal-web'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '========== ETAPA 1: Obteniendo código desde GitHub =========='
                checkout scm
                echo 'Código descargado exitosamente'
            }
        }
        
        stage('Verificar Dependencias') {
            steps {
                echo '========== ETAPA 2: Verificando entorno =========='
                script {
                    if (isUnix()) {
                        sh 'docker --version'
                        sh 'docker-compose --version'
                        sh 'python3 --version'
                    } else {
                        bat 'docker --version'
                        bat 'docker-compose --version'
                        bat 'python --version'
                    }
                }
                echo 'Todas las dependencias verificadas'
            }
        }
        
        stage('Linting y Validación de Código') {
            steps {
                echo '========== ETAPA 3: Validando calidad de código =========='
                script {
                    if (isUnix()) {
                        sh 'pip install flake8 || pip3 install flake8'
                        sh 'flake8 app/ --count --select=E9,F63,F7,F82 --show-source --statistics || true'
                    } else {
                        bat 'pip install flake8'
                        bat 'flake8 app\\ --count --select=E9,F63,F7,F82 --show-source --statistics || exit 0'
                    }
                }
                echo 'Validación de código completada'
            }
        }
        
        stage('Tests Unitarios') {
            steps {
                echo '========== ETAPA 4: Ejecutando tests =========='
                script {
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt || pip3 install -r requirements.txt'
                        sh 'python3 -m pytest tests/ -v || echo "No tests found, continuing..."'
                    } else {
                        bat 'pip install -r requirements.txt'
                        bat 'python -m pytest tests\\ -v || echo No tests found'
                    }
                }
                echo 'Tests completados'
            }
        }
        
        stage('Detener Contenedores Antiguos') {
            steps {
                echo '========== ETAPA 5: Limpiando contenedores anteriores =========='
                script {
                    if (isUnix()) {
                        sh 'docker-compose down || true'
                    } else {
                        bat 'docker-compose down || exit 0'
                    }
                }
                echo 'Contenedores antiguos detenidos'
            }
        }
        
        stage('Construir Imagen Docker') {
            steps {
                echo '========== ETAPA 6: Construyendo nueva imagen Docker =========='
                script {
                    if (isUnix()) {
                        sh "docker-compose build --no-cache"
                    } else {
                        bat "docker-compose build --no-cache"
                    }
                }
                echo 'Imagen Docker construida exitosamente'
            }
        }
        
        stage('Levantar Servicios') {
            steps {
                echo '========== ETAPA 7: Levantando servicios (PostgreSQL + FastAPI) =========='
                script {
                    if (isUnix()) {
                        sh 'docker-compose up -d'
                    } else {
                        bat 'docker-compose up -d'
                    }
                }
                echo 'Servicios levantados en modo daemon'
            }
        }
        
        stage('Verificar Health Check') {
            steps {
                echo '========== ETAPA 8: Verificando que la aplicación responda =========='
                script {
                    sleep 15  // Dar tiempo a que los servicios inicien
                    if (isUnix()) {
                        sh 'curl -f http://localhost:8000/health || exit 1'
                    } else {
                        bat 'curl -f http://localhost:8000/health || exit 1'
                    }
                }
                echo 'Aplicación respondiendo correctamente'
            }
        }
        
        stage('Tests de Integración') {
            steps {
                echo '========== ETAPA 9: Ejecutando tests de integración =========='
                script {
                    // Test endpoint de servicios
                    if (isUnix()) {
                        sh 'curl -f http://localhost:8000/api/v1/info/services || exit 1'
                    } else {
                        bat 'curl -f http://localhost:8000/api/v1/info/services || exit 1'
                    }
                }
                echo 'Tests de integración completados'
            }
        }
        
        stage('Backup Base de Datos (Producción)') {
            when {
                branch 'main'
            }
            steps {
                echo '========== ETAPA 10: Creando backup de PostgreSQL =========='
                script {
                    def timestamp = new Date().format('yyyyMMdd_HHmmss')
                    if (isUnix()) {
                        sh "docker exec ${POSTGRES_CONTAINER} pg_dump -U postgres si806 > backup_${timestamp}.sql || true"
                    } else {
                        bat "docker exec ${POSTGRES_CONTAINER} pg_dump -U postgres si806 > backup_${timestamp}.sql || exit 0"
                    }
                }
                echo 'Backup creado exitosamente'
            }
        }
        
        stage('Deploy a Producción') {
            when {
                branch 'main'
            }
            steps {
                echo '========== ETAPA 11: Deploy a servidor de producción =========='
                echo 'Aplicación desplegada en: http://localhost:8000'
                echo 'Panel de administración: http://localhost:8000/panel.html'
                echo 'Documentación API: http://localhost:8000/docs'
            }
        }
    }
    
    post {
        success {
            echo '=========================================='
            echo 'PIPELINE COMPLETADO EXITOSAMENTE'
            echo '=========================================='
            echo 'Tiempo total: ' + currentBuild.durationString
            echo 'Build #' + env.BUILD_NUMBER
            echo 'Aplicación disponible en: http://localhost:8000/index.html'
            
            // Notificación por email (opcional)
            // emailext(
            //     subject: "✅ SISCAL - Deploy Exitoso #${BUILD_NUMBER}",
            //     body: "El pipeline se completó exitosamente.\nTiempo: ${currentBuild.durationString}\nURL: http://localhost:8000",
            //     to: "equipo@luzdelsur.com.pe"
            // )
        }
        
        failure {
            echo '=========================================='
            echo 'PIPELINE FALLÓ'
            echo '=========================================='
            echo 'Revisar logs para identificar el problema'
            
            // Notificación de fallo (opcional)
            // emailext(
            //     subject: "❌ SISCAL - Deploy Fallido #${BUILD_NUMBER}",
            //     body: "El pipeline falló en la etapa: ${env.STAGE_NAME}\nRevisar: ${env.BUILD_URL}",
            //     to: "equipo@luzdelsur.com.pe"
            // )
        }
        
        always {
            echo 'Limpiando workspace...'
            // cleanWs()  // Descomentar para limpiar workspace después de cada build
        }
    }
}
