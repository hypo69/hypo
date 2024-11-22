<?php

if (!defined('_PS_VERSION_')) {
    exit;
}

use PrestaShop\PrestaShop\Core\Module\WidgetInterface;
use PrestaShop\PrestaShop\Adapter\Category\CategoryProductSearchProvider;
use PrestaShop\PrestaShop\Adapter\Image\ImageRetriever;
use PrestaShop\PrestaShop\Adapter\Product\PriceFormatter;
use PrestaShop\PrestaShop\Core\Product\ProductListingPresenter;
use PrestaShop\PrestaShop\Adapter\Product\ProductColorsRetriever;
use PrestaShop\PrestaShop\Adapter\Translator;
use PrestaShop\PrestaShop\Adapter\LegacyContext;
use PrestaShop\PrestaShop\Core\Product\Search\ProductSearchContext;
use PrestaShop\PrestaShop\Core\Product\Search\ProductSearchQuery;
use PrestaShop\PrestaShop\Core\Product\Search\SortOrder;

class PosNewProducts extends Module implements WidgetInterface{
    private $token = '';
    private $_html = '';
    public static $sort_by = array(
        1 => array('id' =>1 , 'name' => 'Product Name'),
        2 => array('id' =>2 , 'name' => 'Price'),
        3 => array('id' =>3 , 'name' => 'Product ID'),       
        4 => array('id' =>4 , 'name' => 'Position'),
        5 => array('id' =>5 , 'name' => 'Date updated'),
        6 => array('id' =>6 , 'name' => 'Date added'),
    );

    public static $order_by = array(
        1 => array('id' =>1 , 'name' => 'Descending'),
        2 => array('id' =>2 , 'name' => 'Ascending'),
    );
    public function __construct() {
        $this->name         = 'posnewproducts';
        $this->tab          = 'front_office_features';
        $this->version      = '2.0';
        $this->author       = 'posthemes';
        $this->bootstrap    = true;
        $this->_html        = '';
        parent :: __construct();

        $this->displayName = $this->l('Pos New Products module');
        $this->description = $this->l('PosModules');

        $this->templateFile = 'module:posnewproducts/views/templates/hook/posnewproducts.tpl';
       
    }
    
    public function install() {
        Configuration::updateValue($this->name . '_limit', 12);
        Configuration::updateValue($this->name . '_row', 2);
        Configuration::updateValue($this->name . '_items', 6);
        Configuration::updateValue($this->name . '_speed', 1000); 
        Configuration::updateValue($this->name . '_auto', 0);
        Configuration::updateValue($this->name . '_pause', 3000);
        Configuration::updateValue($this->name . '_arrow', 1);
        Configuration::updateValue($this->name . '_pagi', 0);
		Configuration::updateValue($this->name . '_move', 1);
        Configuration::updateValue($this->name . '_per_lg', 4);
        Configuration::updateValue($this->name . '_per_md', 3);
        Configuration::updateValue($this->name . '_per_sm', 2);
        Configuration::updateValue($this->name . '_per_xs', 2);
        Configuration::updateValue($this->name . '_per_xxs', 1);
        Configuration::updateValue($this->name . '_sort', 6);
        Configuration::updateValue($this->name . '_order', 1);
        
        
        return parent :: install()
            && $this->registerHook('displayContainerbottom')
            && $this->registerHook('header')
            && $this->registerHook('addproduct')
            && $this->registerHook('updateproduct')
            && $this->registerHook('deleteproduct')
            && $this->registerHook('categoryUpdate')
            && $this->installFixtures();
    }
    protected function installFixtures()
    {
        $languages = Language::getLanguages(false);
        foreach ($languages as $lang){
            $this->installFixture((int)$lang['id_lang'], 'cms.jpg');
        }

        return true;
    }

    protected function installFixture($id_lang, $image = null)
    {   
        $values['posnewproducts_img'][(int)$id_lang] = $image;
        $values['posnewproducts_link'][(int)$id_lang] = '#';
        $values['posnewproducts_title'][(int)$id_lang] = 'New Arrivals';
		$values['posnewproducts_desc'][(int)$id_lang] = 'Add new products to weekly line up';
        Configuration::updateValue($this->name . '_title', $values['posnewproducts_title']);
		Configuration::updateValue($this->name . '_desc', $values['posnewproducts_desc']);  
        Configuration::updateValue($this->name . '_img', $values['posnewproducts_img']);
        Configuration::updateValue($this->name . '_link', $values['posnewproducts_link']);

    }
    
    public function uninstall() {
        $this->_clearCache('posnewproducts.tpl');

        Configuration::deleteByName($this->name . '_limit');
        Configuration::deleteByName($this->name . '_row');
        Configuration::deleteByName($this->name . '_items');
        Configuration::deleteByName($this->name . '_speed');
        Configuration::deleteByName($this->name . '_auto');
        Configuration::deleteByName($this->name . '_pause');
        Configuration::deleteByName($this->name . '_arrow');
        Configuration::deleteByName($this->name . '_pagi');
		Configuration::deleteByName($this->name . '_move');
        Configuration::deleteByName($this->name . '_per_lg');
        Configuration::deleteByName($this->name . '_per_md');
        Configuration::deleteByName($this->name . '_per_sm');
        Configuration::deleteByName($this->name . '_per_xs');
        Configuration::deleteByName($this->name . '_per_xxs');
        Configuration::deleteByName($this->name . '_sort');
        Configuration::deleteByName($this->name . '_order');
        Configuration::deleteByName($this->name . '_title');
		Configuration::deleteByName($this->name . '_desc');
        Configuration::deleteByName($this->name . '_img');
        
        return parent::uninstall();
    }

  
    public function psversion() {
        $version=_PS_VERSION_;
        $exp=$explode=explode(".",$version);
        return $exp[1];
    }
    
    private function postProcess() {
        if (Tools::isSubmit('submitposnewproducts'))
        {
            if($this->_postValidation()){
                $languages = Language::getLanguages(false);
                $values = array();
                $update_images_values = false;
                
                foreach ($languages as $lang){
                    if (isset($_FILES['posn_img_'.$lang['id_lang']])
                    && isset($_FILES['posn_img_'.$lang['id_lang']]['tmp_name'])
                    && !empty($_FILES['posn_img_'.$lang['id_lang']]['tmp_name']))
                    {
                        if ($error = ImageManager::validateUpload($_FILES['posn_img_'.$lang['id_lang']], 4000000))
                            return $error;
                        else
                        {
                            $ext = substr($_FILES['posn_img_'.$lang['id_lang']]['name'], strrpos($_FILES['posn_img_'.$lang['id_lang']]['name'], '.') + 1);
                            $file_name = md5($_FILES['posn_img_'.$lang['id_lang']]['name']).'.'.$ext;

                            if (!move_uploaded_file($_FILES['posn_img_'.$lang['id_lang']]['tmp_name'], dirname(__FILE__).DIRECTORY_SEPARATOR.'img'.DIRECTORY_SEPARATOR.$file_name))
                                return $this->displayError($this->l('An error occurred while attempting to upload the file.'));
                            else
                            {
                                if (Configuration::hasContext('posn_img', $lang['id_lang'], Shop::getContext())
                                    && Configuration::get('posn_img', $lang['id_lang']) != $file_name)
                                    @unlink(dirname(__FILE__).DIRECTORY_SEPARATOR.'img'.DIRECTORY_SEPARATOR.Configuration::get('posn_img', $lang['id_lang']));

                                $values[$this->name . '_img'][$lang['id_lang']] = $file_name;
                                
                            }
                        }

                        $update_images_values = true;
                    }
                    $values[$this->name . '_link'][$lang['id_lang']] = Tools::getValue('posn_link_'.$lang['id_lang']);
                    $values[$this->name . '_title'][$lang['id_lang']] = Tools::getValue('posn_title_'.$lang['id_lang']);
					$values[$this->name . '_desc'][$lang['id_lang']] = Tools::getValue('posn_desc_'.$lang['id_lang']);
                }
                if ($update_images_values)
                Configuration::updateValue($this->name . '_img', $values[$this->name . '_img']);
                Configuration::updateValue($this->name . '_link', $values[$this->name . '_link']);
                Configuration::updateValue($this->name . '_title', $values[$this->name . '_title']);
				Configuration::updateValue($this->name . '_desc', $values[$this->name . '_desc']);
                Configuration::updateValue($this->name . '_row', Tools::getValue('posn_row'));
                Configuration::updateValue($this->name . '_items', Tools::getValue('posn_items'));
                Configuration::updateValue($this->name . '_speed', Tools::getValue('posn_speed'));
                Configuration::updateValue($this->name . '_auto', Tools::getValue('posn_auto'));
                Configuration::updateValue($this->name . '_pause', Tools::getValue('posn_pause'));
                Configuration::updateValue($this->name . '_arrow', Tools::getValue('posn_arrow'));
                Configuration::updateValue($this->name . '_pagi', Tools::getValue('posn_pagi'));
                Configuration::updateValue($this->name . '_move', Tools::getValue('posn_move'));
                Configuration::updateValue($this->name . '_pausehover', Tools::getValue('posn_pausehover'));
                Configuration::updateValue($this->name . '_limit', Tools::getValue('posn_limit'));
                Configuration::updateValue($this->name . '_sort', Tools::getValue('posn_sort'));
                Configuration::updateValue($this->name . '_order', Tools::getValue('posn_order'));
                Configuration::updateValue($this->name . '_per_lg', Tools::getValue($this->name . '_per_lg'));
                Configuration::updateValue($this->name . '_per_md', Tools::getValue($this->name . '_per_md'));
                Configuration::updateValue($this->name . '_per_sm', Tools::getValue($this->name . '_per_sm'));
                Configuration::updateValue($this->name . '_per_xs', Tools::getValue($this->name . '_per_xs'));
                Configuration::updateValue($this->name . '_per_xxs', Tools::getValue($this->name . '_per_xxs'));
                
                
                return $this->displayConfirmation($this->l('The settings have been updated.'));
            }else{
                return $this->_html;
            }
        }
        
        return '';
    }
    
    public function getContent()
    {       
        return $this->postProcess().$this->renderForm();
    }

    protected function _postValidation()
    {
        $errors = array();
        if (Tools::isSubmit('submitposnewproducts'))
        {

            if (!Validate::isInt(Tools::getValue('posn_row')) || !Validate::isInt(Tools::getValue('posn_items')) ||
                !Validate::isInt(Tools::getValue('posn_speed')) || !Validate::isInt(Tools::getValue('posn_pause')) || !Validate::isInt(Tools::getValue('posn_limit'))
            )
                $errors[] = $this->l('Invalid values');
        } 
        /* Returns if validation is ok */
        if (count($errors))
        {
            $this->_html .= $this->displayError(implode('<br />', $errors));

            return false;
        }

        return true;
    }
    public function renderForm()
    {   
        $id_lang = (int) Context::getContext()->language->id;
        
            $fields_form[0]['form'] = array(
                'legend' => array(
                    'title' => $this->l('Module Settings'),
                    'icon' => 'icon-cogs'
                ),
                'input' => array(
                        array(
                            'type' => 'text',
                            'lang' => true,
                            'label' => $this->l('Module title'),
                            'name' => 'posn_title',
                            'desc' => $this->l('This title will be displayed on front-office.')
                        ),
						 array(
                            'type' => 'text',
                            'lang' => true,
                            'label' => $this->l('Module desc'),
                            'name' => 'posn_desc',
                            'desc' => $this->l('This desc will be displayed on front-office.')
                        ),
                       /*  array(
                            'type' => 'file_lang',
                            'label' => $this->l('Banner image'),
                            'name' => 'posn_img',
                            'desc' => $this->l('Upload an image for your banner. The recommended dimensions are 432px x 694px.'),
                            'lang' => true,
                        ),
                        array(
                            'type' => 'text',
                            'lang' => true,
                            'label' => $this->l('Banner Link'),
                            'name' => 'posn_link',
                            'desc' => $this->l('Enter the link associated to your banner. When clicking on the banner, the link opens in the same window.')
                        ),    */
                        array(
                            'type' => 'select',
                            'label' =>  $this->l('Sort by:'),
                            'name' => 'posn_sort',
                            'options' => array(
                                'query' => self::$sort_by,
                                'id' => 'id',
                                'name' => 'name',
                            ),
                            'validation' => 'isUnsignedInt',
                        ),
                        array(
                            'type' => 'select',
                            'label' =>  $this->l('Order by:'),
                            'name' => 'posn_order',
                            'options' => array(
                                'query' => self::$order_by,
                                'id' => 'id',
                                'name' => 'name',
                            ),
                            'validation' => 'isUnsignedInt',
                        ), 
                        array(
                            'type' => 'text',
                            'label' =>  $this->l('Products limit :'),
                            'name' => 'posn_limit',
                            'class' => 'fixed-width-sm',
                            'desc' =>  $this->l('Set the number of products which you would like to see displayed in this module'),
                        ),
                        
                        
                ),
                'submit' => array(
                    'title' => $this->l('Save'),
                )
            );
            $fields_form[1]['form'] = array(
                'legend' => array(
                    'title' => $this->l('Slider configurations'),
                    'icon' => 'icon-cogs'
                ),
                'input' => array(
                    array(
                            'type' => 'text',
                            'label' => $this->l('Rows'),
                            'name' => 'posn_row',
                            'class' => 'fixed-width-sm',
                            'desc' => $this->l('Number row products will be displayed.'),
                    ),
                    array(
                            'type' => 'text',
                            'label' => $this->l('Number of Items:'),
                            'name' => 'posn_items',
                            'class' => 'fixed-width-sm',
                            'desc' => $this->l('Show number of product visible.'),
                    ),
                    array(
                            'type' => 'text',
                            'label' => $this->l('slide speed:'),
                            'name' => 'posn_speed',
                            'class' => 'fixed-width-sm',
                            'suffix' => 'milliseconds',
                    ),
                    array(
                        'type' => 'switch',
                        'label' => $this->l('Auto play'),
                        'name' => 'posn_auto',
                        'class' => 'fixed-width-xs',
                        'desc' => $this->l('Default is 1000ms'),
                        'values' => array(
                            array(
                                'id' => 'active_on',
                                'value' => 1,
                                'label' => $this->l('Yes'),
                            ),
                            array(
                                'id' => 'active_off',
                                'value' => 0,
                                'label' => $this->l('No'),
                            ),
                        ),
                    ),
                    array(
                            'type' => 'text',
                            'label' => $this->l('Time auto'),
                            'name' => 'posn_pause',
                            'class' => 'fixed-width-sm',
                            'suffix' => 'milliseconds',
                            'desc' => $this->l('This field only is valuable when auto play function is enable. Default is 3000ms.'),
                    ),
                    array(
                        'type' => 'switch',
                        'label' => $this->l('Show Next/Back control:'),
                        'name' => 'posn_arrow',
                        'class' => 'fixed-width-xs',
                        'values' => array(
                            array(
                                'id' => 'active_on',
                                'value' => 1,
                                'label' => $this->l('Yes'),
                            ),
                            array(
                                'id' => 'active_off',
                                'value' => 0,
                                'label' => $this->l('No'),
                            ),
                        ),
                    ),
                    array(
                        'type' => 'switch',
                        'label' => $this->l('Show pagination control:'),
                        'name' => 'posn_pagi',
                        'class' => 'fixed-width-xs',
                        'desc' => $this->l(''),
                        'values' => array(
                            array(
                                'id' => 'active_on',
                                'value' => 1,
                                'label' => $this->l('Yes'),
                            ),
                            array(
                                'id' => 'active_off',
                                'value' => 0,
                                'label' => $this->l('No'),
                            ),
                        ),
                    ),
                    array(
                        'type' => 'radio',
                        'label' => $this->l('Scroll number:'),
                        'name' => 'posn_move',
                        'default_value' => 0,
                        'values' => array(
                            array(
                                'id' => 'posn_move_on',
                                'value' => 1,
                                'label' => $this->l('1 item')),
                            array(
                                'id' => 'posn_move_off',
                                'value' => 0,
                                'label' => $this->l('All visible items')),
                        ),
                        'validation' => 'isBool',
                    ),
                    array(
                        'type' => 'switch',
                        'label' => $this->l('Pause On Hover:'),
                        'name' => 'posn_pausehover',
                        'default_value' => 1,
                        'is_bool' => true,
                        'values' => array(
                            array(
                                'id' => 'active_on',
                                'value' => 1,
                                'label' => $this->l('Yes'),
                            ),
                            array(
                                'id' => 'active_off',
                                'value' => 0,
                                'label' => $this->l('No'),
                            ),
                        ),
                        'validation' => 'isBool',
                    ),
                    'pos_fp_pro' => array(
                        'type' => 'html',
                        'id' => 'pos_fp_pro',
                        'label'=> $this->l('Responsive:'),
                        'name' => '',
                    ),
                    
                ),
                'submit' => array(
                    'title' => $this->l('Save'),
                )       
            );
        $fields_form[1]['form']['input']['pos_fp_pro']['name'] = $this->BuildDropListGroup($this->findCateProPer());
        
        $helper = new HelperForm();
        $helper->show_toolbar = true;
        $helper->table = $this->table;
        $lang = new Language((int)Configuration::get('PS_LANG_DEFAULT'));
        $helper->module = $this;
        $helper->default_form_language = $lang->id;
        $helper->allow_employee_form_lang = Configuration::get('PS_BO_ALLOW_EMPLOYEE_FORM_LANG') ? Configuration::get('PS_BO_ALLOW_EMPLOYEE_FORM_LANG') : 0;
        $helper->identifier = $this->identifier;
        $helper->submit_action = 'submitposnewproducts';
        $helper->currentIndex = $this->context->link->getAdminLink('AdminModules', false).'&configure='.$this->name.'&tab_module='.$this->tab.'&module_name='.$this->name;
        $helper->token = Tools::getAdminTokenLite('AdminModules');
        $module = _PS_MODULE_DIR_ ;
        $helper->tpl_vars = array(
            'module' =>$module,
            'uri' => $this->getPathUri(),
            'fields_value' => $this->getConfigFieldsValues(),
            'languages' => $this->context->controller->getLanguages(),
            'id_language' => $this->context->language->id,
        );

        return $helper->generateForm($fields_form);
    }
    
    public function getConfigFieldsValues()
    {
        $languages = Language::getLanguages(false);
        $fields = array(
            'posn_row'        => Configuration::get($this->name . '_row'),
            'posn_items'      => Configuration::get($this->name . '_items'),
            'posn_speed'      => Configuration::get($this->name . '_speed'),
            'posn_auto'       => Configuration::get($this->name . '_auto'),
            'posn_pause'      => Configuration::get($this->name . '_pause'),
            'posn_arrow'      => Configuration::get($this->name . '_arrow'),
            'posn_pagi'       => Configuration::get($this->name . '_pagi'),
            'posn_move'       => Configuration::get($this->name . '_move'),
            'posn_pausehover' => Configuration::get($this->name . '_pausehover'),
            'posn_sort'       => Configuration::get($this->name . '_sort'),
            'posn_order'      => Configuration::get($this->name . '_order'),
            'posn_limit'      => Configuration::get($this->name . '_limit'),

        );
        
        
        foreach ($languages as $lang)
        {   
            $fields['posn_title'][$lang['id_lang']] = Tools::getValue('posnewproducts_title_'.$lang['id_lang'], Configuration::get($this->name . '_title', $lang['id_lang']));
			$fields['posn_desc'][$lang['id_lang']] = Tools::getValue('posnewproducts_desc_'.$lang['id_lang'], Configuration::get($this->name . '_desc', $lang['id_lang'])); 
            $fields['posn_img'][$lang['id_lang']] = Tools::getValue('posnewproducts_img_'.$lang['id_lang'], Configuration::get($this->name . '_img', $lang['id_lang']));
            $fields['posn_link'][$lang['id_lang']] = Tools::getValue('posnewproducts_link_'.$lang['id_lang'], Configuration::get($this->name . '_link', $lang['id_lang']));
        }
        return $fields;
    }

    public function hookHeader($params){
        $this->context->controller->addJS($this->_path.'js/posnewproducts.js');
    }
    
    protected function getProducts()
    {   
        $sortby = Configuration::get($this->name . '_sort');
        switch($sortby)
        {
            case 1:
            $sortby = 'name';
            break;
            case 2:
            $sortby = 'price';
            break;
            case 3:
            $sortby = 'id_product';
            break;
            case 4:
            $sortby = 'position';
            break;
            case 5:
            $sortby = 'date_upd';
            break;
            case 6:
            $sortby = 'date_add';
            break;
        }
        $orderby = Configuration::get($this->name . '_order');
        if($orderby == 1) {
            $orderby = 'DESC';
        } else {
            $orderby = 'ASC';
        };

        $newProducts = false;
		$limit = (int)Configuration::get($this->name . '_limit');
        if (Configuration::get('PS_NB_DAYS_NEW_PRODUCT')) {
            $newProducts = Product::getNewProducts(
                (int)$this->context->language->id,
                0,
                $limit,
                false,
                $sortby,
                $orderby

            );
        }
        $assembler = new ProductAssembler($this->context);

        $presenterFactory = new ProductPresenterFactory($this->context);
        $presentationSettings = $presenterFactory->getPresentationSettings();
        $presenter = new ProductListingPresenter(
            new ImageRetriever(
                $this->context->link
            ),
            $this->context->link,
            new PriceFormatter(),
            new ProductColorsRetriever(),
            $this->context->getTranslator()
        );

        $products_for_template = array();

        if (is_array($newProducts)) {
            foreach ($newProducts as $rawProduct) {
                $products_for_template[] = $presenter->present(
                    $presentationSettings,
                    $assembler->assembleProduct($rawProduct),
                    $this->context->language
                );
            }
        }

        return $products_for_template;
    }

    public function hookAddProduct($params)
    {
        $this->_clearCache('*');
    }

    public function hookUpdateProduct($params)
    {
        $this->_clearCache('*');
    }

    public function hookDeleteProduct($params)
    {
        $this->_clearCache('*');
    }

    public function hookCategoryUpdate($params)
    {
        $this->_clearCache('*');
    }

    public function _clearCache($template, $cache_id = null, $compile_id = null)
    {
        parent::_clearCache('posnewproducts.tpl', 'posnewproducts');
    }

    private function BuildDropListGroup($group)
    {
        if(!is_array($group) || !count($group))
            return false;

        $html = '<div class="row">';
        foreach($group AS $key => $k)
        {
             if($key==4)
                 $html .= '</div><div class="row">';

             $html .= '<div class="col-xs-4 col-sm-3">'.$k['label'].'</label>'.
             '<select name="'.$k['id'].'" 
             id="'.$k['id'].'" 
             class="'.(isset($k['class']) ? $k['class'] : 'fixed-width-md').'"'.
             (isset($k['onchange']) ? ' onchange="'.$k['onchange'].'"':'').' >';
            
            for ($i=1; $i < 7; $i++){
                $html .= '<option value="'.$i.'" '.(Configuration::get($k['id']) == $i ? ' selected="selected"':'').'>'.$i.'</option>';
            }
                                
            $html .= '</select></div>';
        }

        return $html.'</div>';
    }
    private function findCateProPer()
    {
        return array(
            array(
                'id' => 'posnewproducts_per_lg',
                'label' => $this->l('Desktops (<1200 pixels)'),
            ),            
			array(
                'id' => 'posnewproducts_per_md',
                'label' => $this->l('Tablets (<992 pixels)'),
            ),
            array(
                'id' => 'posnewproducts_per_sm',
                'label' => $this->l('Large Phones (<768 pixels)'),
            ),
            array(
                'id' => 'posnewproducts_per_xs',
                'label' => $this->l('Medium Phones (<576 pixels)'),
            ),
            array(
                'id' => 'posnewproducts_per_xxs',
                'label' => $this->l('Small phones (<360 pixels)'),
            ),
        );
    }
    public function renderWidget($hookName = null, array $configuration = [])
    {

            $variables = $this->getWidgetVariables($hookName, $configuration);

            if (empty($variables)) {
                return false;
            }

            $this->smarty->assign($variables);

        return $this->fetch($this->templateFile);
    }

    public function getWidgetVariables($hookName = null, array $configuration = [])
    {
        $products = $this->getProducts();
        $title = Configuration::get($this->name . '_title', $this->context->language->id);
		$desc = Configuration::get($this->name . '_desc', $this->context->language->id);
        $slider_options = array( 
            'rows' => (int)Configuration::get($this->name . '_row'),
            'number_item' => (int)Configuration::get($this->name . '_items'),
            'speed_slide' => (int)Configuration::get($this->name . '_speed'),
            'auto_play' => (int)Configuration::get($this->name . '_auto'),
            'auto_time' => (int)Configuration::get($this->name . '_pause'),
            'show_arrow' => (int)Configuration::get($this->name . '_arrow'),
            'show_pagination' => (int)Configuration::get($this->name . '_pagi'),
            'move' => (int)Configuration::get($this->name . '_move'),
            'pausehover' => (int)Configuration::get($this->name . '_pausehover'),
            'items_lg' => (int)Configuration::get($this->name . '_per_lg'), 
            'items_md' => (int)Configuration::get($this->name . '_per_md'), 
            'items_sm' => (int)Configuration::get($this->name . '_per_sm'), 
            'items_xs' => (int)Configuration::get($this->name . '_per_xs'), 
            'items_xxs' => (int)Configuration::get($this->name . '_per_xxs'),       
        );
		$imgname = Configuration::get($this->name . '_img', $this->context->language->id);

		if ($imgname && file_exists(_PS_MODULE_DIR_.$this->name.DIRECTORY_SEPARATOR.'img'.DIRECTORY_SEPARATOR.$imgname))
			$this->smarty->assign('banner_img', $this->context->link->protocol_content.Tools::getMediaServer($imgname).$this->_path.'img/'.$imgname);
			
        if (!empty($products)) {
            return array(
                'products' => $products,
                'title' => $title,
				'desc' => $desc,
                'slider_options' => $slider_options,
				'image_link' => Configuration::get($this->name . '_link', $this->context->language->id),		
            );
        }
        return false;
    }
}