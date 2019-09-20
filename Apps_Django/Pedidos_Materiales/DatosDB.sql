-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-09-2019 a las 06:37:11
-- Versión del servidor: 10.3.15-MariaDB
-- Versión de PHP: 7.1.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pedidossena`
--

--
-- Volcado de datos para la tabla `app_materiales_articulo`
--

INSERT INTO `app_materiales_articulo` (`codigo_articulo`, `nombre_articulo`, `fabricante`, `ficha_tecnica`, `valor`, `lote_articulo_r_id`, `tipo_elemento_r_id`, `unidad_metrica_r_id`) VALUES
('26111702', 'BATERIA', 'N/A', 'BATERIA RECARGABLE 9 V', 17000, 'Teleinformatica', 'Consumo', 4),
('32101622', 'MEMORIA USB', 'N/A', 'MEMORIAS USB DE 16 GIGAS', 8800, 'Teleinformatica', 'Consumo', 4),
('32131010', 'COMPONENTE ELECTRONICO', 'N/A', 'SENSOR ESCANER DE HUELLA DIGITAL', 172000, 'Teleinformatica', 'Consumo', 4),
('43202222', 'CABLE HDMI ', 'N/A', 'CABLE HDMI 1.4 MACHO/MACHO  ALTA VELOCIDAD HDMI LONGITUD 15MTS', 59000, 'Teleinformatica', 'Consumo', 4),
('44103105', 'CARTUCHO DE IMPRESIÓN', 'N/A', 'Cartucho Para Impresoras Inyección De Tinta  Canon MP250 Color', 194024, 'Teleinformatica', 'Consumo', 4),
('60121104', 'Papel', NULL, 'RESMA GRAMAJE 75 GRM TAMAÑO OFICIO', 9950, 'Papeleria', 'Consumo', 1);

--
-- Volcado de datos para la tabla `app_materiales_lote`
--

INSERT INTO `app_materiales_lote` (`nombre_lote`, `detalle_lote`) VALUES
('N/A', 'N/A'),
('Papeleria', 'Artículos que tiene que ver con la papelería.'),
('Teleinformatica', 'teleinformatica');

--
-- Volcado de datos para la tabla `app_materiales_tipo_elemento`
--

INSERT INTO `app_materiales_tipo_elemento` (`nombre_tipo_elemento`, `detalle_tipo_elemento`) VALUES
('Consumo', 'Este elemento es de consumo.'),
('N/A', 'N/A');

--
-- Volcado de datos para la tabla `app_materiales_unidad_metrica`
--

INSERT INTO `app_materiales_unidad_metrica` (`id`, `nombre_metrica`, `detalle_metrica`) VALUES
(1, 'Resma', 'Conjunto de veinte manos o quinientos pliegos de papel.'),
(2, 'Rollo', 'Rollo en metros'),
(3, 'N/A', 'N/A'),
(4, 'UNIDAD', 'Valor a 1');

--
-- Volcado de datos para la tabla `app_pedido_estados_pedido`
--

INSERT INTO `app_pedido_estados_pedido` (`estado_pedido`, `descripcion_estado`) VALUES
('Anulado', 'Se anulo el pedido.'),
('Aprobado', 'Se aprobó el pedido.'),
('Borrador', 'El pedido solo esta en borrador.'),
('Entregando', 'El pedido llego y está siendo entregado.'),
('Enviado', 'Se envió el pedido.'),
('Rechazado', 'Se Rechazo el pedido.');

--
-- Volcado de datos para la tabla `app_pedido_guia_pedido`
--

INSERT INTO `app_pedido_guia_pedido` (`checkpoint`, `fecha_novedad`, `nota_pedido`, `area_pedido_r_id`, `estado_r_id`, `responsable_r_id`, `rol_pedido_r_id`) VALUES
(7, '2019-09-11', 'N/A', 1, 'Entregando', 6, 6),
(8, '2019-09-12', 'N/A', 1, 'Entregando', 6, 6);

--
-- Volcado de datos para la tabla `app_pedido_pedido`
--

INSERT INTO `app_pedido_pedido` (`codigo_pedido`, `fecha_pedido`, `cantidad_requerida`, `codigo_articulo_r_id`, `pedido_guia_r_id`, `responsable_r_id`, `existencias`) VALUES
(18, '2019-09-11', 10, '60121104', 7, 6, 5),
(19, '2019-09-12', 100, '26111702', 8, 6, 13),
(20, '2019-09-12', 100, '32101622', 8, 6, 10),
(21, '2019-09-12', 100, '32131010', 8, 6, 21),
(22, '2019-09-12', 100, '43202222', 8, 6, 49),
(23, '2019-09-12', 100, '44103105', 8, 6, 41),
(24, '2019-09-12', 100, '60121104', 8, 6, 23);

--
-- Volcado de datos para la tabla `app_usuarios_area`
--

INSERT INTO `app_usuarios_area` (`codigo_area`, `nombre_area`, `descripcion_area`) VALUES
(1, 'Teleinformática', ''),
(2, 'Mecanica', ''),
(3, 'Electricidad', ''),
(4, 'Construcción', ''),
(5, 'Confección', ''),
(6, 'Soldadura', ''),
(7, 'Automotriz', ''),
(8, 'Refrigeración', ''),
(9, 'Administración', 'Esta area es la encargada de toda la parte administrativa del sena.');

--
-- Volcado de datos para la tabla `app_usuarios_rol_usuario`
--

INSERT INTO `app_usuarios_rol_usuario` (`codigo_rol`, `nombre_rol`, `descripcion_rol`) VALUES
(1, 'Instructor', 'Es el encargado de llenar el pedido.'),
(2, 'Gestor de área', 'Es el encargado de gestionar algún área en concreto, fichas técnicas, fichas información, programas de formación,  proyectos formativos.'),
(3, 'Coordinador académico', 'Es el encargado de verificar lo que pidió el instructor con el proyecto formativo.'),
(4, 'Coordinador misional', 'Es el encargado de verificar con precios lo pedido por el instructor y lo aprobado por el coordinador académico.'),
(5, 'Subdirector', 'Es el encargado de aprobar lo pedido y lo aprobado por el coordinador misional. El subdirector aprueba por lotes.'),
(6, 'Almacenista', 'Es el encargado de verificar lo pedido por el instructor y con una lista de chequeo suministrar los materiales que haya en el almacén al instructor.'),
(7, 'Administrador', 'Es el encargado de que todo funcione correctamente.');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
