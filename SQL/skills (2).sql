-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 20, 2023 at 10:54 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `skills_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `skills`
--

CREATE TABLE `skills` (
  `Skill_Name` text NOT NULL,
  `Skill_ID` int(10) NOT NULL,
  `Skill_Type` text NOT NULL,
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `skills`
--

INSERT INTO `skills` (`Skill_Name`, `Skill_ID`, `Skill_Type`, `ID`) VALUES
('Leadership', 1, 'Soft skills', 1),
('Python', 2, 'Technical skills', 2),
('C_Programming', 3, 'Technical skills', 201),
('ARM_Interfacing', 4, 'Technical Skills', 103),
('Embedded Linux', 5, 'Technical Skills', 103),
('Machine Learning and AI', 6, 'Technical Skills', 302),
('Automotive Engineering', 7, 'Technical Skills', 101),
('LeaderShip', 9, 'Soft Skills', 101),
('Computer Vision', 10, 'Technical Skills', 2011),
('Problem Solving', 11, 'Soft Skills', 2011),
('ARM Interfacing', 12, 'Technical Skills', 201),
('Problem Solving', 13, 'Soft Skills', 201),
('Leadership', 14, 'Soft Skills', 2),
('C\\C++ Software Development', 15, 'Technical Skills', 2),
('Machine Learning', 16, 'Technical Skills', 2011),
('AUTOSAR', 18, 'Technical Skills', 101);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `skills`
--
ALTER TABLE `skills`
  ADD PRIMARY KEY (`Skill_ID`),
  ADD KEY `ID` (`ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `skills`
--
ALTER TABLE `skills`
  ADD CONSTRAINT `skills_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `employees` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
