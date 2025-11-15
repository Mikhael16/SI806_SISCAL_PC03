-- Tabla de roles del sistema
CREATE TABLE rol (
  id_rol SERIAL PRIMARY KEY,
  codigo VARCHAR(40) UNIQUE NOT NULL,   -- CLIENTE, ANALISTA, SUPERVISOR, INTEGRADOR
  nombre VARCHAR(80) NOT NULL
);

-- Tabla de usuarios
CREATE TABLE usuario (
  id_usuario SERIAL PRIMARY KEY,
  email VARCHAR(150) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  estado CHAR(1) NOT NULL DEFAULT 'A',  -- A=activo, I=inactivo
  creado_en TIMESTAMP NOT NULL DEFAULT NOW(),
  actualizado_en TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Relación muchos a muchos entre usuarios y roles
CREATE TABLE usuario_rol (
  id_usuario INT NOT NULL REFERENCES usuario(id_usuario) ON DELETE CASCADE,
  id_rol INT NOT NULL REFERENCES rol(id_rol) ON DELETE RESTRICT,
  PRIMARY KEY (id_usuario, id_rol)
);

-- Tokens de refresco para mantener sesiones
CREATE TABLE refresh_token (
  id_token SERIAL PRIMARY KEY,
  id_usuario INT NOT NULL REFERENCES usuario(id_usuario) ON DELETE CASCADE,
  token VARCHAR(512) UNIQUE NOT NULL,
  expira_en TIMESTAMP NOT NULL
);

-- Historial de inicios de sesión
CREATE TABLE login_historial (
  id_login SERIAL PRIMARY KEY,
  id_usuario INT NOT NULL REFERENCES usuario(id_usuario) ON DELETE CASCADE,
  ip VARCHAR(64),
  user_agent VARCHAR(256),
  creado_en TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Índices para optimizar consultas
CREATE INDEX idx_usuario_email ON usuario(email);
CREATE INDEX idx_usuario_estado ON usuario(estado);
CREATE INDEX idx_login_usuario_fecha ON login_historial(id_usuario, creado_en DESC);
CREATE INDEX idx_refresh_usuario ON refresh_token(id_usuario);
