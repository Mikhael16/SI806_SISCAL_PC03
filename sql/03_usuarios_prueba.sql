
-- Todos los usuarios tienen la contraseña: "LuzDelSur2024"


INSERT INTO usuario (email, password_hash, estado) VALUES
('cliente@luzdelsur.com.pe', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYWYnFy3L8i', 'A');

INSERT INTO usuario_rol (id_usuario, id_rol) VALUES
((SELECT id_usuario FROM usuario WHERE email = 'cliente@luzdelsur.com.pe'),
 (SELECT id_rol FROM rol WHERE codigo = 'CLIENTE'));

INSERT INTO usuario (email, password_hash, estado) VALUES
('analista@luzdelsur.com.pe', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYWYnFy3L8i', 'A');

INSERT INTO usuario_rol (id_usuario, id_rol) VALUES
((SELECT id_usuario FROM usuario WHERE email = 'analista@luzdelsur.com.pe'),
 (SELECT id_rol FROM rol WHERE codigo = 'ANALISTA'));

INSERT INTO usuario (email, password_hash, estado) VALUES
('supervisor@luzdelsur.com.pe', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYWYnFy3L8i', 'A');

INSERT INTO usuario_rol (id_usuario, id_rol) VALUES
((SELECT id_usuario FROM usuario WHERE email = 'supervisor@luzdelsur.com.pe'),
 (SELECT id_rol FROM rol WHERE codigo = 'SUPERVISOR'));

INSERT INTO usuario (email, password_hash, estado) VALUES
('integrador@luzdelsur.com.pe', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYWYnFy3L8i', 'A');

INSERT INTO usuario_rol (id_usuario, id_rol) VALUES
((SELECT id_usuario FROM usuario WHERE email = 'integrador@luzdelsur.com.pe'),
 (SELECT id_rol FROM rol WHERE codigo = 'INTEGRADOR'));

INSERT INTO usuario (email, password_hash, estado) VALUES
('admin@luzdelsur.com.pe', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYWYnFy3L8i', 'A');

INSERT INTO usuario_rol (id_usuario, id_rol) VALUES
((SELECT id_usuario FROM usuario WHERE email = 'admin@luzdelsur.com.pe'),
 (SELECT id_rol FROM rol WHERE codigo = 'ANALISTA')),
((SELECT id_usuario FROM usuario WHERE email = 'admin@luzdelsur.com.pe'),
 (SELECT id_rol FROM rol WHERE codigo = 'SUPERVISOR')),
((SELECT id_usuario FROM usuario WHERE email = 'admin@luzdelsur.com.pe'),
 (SELECT id_rol FROM rol WHERE codigo = 'INTEGRADOR'));
