<?php
/**
* 2022 Codisto
*
* NOTICE OF LICENSE
*
* This source file is subject to the 3-Clause BSD License
* that is bundled with this package in the file LICENSE.txt.
* It is also available through the world-wide-web at this URL:
* https://opensource.org/licenses/BSD-3-Clause
* If you did not receive a copy of the license and are unable to
* obtain it through the world-wide-web, please send an email
* to support@codisto.com so we can send you a copy immediately.
*
* DISCLAIMER
*
* Do not edit or add to this file if you wish to upgrade Codisto to newer
* versions in the future. If you wish to customize Codisto for your
* needs please refer to https://codisto.com for more information.
*
*  @author    Codisto <support@codisto.com>
*  @copyright 2022 Codisto
*  @license   https://opensource.org/licenses/BSD-3-Clause 3-Clause BSD License
*  Property of Codisto
*/
$sql = [];
$sql[_DB_PREFIX_ . 'codisto_order_meta'] = 'CREATE TABLE IF NOT EXISTS `' . _DB_PREFIX_ . 'codisto_order_meta` (
	`id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
	`id_order` bigint UNSIGNED NOT NULL DEFAULT 0,
	`key` varchar(32) DEFAULT NULL,
	`value` text,
	PRIMARY KEY (`id`)
	) ENGINE=' . _MYSQL_ENGINE_ . ' DEFAULT CHARSET=utf8mb4;';

return $sql;