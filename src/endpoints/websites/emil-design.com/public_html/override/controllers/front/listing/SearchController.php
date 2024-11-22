<?php
class SearchController extends SearchControllerCore
 {
    public $php_self = 'search';
    protected  $search_string;
    protected  $search_tag;
    protected $search_category;
    protected $id_lang;

    public function init()
    {
        parent::init();

        $this->search_string = Tools::getValue('s');
        $this->search_category = Tools::getValue('poscats');
        $this->id_lang = Context::getContext()->language->id;
        if (!$this->search_string) {
            $this->search_string = Tools::getValue('search_query');
        }

        $this->search_tag = Tools::getValue('tag');

        $this->context->smarty->assign(array(
            'search_string' => $this->search_string,
            'search_tag' => $this->search_tag,
        ));

    }
    public function initContent()
    {
        parent::initContent();
		if($this->search_tag ) {
			$this->doProductSearch('catalog/listing/search', array('entity' => 'search'));
		} else {
			$this->doProductSearchPos('catalog/listing/search', array('entity' => 'search'));
		}
		
    }
    protected function getStringSearchQuery()
    {
        return $this->search_string;
    }
    protected function getCategorySearchQuery()
    {
        return $this->search_category;
    }
    protected function getIdLanguage()
    {
        return $this->id_lang;
    }
	protected function getAjaxProductSearchVariables()
    {
        $search = $this->getProductSearchVariablesPos();

        $rendered_products_top = $this->render('catalog/_partials/products-top', array('listing' => $search));
		$link = new Link();
        $rendered_products = $this->render('catalog/_partials/products',
            array('listing' => $search,
            'static_token' => Tools::getToken(false), // added token
            'configuration' => $this->getTemplateVarConfiguration(),
			'link' => $link,
            'urls' => array('pages'=>array('cart'=>$this->context->link->getPageLink('cart'))))); 
        $rendered_products_bottom = $this->render('catalog/_partials/products-bottom', array('listing' => $search));

        $data = array(
            'rendered_products_top' => $rendered_products_top,
            'rendered_products' => $rendered_products,
            'rendered_products_bottom' => $rendered_products_bottom,
        );

        foreach ($search as $key => $value) {
            $data[$key] = $value;
        }

        return $data;
    }

 }
