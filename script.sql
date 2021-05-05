DROP TABLE IF EXISTS ville ;  
CREATE TABLE ville (Code_postal BIGINT NOT NULL, ville_nom VARCHAR, PRIMARY KEY (Code_postal) ) ENGINE=InnoDB;  
DROP TABLE IF EXISTS temperature ;  
CREATE TABLE temperature (Code_temperature int AUTO_INCREMENT NOT NULL, temperature_min DOUBLE, temperature_max DOUBLE, PRIMARY KEY (Code_temperature) ) ENGINE=InnoDB;  
DROP TABLE IF EXISTS ville_temperature ;  
CREATE TABLE ville_temperature (Code_postal BIGINT NOT NULL, Code_temperature int NOT NULL, ville_temperature_date DATETIME, temperature_actuelle DOUBLE, PRIMARY KEY (Code_postal,  Code_temperature) ) ENGINE=InnoDB;
ALTER TABLE ville_temperature ADD CONSTRAINT FK_ville_temperature_Code_postal FOREIGN KEY (Code_postal) REFERENCES ville (Code_postal);  
ALTER TABLE ville_temperature ADD CONSTRAINT FK_ville_temperature_Code_temperature FOREIGN KEY (Code_temperature) REFERENCES temperature (Code_temperature);  