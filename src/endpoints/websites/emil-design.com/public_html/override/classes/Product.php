<?php
defined('_PS_VERSION_') or die;
class Product extends ProductCore
{
    /** @var string Long Name */
    public $delivery_additional_message;
    public $affiliate_short_link;
    public $affiliate_text;
    public $affiliate_summary;
    public $affiliate_summary_2;
    public $affiliate_image_small;
    public $affiliate_image_medium;
    public $affiliate_image_large;
    public $ingredients;
    public $how_to_use;
    public $specification;
    public $link_to_video;


    public function __construct($id_product = null, $full = false, $id_lang = null, $id_shop = null, Context $context = null)
    {
        self::$definition['fields']['delivery_additional_message'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['affiliate_short_link'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['affiliate_text'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['affiliate_summary'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['affiliate_summary_2'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        
        self::$definition['fields']['affiliate_image_small'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['affiliate_image_medium'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['affiliate_image_large'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['ingredients'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['how_to_use'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['specification'] = array('type' => self::TYPE_HTML, 'lang' => true, 'validate' => 'isString', 'required' => false, 'size' => 4096);
        self::$definition['fields']['link_to_video'] = array('type' => self::TYPE_STRING, 'validate' => 'isString', 'required' => false, 'size' => 256);
 
        parent::__construct($id_product, $full, $id_lang, $id_shop, $context);
    }
}
