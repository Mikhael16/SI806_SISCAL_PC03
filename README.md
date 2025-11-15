# SISCAL - Sistema de Gestion de Reclamos
## Luz del Sur

Sistema de autenticacion JWT con arquitectura por capas, panel de servicios y gestion de usuarios.

---

## REQUISITOS DEL SISTEMA

- Python 3.8 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno

---

## GUIA DE INSTALACION COMPLETA

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
- Nunca compartir el archivo .env ni subirlo a repositorios publicos

---

## CONTACTO Y SOPORTE

Para consultas tecnicas sobre este proyecto, contactar al equipo de desarrollo de Luz del Sur.

---

## LICENCIA

Copyright 2025 Luz del Sur. Todos los derechos reservados.
