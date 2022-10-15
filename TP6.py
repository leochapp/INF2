import sqlite3
#import pandas as pd

# Connexion à une base de donnée
try:
    connexion = sqlite3.connect("alesc.sqlite")
    cursor = connexion.cursor()
    print("Base de données crée et correctement connectée à SQLite")
    sql = "SELECT sqlite_version();"
    cursor.execute(sql)
    res = cursor.fetchall()
    print("La version de SQLite est: ", res)
except sqlite3.Error as error:
    print("Erreur lors de la connexion à SQLite", error)

def main():
    request = f"SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0; SET " \
              f"@OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0; SET @OLD_SQL_MODE=@@SQL_MODE, " \
              f"SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE," \
              f"ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'; CREATE SCHEMA IF NOT EXISTS `alesc.sqlite` " \
              f"DEFAULT CHARACTER SET utf8 ; USE `alesc.sqlite` ; CREATE TABLE IF NOT EXISTS `alesc.sqlite`.`logeurs` " \
              f"( `idlogeurs` INT NOT NULL, `nom` VARCHAR(45) NULL, `prenom` VARCHAR(45) NULL, `num_rue` INT NULL, " \
              f"`nom_rue` VARCHAR(45) NULL, `code_postal` INT NULL, `ville` VARCHAR(45) NULL, PRIMARY KEY (" \
              f"`idlogeurs`)) ENGINE = InnoDB; CREATE TABLE IF NOT EXISTS `alesc.sqlite`.`etudiants` ( `idetudiants` " \
              f"INT NOT NULL, `nom` VARCHAR(45) NULL, `prenom` VARCHAR(45) NULL, `semestre` VARCHAR(45) NULL, " \
              f"PRIMARY KEY (`idetudiants`)) ENGINE = InnoDB; CREATE TABLE IF NOT EXISTS " \
              f"`alesc.sqlite`.`type_logements` ( `idtype` INT NOT NULL, `nom` VARCHAR(45) NULL, PRIMARY KEY (" \
              f"`idtype`)) ENGINE = InnoDB; CREATE TABLE IF NOT EXISTS `alesc.sqlite`.`logements` ( `idlogement` INT " \
              f"NOT NULL, `idlogeur` INT NULL, `idtype` INT NULL, `num_rue` INT NULL, `nom_rue` VARCHAR(45) NULL, " \
              f"`code_postal` INT NULL, `ville` VARCHAR(45) NULL, `labelisation` INT NULL, PRIMARY KEY (" \
              f"`idlogement`)) ENGINE = InnoDB; SET SQL_MODE=@OLD_SQL_MODE; SET " \
              f"FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS; SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS; "
    cursor.execute(request)
    connexion.commit()
    cursor.close()
    connexion.close()
    print("La connexion SQLite est fermée")