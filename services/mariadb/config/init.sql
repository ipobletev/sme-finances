CREATE DATABASE IF NOT EXISTS sda_nucleus;
USE sda_nucleus;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Estructura de tabla para la tabla sda_iotdata
--
CREATE TABLE sda_iotdata (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `_msgid` VARCHAR(255),
  main_data json default null,
  created_at timestamp NOT NULL DEFAULT current_timestamp(),
  send_status tinyint NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;