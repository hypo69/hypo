<?php
/*
* 2007-2015 PrestaShop
*
* NOTICE OF LICENSE
*
* This source file is subject to the Academic Free License (AFL 3.0)
* that is bundled with this package in the file LICENSE.txt.
* It is also available through the world-wide-web at this URL:
* http://opensource.org/licenses/afl-3.0.php
* If you did not receive a copy of the license and are unable to
* obtain it through the world-wide-web, please send an email
* to license@prestashop.com so we can send you a copy immediately.
*
* DISCLAIMER
*
* Do not edit or add to this file if you wish to upgrade PrestaShop to newer
* versions in the future. If you wish to customize PrestaShop for your
* needs please refer to http://www.prestashop.com for more information.
*
*  @author PrestaShop SA <contact@prestashop.com>
*  @copyright  2007-2015 PrestaShop SA

*  @license    http://opensource.org/licenses/afl-3.0.php  Academic Free License (AFL 3.0)
*  International Registered Trademark & Property of PrestaShop SA
*/

if (!defined('_PS_VERSION_')) {
    exit;
}

use PrestaShop\PrestaShop\Core\Module\WidgetInterface;


class PosThemeoptions extends Module implements WidgetInterface
{
    // Equivalent module on PrestaShop 1.6, sharing the same data

    public static $text_transform = array(
        1 => array('id' =>1 , 'name' => 'None'),
        2 => array('id' =>2 , 'name' => 'Capitalize'),
        3 => array('id' =>3 , 'name' => 'UPPERCASE'),
    );
    public static $product_row = array(
        1 => array('id' =>1 , 'name' => '3'),
        2 => array('id' =>2 , 'name' => '4'),
        3 => array('id' =>3 , 'name' => '5'),
    );
    public $fields_arr_path = '/data/fields_array.php';
    private $_html;
	private $version_compared;
    private $templateFile;

    public function __construct()
    {
        $this->name = 'posthemeoptions';
        $this->author = 'Posthemes';
        $this->version = '1.0.0';
        $this->need_instance = 0;

        $this->bootstrap = true;
        parent::__construct();

        Shop::addTableAssociation('info', array('type' => 'shop'));

        $this->displayName = $this->trans('Pos Themeoptions', array(), 'Modules.Customtext.Admin');
        $this->description = $this->trans('Theme editor', array(), 'Modules.Customtext.Admin');

        $this->ps_versions_compliancy = array('min' => '1.7.0.0', 'max' => _PS_VERSION_);

        if (version_compare(_PS_VERSION_, '1.7.8.0', '<')) {
            $this->version_compared = false;
        }else{
            $this->version_compared = true;
        }
    }

    public function install()
    {
		$this->createHooks();
        //General
        Configuration::updateValue($this->name . 'g_main_color', '#ef1e1e');
        Configuration::updateValue($this->name . 'g_body_gfont_url', 'https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i&display=swap&subset=cyrillic,cyrillic-ext,greek,greek-ext,latin-ext,vietnamese');
        Configuration::updateValue($this->name . 'g_body_gfont_name', '"Open Sans", sans-serif');
        Configuration::updateValue($this->name . 'g_body_font_size', 14);
        Configuration::updateValue($this->name . 'g_body_font_color', '#666666');
        // Configuration::updateValue($this->name . 'g_a_color', '#555555');
        // Configuration::updateValue($this->name . 'g_a_colorh', '#ef1e1e');
        Configuration::updateValue($this->name . 'g_title_gfont_url', 'https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i&display=swap&subset=cyrillic,cyrillic-ext,greek,greek-ext,latin-ext,vietnamese');
        Configuration::updateValue($this->name . 'g_title_gfont_name', '"Open Sans", sans-serif');
        Configuration::updateValue($this->name . 'g_title_font_size', 24);
        Configuration::updateValue($this->name . 'g_title_font_color', '#253237');
        Configuration::updateValue($this->name . 'g_title_font_transform', 2);
        Configuration::updateValue($this->name . 'g_title_font_size_column', 20);
        // Configuration::updateValue($this->name . 'g_button_color', '#ffffff');
        // Configuration::updateValue($this->name . 'g_button_colorh', '#ffffff');
        // Configuration::updateValue($this->name . 'g_button_bgcolor', '#999999');
        // Configuration::updateValue($this->name . 'g_button_bgcolorh', '#ef1e1e');
        // Configuration::updateValue($this->name . 'g_footer_bg_color', '#222222');
        // Configuration::updateValue($this->name . 'g_footer_color', '#999999');
        // Configuration::updateValue($this->name . 'g_footer_a_color', '#999999');
        // Configuration::updateValue($this->name . 'g_footer_a_colorh', '#ef1e1e');
        // Product
        Configuration::updateValue($this->name . 'p_display', 1);
        Configuration::updateValue($this->name . 'p_name_color', '#253237');
        Configuration::updateValue($this->name . 'p_name_colorh', '#ef1e1e');
        Configuration::updateValue($this->name . 'p_name_size', 14);
        Configuration::updateValue($this->name . 'p_name_length', 0);
        Configuration::updateValue($this->name . 'p_name_transform', 2);
        Configuration::updateValue($this->name . 'p_price_color', '#555555');
        Configuration::updateValue($this->name . 'p_price_size', 15);
        // Category page
        Configuration::updateValue($this->name . 'cp_subcategories', 0);
        Configuration::updateValue($this->name . 'PS_PRODUCTS_PER_PAGE', 16);
        Configuration::updateValue($this->name . 'cp_perrow', 2);
        // Product page
        Configuration::updateValue($this->name . 'pp_thumbnail', 0);
        Configuration::updateValue($this->name . 'pp_name_color', '#253237');
        Configuration::updateValue($this->name . 'pp_name_size', 24);
        Configuration::updateValue($this->name . 'pp_name_transform', 2);
        Configuration::updateValue($this->name . 'pp_price_color', '#555555');
        Configuration::updateValue($this->name . 'pp_price_size', 22);
        Configuration::updateValue($this->name . 'pp_infortab', 0);

        return parent::install()
        && $this->registerHook('header');
    }
	public function createHooks(){
		$custom_hooks = array(
			1 => array(
				'name' => 'displayBannersequence',
				'title' => 'displayBannersequence',
				'description' => 'This is a Custom hook'
			),
			2 => array(
				'name' => 'displayNav',
				'title' => 'displayNav',
				'description' => 'This is a Custom hook'
			),
			3 => array(
				'name' => 'displayContainertop',
				'title' => 'displayContainertop',
				'description' => 'This is a Custom hook'
			),
			4 => array(
				'name' => 'displayContainertop2',
				'title' => 'displayContainertop2',
				'description' => 'This is a Custom hook'
			),
			5 => array(
				'name' => 'displayFulltop',
				'title' => 'displayFulltop',
				'description' => 'This is a Custom hook'
			),
			6 => array(
				'name' => 'displayFulltop2',
				'title' => 'displayFulltop2',
				'description' => 'This is a Custom hook'
			),
			7 => array(
				'name' => 'displayContainerbottom',
				'title' => 'displayContainerbottom',
				'description' => 'This is a Custom hook'
			),
			8 => array(
				'name' => 'displayContainerbottom2',
				'title' => 'displayContainerbottom2',
				'description' => 'This is a Custom hook'
			),
			9 => array(
				'name' => 'displayFullbottom',
				'title' => 'displayFullbottom',
				'description' => 'This is a Custom hook'
			),
			10 => array(
				'name' => 'displayFullbottom2',
				'title' => 'displayFullbottom2',
				'description' => 'This is a Custom hook'
			),
		);

		$hook = new Hook();

		foreach($custom_hooks as $custom_hook){
			if($hook->getIdByName($custom_hook['name'])) continue; 

			$hook->name = $custom_hook['name'];
			$hook->title = $custom_hook['title'];
			$hook->description = $custom_hook['description'];
			$hook->add();
		}

		return true;
	}
    public function uninstall()
    {
        return parent::uninstall();
    }


    public function getContent()
    {
        $this->context->controller->addCSS($this->_path.'views/css/back.css');
        $this->context->controller->addJS($this->_path.'views/js/back.js');
        
        $html = '';
        $multiple_arr = array();
        // START RENDER FIELDS
        $this->AllFields();
        // END RENDER FIELDS
        if(Tools::isSubmit('save'.$this->name)){
            foreach($this->fields_form as $key => $value){
                $multiple_arr = array_merge($multiple_arr,$value['form']['input']);
            }
            // START LANG
            $languages = Language::getLanguages(false);
            if(isset($multiple_arr) && !empty($multiple_arr)){
                foreach($multiple_arr as $mvalue){
                    if(isset($mvalue['lang']) && $mvalue['lang'] == true && isset($mvalue['name'])){
                       foreach($languages as $lang){
                        ${$mvalue['name'].'_lang'}[$lang['id_lang']] = Tools::getvalue($mvalue['name'].'_'.$lang['id_lang']);
                       }
                    }
                }
            }
            // END LANG
            if(isset($multiple_arr) && !empty($multiple_arr)){
                //echo '<pre>';print_r($multiple_arr);die;
                foreach($multiple_arr as $mvalue){
                    if(isset($mvalue['lang']) && $mvalue['lang'] == true && isset($mvalue['name'])){
                            Configuration::updateValue($this->name.$mvalue['name'],${$mvalue['name'].'_lang'});
                    }else{
                        if(isset($mvalue['name'])){
                            if($mvalue['name'] == 'PS_PRODUCTS_PER_PAGE'){
                                Configuration::updateValue('PS_PRODUCTS_PER_PAGE',Tools::getvalue($mvalue['name']));
                            }else{
                                Configuration::updateValue($this->name.$mvalue['name'],Tools::getvalue($mvalue['name']));
                            }
                        }
                    }
                }
            }
            $helper = $this->SettingForm();
            $html_form = $helper->generateForm($this->fields_form);
            $html .= $this->displayConfirmation($this->l('Successfully Saved All Fields Values.'));
            $html .= $html_form;
            $this->generateCss();
        }else{
            $helper = $this->SettingForm();
            $html_form = $helper->generateForm($this->fields_form);
            $html .= $html_form;
        }
        return $html;
    }
    public function SettingForm() {
        $languages = Language::getLanguages(false);
        $default_lang = (int) Configuration::get('PS_LANG_DEFAULT');
        $this->AllFields();
        $helper = new HelperForm();
        $helper->module = $this;
        $helper->name_controller = $this->name;
        $helper->token = Tools::getAdminTokenLite('AdminModules');
        $helper->currentIndex = AdminController::$currentIndex . '&configure=' . $this->name;
        foreach ($languages as $lang)
                $helper->languages[] = array(
                        'id_lang' => $lang['id_lang'],
                        'iso_code' => $lang['iso_code'],
                        'name' => $lang['name'],
                        'is_default' => ($default_lang == $lang['id_lang'] ? 1 : 0)
                );
        $helper->toolbar_btn = array(
            'save' =>
            array(
                'desc' => $this->l('Save'),
                'href' => AdminController::$currentIndex . '&configure=' . $this->name . '&save'.$this->name.'token=' . Tools::getAdminTokenLite('AdminModules'),
            )
        );
        $helper->default_form_language = $default_lang;
        $helper->allow_employee_form_lang = $default_lang;
        $helper->title = $this->displayName;
        $helper->show_toolbar = true;
        $helper->toolbar_scroll = true;
        $helper->submit_action = 'save'.$this->name;
        $multiple_arr = array();

        foreach($this->fields_form as $key => $value) {
            if(empty($multiple_arr)){
                if(isset($value['form']['input']) && !empty($value['form']['input'])){
                    $multiple_arr = $value['form']['input'];
                }
            }else{
                if(isset($value['form']['input']) && !empty($value['form']['input'])){
                    $multiple_arr = array_merge($multiple_arr,$value['form']['input']);
                }
            }
        }
        foreach($multiple_arr as $mvalue){
            if(isset($mvalue['lang']) && $mvalue['lang'] == true && isset($mvalue['name'])){
               foreach($languages as $lang){
                    $helper->fields_value[$mvalue['name']][$lang['id_lang']] = Configuration::get($this->name.$mvalue['name'],$lang['id_lang']);
               }
            }else{
                if(isset($mvalue['name'])){
                    if($mvalue['name'] == 'PS_PRODUCTS_PER_PAGE'){
                        $helper->fields_value[$mvalue['name']] = Configuration::get('PS_PRODUCTS_PER_PAGE');
                    }else{
                        $helper->fields_value[$mvalue['name']] = Configuration::get($this->name.$mvalue['name']);
                    }
                }
            }
        }
        return $helper;
    }

    public function AllFields()
    {
        $posthemeoption_settings = array();
        include_once(dirname(__FILE__).$this->fields_arr_path);
        if(isset($posthemeoption_settings) && !empty($posthemeoption_settings)){
            foreach ($posthemeoption_settings as $posthemeoption_setting) {
                $this->fields_form[]['form'] = $posthemeoption_setting;
            }
        }
        //echo '<pre>'; print_r($this->fields_form);die;
        return $this->fields_form;
    }

    public function getPath()
    {
        return $this->_path;
    }
    public function generateCss()
    {
        $css = '';
        $main_color = Configuration::get($this->name . 'g_main_color');
		$css .='
           a:hover,
			#_desktop_wishtlist .wishtlist_top a:hover,
			#_desktop_compare .compare_top a:hover,
			#_mobile_wishtlist .wishtlist_top a:hover,
			#_mobile_compare .compare_top a:hover,
			.selector-block .localiz_block:hover button, 
			.selector-block .localiz_block:hover .current-block,
			.selector-block .localiz_block .dropdown-menu li:hover .dropdown-item,
			.selector-block .localiz_block .dropdown-menu li.current .dropdown-item,
			.selector-mobile button:hover,.selector-mobile .dropdown-menu li a:hover,
			.selector-mobile .dropdown-menu li.current a:hover,
			#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-item.active  > a,
			#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-item.home  > a,
			#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-item:hover  > a,
			#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-dropdown .submenu-item > a:hover,
			#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-dropdown .submenu-item .category-sub-menu a:hover,
			#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-item .menu-dropdown.cat-drop-menu li a:hover,
			#_mobile_megamenu .pos-menu-horizontal .menu-item a:hover,
			#_mobile_megamenu  .pos-menu-horizontal .menu-item .icon-drop-mobile:hover i,
			#_desktop_vegamenu .pos-menu-vertical .menu-content .menu-item.active  > a,
			#_desktop_vegamenu .pos-menu-vertical .menu-content .menu-item:hover  > a,
			#_desktop_vegamenu .pos-menu-vertical .menu-content .menu-dropdown .submenu-item > a:hover,
			#_desktop_vegamenu .pos-menu-vertical .menu-content .menu-dropdown .submenu-item .category-sub-menu a:hover,
			#_desktop_vegamenu .pos-menu-vertical .menu-content .menu-item .menu-dropdown.cat-drop-menu li a:hover,
			#_mobile_vegamenu .pos-menu-vertical .menu-item a:hover,
			#_mobile_vegamenu  .pos-menu-vertical .menu-item .icon-drop-mobile:hover i,
			#_desktop_contact_link .contact-link a:hover,
			#_mobile_user_info .user-info-block .localiz_block:hover button i,
			.blockcart:hover .button_cart a.desktop, .blockcart:hover .button_cart a.mobile,
			.blockcart .popup_cart .price_content .price_inline.cart-total .value,
			.comments_advices a:hover,
			.block-categories .category-sub-menu li[data-depth="0"] > a:hover,
			.block-categories .collapse-icons .add:hover, 
			.block-categories .collapse-icons .remove:hover,
			.block-categories .category-sub-menu .category-sub-link:hover,
			.breadcrumb_container .breadcrumb ol li:last-child a, .breadcrumb_container .breadcrumb ol li:last-child span,
			.breadcrumb_container .breadcrumb ol li a:hover,
			.slideshow_container .pos-slideshow .nivo-directionNav a:hover,
			.poslistcategories .list-categories .desc-listcategoreis .sub a:hover,
			.poslistcategories .list-categories .desc-listcategoreis .view-more a:hover,
			.poslistcategories .list-categories .desc-listcategoreis .view-more a:after,
			.item-testimonials .item .content_test .des_inner:before,
			.js-product-miniature .product_desc .manufacturer a:hover,
			#_desktop_search_category .search-icon:hover,
			.product-price-and-shipping .price.price-sale,				
			.js-product-miniature.style_product_default .add-to-links li a:hover, 
			.js-product-miniature.style_product_default .add-to-links li.cart button.ajax_add_to_cart_button:hover, 
			.js-product-miniature.style_product_default .add-to-links li.cart span.ajax_add_to_cart_button:hover,
			.js-product-miniature.style_product1 .add-to-links li a:hover,	
			.js-product-miniature.style_product1 .add-to-links li.cart button.ajax_add_to_cart_button:hover,
			.js-product-miniature.style_product1 .add-to-links li.cart span.ajax_add_to_cart_button:hover,
			.js-product-miniature .product_desc .product_name:hover,
			.countdown-static .countdown-content .info .countdown-price,
			.tab-category-container-slider ul.tab_cates li:hover,
			.tab-category-container-slider ul.tab_cates li.active,
			.poslistcateproduct .subcategories-list li a:hover,
			.poslistcateproduct .btn-group .dropdown-menu a:hover,
			.home_blog_post_area .blog_slider .item .blog_post .post_title a:hover,
			.home_blog_post_area .blog_slider .item .blog_post:hover .post_content  .post_title a:hover,
			.meta_author span,.meta_category a,
			.home_blog_post_area .blog_slider .item .blog_post:hover .post_content  .read_more a:hover,
			.home_blog_post_area .blog_slider .item .blog_post .read_more a:after,
			.home_blog_post_area .blog_slider .item .blog_post:hover .post_content  .read_more a:hover:after,
			#footer a:hover,
			#footer .footer-container .footer_block .footer_list > li a:hover,
			#footer .footer-container .footer_block .footer_list > ul > li a:hover,
			.ui-widget-content a:hover,
			.product-images .slick-prev:hover:before, .product-images .slick-next:hover:before,	
			#js-product-list-top ul.display li:hover,#js-product-list-top ul.display li.selected,
			#search_filters_wrapper #search_filters .facet .facet-label:hover a,
			.js-product-miniature .product_desc .availability .availability-list span,
			.product-line-grid-right .cart-line-product-actions .remove-from-cart:hover, .product-line-grid-right .product-price .remove-from-cart:hover,
			.page-my-account #content .links a:hover i,
			.panel-product-line #wishlist_button:hover,
			.panel-product-line .compare-button:hover,.panel-product-line .compare-button.cmp_added,
			.social-sharing li a:hover{  
			color: '.$main_color.'; 
		}';
		$css .='
		#pos_search_top .form_search .search_submit ,
		.bottom_bg,.top_bg,.top-mobile,
		#_desktop_compare .compare_top a #poscompare-nb,
		#_desktop_wishtlist .wishtlist_top a .cart-wishlist-number,
		.js-product-miniature.style_product_default .quick-view a.quick_view:hover,
		.js-product-miniature.style_product2 .add-to-links li a:hover,
		.js-product-miniature.style_product3 .add-to-links li a:hover,
		.js-product-miniature.style_product2 .add-to-links li.cart button.ajax_add_to_cart_button:hover, 
		.js-product-miniature.style_product2 .add-to-links li.cart span.ajax_add_to_cart_button:hover,
		.js-product-miniature.style_product3 .add-to-links li.cart button.ajax_add_to_cart_button:hover, 
		.js-product-miniature.style_product3 .add-to-links li.cart span.ajax_add_to_cart_button:hover,
		.blockcart .popup_cart ul li .img_content .product-quantity,
		.blockcart .popup_cart .checkout a:hover,
		.blockcart .button_cart a.desktop .item_count,
		.blockcart .button_cart a.mobile .item_count,
		.desc_slideshow .readmore,
		.slideshow_container .pos-slideshow .nivo-controlNav a:hover,
		.slideshow_container .pos-slideshow .nivo-controlNav a.active, 
		.pos_title:after, .pos_title_column:after,
		.owl-nav > div:hover,
		.owl-dots .owl-dot.active span, .owl-dots .owl-dot:hover span,
		.product-flag .new, .product-flag .on-sale, .product-flag .pack,
		.product-price-and-shipping-top .discount-product,
		.poslistcategories .list-categories .desc-listcategoreis .view-all a:hover,
		.home_blog_post_area .blog_slider .item .blog_post .post_thumbnail .meta_category a:hover,
		.static-banner .txt_cms a:hover,
		.countdown-static .countdown-content .info a,
		.ft_newsletter form .btn:hover,
		#footer .footer-container .footer_block h3:after, 
		.back-top a,
		.block-categories a.h6:before,
		#search_filters_wrapper #search_filters .h6:before,	
		#tags_block h2:before,
		#tags_block .tags_block li a:hover,
		#search_filters .ui-widget-header,
		.pagination a:hover,
		.products-sort-order .select-list:hover,
		.pagination .current a,.product-actions .add-to-cart,
		.tabs .nav-tabs .nav-item .nav-link:hover:after, .tabs .nav-tabs .nav-item .nav-link.active:after,
		.poscompare-product .desc-box div.cart button.ajax_add_to_cart_button:hover, 
		.poscompare-product .desc-box div.cart span.ajax_add_to_cart_button:hover,
		.btn-secondary:hover, .btn-tertiary:hover, .btn-primary:hover,
		.btn-secondary:focus, .btn-tertiary:focus, .btn-primary:focus,
		.btn-secondary:active, .btn-tertiary:active, .btn-primary:active,
		.btn-secondary:active:focus, .btn-tertiary:active:focus, .btn-primary:active:focus
		{ 
			background: '.$main_color.';
		}';
		$css .='#pos_search_top .form_search .form-control,#tags_block .tags_block li a:hover,
		#search_filters_wrapper #search_filters .facet .facet-label:hover .custom-checkbox input[type="checkbox"] + span ,
		#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-item.active  > a,
		#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-item.home  > a,
		#_desktop_megamenu .pos-menu-horizontal .menu-content .menu-item:hover  > a, 
		.owl-nav > div:hover,
		.js-product-miniature:hover, 
		.pos-special-products .js-product-miniature,
		.pos-special-products .js-product-miniature:hover,
		.product-images .thumb-container.slick-current > div:before,
		.product-images .thumb-container:hover > div:before{  
			border-color: '.$main_color.';
		}';
        $body_font_family = Configuration::get($this->name . 'g_body_gfont_name');
        $body_font_size = Configuration::get($this->name . 'g_body_font_size');
        $body_font_color = Configuration::get($this->name . 'g_body_font_color');
        $body_link_color = Configuration::get($this->name . 'g_a_color');
        $body_link_colorh = Configuration::get($this->name . 'g_a_colorh');
        $css .= 'body{
            font-family: '.$body_font_family.';
            font-size: '.$body_font_size.'px;
            color: '.$body_font_color.';
        }';
      
        $title_block_font_family = Configuration::get($this->name . 'g_title_gfont_name');
        $title_block_font_size = Configuration::get($this->name . 'g_title_font_size');
        $title_block_font_color = Configuration::get($this->name . 'g_title_font_color');
        $title_block_font_tranform = $this->convertTransform(Configuration::get($this->name . 'g_title_font_transform'));
        $title_block_font_size_column = Configuration::get($this->name . 'g_title_font_size_column');
        $css .='.pos_title h2{
            font-family: '.$title_block_font_family.';
            font-size: '.$title_block_font_size.'px;
            color: '.$title_block_font_color.';
            text-transform: '.$title_block_font_tranform.';
        }';
        $css .= '.pos_title_column h2{  
            font-size: '.$title_block_font_size_column.'px;
        }';
		$button_color = Configuration::get($this->name . 'g_button_color');
		$button_colorh = Configuration::get($this->name . 'g_button_colorh');
		$button_bgcolor = Configuration::get($this->name . 'g_button_bgcolor');
		$button_bgcolorh = Configuration::get($this->name . 'g_button_bgcolorh');
		
        $footer_bg = Configuration::get($this->name . 'g_footer_bg_color');
        $footer_color = Configuration::get($this->name . 'g_footer_color');
        $footer_link_color = Configuration::get($this->name . 'g_footer_a_color');
        $footer_link_colorh = Configuration::get($this->name . 'g_footer_a_colorh');
       
        //Product grid
        $pg_name_color = Configuration::get($this->name . 'p_name_color');
        $pg_name_colorh = Configuration::get($this->name . 'p_name_colorh');
        $pg_name_font_size = Configuration::get($this->name . 'p_name_size');
        $pg_name_font_transform = $this->convertTransform(Configuration::get($this->name . 'p_name_transform'));
        $pg_price_color = Configuration::get($this->name . 'p_price_color');
        $pg_price_font_size = Configuration::get($this->name . 'p_price_size');
        $css .= '.js-product-miniature .product_desc .product_name{
            color: '.$pg_name_color.';
            font-size: '.$pg_name_font_size.'px;
            text-transform: '.$pg_name_font_transform.';
        }';
        $css .= '.js-product-miniature .product_desc .product_name:hover{
            color: '.$pg_name_colorh.';
        }';
        $css .= '.product-price-and-shipping .price{
            color:'.$pg_price_color.';
            font-size: '.$pg_price_font_size.'px;
        }';

        $pp_name_color = Configuration::get($this->name . 'pp_name_color');
        $pp_name_font_size = Configuration::get($this->name . 'pp_name_size');
        $pp_name_font_transform = $this->convertTransform(Configuration::get($this->name . 'pp_name_transform'));
        $pp_price_color = Configuration::get($this->name . 'pp_price_color');
        $pp_price_font_size = Configuration::get($this->name . 'pp_price_size');
        $css .= '.h1.namne_details, .product_name_h1{
            color: '.$pp_name_color.';
            font-size: '.$pp_name_font_size.'px;
            text-transform: '.$pp_name_font_transform.';
        }';
        $css .= '.product-prices .price, .product-prices .current-price span:first-child{
            color:'.$pp_price_color.';
            font-size: '.$pp_price_font_size.'px;
        }';
        if (Shop::getContext() == Shop::CONTEXT_SHOP)
            $my_file = $this->local_path.'views/css/posthemeoptions_s_'.(int)$this->context->shop->getContextShopID().'.css';
        
        $fh = fopen($my_file, 'w') or die("can't open file");
        fwrite($fh, $css);
        fclose($fh);
    }
    public function convertTransform($value) {
            switch($value) {
                case 2 :
                    $transform_option = 'capitalize';
                    break;
                case 1 :
                    $transform_option = 'none';
                    break;
                default :
                    $transform_option = 'uppercase';
            }
            return  $transform_option;
    }

    public function renderWidget($hookName = null, array $configuration = [])
    {
        return false;
    }
    public function getWidgetVariables($hookName = null, array $configuration = [])
    {
        return false;
    }

    public function hookHeader($params)
	{
		if (Shop::getContext() == Shop::CONTEXT_SHOP)
		$this->context->controller->addCSS(($this->_path).'views/css/posthemeoptions_s_'.(int)$this->context->shop->getContextShopID().'.css', 'all');
		$body_font_family = Configuration::get($this->name . 'g_body_gfont_url');
		if($body_font_family) $this->context->controller->registerStylesheet('posthemeoptions-body-fonts', $body_font_family,['server' => 'remote']);
		$title_font_family = Configuration::get($this->name . 'g_title_gfont_url');
		if($body_font_family && $title_font_family != $body_font_family)$this->context->controller->registerStylesheet('posthemeoptions-title-fonts', $title_font_family,['server' => 'remote']);

		$smart_vals = array(
			'grid_type' => Configuration::get($this->name . 'p_display'),
			'name_length' => Configuration::get($this->name . 'p_name_length'),
			'cate_default_display' => Configuration::get($this->name . 'cp_display'),
			'cate_show_subcategories' => Configuration::get($this->name . 'cp_subcategories'),
			'cate_product_per_row' => Configuration::get($this->name . 'cp_perrow'),
			'product_thumbnail' => Configuration::get($this->name . 'pp_thumbnail'),
			'product_infotab' => Configuration::get($this->name . 'pp_infortab'),
			'version' => $this->version_compared,
		);
		$this->context->smarty->assign('postheme', $smart_vals);
	}
}
