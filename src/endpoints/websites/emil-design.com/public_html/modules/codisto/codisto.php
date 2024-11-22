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
if (!defined('_PS_VERSION_')) {
    exit;
}

class Codisto extends Module
{
    protected $ping = null;
    protected $home;
    protected $listings;
    protected $settings;
    protected $orders;
    protected $account;
    protected $ebayTemplate;

    public function __construct()
    {
        $this->name = 'codisto';
        $this->tab = 'administration';
        $this->version = '1.0.8';
        $this->author = 'Codisto';
        $this->controllers = ['home'];
        $this->need_instance = 0;
        $this->ps_versions_compliancy = [
            'min' => '1.6',
            'max' => _PS_VERSION_,
        ];
        $this->module_key = '95c9ac1121adbcf3f1cba3b8ba832632';

        // Set $this->bootstrap to true if your module is compliant with bootstrap (PrestaShop 1.6)
        $this->bootstrap = true;

        parent::__construct();

        $this->displayName = $this->trans('Codisto', [], 'Modules.Codisto.Codisto');
        $this->description = $this->trans('Sell multichannel on Google, Amazon, eBay, Google & Walmart direct from PrestaShop. Create listings & sync products, inventory & orders directly from PrestaShop', [], 'Modules.Codisto.Codisto');

        $this->confirmUninstall = $this->trans('Are you sure you want to uninstall?', [], 'Modules.Codisto.Codisto');

        $this->confirmUninstall = $this->l('Are you sure you want to uninstall?');
        register_shutdown_function([$this, 'signalEdit']);

        $this->home = $this->trans('Home', [], 'Modules.Codisto.Codisto');
        $this->listings = $this->trans('Listings', [], 'Modules.Codisto.Codisto');
        $this->settings = $this->trans('Settings', [], 'Modules.Codisto.Codisto');
        $this->orders = $this->trans('Orders', [], 'Modules.Codisto.Codisto');
        $this->account = $this->trans('Account', [], 'Modules.Codisto.Codisto');
        $this->ebayTemplate = $this->trans('eBay Templates', [], 'Modules.Codisto.Codisto');
    }

    /**
     * Don't forget to create update methods if needed:
     * http://doc.prestashop.com/display/PS16/Enabling+the+Auto-Update
     */
    public function install()
    {
        if (Shop::isFeatureActive()) {
            Shop::setContext(Shop::CONTEXT_ALL);
        }

        if (!parent::install()
            || !$this->installDb()
            || !$this->installTab()
            || !$this->registerHook('moduleRoutes')
            || !$this->registerHook('displayBackOfficeHeader')
            || !$this->registerHook('actionProductSave')
            || !$this->registerHook('actionValidateOrder')
        ) {
            return false;
        }

        return true;
    }

    public function uninstall()
    {
        Configuration::deleteByName('CODISTO_LIVE_MODE');

        return $this->uninstallTab() &&
        parent::uninstall();
    }

    public function installDb()
    {
        $return = true;
        $sql = include __DIR__ . '/sql_install.php';
        if (!empty($sql)) {
            foreach ($sql as $s) {
                $return &= Db::getInstance()->execute($s);
            }
        }

        return $return;
    }

    public function installTab()
    {
        // Main Parent menu
        if (!(int) Tab::getIdFromClassName('AdminCodistoParent')) {
            $parentTab = new Tab();
            $parentTab->active = 1;
            $parentTab->name = [];
            $parentTab->class_name = 'AdminCodistoParent';
            foreach (Language::getLanguages(true) as $language) {
                $parentTab->name[$language['id_lang']] = 'Codisto';
            }
            $parentTab->id_parent = 0;
            $parentTab->module = $this->name;
            $parentTab->add();
        }

        // Sub menu code
        if (!(int) Tab::getIdFromClassName('AdminCodisto')) {
            $parentTabID = Tab::getIdFromClassName('AdminCodistoParent');
            $parentTab = new Tab($parentTabID);

            $tab = new Tab();
            $tab->active = 1;
            $tab->class_name = 'AdminCodisto';
            $tab->icon = 'settings';
            $tab->visible = true;
            $tab->name = [];
            foreach (Language::getLanguages(true) as $language) {
                $tab->name[$language['id_lang']] = 'Codisto';
            }
            $tab->id_parent = $parentTab->id;
            $tab->parent_class_name = 'AdminCodisto';
            $tab->module = $this->name;
            $tab->add();
        }

        if (!(int) Tab::getIdFromClassName('AdminCodistoHome')) {
            $parentTabID = Tab::getIdFromClassName('AdminCodisto');
            $parentTab = new Tab($parentTabID);

            $tab = new Tab();
            $tab->active = 1;
            $tab->class_name = 'AdminCodistoHome';
            $tab->route_name = 'admin_codistohome';
            $tab->visible = true;
            $tab->name = [];
            foreach (Language::getLanguages(true) as $language) {
                $tab->name[$language['id_lang']] = $this->trans('Home', [], 'Modules.Codisto.Codisto', $language['locale']);
            }
            $tab->id_parent = $parentTab->id;
            $tab->parent_class_name = 'AdminCodisto';
            $tab->wording = 'Home';
            $tab->wording_domain = 'Modules.Codisto.Codisto';
            $tab->module = $this->name;
            $tab->add();
        }

        if (!(int) Tab::getIdFromClassName('AdminCodistoListings')) {
            $parentTabID = Tab::getIdFromClassName('AdminCodisto');
            $parentTab = new Tab($parentTabID);

            $tab = new Tab();
            $tab->active = 1;
            $tab->class_name = 'AdminCodistoListings';
            $tab->route_name = 'admin_codistolistings';
            $tab->visible = true;
            $tab->name = [];
            foreach (Language::getLanguages(true) as $language) {
                $tab->name[$language['id_lang']] = $this->trans('Listings', [], 'Modules.Codisto.Codisto', $language['locale']);
            }
            $tab->id_parent = $parentTab->id;
            $tab->parent_class_name = 'AdminCodisto';
            $tab->wording = 'Listings';
            $tab->wording_domain = 'Modules.Codisto.Codisto';
            $tab->module = $this->name;
            $tab->add();
        }

        if (!(int) Tab::getIdFromClassName('AdminCodistoOrders')) {
            $parentTabID = Tab::getIdFromClassName('AdminCodisto');
            $parentTab = new Tab($parentTabID);

            $tab = new Tab();
            $tab->active = 1;
            $tab->class_name = 'AdminCodistoOrders';
            $tab->route_name = 'admin_codistoorders';
            $tab->visible = true;
            $tab->name = [];
            foreach (Language::getLanguages(true) as $language) {
                $tab->name[$language['id_lang']] = $this->trans('Orders', [], 'Modules.Codisto.Codisto', $language['locale']);
            }
            $tab->id_parent = $parentTab->id;
            $tab->parent_class_name = 'AdminCodisto';
            $tab->wording = 'Orders';
            $tab->wording_domain = 'Modules.Codisto.Codisto';
            $tab->module = $this->name;
            $tab->add();
        }

        if (!(int) Tab::getIdFromClassName('AdminCodistoSettings')) {
            $parentTabID = Tab::getIdFromClassName('AdminCodisto');
            $parentTab = new Tab($parentTabID);

            $tab = new Tab();
            $tab->active = 1;
            $tab->class_name = 'AdminCodistoSettings';
            $tab->route_name = 'admin_codistosettings';
            $tab->visible = true;
            $tab->name = [];
            foreach (Language::getLanguages(true) as $language) {
                $tab->name[$language['id_lang']] = $this->trans('Settings', [], 'Modules.Codisto.Codisto', $language['locale']);
            }
            $tab->id_parent = $parentTab->id;
            $tab->parent_class_name = 'AdminCodisto';
            $tab->wording = 'Settings';
            $tab->wording_domain = 'Modules.Codisto.Codisto';
            $tab->module = $this->name;
            $tab->add();
        }

        if (!(int) Tab::getIdFromClassName('AdminCodistoAccount')) {
            $parentTabID = Tab::getIdFromClassName('AdminCodisto');
            $parentTab = new Tab($parentTabID);

            $tab = new Tab();
            $tab->active = 1;
            $tab->class_name = 'AdminCodistoAccount';
            $tab->route_name = 'admin_codistoaccount';
            $tab->visible = true;
            $tab->name = [];
            foreach (Language::getLanguages(true) as $language) {
                $tab->name[$language['id_lang']] = $this->trans('Account', [], 'Modules.Codisto.Codisto', $language['locale']);
            }
            $tab->id_parent = $parentTab->id;
            $tab->parent_class_name = 'AdminCodisto';
            $tab->wording = 'Account';
            $tab->wording_domain = 'Modules.Codisto.Codisto';
            $tab->module = $this->name;
            $tab->add();
        }

        if (!(int) Tab::getIdFromClassName('AdminCodistoEbayTemplates')) {
            $parentTabID = Tab::getIdFromClassName('AdminCodisto');
            $parentTab = new Tab($parentTabID);

            $tab = new Tab();
            $tab->active = 1;
            $tab->class_name = 'AdminCodistoEbayTemplates';
            $tab->route_name = 'admin_codistoebay_templates';
            $tab->visible = true;
            $tab->name = [];
            foreach (Language::getLanguages(true) as $language) {
                $tab->name[$language['id_lang']] = $this->trans('eBay Templates', [], 'Modules.Codisto.Codisto', $language['locale']);
            }
            $tab->id_parent = $parentTab->id;
            $tab->parent_class_name = 'AdminCodisto';
            $tab->wording = 'eBay Templates';
            $tab->wording_domain = 'Modules.Codisto.Codisto';
            $tab->module = $this->name;
            $tab->add();
        }

        if (!(int) Tab::getIdFromClassName('AdminCodistoEbayTemplates')) {
            $parentTabID = Tab::getIdFromClassName('AdminCodisto');
            $parentTab = new Tab($parentTabID);

            $tab = new Tab();
            $tab->active = 1;
            $tab->class_name = 'AdminEbayTemplates';
            $tab->route_name = 'admin_codistoebay_templates';
            $tab->visible = true;
            $tab->name = [];
            foreach (Language::getLanguages(true) as $language) {
                $tab->name[$language['id_lang']] = 'eBay Templates';
            }
            $tab->id_parent = $parentTab->id;
            $tab->parent_class_name = 'AdminCodisto';
            $tab->module = $this->name;
            $tab->add();
        }

        return true;
    }

    public function uninstallTab()
    {
        $uninstallTabCompleted = true;
        $id_tab = (int) Tab::getIdFromClassName('AdminCodistoParent');
        if ($id_tab) {
            $tab = new Tab($id_tab);

            $uninstallTabCompleted = $uninstallTabCompleted && $tab->delete();

            // delete child tabs
            $childTabCodisto = Tab::getInstanceFromClassName('AdminCodisto');
            $childTabCodisto->id_parent = $childTabCodisto->id_parent;
            $uninstallTabCompleted = $uninstallTabCompleted && $childTabCodisto->delete();

            $childTabListings = Tab::getInstanceFromClassName('AdminCodistoListings');
            $childTabListings->id_parent = $childTabListings->id_parent;
            $uninstallTabCompleted = $uninstallTabCompleted && $childTabListings->delete();

            $childTabOrders = Tab::getInstanceFromClassName('AdminCodistoOrders');
            $childTabOrders->id_parent = $childTabOrders->id_parent;
            $uninstallTabCompleted = $uninstallTabCompleted && $childTabOrders->delete();

            $childTabSettings = Tab::getInstanceFromClassName('AdminCodistoSettings');
            $childTabSettings->id_parent = $childTabSettings->id_parent;
            $uninstallTabCompleted = $uninstallTabCompleted && $childTabSettings->delete();

            $childTabAccount = Tab::getInstanceFromClassName('AdminCodistoAccount');
            $childTabAccount->id_parent = $childTabAccount->id_parent;
            $uninstallTabCompleted = $uninstallTabCompleted && $childTabAccount->delete();

            $childTabEbayTemplate = Tab::getInstanceFromClassName('AdminCodistoEbayTemplates');
            $childTabEbayTemplate->id_parent = $childTabEbayTemplate->id_parent;
            $uninstallTabCompleted = $uninstallTabCompleted && $childTabEbayTemplate->delete();
        }

        return $uninstallTabCompleted;
    }

    public function hookDisplayBackOfficeHeader($isNewTheme = false)
    {
        if (Tools::getValue('controller') == 'AdminCodistoHome' || Tools::getValue('controller') == 'AdminCodistoListings' || Tools::getValue('controller') == 'AdminCodistoOrders' || Tools::getValue('controller') == 'AdminCodistoSettings' || Tools::getValue('controller') == 'AdminCodistoAccount' || Tools::getValue('controller') == 'AdminCodistoEbayTemplates') {
            if (version_compare(_PS_VERSION_, '8.0.0', '<')) {
                $this->context->controller->addCSS($this->_path . 'views/css/back.css', 'all');
            } else {
                $this->context->controller->addCSS($this->_path . 'views/css/backv8.css', 'all');
            }
            $this->context->controller->addJS($this->_path . 'views/js/back.js', 'all');
        }
    }

    /**
     * Load the configuration page
     */
    public function getContent()
    {
        $this->context->smarty->assign('module_dir', $this->_path);
        $output = $this->context->smarty->fetch($this->local_path . 'views/templates/admin/configure.tpl');

        return $output;
    }

    // register sync-route for product and order
    public function hookModuleRoutes($params)
    {
        $codisto_routes = [
            'module-codisto-sync' => [
                'rule' => '{indexphp}codisto-sync/{link_rewrite}',
                'keywords' => [
                    'link_rewrite' => ['regexp' => '[_a-zA-Z0-9-\pL]*', 'param' => 'link_rewrite'],
                    'indexphp' => ['regexp' => '(\/?index.php\/)?', 'param' => 'indexphp'],
                ],
                'controller' => 'home',
                'params' => [
                    'fc' => 'module',
                    'module' => 'codisto',
                ],
            ],
            'module-codisto-proxy' => [
                'rule' => '{indexphp}codisto-proxy/{link_rewrite}',
                'keywords' => [
                    'link_rewrite' => ['regexp' => '.+', 'param' => 'link_rewrite'],
                    'indexphp' => ['regexp' => '(\/?index.php\/)?', 'param' => 'indexphp'],
                ],
                'controller' => 'proxy',
                'params' => [
                    'fc' => 'module',
                    'module' => 'codisto',
                ],
            ],
        ];

        return $codisto_routes;
    }

    // actionProductSave hook handler used to notify changes to products to codisto
    public function hookActionProductSave()
    {
        $id = Tools::getValue('id_product');

        if (!$this->ping) {
            $this->ping = [];
        }

        if (!isset($this->ping['products'])) {
            $this->ping['products'] = [];
        }

        $pingProducts = $this->ping['products'];

        if (!in_array($id, $pingProducts)) {
            $pingProducts[] = $id;
        }

        $this->ping['products'] = $pingProducts;
    }

    // actionOrderSave hook handler used to notify stock changes to products to codisto
    public function hookActionValidateOrder($params)
    {
        $order = $params['order'];
        $cart = $this->context->cart;
        $products = $cart->getProducts();
        $product_ids = [];

        foreach ($products as $key => $product) {
            $product_ids[] = $product['id_product'];
        }

        if (count($product_ids) > 0) {
            if (!$this->ping) {
                $this->ping = [];
            }

            if (!isset($this->ping['products'])) {
                $this->ping['products'] = [];
            }

            $pingProducts = $this->ping['products'];

            foreach ($product_ids as $id) {
                if (!in_array($id, $pingProducts)) {
                    $pingProducts[] = $id;
                }
            }

            $this->ping['products'] = $pingProducts;
        }
    }

    /**
     * takes collected set of signals during post handling and transmits to codisto
     *this runs within the shutdown hook to avoid standard stalling admin processing
     */
    public function signalEdit()
    {
        $merchantId = Configuration::get('CODISTO_MERCHANTID');
        $hostKey = Configuration::get('CODISTO_KEY');

        $requestHeaders = [
            'method: POST',
            'timeout: 5',
            'httpversion: 1.0',
            'blocking: true',
            'redirection: 0',
            'X-HostKey: ' . $hostKey,
            'Content-Type: application/x-www-form-urlencoded',
        ];

        $remoteUrl = 'https://api.codisto.com/' . $merchantId;

        if (is_array($this->ping) && isset($this->ping['products'])) {
            $body = 'action=sync&productid=[' . implode(',', $this->ping['products']) . ']';
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
            curl_setopt($ch, CURLOPT_URL, $remoteUrl);
            curl_setopt($ch, CURLOPT_HTTPHEADER, $requestHeaders);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $body);

            $result = curl_exec($ch);
            $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            $curl_err = curl_error($ch);
            curl_close($ch);
        } elseif (is_array($this->ping)) {
            $body = 'action=sync';
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
            curl_setopt($ch, CURLOPT_URL, $remoteUrl);
            curl_setopt($ch, CURLOPT_HTTPHEADER, $requestHeaders);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $body);

            $result = curl_exec($ch);
            $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            $curl_err = curl_error($ch);
            curl_close($ch);
        }
    }

    public function isUsingNewTranslationSystem()
    {
        return true;
    }
}
