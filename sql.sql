-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : ven. 26 fév. 2021 à 07:26
-- Version du serveur :  8.0.23-0ubuntu0.20.04.1
-- Version de PHP : 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `weather`
--

-- --------------------------------------------------------

--
-- Structure de la table `clouds`
--

CREATE TABLE `clouds` (
  `id` int NOT NULL,
  `alls` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `coord`
--

CREATE TABLE `coord` (
  `id` int NOT NULL,
  `lon` int DEFAULT NULL,
  `lat` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `main`
--

CREATE TABLE `main` (
  `id` int NOT NULL,
  `temp` text,
  `feels_like` text,
  `temp_min` text,
  `temp_max` text,
  `pressure` text,
  `humidity` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `sys`
--

CREATE TABLE `sys` (
  `id` int NOT NULL,
  `type` int DEFAULT NULL,
  `country` text,
  `sunrise` int DEFAULT NULL,
  `sunset` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `weather`
--

CREATE TABLE `weather` (
  `id` int NOT NULL,
  `id_coord` int DEFAULT NULL,
  `id_weatherElement` int DEFAULT NULL,
  `base` text,
  `id_main` int DEFAULT NULL,
  `visibility` int DEFAULT NULL,
  `id_wind` int DEFAULT NULL,
  `id_clouds` int DEFAULT NULL,
  `dt` int DEFAULT NULL,
  `id_sys` int DEFAULT NULL,
  `timezone` int DEFAULT NULL,
  `name` text,
  `cod` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `weatherElement`
--

CREATE TABLE `weatherElement` (
  `id` int NOT NULL,
  `main` text,
  `description` text,
  `icon` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `wind`
--

CREATE TABLE `wind` (
  `id` int NOT NULL,
  `speed` int DEFAULT NULL,
  `deg` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `clouds`
--
ALTER TABLE `clouds`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `coord`
--
ALTER TABLE `coord`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `main`
--
ALTER TABLE `main`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `sys`
--
ALTER TABLE `sys`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `weather`
--
ALTER TABLE `weather`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_coord` (`id_coord`),
  ADD KEY `id_weatherElement` (`id_weatherElement`),
  ADD KEY `id_main` (`id_main`),
  ADD KEY `id_wind` (`id_wind`),
  ADD KEY `id_clouds` (`id_clouds`),
  ADD KEY `id_sys` (`id_sys`);

--
-- Index pour la table `weatherElement`
--
ALTER TABLE `weatherElement`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `wind`
--
ALTER TABLE `wind`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `clouds`
--
ALTER TABLE `clouds`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `coord`
--
ALTER TABLE `coord`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `main`
--
ALTER TABLE `main`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `sys`
--
ALTER TABLE `sys`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `weather`
--
ALTER TABLE `weather`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `wind`
--
ALTER TABLE `wind`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `weather`
--
ALTER TABLE `weather`
  ADD CONSTRAINT `weather_ibfk_1` FOREIGN KEY (`id_coord`) REFERENCES `coord` (`id`),
  ADD CONSTRAINT `weather_ibfk_2` FOREIGN KEY (`id_main`) REFERENCES `main` (`id`),
  ADD CONSTRAINT `weather_ibfk_3` FOREIGN KEY (`id_wind`) REFERENCES `wind` (`id`),
  ADD CONSTRAINT `weather_ibfk_4` FOREIGN KEY (`id_clouds`) REFERENCES `clouds` (`id`),
  ADD CONSTRAINT `weather_ibfk_5` FOREIGN KEY (`id_sys`) REFERENCES `sys` (`id`),
  ADD CONSTRAINT `weather_ibfk_6` FOREIGN KEY (`id_weatherElement`) REFERENCES `weatherElement` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
