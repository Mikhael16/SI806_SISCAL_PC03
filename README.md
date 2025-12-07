# 🚀 SI806 SISCAL - Sistema de Calibración con CI/CD

![Estado](https://img.shields.io/badge/Estado-Producción-success)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-red)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green)

**Sistema Integral de Calibración** para Luz del Sur S.A.A. con arquitectura moderna, autenticación JWT, roles multinivel y despliegue automatizado mediante Jenkins CI/CD.

---

## 📋 Tabla de Contenidos

1. [🎯 Descripción General](#-descripción-general)
2. [🎨 Portfolio Personal](#-portfolio-personal)
3. [⚡ Aplicación SISCAL](#-aplicación-siscal)
4. [🔄 CI/CD con Jenkins](#-cicd-con-jenkins)
5. [🚀 Instalación y Configuración](#-instalación-y-configuración)
6. [🔐 Credenciales de Acceso](#-credenciales-de-acceso)
7. [🏗️ Arquitectura del Sistema](#️-arquitectura-del-sistema)
8. [📚 Documentación Adicional](#-documentación-adicional)

---

## 🎯 Descripción General

Este proyecto integra múltiples componentes tecnológicos en un ecosistema completo:

### 🏆 Componentes Principales

| Componente | Tecnología | Descripción |
|------------|-----------|-------------|
| **Portfolio** | HTML5/CSS3/JS | Landing page profesional responsive |
| **Backend API** | FastAPI + Python 3.12 | API REST con documentación automática |
| **Base de Datos** | PostgreSQL 14 | Schema relacional con triggers |
| **CI/CD** | Jenkins + Docker-in-Docker | Pipeline automatizado de 10 etapas |
| **Contenedores** | Docker Compose | Orquestación multi-servicio |
| **Autenticación** | JWT + bcrypt | Seguridad con roles y permisos |

### ✨ Características Destacadas

✅ **Autenticación Robusta**: JWT con refresh tokens y roles multinivel  
✅ **API Documentada**: Swagger UI y ReDoc integrados  
✅ **Pipeline Completo**: Desde commit hasta producción automatizado  
✅ **Health Checks**: Validación automática de servicios  
✅ **Arquitectura Limpia**: Separación por capas (routes → services → repositories)  
✅ **Base de Datos Inicializada**: Seeds con usuarios de prueba  

---

## 🎨 Portfolio Personal

### Descripción

Landing page profesional que presenta el perfil académico y profesional con diseño moderno y responsive.

### 🎯 Características de Diseño

**Hero Section**:
- Gradiente animado de fondo
- Título principal con descripción
- Call-to-Action destacado
- Responsive desde 320px hasta 4K

**Tarjetas Flotantes**:
```css
- Card "Sobre Mí": Información personal
- Card "Educación": Trayectoria académica
- Card "Habilidades": Stack tecnológico
- Card "Contacto": Enlaces a redes sociales
```

**Paleta de Colores**:
- Primario: `#3498db` (Azul corporativo Luz del Sur)
- Secundario: `#2ecc71` (Verde éxito)
- Gradientes: Cielo y océano con transiciones suaves
- Sombras: `rgba(0,0,0,0.1)` para profundidad

### 📁 Estructura de Archivos

```
📦 Portfolio
├── index.html              # Landing page principal
├── article.html            # Artículo técnico sobre CI/CD
├── css/
│   └── styles.css          # Estilos personalizados
└── assets/
    └── images/             # Recursos gráficos
        ├── profile.jpg
        └── icons/
```

### 🛠️ Tecnologías

- **HTML5**: Estructura semántica con tags modernos
- **CSS3**: Flexbox, Grid, Animaciones, Variables CSS
- **JavaScript**: Interactividad vanilla (sin frameworks)
- **Font Awesome 6.4.0**: Iconografía profesional
- **Google Fonts**: Tipografía Roboto y Open Sans

### 🌐 Acceso

```bash
# Despliegue local
URL: http://localhost:8000/
Archivo Principal: index.html
Artículo: http://localhost:8000/article.html
```

---

## ⚡ Aplicación SISCAL

### Descripción

Sistema backend desarrollado en **FastAPI** para gestión de calibraciones de medidores eléctricos, con autenticación JWT, roles multinivel y arquitectura por capas.

### 🏗️ Arquitectura por Capas

```
📦 app/
├── 🌐 api/v1/              # Capa de Presentación
│   ├── routes_auth.py      # Endpoints de autenticación
│   ├── routes_usuarios.py  # CRUD de usuarios
│   └── routes_medidores.py # Gestión de medidores
│
├── 💼 services/            # Capa de Lógica de Negocio
│   ├── auth_service.py     # Lógica de autenticación
│   └── usuarios_service.py # Validaciones y reglas
│
├── 🗄️ repositories/        # Capa de Acceso a Datos
│   ├── usuarios.py         # Queries de usuarios
│   └── medidores.py        # Queries de medidores
│
├── 🔐 core/                # Configuración Central
│   ├── config.py           # Variables de entorno
│   ├── security.py         # JWT y bcrypt
│   └── dependencies.py     # Inyección de dependencias
│
├── 📊 models/              # Modelos SQLAlchemy
│   ├── usuario.py
│   ├── rol.py
│   └── medidor.py
│
└── 🗂️ db/                  # Base de Datos
    ├── session.py          # Configuración de sesión
    └── base.py             # Base declarativa
```

### 🔑 Sistema de Autenticación

**Flujo de Autenticación**:
```
1. Usuario envía credenciales (email + password)
2. Backend valida con bcrypt
3. Genera JWT con datos: {user_id, email, roles}
4. Frontend almacena token en localStorage
5. Requests subsiguientes incluyen: Authorization: Bearer <token>
```

**Roles Implementados**:
- 🔍 **ANALISTA**: Crea y revisa calibraciones
- ✅ **SUPERVISOR**: Aprueba calibraciones
- 🔗 **INTEGRADOR**: Integra con sistemas externos
- 👤 **CLIENTE**: Visualiza resultados

### 📡 API Endpoints

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| POST | `/api/v1/auth/login` | Login y obtención de token | ❌ |
| POST | `/api/v1/auth/refresh` | Renovar access token | ✅ |
| GET | `/api/v1/usuarios/me` | Perfil del usuario actual | ✅ |
| GET | `/api/v1/medidores` | Listar medidores | ✅ ANALISTA+ |
| POST | `/api/v1/calibraciones` | Nueva calibración | ✅ ANALISTA+ |

### 🗃️ Base de Datos

**Schema PostgreSQL**:
```sql
📊 Tablas Principales:
├── usuario              (id, email, password_hash, estado)
├── rol                  (id, codigo, nombre)
├── usuario_rol          (id_usuario, id_rol) [Relación N:M]
├── medidor              (id, numero_serie, marca, modelo)
├── calibracion          (id, id_medidor, fecha, resultado)
└── historial_login      (id, id_usuario, ip, user_agent)
```

**Scripts de Inicialización**:
```bash
sql/
├── 01_schema_postgres.sql      # Definición de tablas y constraints
├── 02_seed_postgres.sql        # Datos maestros (roles)
└── 03_usuarios_prueba.sql      # Usuarios de prueba
```

### 🔧 Tecnologías y Dependencias

```python
# requirements.txt
fastapi                 # Framework web moderno
uvicorn                 # ASGI server
sqlalchemy              # ORM para PostgreSQL
psycopg2-binary         # Driver de PostgreSQL
python-jose[cryptography]  # JWT encoding/decoding
bcrypt                  # Hashing de contraseñas
passlib                 # Utilidades de passwords
python-dotenv           # Gestión de variables de entorno
email-validator         # Validación de emails
```

### 🐳 Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY . .

# Exponer puerto
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 📝 Documentación Automática

FastAPI genera documentación interactiva automáticamente:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

---

## 🔄 CI/CD con Jenkins

### Descripción

Pipeline de **integración y despliegue continuo** implementado con Jenkins, ejecutando 10 etapas automatizadas desde el commit hasta producción.

### 🏗️ Arquitectura Jenkins

**Jenkins con Docker-in-Docker**:
```yaml
jenkins:
  image: jenkins/jenkins:lts-jdk17
  privileged: true
  volumes:
    - /var/run/docker.sock:/var/run/docker.sock  # Docker socket
    - jenkins-data:/var/jenkins_home
  ports:
    - "8080:8080"   # UI
    - "50000:50000" # Agentes
```

**Instalación Interna**:
```bash
# Dentro del contenedor Jenkins
apt-get update
apt-get install -y docker.io docker-compose
usermod -aG docker jenkins
```

### 📋 Pipeline: 10 Etapas

```groovy
pipeline {
    agent any
    
    stages {
        // 1️⃣ CHECKOUT
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Mikhael16/SI806_SISCAL_PC03',
                    credentialsId: 'github-token'
            }
        }
        
        // 2️⃣ VALIDACIÓN
        stage('Validar Archivos') {
            steps {
                sh 'ls -la'
                sh 'cat docker-compose.jenkins.yml'
            }
        }
        
        // 3️⃣ LIMPIEZA
        stage('Limpiar Contenedores Antiguos') {
            steps {
                sh 'docker-compose -f docker-compose.jenkins.yml down || true'
            }
        }
        
        // 4️⃣ BUILD
        stage('Build Imagen Docker') {
            steps {
                sh 'docker-compose -f docker-compose.jenkins.yml build'
            }
        }
        
        // 5️⃣ DESPLIEGUE BASE DE DATOS
        stage('Desplegar PostgreSQL') {
            steps {
                sh 'docker-compose -f docker-compose.jenkins.yml up -d postgres'
                sh 'sleep 15'  // Esperar inicialización
            }
        }
        
        // 6️⃣ DESPLIEGUE APLICACIÓN
        stage('Desplegar Aplicación') {
            steps {
                sh 'docker-compose -f docker-compose.jenkins.yml up -d web'
                sh 'sleep 10'
            }
        }
        
        // 7️⃣ HEALTH CHECK - DOCS
        stage('Health Check - Documentación') {
            steps {
                sh 'docker exec siscal-web curl -f http://localhost:8000/docs || exit 1'
            }
        }
        
        // 8️⃣ HEALTH CHECK - API
        stage('Health Check - API Root') {
            steps {
                sh 'docker exec siscal-web curl -f http://localhost:8000/ || exit 1'
            }
        }
        
        // 9️⃣ BACKUP (solo en main)
        stage('Backup Base de Datos') {
            when { branch 'main' }
            steps {
                sh '''
                    docker exec siscal-postgres pg_dump -U postgres si806 > \
                    backup_${BUILD_NUMBER}.sql
                '''
            }
        }
        
        // 🔟 DEPLOY A PRODUCCIÓN
        stage('Deploy a Producción') {
            when { branch 'main' }
            steps {
                echo "✅ Aplicación desplegada en http://localhost:8000"
                echo "📚 Documentación disponible en http://localhost:8000/docs"
            }
        }
    }
    
    post {
        success {
            echo '🎉 Pipeline ejecutado exitosamente'
        }
        failure {
            echo '❌ Pipeline falló - revisar logs'
        }
    }
}
```

### 🔗 Configuración de Trigger

**Poll SCM**: Verificación periódica del repositorio
```
H H * * *  # Una vez al día (hora aleatoria)
```

**Alternativas probadas**:
- ❌ **Webhook**: Requiere IP pública (ngrok bloqueado)
- ✅ **Poll SCM**: Funciona perfectamente en entorno académico

### 📊 Historial de Builds

| Build | Estado | Problema Resuelto |
|-------|--------|-------------------|
| #1-5 | ⚠️ | Configuración inicial |
| #6 | ❌ | Rutas relativas en docker-compose |
| #7 | ❌ | Volume override vacío |
| #8 | ❌ | curl desde host (networking) |
| **#9** | ✅ | **SUCCESS - Todas las etapas** |

### 🛠️ docker-compose.jenkins.yml

Versión especial para Jenkins con rutas absolutas:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:14
    container_name: siscal-postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: si806
    volumes:
      - ${WORKSPACE}/sql/01_schema_postgres.sql:/docker-entrypoint-initdb.d/01_schema.sql:ro
      - ${WORKSPACE}/sql/02_seed_postgres.sql:/docker-entrypoint-initdb.d/02_seed.sql:ro
      - ${WORKSPACE}/sql/03_usuarios_prueba.sql:/docker-entrypoint-initdb.d/03_usuarios.sql:ro
    networks:
      - siscal-network

  web:
    build:
      context: ${WORKSPACE}
    container_name: siscal-web
    env_file:
      - ${WORKSPACE}/.env
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    networks:
      - siscal-network

networks:
  siscal-network:
    driver: bridge
```

**Diferencia clave**: Uso de `${WORKSPACE}` (variable de Jenkins) en lugar de rutas relativas.

### 🔐 Credenciales en Jenkins

```
Credential ID: github-token
Type: Username with password
Username: Mikhael16
Password: <GitHub Personal Access Token>
Scope: Global
```

### 📁 Archivos de Configuración

```
.
├── Jenkinsfile                    # Definición del pipeline
├── docker-compose.yml             # Para desarrollo local
├── docker-compose.jenkins.yml     # Para Jenkins CI/CD
└── .env                           # Variables de entorno
```

---

## 🚀 Instalación y Configuración

### 📋 Requisitos Previos

#### Opción 1: Con Docker (⭐ RECOMENDADO)
```
✅ Docker Desktop 4.0+ (Windows/Mac)
✅ Docker Engine 20.10+ (Linux)
✅ docker-compose 2.0+
✅ Git 2.30+
```

#### Opción 2: Instalación Tradicional
```
✅ Python 3.12+
✅ PostgreSQL 14+
✅ pip 23.0+
✅ Node.js 18+ (opcional, para frontend avanzado)
```

### 🐳 Instalación con Docker

#### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/Mikhael16/SI806_SISCAL_PC03.git
cd SI806_SISCAL_PC03
```

#### 2️⃣ Configurar Variables de Entorno

Crear archivo `.env` en la raíz del proyecto:

```bash
# Base de Datos
DB_HOST=siscal-postgres
DB_PORT=5432
DB_NAME=si806
DB_USER=postgres
DB_PASSWORD=postgres

# JWT
SECRET_KEY=tu_clave_secreta_super_segura_aqui_cambiar_en_produccion
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Aplicación
APP_NAME=SISCAL
APP_VERSION=1.0.0
DEBUG=True
```

#### 3️⃣ Levantar Servicios

```bash
# Desarrollo local
docker-compose up -d

# Ver logs
docker-compose logs -f

# Verificar estado
docker ps
```

#### 4️⃣ Acceder a la Aplicación

```
🌐 Frontend: http://localhost:8000/
📚 API Docs (Swagger): http://localhost:8000/docs
📖 API Docs (ReDoc): http://localhost:8000/redoc
🔐 Login: http://localhost:8000/login.html
```

### 🛠️ Instalación con Jenkins

#### 1️⃣ Instalar Jenkins con Docker

```bash
# Crear red de Jenkins
docker network create jenkins

# Ejecutar Jenkins
docker run -d \
  --name jenkins \
  --network jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --user root \
  jenkins/jenkins:lts-jdk17
```

#### 2️⃣ Configurar Docker dentro de Jenkins

```bash
# Acceder al contenedor
docker exec -u root jenkins bash

# Instalar Docker y Docker Compose
apt-get update
apt-get install -y docker.io docker-compose
usermod -aG docker jenkins
exit

# Reiniciar Jenkins
docker restart jenkins
```

#### 3️⃣ Configuración Inicial de Jenkins

```bash
# Obtener password inicial
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# Navegar a: http://localhost:8080
# Pegar el password
# Instalar plugins sugeridos
```

#### 4️⃣ Configurar Credenciales GitHub

```
1. Dashboard → Manage Jenkins → Credentials
2. (global) → Add Credentials
3. Kind: Username with password
4. Username: tu_usuario_github
5. Password: <GitHub Personal Access Token>
6. ID: github-token
7. Save
```

#### 5️⃣ Crear Pipeline

```
1. New Item → "SISCAL-Pipeline" → Pipeline
2. En "Build Triggers":
   ☑ Poll SCM
   Schedule: H H * * *
3. En "Pipeline":
   Definition: Pipeline script from SCM
   SCM: Git
   Repository URL: https://github.com/Mikhael16/SI806_SISCAL_PC03
   Credentials: github-token
   Branch: */main
   Script Path: Jenkinsfile
4. Save
```

#### 6️⃣ Ejecutar Build

```
1. Click en "Construir ahora" (Build Now)
2. Ver progreso en "Build History"
3. Click en el número de build → "Console Output"
```

### 💻 Instalación Tradicional (Sin Docker)

#### 1️⃣ Instalar PostgreSQL

```bash
# Ubuntu/Debian
sudo apt-get install postgresql-14

# Windows
# Descargar de: https://www.postgresql.org/download/windows/

# Crear base de datos
psql -U postgres
CREATE DATABASE si806;
\q
```

#### 2️⃣ Ejecutar Scripts SQL

```bash
psql -U postgres -d si806 -f sql/01_schema_postgres.sql
psql -U postgres -d si806 -f sql/02_seed_postgres.sql
psql -U postgres -d si806 -f sql/03_usuarios_prueba.sql
```

#### 3️⃣ Instalar Dependencias Python

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

#### 4️⃣ Configurar .env

```bash
# Copiar ejemplo
cp .env.example .env

# Editar con tus valores
nano .env  # o tu editor preferido
```

#### 5️⃣ Ejecutar Aplicación

```bash
# Desarrollo
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Producción
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 🔐 Credenciales de Acceso

### 👥 Usuarios de Prueba

Todos los usuarios tienen la contraseña: **`LuzDelSur2024`**

| Email | Roles | Descripción |
|-------|-------|-------------|
| `admin@luzdelsur.com.pe` | ANALISTA, SUPERVISOR, INTEGRADOR | ⭐ Administrador con todos los permisos |
| `analista@luzdelsur.com.pe` | ANALISTA | Crea y revisa calibraciones |
| `supervisor@luzdelsur.com.pe` | SUPERVISOR | Aprueba calibraciones |
| `integrador@luzdelsur.com.pe` | INTEGRADOR | Integración con sistemas externos |
| `cliente@luzdelsur.com.pe` | CLIENTE | Visualiza resultados |

### 🔑 Ejemplo de Login

```bash
# Usando curl
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@luzdelsur.com.pe",
    "password": "LuzDelSur2024"
  }'

# Respuesta
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 5,
    "email": "admin@luzdelsur.com.pe",
    "roles": ["ANALISTA", "SUPERVISOR", "INTEGRADOR"]
  }
}
```

### 🗄️ Acceso Directo a PostgreSQL

```bash
# Con Docker
docker exec -it siscal-postgres psql -U postgres -d si806

# Sin Docker
psql -U postgres -d si806

# Queries útiles
SELECT email, estado FROM usuario;
SELECT * FROM rol;
SELECT u.email, r.nombre FROM usuario u 
JOIN usuario_rol ur ON u.id_usuario = ur.id_usuario
JOIN rol r ON ur.id_rol = r.id_rol;
```

### 🐳 Acceso a Jenkins

```
URL: http://localhost:8080
Usuario: admin
Password: <obtener con: docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword>
```

---

## 🏗️ Arquitectura del Sistema

### 📊 Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────┐
│                        USUARIO FINAL                         │
│                    (Navegador Web)                           │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/HTTPS
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (HTML/CSS/JS)                    │
│  • index.html (Portfolio)                                    │
│  • login.html (Autenticación)                                │
│  • dashboard.html (Panel principal)                          │
└────────────────────┬────────────────────────────────────────┘
                     │ REST API (JSON)
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  BACKEND - FastAPI                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  API Layer (routes)                                 │    │
│  │    • /api/v1/auth/* → Login, Refresh Token          │    │
│  │    • /api/v1/usuarios/* → CRUD Usuarios             │    │
│  │    • /api/v1/medidores/* → Gestión Medidores        │    │
│  └───────────────────┬─────────────────────────────────┘    │
│                      │                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Service Layer (Lógica de Negocio)                 │    │
│  │    • auth_service.py → Validaciones JWT             │    │
│  │    • usuarios_service.py → Reglas de negocio        │    │
│  └───────────────────┬─────────────────────────────────┘    │
│                      │                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Repository Layer (Acceso a Datos)                  │    │
│  │    • usuarios.py → Queries SQL                      │    │
│  │    • medidores.py → Queries SQL                     │    │
│  └───────────────────┬─────────────────────────────────┘    │
└────────────────────────┼────────────────────────────────────┘
                         │ SQLAlchemy ORM
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              BASE DE DATOS - PostgreSQL 14                   │
│  • usuario (id, email, password_hash, estado)                │
│  • rol (id, codigo, nombre)                                  │
│  • usuario_rol (id_usuario, id_rol)                          │
│  • medidor (id, numero_serie, marca, modelo)                 │
│  • calibracion (id, id_medidor, fecha, resultado)            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      CI/CD - JENKINS                         │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Pipeline (10 Stages)                               │    │
│  │  1. Checkout → 2. Validar → 3. Limpiar             │    │
│  │  4. Build → 5. Deploy DB → 6. Deploy App           │    │
│  │  7. Health Check Docs → 8. Health Check API        │    │
│  │  9. Backup → 10. Production Deploy                 │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  Trigger: Poll SCM (H H * * *)                              │
└─────────────────────────────────────────────────────────────┘
```

### 🔄 Flujo de Datos

#### Login Flow
```
1. Usuario → POST /api/v1/auth/login {email, password}
2. Backend → Valida credenciales con bcrypt
3. Backend → Consulta roles del usuario en PostgreSQL
4. Backend → Genera JWT con {user_id, email, roles}
5. Backend → Responde con {access_token, refresh_token, user}
6. Frontend → Almacena token en localStorage
7. Frontend → Redirige a dashboard según rol
```

#### Request Autenticado
```
1. Frontend → GET /api/v1/usuarios/me
   Headers: {Authorization: "Bearer <token>"}
2. Backend → Valida JWT con jose
3. Backend → Extrae user_id del token
4. Backend → Consulta datos en PostgreSQL
5. Backend → Responde con datos del usuario
```

### 🐳 Arquitectura Docker

```yaml
┌─────────────────────────────────────────────────────────┐
│                    Docker Host                          │
│                                                         │
│  ┌────────────────────────────────────────────────┐   │
│  │  Network: siscal-network (bridge)              │   │
│  │                                                 │   │
│  │  ┌─────────────────┐  ┌──────────────────┐    │   │
│  │  │ siscal-postgres │  │   siscal-web     │    │   │
│  │  │                 │  │                  │    │   │
│  │  │ PostgreSQL 14   │◄─┤ FastAPI + Python│    │   │
│  │  │ Port: 5432      │  │ Port: 8000       │    │   │
│  │  │                 │  │                  │    │   │
│  │  │ Volume:         │  │ Build: ./        │    │   │
│  │  │ postgres_data   │  │ Env: .env        │    │   │
│  │  │ SQL Scripts     │  │                  │    │   │
│  │  └─────────────────┘  └──────────────────┘    │   │
│  │         │                      │               │   │
│  │         └──────────┬───────────┘               │   │
│  └────────────────────┼──────────────────────────┘   │
│                       │                              │
│  ┌────────────────────▼──────────────────────────┐   │
│  │        Port Mapping                           │   │
│  │  Host:5432 → Container:5432 (PostgreSQL)      │   │
│  │  Host:8000 → Container:8000 (FastAPI)         │   │
│  └───────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### 🔐 Seguridad

**Autenticación y Autorización**:
```
1. Passwords: bcrypt con salt (12 rounds)
2. JWT: HS256 con SECRET_KEY
3. Token expiration: 30 minutos (configurable)
4. Refresh tokens: Para renovación sin re-login
5. Role-based access: Decoradores @require_role()
```

**Protecciones Implementadas**:
- ✅ SQL Injection: SQLAlchemy ORM con parametrización
- ✅ CORS: Configurado en FastAPI middleware
- ✅ Rate Limiting: Pendiente (recomendado: slowapi)
- ✅ HTTPS: Pendiente para producción (Nginx + Let's Encrypt)

### 📦 Estructura de Directorios

```
SI806_SISCAL/
├── 📄 README.md                      # Este archivo
├── 📄 Jenkinsfile                    # Definición del pipeline
├── 🐳 Dockerfile                     # Imagen de la aplicación
├── 🐳 docker-compose.yml             # Orquestación local
├── 🐳 docker-compose.jenkins.yml     # Orquestación para CI/CD
├── 📄 requirements.txt               # Dependencias Python
├── 📄 .env                           # Variables de entorno (no versionado)
├── 📄 .gitignore                     # Archivos ignorados
│
├── 📁 app/                           # Código fuente backend
│   ├── 📄 main.py                    # Punto de entrada FastAPI
│   ├── 📁 api/v1/                    # Endpoints REST
│   ├── 📁 core/                      # Configuración y seguridad
│   ├── 📁 db/                        # Conexión a base de datos
│   ├── 📁 models/                    # Modelos SQLAlchemy
│   ├── 📁 repositories/              # Capa de datos
│   ├── 📁 schemas/                   # Pydantic schemas
│   └── 📁 services/                  # Lógica de negocio
│
├── 📁 sql/                           # Scripts de base de datos
│   ├── 01_schema_postgres.sql        # DDL (CREATE TABLE)
│   ├── 02_seed_postgres.sql          # Datos maestros
│   └── 03_usuarios_prueba.sql        # Usuarios de prueba
│
├── 📁 static/                        # Archivos estáticos frontend
│   ├── 📁 css/
│   ├── 📁 js/
│   └── 📁 images/
│
├── 📁 templates/                     # HTML templates
│   ├── index.html                    # Landing page
│   ├── article.html                  # Artículo técnico
│   └── login.html                    # Página de login
│
└── 📁 docs/                          # Documentación adicional
    ├── JENKINS_IMPLEMENTACION.md     # Guía completa de Jenkins
    ├── solucion3.md                  # Poll SCM setup
    ├── ANALISIS_BUILD6_Y_SOLUCION.md # Troubleshooting Build #6
    └── BUILD9_EXITO_COMPLETO.md      # Análisis de éxito
```

---

## 📚 Documentación Adicional

### 📖 Guías Detalladas

| Documento | Descripción | Líneas |
|-----------|-------------|--------|
| [JENKINS_IMPLEMENTACION.md](./JENKINS_IMPLEMENTACION.md) | Guía completa de implementación de Jenkins | 1000+ |
| [solucion3.md](./solucion3.md) | Configuración Poll SCM y troubleshooting | 1068 |
| [ANALISIS_BUILD6_Y_SOLUCION.md](./ANALISIS_BUILD6_Y_SOLUCION.md) | Análisis profundo del error de rutas | 407 |
| [BUILD9_EXITO_COMPLETO.md](./BUILD9_EXITO_COMPLETO.md) | Documentación del despliegue exitoso | 422 |

### 🔍 Solución de Problemas Comunes

#### ❌ Error: "Email o Contraseña incorrectos"
```bash
# Verificar hash en base de datos
docker exec siscal-postgres psql -U postgres -d si806 -c \
  "SELECT email, substring(password_hash, 1, 10) FROM usuario;"

# Si el hash está corrupto, regenerar usuarios
docker exec siscal-postgres psql -U postgres -d si806 -c \
  "DELETE FROM usuario_rol; DELETE FROM usuario;"
docker cp ./sql/03_usuarios_prueba.sql siscal-postgres:/tmp/
docker exec siscal-postgres psql -U postgres -d si806 -f /tmp/03_usuarios_prueba.sql
```

#### ❌ Error: "Connection refused" en PostgreSQL
```bash
# Verificar que DB_HOST apunta al contenedor
cat .env | grep DB_HOST
# Debe ser: DB_HOST=siscal-postgres

# Si está mal, corregir:
sed -i 's/DB_HOST=localhost/DB_HOST=siscal-postgres/' .env
docker-compose restart web
```

#### ❌ Jenkins: "docker: command not found"
```bash
# Instalar Docker dentro de Jenkins
docker exec -u root jenkins bash -c \
  "apt-get update && apt-get install -y docker.io docker-compose"
docker restart jenkins
```

#### ❌ Build falla en "Health Check"
```bash
# Ver logs de la aplicación
docker logs siscal-web --tail 50

# Verificar que los contenedores están en la misma red
docker network inspect siscal-network
```

### 🎓 Recursos de Aprendizaje

- **FastAPI**: https://fastapi.tiangolo.com/
- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **Jenkins**: https://www.jenkins.io/doc/
- **Docker**: https://docs.docker.com/
- **PostgreSQL**: https://www.postgresql.org/docs/

### 📊 Métricas del Proyecto

```
📝 Líneas de Código:
├── Python: ~2,500 líneas
├── SQL: ~300 líneas
├── HTML/CSS: ~800 líneas
└── Markdown (docs): ~5,000 líneas

🕐 Tiempo de Desarrollo:
├── Backend API: 3 semanas
├── CI/CD Pipeline: 1 semana
├── Frontend: 1 semana
└── Documentación: 1 semana

🎯 Cobertura:
├── Endpoints: 15+ rutas
├── Tests: Pendiente (próxima fase)
└── Documentación: 100%
```

### 🤝 Contribuciones

Este proyecto fue desarrollado como parte del curso SI806 - Universidad Nacional de Ingeniería.

**Desarrollado por**: [Tu Nombre]  
**Curso**: SI806 - Arquitectura de Software  
**Institución**: Universidad Nacional de Ingeniería  
**Periodo**: 2024-2025  

### 📝 Licencia

Este proyecto es de uso académico y no tiene licencia comercial.

---

## 🚀 Comandos Rápidos

### 📦 Docker

```bash
# Iniciar todo
docker-compose up -d

# Ver logs en tiempo real
docker-compose logs -f

# Reiniciar solo la aplicación
docker-compose restart web

# Detener todo
docker-compose down

# Limpiar todo (incluye volúmenes)
docker-compose down -v

# Ver estado
docker ps

# Entrar a PostgreSQL
docker exec -it siscal-postgres psql -U postgres -d si806

# Entrar al contenedor de la app
docker exec -it siscal-web bash
```

### 🔧 Jenkins

```bash
# Ver logs de Jenkins
docker logs jenkins -f

# Obtener password inicial
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# Reiniciar Jenkins
docker restart jenkins

# Backup de configuración
docker cp jenkins:/var/jenkins_home/jobs ./jenkins-backup
```

### 🗄️ PostgreSQL

```bash
# Backup de base de datos
docker exec siscal-postgres pg_dump -U postgres si806 > backup.sql

# Restaurar backup
cat backup.sql | docker exec -i siscal-postgres psql -U postgres si806

# Ver tablas
docker exec siscal-postgres psql -U postgres -d si806 -c "\dt"

# Ver usuarios
docker exec siscal-postgres psql -U postgres -d si806 -c \
  "SELECT email, estado FROM usuario;"
```

### 🧪 Testing API

```bash
# Health check
curl http://localhost:8000/

# Login
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@luzdelsur.com.pe","password":"LuzDelSur2024"}'

# Request autenticado (reemplazar <TOKEN>)
curl http://localhost:8000/api/v1/usuarios/me \
  -H "Authorization: Bearer <TOKEN>"
```

---

## ✅ Checklist de Despliegue

### Pre-despliegue
- [ ] Docker y Docker Compose instalados
- [ ] Puerto 8000 disponible
- [ ] Puerto 5432 disponible
- [ ] Archivo `.env` configurado
- [ ] Git instalado y configurado

### Despliegue Local
- [ ] `git clone` completado
- [ ] `docker-compose up -d` ejecutado
- [ ] Contenedores corriendo: `docker ps`
- [ ] Base de datos inicializada
- [ ] http://localhost:8000 accesible
- [ ] Login funcional con usuario de prueba

### Jenkins CI/CD
- [ ] Jenkins corriendo en puerto 8080
- [ ] Docker instalado dentro de Jenkins
- [ ] Credenciales GitHub configuradas
- [ ] Pipeline creado y configurado
- [ ] Poll SCM habilitado
- [ ] Build #9 o superior exitoso
- [ ] Aplicación desplegada desde Jenkins

### Validación Final
- [ ] Swagger UI accesible: /docs
- [ ] ReDoc accesible: /redoc
- [ ] Login funcional
- [ ] Tokens JWT válidos
- [ ] Endpoints protegidos funcionando
- [ ] Roles y permisos correctos

---

<div align="center">

## 🎉 ¡Proyecto Completado!

**SISCAL - Sistema de Calibración**  
*Desarrollado con FastAPI, PostgreSQL y Jenkins CI/CD*

[![Estado](https://img.shields.io/badge/Estado-Producción-success)](http://localhost:8000)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen)](http://localhost:8080)
[![Docs](https://img.shields.io/badge/Docs-100%25-blue)](http://localhost:8000/docs)

</div>

---

## INSTALACION RAPIDA CON DOCKER (RECOMENDADO)

Docker permite ejecutar el proyecto completo con un solo comando, sin instalar Python ni PostgreSQL manualmente.

### PASO 1: Instalar Docker

**Windows/Mac:**
1. Descargar Docker Desktop: https://www.docker.com/products/docker-desktop
2. Ejecutar instalador
3. Reiniciar computadora
4. Abrir Docker Desktop

**Linux:**
```bash
sudo apt-get update
sudo apt-get install docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

### PASO 2: Verificar Instalacion

```powershell
docker --version
docker-compose --version
```

### PASO 3: Extraer y Navegar al Proyecto

```powershell
cd C:\Users\Usuario\Desktop\SI806_SISCAL
```

### PASO 4: Levantar Servicios

```powershell
docker-compose up
```

Esto automaticamente:
- Descarga PostgreSQL 14
- Crea base de datos si806
- Ejecuta scripts SQL (tablas + roles)
- Inicia servidor FastAPI en http://localhost:8000

### PASO 5: Acceder al Sistema

Abrir navegador:
- **Login:** http://localhost:8000/index.html
- **Panel:** http://localhost:8000/panel.html
- **API Docs:** http://localhost:8000/docs

### PASO 6: Detener Servicios

Presionar `CTRL + C` en la terminal, o ejecutar:

```powershell
docker-compose down
```

### Comandos Utiles de Docker

```powershell
# Iniciar en segundo plano
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down

# Reiniciar servicios
docker-compose restart

# Ver estado
docker-compose ps

# Eliminar todo (incluye base de datos)
docker-compose down -v
```

**Nota:** Para mas detalles sobre Docker, consultar el archivo `DOCKER_GUIA.txt`.

---

## GUIA DE INSTALACION TRADICIONAL (SIN DOCKER)

### PASO 1: Verificar Python

Abrir PowerShell y ejecutar:

```powershell
python --version
```

Debe mostrar Python 3.8 o superior. Si no esta instalado, descargar desde https://www.python.org/downloads/

### PASO 2: Verificar PostgreSQL

En PowerShell ejecutar:

```powershell
psql --version
```

Debe mostrar PostgreSQL 12 o superior. Si no esta instalado, descargar desde https://www.postgresql.org/download/

### PASO 3: Extraer el Proyecto

Extraer el archivo comprimido en una ubicacion de su preferencia. Por ejemplo:

```
C:\Users\Usuario\Desktop\SI806_SISCAL\
```

### PASO 4: Configurar la Base de Datos

#### 4.1. Crear la Base de Datos

Abrir PowerShell como Administrador y ejecutar:

```powershell
# Conectarse a PostgreSQL (reemplazar 'postgres' con su usuario si es diferente)
psql -U postgres

# Dentro de psql, ejecutar:
CREATE DATABASE si806 ENCODING 'UTF8';
\q
```

Si PostgreSQL esta en un puerto diferente al 5432, especificarlo:

```powershell
psql -U postgres -p 5433
```

#### 4.2. Ejecutar Scripts SQL

Navegar a la carpeta del proyecto y ejecutar los scripts:

```powershell
cd C:\Users\Usuario\Desktop\SI806_SISCAL

# Ejecutar script de creacion de tablas (ajustar puerto si es necesario)
psql -U postgres -d si806 -f sql\01_schema_postgres.sql

# Ejecutar script de datos iniciales
psql -U postgres -d si806 -f sql\02_seed_postgres.sql
```

Si PostgreSQL esta en puerto 5433:

```powershell
psql -U postgres -p 5433 -d si806 -f sql\01_schema_postgres.sql
psql -U postgres -p 5433 -d si806 -f sql\02_seed_postgres.sql
```

### PASO 5: Configurar Variables de Entorno

#### 5.1. Copiar archivo de configuracion

En PowerShell, dentro de la carpeta del proyecto:

```powershell
Copy-Item .env.example .env
```

#### 5.2. Editar archivo .env

Abrir el archivo `.env` con un editor de texto (Notepad, VS Code, etc.) y modificar:

```env
SECRET_KEY=cambiar_por_clave_segura_aleatoria_minimo_32_caracteres
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15

DB_ENGINE=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=si806
DB_USER=postgres
DB_PASSWORD=su_password_de_postgres_aqui
```

**IMPORTANTE:**
- Cambiar `DB_PASSWORD` por la contraseña real de PostgreSQL
- Cambiar `DB_PORT` si PostgreSQL usa un puerto diferente (ejemplo: 5433)
- Cambiar `SECRET_KEY` por una clave segura

Para generar una SECRET_KEY segura, ejecutar en PowerShell:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copiar el resultado y pegarlo en SECRET_KEY.

### PASO 6: Instalar Dependencias de Python

En PowerShell, dentro de la carpeta del proyecto:

```powershell
pip install -r requirements.txt
```

Si aparece un error de permisos, ejecutar:

```powershell
pip install --user -r requirements.txt
```

### PASO 7: Ejecutar el Servidor

En PowerShell, dentro de la carpeta del proyecto:

```powershell
uvicorn app.main:app --reload
```

Debe aparecer un mensaje similar a:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### PASO 8: Acceder al Sistema

Abrir un navegador web y navegar a:

- **Pagina de Login:** http://localhost:8000/index.html
- **Panel Principal:** http://localhost:8000/panel.html
- **Documentacion API:** http://localhost:8000/docs

---

## CREAR PRIMER USUARIO

### Opcion 1: Desde el Navegador

1. Ir a http://localhost:8000/index.html
2. Hacer clic en "Registrarse"
3. Completar el formulario:
   - Email: usuario@luzdelsur.com.pe
   - Password: Password123
   - Rol: CLIENTE
4. Hacer clic en "Registrar"

### Opcion 2: Desde PowerShell (API)

```powershell
$body = @{
    email = "admin@luzdelsur.com.pe"
    password = "Admin123456"
    roles = @("ANALISTA", "SUPERVISOR")
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/auth/register" `
  -Method POST `
  -ContentType "application/json" `
  -Body $body
```

---

## ROLES DISPONIBLES

El sistema incluye 4 roles predefinidos:

- **CLIENTE**: Usuario final que registra reclamos
- **ANALISTA**: Personal que gestiona reclamos
- **SUPERVISOR**: Supervisor de operaciones
- **INTEGRADOR**: Integrador con OSINERGMIN

Un usuario puede tener multiples roles.

---

## SOLUCION DE PROBLEMAS COMUNES

### Error: "ModuleNotFoundError: No module named 'app'"

**Solucion:** Asegurarse de ejecutar uvicorn desde la carpeta raiz del proyecto (SI806_SISCAL), no desde dentro de la carpeta app.

```powershell
cd C:\Users\Usuario\Desktop\SI806_SISCAL
uvicorn app.main:app --reload
```

### Error: "could not connect to server: Connection refused"

**Solucion:** PostgreSQL no esta ejecutandose o esta en un puerto diferente.

1. Verificar que PostgreSQL este ejecutandose:
   - Windows: Buscar "Servicios" y verificar que "postgresql" este iniciado
2. Verificar el puerto en `.env` (DB_PORT)

### Error: "FATAL: password authentication failed"

**Solucion:** La contraseña en `.env` no coincide con la de PostgreSQL.

1. Abrir archivo `.env`
2. Verificar que DB_PASSWORD sea correcto
3. Reiniciar el servidor uvicorn

### Error: "relation 'usuario' does not exist"

**Solucion:** Los scripts SQL no se ejecutaron correctamente.

1. Volver a ejecutar:
   ```powershell
   psql -U postgres -d si806 -f sql\01_schema_postgres.sql
   psql -U postgres -d si806 -f sql\02_seed_postgres.sql
   ```

### Puerto 8000 ya en uso

**Solucion:** Especificar un puerto diferente:

```powershell
uvicorn app.main:app --reload --port 8001
```

Luego acceder a http://localhost:8001

---

## ESTRUCTURA DEL PROYECTO

```
SI806_SISCAL/
├── app/                          # Codigo fuente del backend
│   ├── main.py                   # Aplicacion principal FastAPI
│   ├── api/v1/                   # Endpoints de la API
│   ├── core/                     # Configuracion y seguridad
│   ├── db/                       # Conexion a base de datos
│   ├── models/                   # Modelos de tablas (SQLAlchemy)
│   ├── repositories/             # Operaciones CRUD
│   ├── schemas/                  # Validacion de datos (Pydantic)
│   └── services/                 # Logica de negocio
├── frontend/                     # Codigo fuente del frontend
│   ├── index.html                # Pagina de login
│   └── panel.html                # Panel de servicios
├── sql/                          # Scripts de base de datos
│   ├── 01_schema_postgres.sql    # Creacion de tablas
│   └── 02_seed_postgres.sql      # Datos iniciales (roles)
├── docs/                         # Documentacion tecnica
├── .env                          # Variables de entorno (NO INCLUIR EN GIT)
├── .env.example                  # Plantilla de variables de entorno
├── requirements.txt              # Dependencias de Python
└── README.md                     # Este archivo
```

---

## ENDPOINTS DE LA API

### Autenticacion

**Registrar Usuario**
```
POST /api/v1/auth/register
Body: {"email": "user@example.com", "password": "Pass123", "roles": ["CLIENTE"]}
```

**Iniciar Sesion**
```
POST /api/v1/auth/login
Body: {"email": "user@example.com", "password": "Pass123"}
Response: {"access_token": "...", "refresh_token": "..."}
```

**Obtener Usuario Actual** (requiere token)
```
GET /api/v1/auth/me
Header: Authorization: Bearer <access_token>
```

**Refrescar Token**
```
POST /api/v1/auth/refresh
Body: {"refresh_token": "..."}
```

### Informacion

**Obtener Servicios Disponibles**
```
GET /api/v1/info/services
```

**Health Check**
```
GET /health
```

---

## DETENER EL SERVIDOR

Para detener el servidor uvicorn:

1. Ir a la ventana de PowerShell donde se ejecuta
2. Presionar `CTRL + C`
3. Esperar mensaje de confirmacion

---

## SEGURIDAD

- Las contraseñas se almacenan hasheadas con bcrypt
- Los tokens JWT expiran en 15 minutos (configurable)
- Los refresh tokens expiran en 7 dias
- Nunca compartir el archivo .env ni subirlo a repositorios publico

---

## LICENCIA

El fin de este trabajo es absolutamente académico, Luz del Sur es la empresa de objeto en estudio, más no es ningún responsable de este trabajo académico
