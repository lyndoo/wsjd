-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: wsjd
-- ------------------------------------------------------
-- Server version	8.0.12

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
-- Table structure for table `attach`
--

DROP TABLE IF EXISTS `attach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `attach` (
  `ser` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`ser`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='附件表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attach`
--

LOCK TABLES `attach` WRITE;
/*!40000 ALTER TABLE `attach` DISABLE KEYS */;
INSERT INTO `attach` VALUES (1,'2018-10-12\\4ad3af38-cdea-11e8-80c5-001a7dda7111.jpeg'),(2,'2018-10-12\\4ad45f02-cdea-11e8-a732-001a7dda7111.jpeg'),(3,'2018-10-12\\026b79f8-cdeb-11e8-9666-001a7dda7111.jpeg'),(4,'2018-10-12\\026c6492-cdeb-11e8-aa61-001a7dda7111.jpeg'),(5,'2018-10-12\\026dc3e8-cdeb-11e8-9ac0-001a7dda7111.jpeg'),(6,'2018-10-12\\0592ef54-cdeb-11e8-9c59-001a7dda7111.jpeg'),(7,'2018-10-12\\05943d36-cdeb-11e8-a005-001a7dda7111.jpeg'),(8,'2018-10-12\\05964ab6-cdeb-11e8-92bc-001a7dda7111.jpeg'),(9,'2018-10-12\\0a606b88-cdeb-11e8-bc8b-001a7dda7111.jpeg'),(10,'2018-10-12\\0a612eb4-cdeb-11e8-8813-001a7dda7111.jpeg'),(11,'2018-10-12\\0a62a1cc-cdeb-11e8-a5c4-001a7dda7111.jpeg'),(12,'2018-10-16\\a438b9c0-d0fe-11e8-927d-001a7dda7111.jpeg'),(13,'2018-10-16\\a4392ee4-d0fe-11e8-a326-001a7dda7111.jpeg');
/*!40000 ALTER TABLE `attach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `report` (
  `ser` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL COMMENT '举报标题',
  `content` text COMMENT '举报内容',
  `informer` varchar(50) DEFAULT NULL,
  `informerPhone` varchar(20) DEFAULT NULL,
  `informerAddress` varchar(256) DEFAULT NULL,
  `Attach` varchar(200) DEFAULT NULL,
  `Reply` text,
  `ReplyTime` datetime DEFAULT NULL,
  `IsReply` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`ser`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='在线投诉';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` VALUES (1,'3','3','3','3','3','1,2',NULL,NULL,0),(2,'3333','5555','6666','777','888','3,4,5',NULL,NULL,0),(3,'3333','5555','6666','777','888','6,7,8',NULL,NULL,0),(4,'3333','5555','6666','777','888','9,10,11',NULL,'2018-10-16 16:29:04',1),(5,'12','2','3','4','','',NULL,'2018-10-16 16:28:17',1),(6,'投诉某人又问题','作风有问题','王小二','55568898','未知','12,13',NULL,NULL,0);
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-16 16:34:05
