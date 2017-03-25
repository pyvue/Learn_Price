/* 分隔符更改为 ; */
/* 连接到 127.0.0.1 （经由 MySQL (TCP/IP)），用户名 root，密码：No ... */
USE `goods_db`;

CREATE TABLE `goods_info` (
	`ID` INT(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT COMMENT '货物ID',
	`GoodsName` VARCHAR(50) NOT NULL COMMENT '货物名称' COLLATE 'utf8_bin',
	`Minivalence` DECIMAL(10,2) NOT NULL COMMENT '最低价',
	`MiddlePrice` DECIMAL(10,2) NOT NULL COMMENT '平均价',
	`HighestPrice` DECIMAL(10,2) NOT NULL COMMENT '最高价',
	`Specification` VARCHAR(10) NOT NULL COMMENT '规格' COLLATE 'utf8_bin',
	`Unit` VARCHAR(10) NULL DEFAULT NULL COMMENT '单位' COLLATE 'utf8_bin',
	`DataTime` DATE NULL DEFAULT NULL COMMENT '时间',
	PRIMARY KEY (`ID`) /*ID 作为主键*/
)
COMMENT='jichu biao '
COLLATE='utf8_bin'
ENGINE=MyISAM
AUTO_INCREMENT=4
;




INSERT INTO `goods_db`.`goods_info` (`GoodsName`, `Minivalence`, `MiddlePrice`, `HighestPrice`, `Specification`, `Unit`, `DataTime`) VALUES ('小白菜', '14.00', '12.13', '14.16', '普通', '斤', '2017-03-23');
SELECT LAST_INSERT_ID();
SELECT `ID`, `GoodsName`, `Minivalence`, `MiddlePrice`, `HighestPrice`, `Specification`, `Unit`, `DataTime` FROM `goods_db`.`goods_info` WHERE  `ID`=4;