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

if (!defined('_PS_VERSION_'))
    exit;
header('X-Frame-Options: GOFORIT'); 

if ( _PS_VERSION_ >= '1.7') {
    require_once _PS_MODULE_DIR_.'/sfkwhatsappchat/classes/Sfkwhatsappchat.php';
}

class Sfkwhatsappchat extends Module {

    public function __construct() {
        $this->bootstrap = true;
        $this->name = 'sfkwhatsappchat';
        $this->tab = 'administration';
        $this->version = '2.0.0';
        $this->author = 'Shahab';
        $this->module_key = '0996ec3edceb9e352b81faa5a814b34f';
        $this->author_address = '0xfd95542428628BB79Df5B6ACa966fbF3c7FdD948';
        parent::__construct();
        $this->displayName = $this->l('WhatsApp Chat Support.');
        $this->description = $this->l('The module helps to communicate with clients on your online store and turn visitors into customers.This helps to build relationship with customers,provide
personalized service and increase in sales.');
        $this->confirmUninstall = $this->l('Are you sure you want to remove this module?');
    }

    public function install() {
		
         // New Tab
        if (_PS_VERSION_ >= '1.7') {
            $parentTabID = Tab::getIdFromClassName('AdminAdmin');
            $tab = new Tab();
            $tab->active = 1;
            $tab->id_parent = $parentTabID;
        } else {
           // $parentTabID = Tab::getIdFromClassName('AdminAdmin');
            $tab = new Tab();
            $tab->active = 1;
            $tab->id_parent = 0;
        }
        $tab->class_name = "AdminSfkwhatsappchat"; 
        $tab->name = array();
        foreach (Language::getLanguages() as $lang){
                $tab->name[$lang['id_lang']] = "WhatsApp Chat Support";
        }
       // $tab->id_parent = $parentTabID;
        $tab->module = 'sfkwhatsappchat';
        $tab->add();
        if (Validate::isLoadedObject($tab))
                Configuration::updateValue('PS_SFKWHATSAPPCHAT_MODULE_IDTAB', (int)$tab->id);
        else
                return $this->_abortInstall($this->l('Unable to load the "AdminSfkwhatsappchat" tab'));
        
        Db::getInstance()->Execute('
                CREATE TABLE IF NOT EXISTS `' . _DB_PREFIX_ . 'sfkwhatsappchat` (
                    `id_sfkwhatsappchat` int(11) NOT NULL AUTO_INCREMENT,
                    `sfk_sfkwhatsappchat_number` varchar(500) DEFAULT NULL,
                    `sfk_sfkwhatsappchat_message` text DEFAULT NULL,
                    `sfk_language` varchar(500) DEFAULT NULL,
                    `sfk_dates` date DEFAULT NULL,
                    `sfk_status` int(11) DEFAULT 0,
                    `created_date` date DEFAULT NULL,
                    `active` int(11) DEFAULT 0,
                    `type` int(11) DEFAULT 0,
                    PRIMARY KEY (`id_sfkwhatsappchat`)
                ) ENGINE=' . _MYSQL_ENGINE_ . ' default CHARSET=utf8');
        Db::getInstance()->Execute('
                CREATE TABLE IF NOT EXISTS `' . _DB_PREFIX_ . 'sfkwhatsappchat_lang` (
                    `id_sfkwhatsappchat` int(10) unsigned NOT NULL,
                    `id_lang` int(10) unsigned NOT NULL,
                    PRIMARY KEY (`id_sfkwhatsappchat`,`id_lang`),
                    KEY `id_sfkwhatsappchat` (`id_sfkwhatsappchat`)
                ) ENGINE=' . _MYSQL_ENGINE_ . ' default CHARSET=utf8');
        
    if (parent::install()) {
        
        /* Register left column hook */
        $this->registerHook('displayFooter');

        Db::getInstance()->Execute('UPDATE `' . _DB_PREFIX_ . 'tab` SET module=NULL WHERE class_name="AdminSfkwhatsappchat" ');
        //Move class and controllers files - Permission required on Linux machine.
        Tools::copy(dirname(__FILE__) . DIRECTORY_SEPARATOR . '/controllers/admin/AdminSfkwhatsappchatController.php', _PS_ROOT_DIR_ . DIRECTORY_SEPARATOR . 'controllers' .
                DIRECTORY_SEPARATOR . 'admin' . DIRECTORY_SEPARATOR . 'AdminSfkwhatsappchatController.php');
        Tools::copy(dirname(__FILE__) . DIRECTORY_SEPARATOR . '/classes/Sfkwhatsappchat.php', _PS_ROOT_DIR_ . DIRECTORY_SEPARATOR . 'classes' .
                DIRECTORY_SEPARATOR . 'Sfkwhatsappchat.php');
        // Copy Images
        Tools::copy(dirname(__FILE__) . DIRECTORY_SEPARATOR . '/views/img/admin/tab-sfkwhatsappchat.gif', _PS_ROOT_DIR_ . DIRECTORY_SEPARATOR . 'img' .
                DIRECTORY_SEPARATOR . 'admin' . DIRECTORY_SEPARATOR . 'tab-sfkwhatsappchat.gif');
        Tools::copy(dirname(__FILE__) . DIRECTORY_SEPARATOR . '/views/img/admin/AdminSfkwhatsappchat.gif', _PS_ROOT_DIR_ . DIRECTORY_SEPARATOR . 'img' .
                DIRECTORY_SEPARATOR . 'admin' . DIRECTORY_SEPARATOR . 'AdminSfkwhatsappchat.gif');

        // Clear cache
        include_once(_PS_ROOT_DIR_.'/config/config.inc.php');
        include_once(_PS_ROOT_DIR_.'/init.php');
        Tools::clearSmartyCache();
        Tools::clearXMLCache();
        Media::clearCache();
        Tools::generateIndex();

        $get_url = Db::getInstance()->ExecuteS('SELECT domain,physical_uri FROM '._DB_PREFIX_.'shop_url ');
        $protocol = (isset($_SERVER['HTTPS']) ? "https" : "http") ;
        $site_url = "$protocol://".$get_url[0]['domain'].'/'.$get_url[0]['physical_uri'];
        $this->context->smarty->assign('SITEURL',$site_url);

        $to = "shahab.hrms@gmail.com";
        $subject = "Free Module Installed Successfully - WhatsApp Chat Support";

        $message = "
        <html>
        <head>
        <title>Free Module Installed Successfully - WhatsApp Chat Support</title>
        </head>
        <body>
        <p>Free Module Installed Successfully - WhatsApp Chat Support!</p>
        <table>
        <tr>
        <th>URL => $site_url </th>

        </tr>
        <tr>
        <td>Shahab (Zohaib)</td>

        </tr>
        </table>
        </body>
        </html>
        ";

        // Always set content-type when sending HTML email
        $headers = "MIME-Version: 1.0" . "\r\n";
        $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

        mail($to,$subject,$message,$headers);

        return true;
        
        } else
            return false;
        //return parent::install();
    }

    public function uninstall() {
        if ($id_tab = Tab::getIdFromClassName('AdminSfkwhatsappchat')) {
            $tab = new Tab((int) $id_tab);
            $tab->delete();
        }
        Db::getInstance()->Execute(' DROP TABLE IF EXISTS `' . _DB_PREFIX_ . 'sfkwhatsappchat`, `' . _DB_PREFIX_ . 'sfkwhatsappchat_lang`; ');
        return parent::uninstall();
    }

    public function showData()
    {
        $SFKNumber = NULL; 
        $SFKMessage = NULL;
        $id_lang = $this->context->language->id;

        $result      = Db::getInstance()->ExecuteS("SELECT * FROM "._DB_PREFIX_."sfkwhatsappchat WHERE sfk_status=1 AND FIND_IN_SET('".pSQL($id_lang)."', `sfk_language`)  LIMIT 0,1 ");
        foreach ($result as $row)
        {
            $SFKNumber = $row['sfk_sfkwhatsappchat_number'];
            $SFKMessage = $row['sfk_sfkwhatsappchat_message'];
        }	
        
        $this->context->smarty->assign('SFKNUMBER',$SFKNumber);
        $this->context->smarty->assign('SFKMESSAGE',rawurlencode($SFKMessage));
        
        $get_url     = Db::getInstance()->ExecuteS('SELECT domain,physical_uri FROM '._DB_PREFIX_.'shop_url ');
        $protocol = (isset($_SERVER['HTTPS']) ? "https" : "http") ;
        $image_url = "$protocol://".$get_url[0]['domain'].'/'.$get_url[0]['physical_uri']."modules/sfkwhatsappchat/views/img/whatsapp.png";

        $this->context->smarty->assign('SFKIMAGEPATH',$image_url);
        
        if (_PS_VERSION_ >= '1.7') {
            $this->context->smarty->assign('PS7_FLAG',"YES");
        } else {
            $this->context->smarty->assign('PS7_FLAG',"");
        }
        
        if(strstr(strtolower($_SERVER['HTTP_USER_AGENT']), 'mobile') || strstr(strtolower($_SERVER['HTTP_USER_AGENT']), 'android')) {
	    $this->context->smarty->assign('DEVICE',"api");
	} else {
	    $this->context->smarty->assign('DEVICE',"web");
	}
	
        return $this->display(__FILE__, './views/templates/front/sfkwhatsappchat.tpl');
    }
    
    public function hookDisplayFooter()
    {
        return $this->showData();
    }
	
    /**
    * Surcharge de la fonction de traduction sur PS 1.7 et supérieur.
    * La fonction globale ne fonctionne pas
    * @param type $string
    * @param type $class
    * @param type $addslashes
    * @param type $htmlentities
    * @return type
    */
    public function l($string, $class = null, $addslashes = false, $htmlentities = true)
    {
        if ( _PS_VERSION_ >= '1.7') {
            return Context::getContext()->getTranslator()->trans($string);
        } else {
            return parent::l($string, $class, $addslashes, $htmlentities);
        }
    }
}


?>
