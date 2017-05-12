CREATE SCHEMA `school` DEFAULT CHARACTER SET utf8 ;
use school;
CREATE TABLE `school`.`department` (
  `dept_name` VARCHAR(45) NOT NULL,
  `building` VARCHAR(45) NULL,
  `budget` INT(10) UNSIGNED NULL,
  PRIMARY KEY (`dept_name`));
  
CREATE TABLE `school`.`student` (
  `ID` INT(11) NOT NULL,
  `name` VARCHAR(45) NULL,
  `sex` CHAR(1) NULL,
  `age` INT(10) UNSIGNED NULL,
  `emotion_state` VARCHAR(45) NULL,
  `dept_name` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_student_1_idx` (`dept_name` ASC),
  CONSTRAINT `fk_student_1`
    FOREIGN KEY (`dept_name`)
    REFERENCES `school`.`department` (`dept_name`)
    ON DELETE SET NULL
    ON UPDATE CASCADE); 
 
 CREATE TABLE `school`.`exam` (
  `student_ID` INT(11) NOT NULL,
  `exam_Name` VARCHAR(45) NOT NULL,
  `grade` INT(10) UNSIGNED NULL,
  PRIMARY KEY (`student_ID`, `exam_Name`),
  CONSTRAINT `fk_exam_1`
    FOREIGN KEY (`student_ID`)
    REFERENCES `school`.`student` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

