-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 25-11-2013 a las 11:18:31
-- Versión del servidor: 5.5.31
-- Versión de PHP: 5.4.6-1ubuntu1.2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `b3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `weaponrecord`
--

CREATE TABLE IF NOT EXISTS `weaponrecord` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `client_id` int(100) NOT NULL,
  `knife` int(100) NOT NULL DEFAULT '0',
  `beretta` int(100) NOT NULL DEFAULT '0',
  `desert` int(100) NOT NULL DEFAULT '0',
  `spas` int(100) NOT NULL DEFAULT '0',
  `ump` int(100) NOT NULL DEFAULT '0',
  `mp5k` int(100) NOT NULL DEFAULT '0',
  `lr300` int(100) NOT NULL DEFAULT '0',
  `m4a1` int(100) NOT NULL DEFAULT '0',
  `ak` int(100) NOT NULL DEFAULT '0',
  `g36` int(100) NOT NULL DEFAULT '0',
  `sr8` int(100) NOT NULL DEFAULT '0',
  `psg` int(100) NOT NULL DEFAULT '0',
  `negev` int(100) NOT NULL DEFAULT '0',
  `hk` int(100) NOT NULL DEFAULT '0',
  `he` int(100) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1;
