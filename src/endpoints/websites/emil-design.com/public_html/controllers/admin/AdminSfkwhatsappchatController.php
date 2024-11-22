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

class AdminSfkwhatsappchatControllerCore extends AdminController {

    public function __construct() 
    {
        $this->bootstrap = true;
        $this->table = 'sfkwhatsappchat';
        $this->className = 'Sfkwhatsappchat';
        $this->lang = false;
        $this->addRowAction('edit');
        $this->addRowAction('delete');
        $this->context = Context::getContext();
        if (!Tools::getValue('realedit'))
            $this->deleted = false;
        $this->bulk_actions = array(
            'delete' => array(
                'text' => $this->l('Delete selected'),
                'confirm' => $this->l('Delete selected items?')
            )
        );
        $this->fields_list = array(
            'id_sfkwhatsappchat' => array(
                'title' => $this->l('Sr. No.'),
                'align' => 'left',
                'width' => 'auto'
            ),
            'sfk_sfkwhatsappchat_number' =>
            array(
                'title' => $this->l('Whats App Number'), 'filter_key' => 'sfk_sfkwhatsappchat_number', 'align' => 'left', 'width' => 'auto'),
            'sfk_dates' => array('title' => $this->l('Date'), 'filter_key' => 'sfk_dates', 'align' => 'left', 'width' => 'auto')
        );
        
        if(!$this->ajax && !isset($this->display)){
            $this->context->smarty->assign(array(
                'modules_dir' => _MODULE_DIR_
            ));
            $this->content .= $this->context->smarty->fetch(_PS_MODULE_DIR_.'sfkwhatsappchat/views/templates/admin/sfkwhatsappchat.tpl');
        }
        
        parent::__construct();
    }

    public function renderForm() 
    {
        $languages = Db::getInstance()->executeS('SELECT * FROM '._DB_PREFIX_.'lang WHERE active=1 ');
        
		if (_PS_VERSION_ < '1.6') {
            $type = 'radio' ;
        } else {
            $type = 'switch' ;
        }
		
        $this->fields_form = array(
            'legend' => array(
                'title' => $this->l('WhatsApp Chat Support Management'),
                'image' => '../img/admin/tab-sfkwhatsappchat.gif'
            ),
            'input' => array
                (
                array(
                    'type' => 'text',
                    'label' => $this->l('Whats App Mobile Number:'),
                    'name' => 'sfk_sfkwhatsappchat_number',
                    'lang' => false,
                    'size' => 33,
                    'required' => true,
                    'desc' => $this->l('The format to enter whats app number is "plus sign country code mobile number".For Example +918805967041.')
                ),
                array(
                    'type' => 'textarea',
                    'label' => $this->l('Whats App Message from Chat:'),
                    'name' => 'sfk_sfkwhatsappchat_message',
                    'lang' => false,
                    'cols' => 50,
                    'rows' => 10,
                    'required' => true,
                    'desc' => $this->l('The message support person receive when customer try to communicate.')
                ),
                array(
                    'type' => 'select',
                    'label' => $this->l('Choose Language'),
                    'name' => 'sfk_language[]',
                    'required' => false,
                    'multiple' => true,
                    'expanded' => true,
                    'desc' => $this->l('Chat widget will be shown only on selected languages on front-office.'),
                    'options' => array(
                    'query' => $languages,
                        'id' => 'id_lang',
                        'name' => 'name'
                    )
                ),
                array(
                    'type' => "$type",
                    'label' => $this->l('Active:'),
                    'name' => 'sfk_status',
                    'is_bool' => true,
                    'values' => array(
                    array(
                        'id' => 'sfk_status_on',
                        'value' => 1,
                        'label' => $this->l('Yes')
                    ),
                    array(
                        'id' => 'sfk_status_off',
                        'value' => 0,
                        'label' => $this->l('No')
                    )
                ),
                    'required' => false,
                    'desc' => $this->l('Active or Inactive record status.')
                ),
                array(
                    'type' => 'date',
                    'label' => $this->l('Date:'),
                    'name' => 'sfk_dates',
                    'size' => 20,
                    'search' => false,
                    'desc' => $this->l('The date added or updated.')
                ),
            ),
            'submit' => array(
                'title' => $this->l('Save'),
                'class' => 'btn btn-default'
            )
        );
        
        if(isset($_REQUEST['id_sfkwhatsappchat']))
        {
            $id_sfkwhatsappchat = (trim($_REQUEST['id_sfkwhatsappchat']));
        }

        if(!empty($id_sfkwhatsappchat)) 
        {
            $sfk_language = Db::getInstance()->getValue('SELECT sfk_language FROM '._DB_PREFIX_.'sfkwhatsappchat WHERE 
            id_sfkwhatsappchat='.pSQL($id_sfkwhatsappchat).' ');
            
            $this->fields_value['sfk_language[]'] = explode(',',$sfk_language); 
        }	
        
        return parent::renderForm();
    }
    
    public function postProcess()
    {
        $multiple_languages = array();
        $multiple_languages = Tools::getValue('sfk_language');
        
        $_POST['sfk_language'] = implode(',',(array)$multiple_languages);
        
        parent::postProcess();
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
        if (_PS_VERSION_ >= '1.7') {
            return Context::getContext()->getTranslator()->trans($string);
        } else {
            return parent::l($string, $class, $addslashes, $htmlentities);
        }
    }
    

}
