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
  `knife` mediumint(8) NOT NULL DEFAULT '0',
  `beretta` mediumint(8) NOT NULL DEFAULT '0',
  `desert` mediumint(8) NOT NULL DEFAULT '0',
  `spas` mediumint(8) NOT NULL DEFAULT '0',
  `ump` mediumint(8) NOT NULL DEFAULT '0',
  `mp5k` mediumint(8) NOT NULL DEFAULT '0',
  `lr300` mediumint(8) NOT NULL DEFAULT '0',
  `m4a1` mediumint(8) NOT NULL DEFAULT '0',
  `ak` mediumint(8) NOT NULL DEFAULT '0',
  `g36` mediumint(8) NOT NULL DEFAULT '0',
  `sr8` mediumint(8) NOT NULL DEFAULT '0',
  `psg` mediumint(8) NOT NULL DEFAULT '0',
  `negev` mediumint(8) NOT NULL DEFAULT '0',
  `hk` mediumint(8) NOT NULL DEFAULT '0',
  `he` mediumint(8) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `weaponmaprecord`
--

CREATE TABLE IF NOT EXISTS `weaponmaprecord` (
  `id` mediumint(8) NOT NULL AUTO_INCREMENT,
  `map` varchar(32) NOT NULL,
  `client_id` int(100) NOT NULL,
  `weapon` varchar(32) NOT NULL,
  `kills` mediumint(8) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1;
