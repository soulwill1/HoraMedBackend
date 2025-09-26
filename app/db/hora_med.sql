-- Creating DB
CREATE DATABASE HoraMed;
USE HoraMed;

-- User table
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    tipo ENUM('paciente', 'cuidador') DEFAULT 'paciente'
);

-- Medication table
CREATE TABLE medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    dosagem VARCHAR(50) NOT NULL,
    instrucoes TEXT
);

-- Reminder table
CREATE TABLE lembretes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    horario TIME NOT NULL,
    dias VARCHAR(50) NOT NULL,
    status ENUM('ativo', 'inativo') DEFAULT 'ativo',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id)
);

-- Sample data
INSERT INTO usuarios (nome, email, senha, tipo) VALUES
('Maria Silva', 'maria@email.com', '123456', 'paciente'),
('João Souza', 'joao@email.com', '654321', 'cuidador'),
('Ana Lima', 'ana@email.com', 'senha123', 'paciente');

INSERT INTO medicamentos (nome, dosagem, instrucoes) VALUES
('Dipirona', '500mg', 'Tomar após as refeições'),
('Amoxicilina', '875mg', 'Tomar a cada 12h'),
('Losartana', '50mg', 'Tomar pela manhã');

INSERT INTO lembretes (usuario_id, medicamento_id, horario, dias, status) VALUES
(1, 1, '08:00:00', 'Seg,Qua,Sex', 'ativo'),
(1, 3, '09:00:00', 'Todos', 'ativo'),
(3, 2, '20:00:00', 'Ter,Qui', 'ativo');
