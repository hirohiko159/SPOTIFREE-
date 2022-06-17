-- MariaDB dump 10.19  Distrib 10.5.13-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: SPOTIFREE
-- ------------------------------------------------------
-- Server version	10.5.13-MariaDB-0ubuntu0.21.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `musique`
--

DROP TABLE IF EXISTS `musique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `musique` (
  `id` int(11) NOT NULL,
  `nom_musique` text DEFAULT NULL,
  `nom_artiste` text DEFAULT NULL,
  `album` text DEFAULT NULL,
  `chemin_fichier` text DEFAULT NULL,
  `annee_sortie` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musique`
--

LOCK TABLES `musique` WRITE;
/*!40000 ALTER TABLE `musique` DISABLE KEYS */;
INSERT INTO `musique` VALUES (1,'\'Arctic Monkeys - Do I Wanna Know (Official Video).mp3\'','Arctic Monkeys','AM','/home/thomas/Téléchargements/\'Arctic Monkeys - Do I Wanna Know (Official Video).mp3\'',2013),(2,'\'Guts - Come Closer (Official Audio).mp3\'','Guts','Paradise for All','/home/thomas/Téléchargements/\'Guts - Come Closer (Official Audio).mp3\'',2011),(3,'\'Kutiman - Mix Tel Aviv.mp3\'','Kutiman','Mix Tel Aviv','/home/thomas/Téléchargements/\'Kutiman - Mix Tel Aviv.mp3\'',2015),(4,'\'Kutiman - Tanzania.mp3\'','Kutiman','Wachaga','/home/thomas/Téléchargements/\'Kutiman - Tanzania.mp3\'',2020),(5,'\'Metronomy - The Look (Official Video).mp3\'','Metronomy','Nova Tunes','/home/thomas/Téléchargements/\'Metronomy - The Look (Official Video).mp3\'',2011),(6,'\'Naâman - Outta Road (Clip Officiel).mp3\'','Naâman','Rays of Resistance','/home/thomas/Téléchargements/\'Naâman - Outta Road (Clip Officiel).mp3\'',2015),(7,'\'VANUPIÉ - ROCKADOWN - SUBWAY SESSION (FEAT. LIDIOP).mp3\'','VANUPIÉ','Rockadown Subway Session','/home/thomas/Téléchargements/\'VANUPIÉ - ROCKADOWN - SUBWAY SESSION (FEAT. LIDIOP).mp3\'',2017);
/*!40000 ALTER TABLE `musique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `musiques_playlist`
--

DROP TABLE IF EXISTS `musiques_playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `musiques_playlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom_playlist` text DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  `id_musique` int(11) DEFAULT NULL,
  `authorized_users` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_user` (`id_user`),
  KEY `id_musique` (`id_musique`),
  CONSTRAINT `musiques_playlist_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`),
  CONSTRAINT `musiques_playlist_ibfk_2` FOREIGN KEY (`id_musique`) REFERENCES `musique` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musiques_playlist`
--

LOCK TABLES `musiques_playlist` WRITE;
/*!40000 ALTER TABLE `musiques_playlist` DISABLE KEYS */;
INSERT INTO `musiques_playlist` VALUES (2,'test_toto',2,1,NULL),(12,'ma_premiere_playlist',1,4,NULL),(15,'nouvelle_playlist',1,2,NULL);
/*!40000 ALTER TABLE `musiques_playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `nom_user` text DEFAULT NULL,
  `pwd` text DEFAULT NULL,
  `liste_amis` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'formation','formation','tartuffe:sdfnkskfk'),(2,'toto','toto',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-17 14:32:34
