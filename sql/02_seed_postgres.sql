-- Insertar roles del sistema
INSERT INTO rol (codigo, nombre) VALUES
 ('CLIENTE','Cliente'),
 ('ANALISTA','Analista'),
 ('SUPERVISOR','Supervisor/Especialista'),
 ('INTEGRADOR','Integrador OSINERGMIN')
ON CONFLICT (codigo) DO NOTHING;
