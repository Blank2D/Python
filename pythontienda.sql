-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 12-07-2022 a las 02:04:49
-- Versión del servidor: 5.7.33
-- Versión de PHP: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pythontienda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `description` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `stock` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `items`
--

INSERT INTO `items` (`id`, `name`, `description`, `stock`, `price`) VALUES
(1, 'Intel Core i5-12400', '2.5GHz Turbo 4.4GHz, Socket LGA 1700, 6-Core / 12-Threads', 15, 229990),
(2, 'Intel Core i3 10105', '3.7 GHz, Intel UHD Graphics 630, Socket 1200, Quad-Core', 10, 129990),
(3, 'Intel Core i3-10100F', '6M Cache, up to 4.30 GHz) LGA1200, Sin Graficos', 25, 89990),
(4, 'RTX 3080 XLR8', 'Uprising Epic-X RGB, 10GB, GDDR6X, PCI-e 4.0, 320-Bit, LHR', 2, 1199990),
(5, 'PNY GeForce RTX 3070', '8GB UPRISING Dual Fan LHR', 18, 749990),
(6, 'PNY GeForce RTX 3050', 'Uprising Dual, 8GB, 128-Bit, GDDR6, PCI-e 4.0, HDMI, DP', 28, 399990);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `items`
--
ALTER TABLE `items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
