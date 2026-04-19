db (Jamaica & johnny jonard)
studentsystem_db.sql

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- ----------------------------
-- DATABASE
-- ----------------------------
CREATE DATABASE IF NOT EXISTS `studentsystem`;
USE `studentsystem`;

-- ----------------------------
-- TABLE STRUCTURE
-- ----------------------------
CREATE TABLE `studentsystem_db` (
  `student_id` VARCHAR(50) NOT NULL,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `gender` VARCHAR(30) NOT NULL,
  `birthdate` DATE NOT NULL,
  `address` VARCHAR(100) NOT NULL,
  `contact_number` VARCHAR(50) NOT NULL,
  `course_id` VARCHAR(50) NOT NULL,
  `course_name` VARCHAR(100) NOT NULL,
  `course_code` VARCHAR(50) NOT NULL,
  `enrollment_id` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- SAMPLE DATA (FOR TESTING)
-- ----------------------------
INSERT INTO `studentsystem_db` (
  `student_id`,
  `first_name`,
  `last_name`,
  `gender`,
  `birthdate`,
  `address`,
  `contact_number`,
  `course_id`,
  `course_name`,
  `course_code`,
  `enrollment_id`
) VALUES
('2026-001', 'Juan', 'Dela Cruz', 'Male', '2005-01-01', 'Cagayan', '09123456789', 'BSIT-01', 'BS Information Technology', 'BSIT', 'ENR-001'),
('2026-002', 'Maria', 'Santos', 'Female', '2004-05-12', 'Tuguegarao', '09987654321', 'BSCS-01', 'Computer Science', 'BSCS', 'ENR-002');

COMMIT;# student-info-system
