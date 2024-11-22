<?php
/**
* The module helps to add whats app chat support on online store and turn visitors into customers.This helps to build relationship with customers,provide personalized service and increase in sales.
*
* NOTICE OF LICENSE
* 
* Each copy of the software must be used for only one production website, it may be used on additional
* test servers. You are not permitted to make copies of the software without first purchasing the
* appropriate additional licenses. This license does not grant any reseller privileges.
* 
* @author    Shahab
* @copyright 2007-2022 Shahab-FK Enterprises
* @license   Prestashop Commercial Module License
*/

class SfkwhatsappchatCore extends ObjectModel {

    public $sfk_sfkwhatsappchat_message;
    public $sfk_sfkwhatsappchat_number;
    public $sfk_dates;
    public $sfk_status;
    public $sfk_language;

    /**
     * @see ObjectModel::$definition
     */
    public static $definition = array('table' => 'sfkwhatsappchat', 'primary' => 'id_sfkwhatsappchat', 'multilang' => false, 'fields' =>
    array(
    'sfk_sfkwhatsappchat_message' => array('type' => self::TYPE_HTML, 'lang' => false, 'required' => false, 'size' => 5000),
    'sfk_sfkwhatsappchat_number' => array('type' => self::TYPE_STRING, 'lang' => false, 'validate' => 'isString', 'required' => true, 'size' => 500),
    'sfk_language' =>array('type' => self::TYPE_STRING, 'lang' => false, 'validate' => 'isString', 'required' => false, 'size' => 500),
    'sfk_status' =>array('type' => self::TYPE_INT, 'lang' => false, 'validate' => 'isInt', 'required' => false, 'size' => 500), 
    'sfk_dates' => array('type' => self::TYPE_DATE, 'lang' => false, 'validate' => 'isDateFormat', 'copy_post' => false)));

    public static function getSfkwhatsappchat($id_lang = null) {
        if (is_null($id_lang))
            $id_lang = Context::getContext()->language->id;
        $sfkwhatsappchat = new Collection('Sfkwhatsappchat', $id_lang);
        return $sfkwhatsappchat;
    }

    public function __construct($id = null, $id_lang = null, $id_shop = null) {
        parent::__construct($id, $id_lang, $id_shop);
        $this->image_dir = _PS_GENDERS_DIR_;
    }

}
