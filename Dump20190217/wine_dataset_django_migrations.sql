CREATE DATABASE  IF NOT EXISTS `wine_dataset` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `wine_dataset`;
-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: wine_dataset
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-02-17 11:13:41.263743'),(2,'auth','0001_initial','2019-02-17 11:13:41.638973'),(3,'admin','0001_initial','2019-02-17 11:13:41.788204'),(4,'admin','0002_logentry_remove_auto_add','2019-02-17 11:13:41.801738'),(5,'admin','0003_logentry_add_action_flag_choices','2019-02-17 11:13:41.826162'),(6,'contenttypes','0002_remove_content_type_name','2019-02-17 11:13:41.906888'),(7,'auth','0002_alter_permission_name_max_length','2019-02-17 11:13:41.948087'),(8,'auth','0003_alter_user_email_max_length','2019-02-17 11:13:41.976817'),(9,'auth','0004_alter_user_username_opts','2019-02-17 11:13:41.990908'),(10,'auth','0005_alter_user_last_login_null','2019-02-17 11:13:42.031488'),(11,'auth','0006_require_contenttypes_0002','2019-02-17 11:13:42.037259'),(12,'auth','0007_alter_validators_add_error_messages','2019-02-17 11:13:42.048959'),(13,'auth','0008_alter_user_username_max_length','2019-02-17 11:13:42.101993'),(14,'auth','0009_alter_user_last_name_max_length','2019-02-17 11:13:42.154200'),(15,'sessions','0001_initial','2019-02-17 11:13:42.182355'),(16,'wineapp','0001_initial','2019-02-17 11:13:42.214570'),(17,'wineapp','0002_auto_20190217_0952','2019-02-17 11:13:42.259634'),(18,'wineapp','0003_auto_20190217_1046','2019-02-17 11:13:42.436990'),(19,'wineapp','0004_auto_20190217_1102','2019-02-17 11:13:42.500718'),(20,'wineapp','0005_auto_20190217_1113','2019-02-17 11:13:42.578116'),(21,'wineapp','0006_auto_20190217_1123','2019-02-17 11:23:39.704888');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-17 23:50:25
