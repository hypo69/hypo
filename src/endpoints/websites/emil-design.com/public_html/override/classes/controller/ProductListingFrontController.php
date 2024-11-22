<?php

use PrestaShop\PrestaShop\Core\Product\Search\ProductSearchQuery;
use PrestaShop\PrestaShop\Core\Product\Search\Pagination;
use PrestaShop\PrestaShop\Core\Product\Search\ProductSearchContext;
use PrestaShop\PrestaShop\Core\Product\Search\ProductSearchResult;
use PrestaShop\PrestaShop\Core\Product\Search\Facet;
use PrestaShop\PrestaShop\Core\Product\Search\SortOrder;
use PrestaShop\PrestaShop\Core\Product\Search\ProductSearchProviderInterface;
use PrestaShop\PrestaShop\Core\Product\Search\FacetsRendererInterface;

abstract class ProductListingFrontController extends ProductListingFrontControllerCore
{
    
    public function getProductSearchVariablesPos()
    {
        include_once(_PS_MODULE_DIR_.'possearchproducts/PosSearch.php');
        /*
         * To render the page we need to find something (a ProductSearchProviderInterface)
         * that knows how to query products.
         */

        // the search provider will need a context (language, shop...) to do its job
        $context = $this->getProductSearchContext();

        // the controller generates the query...
        $query = $this->getProductSearchQuery();

        // ...modules decide if they can handle it (first one that can is used)
        $provider = $this->getProductSearchProviderFromModules($query);

        // if no module wants to do the query, then the core feature is used
        if (null === $provider) {
            $provider = $this->getDefaultProductSearchProvider();
        }

        $resultsPerPage = (int) Tools::getValue('resultsPerPage');
        if ($resultsPerPage <= 0 || $resultsPerPage > 36) {
            $resultsPerPage = Configuration::get('PS_PRODUCTS_PER_PAGE');
        }

        // we need to set a few parameters from back-end preferences
        $query
            ->setResultsPerPage($resultsPerPage)
            ->setPage(max((int) Tools::getValue('page'), 1))
        ;

        // set the sort order if provided in the URL
        if (($encodedSortOrder = Tools::getValue('order'))) {
            $query->setSortOrder(SortOrder::newFromString(
                $encodedSortOrder
            ));
        }

        // get the parameters containing the encoded facets from the URL
        $encodedFacets = Tools::getValue('q');

        /*
         * The controller is agnostic of facets.
         * It's up to the search module to use /define them.
         *
         * Facets are encoded in the "q" URL parameter, which is passed
         * to the search provider through the query's "$encodedFacets" property.
         */

        $query->setEncodedFacets($encodedFacets);

        // We're ready to run the actual query!
        $result = $provider->runQuery(
            $context,
            $query
        );
        //echo '<pre>'; print_r($result); die;
        $string_query = $this->getStringSearchQuery();
        $id_lang = $this->getIdLanguage();
        $id_category = $this->getCategorySearchQuery();
		$page_number = (int) Tools::getValue('page'); 
		 if ($page_number < 1) $page_number = 1;
        $posproducts = PosSearch::find($id_lang,$string_query,$id_category,$page_number,$resultsPerPage);
        //echo '<pre>'; print_r($posproducts); die;
        // sort order is useful for template,
        // add it if undefined - it should be the same one
        // as for the query anyway
        if (!$result->getCurrentSortOrder()) {
            $result->setCurrentSortOrder($query->getSortOrder());
        }
        // prepare the products
        $products = $this->prepareMultipleProductsForTemplate($posproducts['result']);
        //echo '<pre>'; print_r($products); die;
        // render the facets
        if ($provider instanceof FacetsRendererInterface) {
            // with the provider if it wants to
            $rendered_facets = $provider->renderFacets(
                $context,
                $result
            );
            $rendered_active_filters = $provider->renderActiveFilters(
                $context,
                $result
            );
        } else {
            // with the core
            $rendered_facets = $this->renderFacets(
                $result
            );
            $rendered_active_filters = $this->renderActiveFilters(
                $result
            );
        }

        $pagination = $this->getTemplateVarPaginationPos(
            $query,
            $posproducts
        );
        //echo '<pre>'; print_r($posproducts); die;
        // prepare the sort orders
        // note that, again, the product controller is sort-orders
        // agnostic
        // a module can easily add specific sort orders that it needs
        // to support (e.g. sort by "energy efficiency")
        $sort_orders = $this->getTemplateVarSortOrders(
            $result->getAvailableSortOrders(),
            $query->getSortOrder()->toString()
        );

        $sort_selected = false;
        if (!empty($sort_orders)) {
            foreach ($sort_orders as $order) {
                if (isset($order['current']) && true === $order['current']) {
                    $sort_selected = $order['label'];
                    break;
                }
            }
        }

        $searchVariables = array(
            'label' => $this->getListingLabel(),
            'products' => $products,
            'sort_orders' => $sort_orders,
            'sort_selected' => $sort_selected,
            'pagination' => $pagination,
            'rendered_facets' => $rendered_facets,
            'rendered_active_filters' => $rendered_active_filters,
            'js_enabled' => $this->ajax,
            'current_url' => $this->updateQueryString(array(
                'q' => $result->getEncodedFacets(),
            )),
        );

        Hook::exec('filterProductSearch', array('searchVariables' => &$searchVariables));
        Hook::exec('actionProductSearchAfter', $searchVariables);

        return $searchVariables;
    }

    protected function getTemplateVarPaginationPos(
        ProductSearchQuery $query, $posproducts
    ) {
        $pagination = new Pagination();
        $pagination
            ->setPage($query->getPage())
            ->setPagesCount(
              (int)  ceil($posproducts['total'] / $query->getResultsPerPage())
            )
        ;
        $totalItems = $posproducts['total'];
        $itemsShownFrom = ($query->getResultsPerPage() * ($query->getPage() - 1)) + 1;
        $itemsShownTo = $query->getResultsPerPage() * $query->getPage();

        return array(
            'total_items' => $totalItems,
            'items_shown_from' => $itemsShownFrom,
            'items_shown_to' => ($itemsShownTo <= $totalItems) ? $itemsShownTo : $totalItems,
            'pages' => array_map(function ($link) {
                $link['url'] = $this->updateQueryString(array(
                    'page' => $link['page'],
                ));

                return $link;
            }, $pagination->buildLinks()),
            'should_be_displayed' => (count($pagination->buildLinks()) > 3)
        );
    }
    public function doProductSearchPos($template, $params = array(), $locale = null)
    {
        if ($this->ajax) {
           return $this->getAjaxProductSearchVariables(); 
        } else {
            if(Tools::getValue('tag')) {
				$variables = $this->getProductSearchVariables();
			} else {
				$variables = $this->getProductSearchVariablesPos();
			}
			
            $this->context->smarty->assign(array(
                'listing' => $variables,
            ));
            //echo '<pre>'; print_r($variables);die;
            $this->setTemplate($template, $params, $locale);
        }
    }
    private function getProductSearchProviderFromModules($query)
    {
        $providers = Hook::exec(
            'productSearchProvider',
            array('query' => $query),
            null,
            true
        );

        if (!is_array($providers)) {
            $providers = array();
        }

        foreach ($providers as $provider) {
            if ($provider instanceof ProductSearchProviderInterface) {
                return $provider;
            }
        }

        return;
    }
	protected function getAjaxProductSearchVariables122()
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

        return ;
    }
	    protected function getAjaxProductSearchVariables()
    {
		 $controller = Tools::getValue('controller'); 
		if($controller == 'search') {
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
		} else {
			$search = $this->getProductSearchVariables();

			$rendered_products_top = $this->render('catalog/_partials/products-top', array('listing' => $search));
			$rendered_products = $this->render('catalog/_partials/products', array('listing' => $search));
			$rendered_products_bottom = $this->render('catalog/_partials/products-bottom', array('listing' => $search));

			$data = array_merge(
				array(
					'rendered_products_top' => $rendered_products_top,
					'rendered_products' => $rendered_products,
					'rendered_products_bottom' => $rendered_products_bottom,
				),
				$search
			);

			if (!empty($data['products']) && is_array($data['products'])) {
				$data['products'] = $this->prepareProductArrayForAjaxReturn($data['products']);
			}
		}

        return $data;
    }
}
