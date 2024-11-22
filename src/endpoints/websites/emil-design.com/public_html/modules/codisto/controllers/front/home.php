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

if (!defined('_PS_BASE_URL_SSL_')) {
    define('_PS_BASE_URL_SSL_', Tools::getShopDomainSsl(true));
}

require_once __DIR__ . '/../AbstractCodistoController.php';

class CodistoHomeModuleFrontController extends AbstractCodistoController
{
    const STATE_PAID = 2;
    const STATE_PROCESSING_PROGRESS = 3;
    const STATE_SHIPPED = 4;
    const STATE_CANCELED = 6;
    const STATE_REFUND = 7;
    const STATE_PAYMENT_FAILED = 8;
    const STATE_WAITING_CAPTURE = 19;

    // Match the host key
    private function checkHash()
    {
        if (!isset($_SERVER['HTTP_X_CODISTONONCE']) || !isset($_SERVER['HTTP_X_CODISTOKEY'])) {
            $this->sendHttpHeaders(
                '400 Security Error',
                [
                    'Content-Type' => 'application/json',
                    'Cache-Control' => 'no-cache, no-store',
                    'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                    'Pragma' => 'no-cache',
                ]
            );

            echo json_encode(['ack' => 'error', 'message' => 'Security Error - Missing Headers']);

            return false;
        }

        $key = Configuration::get('CODISTO_KEY') . $_SERVER['HTTP_X_CODISTONONCE'];
        $base = hash('sha256', $key, true);
        $checkHash = base64_encode($base);
        if (!hash_equals($_SERVER['HTTP_X_CODISTOKEY'], $checkHash)) {
            $this->sendHttpHeaders(
                '400 Security Error',
                [
                    'Content-Type' => 'application/json',
                    'Cache-Control' => 'no-cache, no-store',
                    'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                    'Pragma' => 'no-cache',
                ]
            );

            echo json_encode(['ack' => 'error', 'message' => 'Security Error']);

            return false;
        }

        return true;
    }

    /**
     * common http status and header output function
     *
     * @param int $status the http status to send
     * @param array $headers an array of headers to send
     */
    private function sendHttpHeaders($status, $headers)
    {
        $statusheader = preg_split('/ /', $status, 2);
        http_response_code((int) $statusheader[0]);
        foreach ($headers as $header => $value) {
            header($header . ': ' . $value);
        }
    }

    // Sync product, category, order & template
    protected function processGetRequest()
    {
        $db = Db::getInstance();
        $idLang = (int) Context::getContext()->language->id;
        $type = Tools::getValue('link_rewrite');

        if ($type == 'test' || ($type == 'sync' && preg_match('/\/sync\/testHash\?/', $_SERVER['REQUEST_URI']))) {
            if (!$this->checkHash()) {
                exit;
            }

            $response = ['ack' => 'ok'];

            $this->sendHttpHeaders(
                '200 OK',
                [
                    'Content-Type' => 'application/json',
                    'Cache-Control' => 'no-cache, no-store',
                    'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                    'Pragma' => 'no-cache',
                ]
            );

            $this->ajaxDie(json_encode($response));
        } elseif ($type === 'settings') {
            if (!$this->checkHash()) {
                exit;
            }
            $shopName = Configuration::get('PS_SHOP_NAME');

            $logoUrl = _PS_BASE_URL_SSL_ . __PS_BASE_URI__ . '/img/' . Configuration::get('PS_LOGO');

            $getCurrency = Context::getContext()->currency;
            $currency = $getCurrency->symbol;

            $getCountry = $this->context->country;

            $countryCode = isset($getCountry->iso_code) ? $getCountry->iso_code : '';
            $stateCode = '';

            $dimensionUnit = Configuration::get('PS_DIMENSION_UNIT');

            $weightUnit = Configuration::get('PS_WEIGHT_UNIT');

            $module = Module::getInstanceByName('codisto');
            $version = $module->version;

            $response = [
                'ack' => 'ok',
                'shop_name' => $shopName,
                'logo' => $logoUrl,
                'currency' => $currency,
                'dimension_unit' => $dimensionUnit,
                'weight_unit' => $weightUnit,
                'country_code' => $countryCode,
                'state_code' => $stateCode,
                'version' => $version,
            ];

            $this->ajaxDie(json_encode($response));
        } elseif ($type == 'tax') {
            if (!$this->checkHash()) {
                exit;
            }
            $tax_enabled = true;
            $rates = [];

            if ($tax_enabled) {
                $rates = $this->getTaxes($idLang);
            }

            $response = ['ack' => 'ok', 'tax_rates' => $rates];

            $this->sendHttpHeaders(
                '200 OK',
                [
                    'Content-Type' => 'application/json',
                    'Cache-Control' => 'no-cache, no-store',
                    'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                    'Pragma' => 'no-cache',
                ]
            );

            $this->ajaxDie(json_encode($response));
        } elseif ($type == 'products') {
            if (!$this->checkHash()) {
                exit;
            }

            $page = !empty(Tools::getValue('page')) ? (int) Tools::getValue('page') : 0;
            $count = !empty(Tools::getValue('count')) ? (int) Tools::getValue('count') : 0;

            $productIds = !empty(Tools::getValue('product_ids')) ? json_decode(Tools::getValue('product_ids')) : null;

            if (!is_null($productIds)) {
                if (!is_array($productIds)) {
                    $productIds = [$productIds];
                }

                $productIds = array_filter($productIds, 'is_numeric');

                if (empty($_GET['count'])) {
                    $count = count($productIds);
                }
            }

            $request = 'SELECT `id_product` FROM `' . _DB_PREFIX_ . 'product` ' . (is_array($productIds) ? 'WHERE `id_product` IN (' . implode(',', $productIds) . ')' : '') . ' ORDER BY `id_product` LIMIT ' . (int) $page * (int) $count . ',' . (int) $count;

            $products = $db->executeS($request);

            if (!is_array($productIds) && $page === 0) {
                $total_count = $db->getValue('SELECT COUNT(*) FROM `' . _DB_PREFIX_ . 'product`');
            }

            foreach ($products as $key => $product) {
                // Load product object
                $psProduct = new Product($product['id_product'], true, $idLang);

                $products[$key]['reference'] = $psProduct->reference;
                $products[$key]['name'] = $psProduct->name;
                $products[$key]['description'] = $psProduct->description;
                $products[$key]['description_short'] = $psProduct->description_short;
                $products[$key]['active'] = $psProduct->active;
                $products[$key]['price'] = $psProduct->base_price;
                $products[$key]['listprice'] = $psProduct->getPrice(true);
                $products[$key]['is_taxable'] = ($psProduct->tax_rate == 0) ? 0 : 1;
                $products[$key]['stock_control'] = Configuration::get('PS_STOCK_MANAGEMENT');
                $products[$key]['stock_level'] = $psProduct->quantity;
                $products[$key]['product_type'] = $psProduct->product_type;
                $products[$key]['width'] = $psProduct->width;
                $products[$key]['height'] = $psProduct->height;
                $products[$key]['depth'] = $psProduct->depth;
                $products[$key]['weight'] = $psProduct->weight;
                $products[$key]['tax_class'] = $this->getTaxRuleGroupNameById($psProduct->id_tax_rules_group);

                // Get product catgories
                $products[$key]['categories'] = [];
                $productCategories = $psProduct->getCategories();

                if (is_array($productCategories)) {
                    $sequence = 0;
                    foreach ($productCategories as $category) {
                        $products[$key]['categories'][] = ['category_id' => $category, 'sequence' => $sequence];
                        $sequence = $sequence + 1;
                    }
                }

                // get features as product attributes
                $productFeatures = $psProduct->getFeaturesStatic($product['id_product']);
                $features = [];

                foreach ($productFeatures as $featureKey => $feature) {
                    $featureValue = $this->getFeatureValue($feature['id_feature_value'], $idLang);
                    $featureName = Feature::getFeature($idLang, $feature['id_feature']);

                    if (!empty($featureName['name'])) {
                        $features[$featureKey]['name'] = $featureName['name'];
                        $features[$featureKey]['value'] = $featureValue;
                    }
                }

                $products[$key]['features'] = array_values($features);

                // get images
                $images = $psProduct->getImages($idLang);
                $listImage = [];

                foreach ($images as $img) {
                    $image['cover'] = (bool) $img['cover'];
                    $image['url'] = $this->context->link->getImageLink($psProduct->link_rewrite, $img['id_image'], ImageType::getFormattedName('home'));

                    $image['position'] = $img['position'];
                    array_push($listImage, $image);
                }

                $products[$key]['images'] = $listImage;

                // get product tags
                $products[$key]['tags'] = [];
                if (is_array($psProduct->tags)) {
                    foreach ($psProduct->tags as $tags) {
                        $sequence = 0;
                        foreach ($tags as $index => $tag) {
                            $products[$key]['tags'][$index] = ['tag' => $tag, 'sequence' => $sequence];
                            $sequence = $sequence + 1;
                        }
                    }
                }

                // specific price or discount
                if (!empty($psProduct->specificPrice)) {
                    $products[$key]['specificPrice'] = $psProduct->specificPrice;
                }

                // get child products
                if ($psProduct->product_type == 'combinations') {
                    $products[$key]['skus'] = [];
                    $attributes = [];
                    $productVariant = [];
                    $idAttributeGroup = [];
                    $children = $psProduct->getAttributesResume($idLang);

                    foreach ($children as $index => $childProduct) {
                        $children[$index]['price'] = $psProduct->getPrice(true, $childProduct['id_product_attribute']);
                        $children[$index]['listprice'] = $psProduct->getPrice(true, $childProduct['id_product_attribute']);
                        $children[$index]['is_taxable'] = ($psProduct->tax_rate == 0) ? 0 : 1;
                        $children[$index]['stock_control'] = Configuration::get('PS_STOCK_MANAGEMENT');
                        $skuImages = Image::getImages($idLang, $product['id_product'], $childProduct['id_product_attribute']);

                        $listSkuImage = [];
                        if (!empty($skuImages)) {
                            foreach ($skuImages as $sku_img) {
                                $sku_image['cover'] = (bool) $sku_img['cover'];

                                $sku_image['url'] = $this->context->link->getImageLink($psProduct->link_rewrite, $sku_img['id_image'], ImageType::getFormattedName('home'));

                                $sku_image['position'] = $sku_img['position'];
                                array_push($listSkuImage, $sku_image);
                            }
                        }
                        $children[$index]['images'] = $listSkuImage;

                        // get attributes
                        $getAttributes = $psProduct->getAttributesGroups($idLang, $childProduct['id_product_attribute']);

                        foreach ($getAttributes as $name => $row) {
                            $attributes[$name]['name'] = $row['group_name'];
                            $attributes[$name]['value'] = $row['attribute_name'];

                            if (!in_array($row['id_attribute_group'], $idAttributeGroup)) {
                                $idAttributeGroup[$row['group_name']] = $row['id_attribute_group'];
                            }
                        }

                        $children[$index]['attributes'] = $attributes;
                    }
                    $products[$key]['skus'] = $children;

                    // get variant VALUES
                    if (!empty($idAttributeGroup)) {
                        foreach ($idAttributeGroup as $groupName => $groupId) {
                            $valmap = [];
                            $variants = AttributeGroup::getAttributes($idLang, $groupId);
                            foreach ($variants as $single) {
                                $valmap[] = $single['name'];
                            }

                            $productVariant[] = ['name' => $groupName,  'values' => implode('|', $valmap)];
                        }
                    }
                    $products[$key]['variantvalues'] = $productVariant;
                } elseif ($psProduct->product_type == 'pack') {
                    $childProductData = [];
                    $children = Pack::getItems($product['id_product'], $idLang);

                    foreach ($children as $index => $childProduct) {
                        $childProductData[] = [
                            'id' => $childProduct->id,
                            'price' => $childProduct->price,
                            'sku' => $childProduct->reference,
                            'name' => $childProduct->name,
                        ];
                    }
                    $products[$key]['skus'] = $childProductData;
                }
            }

            $response = ['ack' => 'ok', 'products' => $products];

            if (!empty($total_count)) {
                $response['total_count'] = $total_count;
            }

            $this->ajaxDie(json_encode($response));
        } elseif ($type == 'categories') {
            if (!$this->checkHash()) {
                exit;
            }

            $categories = Category::getCategories($idLang);

            $result = [];
            foreach ($categories as $key => $category) {
                foreach ($category as $value) {
                    $result[] = [
                        'category_id' => $value['infos']['id_category'],
                        'name' => $value['infos']['name'],
                        'parent_id' => $value['infos']['id_parent'],
                    ];
                }
            }

            $response = ['ack' => 'ok', 'categories' => $result, 'total_count' => count($result)];

            $this->ajaxDie(json_encode($response));
        } elseif ($type == 'orders') {
            if (!$this->checkHash()) {
                exit;
            }

            $idLang = (int) Context::getContext()->language->id;

            $page = !empty(Tools::getValue('page')) ? (int) Tools::getValue('page') : 0;
            $count = !empty(Tools::getValue('count')) ? (int) Tools::getValue('count') : 0;
            $merchantid = !empty(Tools::getValue('merchantid')) ? (int) Tools::getValue('merchantid') : 0;

            $sql_orders = 'SELECT (
                SELECT `value` FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `id_order` = PO.`id_order` AND `key` = "_codisto_orderid" AND
                    (
                        EXISTS (SELECT 1 FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `key` = "_codisto_merchantid" AND `value` = ' . (int) $merchantid . ' AND `id_order` = PO.`id_order`)
                        OR NOT EXISTS (SELECT 1 FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `key` = "_codisto_merchantid" AND `id_order` = PO.`id_order`)
                    )
                ) AS `id`, `id_order`, `reference` AS `order_reference`, `current_state` AS `status`, `id_carrier`, `delivery_date` FROM `' . _DB_PREFIX_ . 'orders` AS PO
                WHERE date_add > DATE_SUB( CURRENT_TIMESTAMP(), INTERVAL 90 DAY )
                AND `id_order` IN
                    ( SELECT `id_order` FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `key` = "_codisto_orderid" AND (
                        EXISTS ( SELECT 1 FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `key` = "_codisto_merchantid" AND `value` = ' . (int) $merchantid . ' AND `id_order` = PO.`id_order`)
                        OR NOT EXISTS ( SELECT 1 FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `key` = "_codisto_merchantid" AND `id_order` = PO.`id_order` )
                    )
                ) ORDER BY `id_order` LIMIT ' . (int) $page * (int) $count . ',' . (int) $count;

            $orders = $db->executeS($sql_orders);

            if ($page == 0) {
                $sqlOrderCount = 'SELECT count(*) FROM `' . _DB_PREFIX_ . 'orders` AS PO WHERE date_add > DATE_SUB( CURRENT_TIMESTAMP(), INTERVAL 90 DAY ) AND `id_order` IN ( SELECT `id_order` FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `key` = "_codisto_orderid" AND (
                    EXISTS ( SELECT 1 FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `key` = "_codisto_merchantid" AND `value` = ' . (int) $merchantid . ' AND `id_order` = PO.`id_order`)
                    OR NOT EXISTS ( SELECT 1 FROM `' . _DB_PREFIX_ . 'codisto_order_meta` WHERE `key` = "_codisto_merchantid" AND `id_order` = PO.`id_order` ))
                )';

                $totalCount = $db->getValue($sqlOrderCount);
            }

            $orderData = [];

            if (!empty($orders)) {
                foreach ($orders as $key => $order) {
                    $order['ship_date'] = $order['delivery_date'];
                    $order['carrier'] = $this->getCarrier($order['id_carrier']);
                    $order['track_number'] = $this->getTrackingNumber($order['id_order']);
                    $order['pay_date'] = $this->getPaymentDate($order['order_reference']);
                    $order['status'] = $this->getCurrentStatus($idLang, $order['status']);

                    $orderData[] = $order;
                }
            }

            $response = ['ack' => 'ok', 'orders' => $orderData];

            if (!empty($totalCount)) {
                $response['total_count'] = $totalCount;
            }

            $this->sendHttpHeaders(
                '200 OK',
                [
                    'Content-Type' => 'application/json',
                    'Cache-Control' => 'no-cache, no-store',
                    'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                    'Pragma' => 'no-cache',
                ]
            );

            $this->ajaxDie(json_encode($response));
        } elseif ($type == 'sync') {
            if ($_SERVER['HTTP_X_ACTION'] === 'TEMPLATE') {
                if (!$this->checkHash()) {
                    exit;
                }

                $ebayTemplateDir = _PS_ROOT_DIR_ . '/upload/codistoebaytemplates/';

                $merchantid = (int) Tools::getValue('merchantid');
                if (!$merchantid) {
                    $merchantid = 0;
                }

                if (!empty(Tools::getValue('markreceived'))) {
                    $this->sendHttpHeaders(
                        '200 OK',
                        [
                            'Content-Type' => 'application/json',
                            'Cache-Control' => 'no-cache, must-revalidate',
                            'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                            'Pragma' => 'no-cache',
                        ]
                    );
                    $response = ['ack' => 'ok'];
                    $this->ajaxDie(json_encode($response));
                } else {
                    $filelist = $this->files_in_dir($ebayTemplateDir);

                    $filestozip = [];

                    foreach ($filelist as $key => $name) {
                        try {
                            $fileName = $ebayTemplateDir . $name;
                            if (!in_array($name, ['README'])) {
                                array_push($filestozip, $fileName);
                            }
                        } catch (Exception $e) {
                            // Nothing
                        }
                    }

                    if (sizeof($filestozip) == 0) {
                        $this->sendHttpHeaders(
                            '204 No Content',
                            [
                                'Cache-Control' => 'no-cache, must-revalidate',
                                'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                                'Pragma' => 'no-cache',
                            ]
                        );
                    } else {
                        $tmpfile = uniqid() . '.zip';
                        $zip = new \ZipArchive();
                        $zipsuccess = $zip->open($tmpfile, \ZipArchive::CREATE);

                        foreach ($filestozip as $file) {
                            $zip->addFromString(basename($file), Tools::file_get_contents($file));
                        }

                        $zip->close();

                        if ($zipsuccess) {
                            $this->sendHttpHeaders(
                                '200 OK',
                                [
                                    'Cache-Control' => 'no-cache, must-revalidate',
                                    'Pragma' => 'no-cache',
                                    'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                                    'X-Codisto-Content-Type' => 'application/zip',
                                    'Content-Type' => 'application/zip, application/octet-stream',
                                    'Content-Disposition' => 'attachment; filename=' . basename($tmpfile),
                                    'Content-Length' => filesize($tmpfile),
                                ]
                            );
                            readfile($tmpfile);
                        } else {
                            $this->sendHttpHeaders(
                                '200 OK',
                                [
                                    'Content-Type' => 'application/json',
                                    'Cache-Control' => 'no-cache, no-store',
                                    'X-Codisto-Content-Type' => 'application/json',
                                    'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                                    'Pragma' => 'no-cache',
                                ]
                            );
                        }
                        unlink($tmpfile);
                    }

                    exit;
                }
            }
        }

        $response = ['ack' => 'failed', 'message' => 'Resource Not Found'];

        $this->sendHttpHeaders(
            '404 Not Found',
            [
                'Content-Type' => 'text/html',
                'Cache-Control' => 'no-cache, no-store',
                'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                'Pragma' => 'no-cache',
            ]
        );

        $this->ajaxDie(json_encode($response));
    }

    // Push Order
    protected function processPostRequest()
    {
        if (!$this->checkHash()) {
            exit;
        }

        $db = Db::getInstance();
        $idLang = (int) Context::getContext()->language->id;
        $type = Tools::getValue('link_rewrite');

        if ($type === 'createorder') {
            try {
                $xml = simplexml_load_string(Tools::file_get_contents('php://input'));

                $ordercontent = $xml->entry->content->children('http://api.codisto.com/schemas/2009/');

                $db->query('SET TRANSACTION ISOLATION LEVEL SERIALIZABLE');
                $db->query('START TRANSACTION');

                $billingAddress = $ordercontent->orderaddresses->orderaddress[0];
                $shippingAddress = $ordercontent->orderaddresses->orderaddress[1];

                $amazonorderid = pSQL($ordercontent->amazonorderid);
                if (!$amazonorderid) {
                    $amazonorderid = '';
                }

                $amazonfulfillmentchannel = pSQL($ordercontent->amazonfulfillmentchannel);
                if (!$amazonfulfillmentchannel) {
                    $amazonfulfillmentchannel = '';
                }

                $ebayusername = pSQL($ordercontent->ebayusername);
                if (!$ebayusername) {
                    $ebayusername = '';
                }

                $ebaysalesrecordnumber = pSQL($ordercontent->ebaysalesrecordnumber);
                if (!$ebaysalesrecordnumber) {
                    $ebaysalesrecordnumber = '';
                }

                $ebaytransactionid = pSQL($ordercontent->ebaytransactionid);
                if (!$ebaytransactionid) {
                    $ebaytransactionid = '';
                }

                $billingFirstName = $billingLastName = 'Noname';
                if (strpos($billingAddress->name, ' ') !== false) {
                    $billingName = explode(' ', $billingAddress->name, 2);
                    $billingFirstName = $billingName[0];
                    $billingLastName = $billingName[1];
                } else {
                    $billingFirstName = $billingAddress->name;
                    $billingLastName = 'Noname';
                }

                $shippingFirstName = $shippingLastName = 'Noname';
                if (strpos($shippingAddress->name, ' ') !== false) {
                    $shippingName = explode(' ', $shippingAddress->name, 2);
                    $shippingFirstName = $shippingName[0];
                    $shippingLastName = $shippingName[1];
                } else {
                    $shippingFirstName = $shippingAddress->name;
                    $shippingLastName = 'Noname';
                }

                // Remove not allowed chars from FirstName and LastName
                $pattern = '/[?:[^0-9!<>,;?=+()\/\\@#"°*`{}_^$%:¤\[\]|\.。]|[\.。](?:\s|$)]+/u';
                $billingFirstName = trim(preg_replace($pattern, ' ', $billingFirstName));
                $billingLastName = trim(preg_replace($pattern, ' ', $billingLastName));
                $shippingFirstName = trim(preg_replace($pattern, ' ', $shippingFirstName));
                $shippingLastName = trim(preg_replace($pattern, ' ', $shippingLastName));

                $invoiceAddress = null;
                $orderId = null;

                if (!empty($ordercontent->orderid) && !empty($ordercontent->ordernumber) && (int) $ordercontent->orderid !== (int) $ordercontent->ordernumber) {
                    $sql = 'SELECT `id_order` FROM ' . _DB_PREFIX_ . "codisto_order_meta WHERE `id_order` = '" . pSQL($ordercontent->ordernumber) . "' AND (`key` = '_codisto_merchantid' AND value = '" . (int) $ordercontent->merchantid . "')' LIMIT 1";
                    $orderId = Db::getInstance()->getValue($sql, false);
                }

                $email = $billingAddress->email;
                if (!$email) {
                    $email = $shippingAddress->email;
                }

                // Create Customer
                if ($email) {
                    $user_sql = 'SELECT * FROM `' . _DB_PREFIX_ . 'customer` WHERE `email` = "' . pSQL($email) . '"';

                    $user = $db->getRow($user_sql);

                    if (!$user && !$orderId) {
                        $password = md5(_COOKIE_KEY_ . Tools::passwdGen(8));
                        $newCustomer = new Customer();
                        $newCustomer->email = $email;
                        $newCustomer->lastname = ($billingLastName) ? $billingLastName : $shippingLastName;
                        $newCustomer->firstname = ($billingFirstName) ? $billingFirstName : $shippingFirstName;
                        $newCustomer->passwd = $password;
                        $newCustomer->is_active = true;
                        $newCustomer->is_guest = true;
                        $newCustomer->add();
                        $customerId = $newCustomer->id;

                        $invoiceAddress = $this->createAddress($customerId, $billingAddress);
                        $idAddressInvoice = $invoiceAddress->id;
                    } else {
                        $customerId = $user['id_customer'];

                        $invoiceAddress = $this->getAddressByCustomerId($customerId);
                        $idAddressInvoice = $invoiceAddress;

                        if (!$invoiceAddress) {
                            $invoiceAddress = $this->createAddress($customerId, $billingAddress);
                            $idAddressInvoice = $invoiceAddress->id;
                        }
                    }
                } else {
                    $customerId = 0;
                }

                $isSameAddress = $this->isSameAddress($billingAddress, $billingFirstName, $billingLastName, $shippingAddress, $shippingFirstName, $shippingLastName);

                if ($isSameAddress) {
                    $idAddressDelivery = (!empty($idAddressInvoice)) ? $idAddressInvoice : '';
                } else {
                    $deliveryAddress = $this->createAddress($customerId, $shippingAddress);
                    $idAddressDelivery = $deliveryAddress->id_address;
                }

                if (!$orderId) {
                    // Create Cart
                    $this->cleanCustomerCarts($customerId);

                    $secureKey = $this->generateSecurityKey();

                    $defaultcurrency = count($ordercontent->defaultcurrency) ? $ordercontent->defaultcurrency : $ordercontent->transactcurrency;
                    $getCurrency = Context::getContext()->currency;
                    $currency = Currency::getIdByIsoCode($defaultcurrency);
                    $currencyId = ($currency) ? $currency->id : $getCurrency->id;

                    $carrierId = 0;
                    $carrierName = (!empty($ordercontent->ordershipments[0])) ? $ordercontent->ordershipments[0]->ordershipment->carrier : '';

                    if (!empty($carrierName)) {
                        $carrierId = $this->getCarrierIdByName($carrierName);
                    } else {
                        $carrierId = Configuration::get('PS_CARRIER_DEFAULT');
                    }

                    if (!$carrierId && !empty($carrierName)) {
                        $carrierId = $this->createPrestaShopCarrier($carrierName);
                    }

                    $countryId = ($shippingAddress->countrycode) ? Country::getByIso($shippingAddress->countrycode) : 0;

                    $cart = new Cart();
                    $cart->id_customer = $customerId;
                    $cart->secure_key = $secureKey;
                    $cart->id_address_delivery = $idAddressDelivery;
                    $cart->id_address_invoice = (!empty($idAddressInvoice)) ? $idAddressInvoice : '';
                    $cart->id_lang = $idLang;
                    $cart->id_currency = $currencyId;
                    $cart->id_carrier = $carrierId;
                    $cart->recyclable = 0;
                    $cart->add();

                    if (!empty($ordercontent->orderlines)) {
                        foreach ($ordercontent->orderlines->orderline as $orderline) {
                            if ($orderline->productcode[0] != 'FREIGHT') {
                                $productcode = $orderline->productcode;
                                if ($productcode == null) {
                                    $productcode = '';
                                }

                                $productname = $orderline->productname;
                                if ($productname == null) {
                                    $productname = '';
                                }

                                $product_id = $orderline->externalreference[0];
                                if ($product_id != null) {
                                    $product_id = (int) $product_id;
                                }

                                $variation_id = null;

                                $product_type = $this->getProductType($productcode);

                                if ($product_type == 'combinations') {
                                    $variation_id = (int) $product_id;
                                    $product_id = $this->getProductIdByIdProductAttribute($product_id);
                                }

                                $qty = (int) $orderline->quantity[0];

                                $cart->updateQty($qty, $product_id, $variation_id);
                            }
                        }
                    }

                    // Add the products to the cart
                    $cart->update();

                    $idOrderState = $this->convertOrderStateToPrestaOrderStatus($ordercontent->orderstate, $ordercontent->paymentstatus, $ordercontent->shipmentstatus);

                    // Creating order from cart
                    $paymentModule = Module::getInstanceByName('ps_wirepayment');
                    $paymentMethod = pSQL($ordercontent->orderpayments[0]->orderpayment->paymentmethod);

                    // if order state is waiting capture or payment failed then $total=0
                    $idOrderState == 19;
                    if ($idOrderState == 19 || $idOrderState == 8) {
                        $total = 0;
                    } else {
                        $cartTotal = (float) $cart->getOrderTotal(true);
                        $total = $cartTotal;
                    }

                    $result = $paymentModule->validateOrder($cart->id, $idOrderState, $total, $paymentMethod, null, [], (int) $cart->id_currency, false, $cart->secure_key);

                    // Get the order id after creating it from the cart.
                    $orderId = Order::getOrderByCartId($cart->id);
                    $order = new Order($orderId);

                    // Create order note
                    $merchantNote = @count($ordercontent->merchantinstructions) ? pSQL($ordercontent->merchantinstructions) : pSQL('');
                    $order->note = $merchantNote;
                    $order->update();

                    if ($ordercontent->paymentstatus == 'complete') {
                        $orderPayment = OrderPayment::getByOrderReference($order->reference);
                        $transactionId = pSQL($ordercontent->orderpayments[0]->orderpayment->transactionid);
                        $paymentMethod = pSQL($ordercontent->orderpayments[0]->orderpayment->paymentmethod);

                        if ($transactionId && $paymentMethod) {
                            if (!empty($orderPayment[0])) {
                                $orderPayment[0]->payment_method = $paymentMethod;
                                $orderPayment[0]->transaction_id = $transactionId;
                                $orderPayment[0]->update();
                            } else {
                                $order->addOrderPayment($order->total_paid_real, $paymentMethod, $transactionId, $order->id_currency);
                            }
                        }
                    }

                    $this->updateOrderMeta($orderId, '_codisto_orderid', (int) $ordercontent->orderid);
                    $this->updateOrderMeta($orderId, '_codisto_merchantid', (int) $ordercontent->merchantid);

                    if ($amazonorderid) {
                        $this->updateOrderMeta($orderId, '_codisto_amazonorderid', $amazonorderid);
                    }

                    if ($amazonfulfillmentchannel) {
                        $this->updateOrderMeta($orderId, '_codisto_amazonfulfillmentchannel', $amazonfulfillmentchannel);
                    }

                    if ($ebayusername) {
                        $this->updateOrderMeta($orderId, '_codisto_ebayusername', $ebayusername);
                    }

                    if ($ebaysalesrecordnumber) {
                        $this->updateOrderMeta($orderId, '_codisto_ebaysalesrecordnumber', $ebaysalesrecordnumber);
                    }

                    if ($ebaytransactionid) {
                        $this->updateOrderMeta($orderId, '_codisto_ebaytransactionid', $ebaytransactionid);
                    }
                } else {
                    $order = new Order((int) $orderId);

                    if ($ordercontent->paymentstatus == 'complete') {
                        $orderPayment = OrderPayment::getByOrderReference($order->reference);
                        $transactionId = pSQL($ordercontent->orderpayments[0]->orderpayment->transactionid);
                        $paymentMethod = pSQL($ordercontent->orderpayments[0]->orderpayment->paymentmethod);

                        if ($transactionId && $paymentMethod) {
                            if (!empty($orderPayment[0])) {
                                $orderPayment[0]->payment_method = $paymentMethod;
                                $orderPayment[0]->transaction_id = $transactionId;
                                $orderPayment[0]->update();
                            } else {
                                $order->addOrderPayment($order->total_paid_real, $paymentMethod, $transactionId, $order->id_currency);
                            }
                        }
                    }
                }

                if (is_object($order)) {
                    $idOrderState = $this->convertOrderStateToPrestaOrderStatus($ordercontent->orderstate, $ordercontent->paymentstatus, $ordercontent->shipmentstatus);

                    $order->setCurrentState($idOrderState);
                    $order->save();
                }

                $db->query('COMMIT');

                $response = ['ack' => 'ok', 'orderid' => $orderId];

                $this->sendHttpHeaders(
                    '200 OK',
                    [
                        'Content-Type' => 'application/json',
                        'Cache-Control' => 'no-cache, no-store',
                        'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                        'Pragma' => 'no-cache',
                    ]
                );

                $this->ajaxDie(json_encode($response));
            } catch (Exception $e) {
                $db->query('ROLLBACK');
                $response = ['ack' => 'failed', 'message' => $e->getMessage() . '  ' . $e->getFile() . ' ' . $e->getLine()];

                $this->sendHttpHeaders(
                    '200 OK',
                    [
                        'Content-Type' => 'application/json',
                        'Cache-Control' => 'no-cache, no-store',
                        'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                        'Pragma' => 'no-cache',
                    ]
                );

                $this->ajaxDie(json_encode($response));
            }
        } elseif ($type === 'sync') {
            if ($_SERVER['HTTP_X_ACTION'] === 'TEMPLATE') {
                if (!$this->checkHash()) {
                    exit;
                }

                $ebayTemplateDir = _PS_ROOT_DIR_ . '/upload/codistoebaytemplates/';
                $tmpPath = uniqid() . '.html';

                @file_put_contents($tmpPath, Tools::file_get_contents('php://input'));

                $db = new PDO('sqlite:' . $tmpPath);
                $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                $db->exec('PRAGMA synchronous=0');
                $db->exec('PRAGMA temp_store=2');
                $db->exec('PRAGMA page_size=65536');
                $db->exec('PRAGMA encoding=\'UTF-8\'');
                $db->exec('PRAGMA cache_size=15000');
                $db->exec('PRAGMA soft_heap_limit=67108864');
                $db->exec('PRAGMA journal_mode=MEMORY');

                $files = $db->prepare('SELECT Name, Content FROM File');
                $files->execute();

                $files->bindColumn(1, $name);
                $files->bindColumn(2, $content);

                while ($files->fetch()) {
                    $fileName = $ebayTemplateDir . $name;

                    if (strpos($name, '..') === false) {
                        if (!file_exists($fileName)) {
                            $dir = dirname($fileName);

                            if (!is_dir($dir)) {
                                mkdir($dir . '/', 0755, true);
                            }

                            @file_put_contents($fileName, $content);
                        }
                    }
                }

                $db = null;
                unlink($tmpPath);

                $this->sendHttpHeaders(
                    '200 OK',
                    [
                        'Content-Type' => 'application/json',
                        'Cache-Control' => 'no-cache, no-store',
                        'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                        'Pragma' => 'no-cache',
                    ]
                );

                $response = ['ack' => 'ok'];

                $this->ajaxDie(json_encode($response));
            }
        }

        $response = ['ack' => 'failed', 'message' => 'Resource Not Found'];

        $this->sendHttpHeaders(
            '404 Not Found',
            [
                'Content-Type' => 'text/html',
                'Cache-Control' => 'no-cache, no-store',
                'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                'Pragma' => 'no-cache',
            ]
        );

        $this->ajaxDie(json_encode($response));
    }

    protected function processPutRequest()
    {
        // do something then output the result
        $this->ajaxDie(json_encode([
            'success' => true,
            'operation' => 'put',
        ]));
    }

    protected function processDeleteRequest()
    {
        // do something then output the result
        $this->ajaxDie(json_encode([
            'success' => true,
            'operation' => 'delete',
        ]));
    }

    public function cleanCustomerCarts($customerId)
    {
        $customerCarts = Cart::getCustomerCarts($customerId, false);

        foreach ($customerCarts as $singleCart) {
            $tmpCart = new Cart($singleCart['id_cart']);
            $tmpCart->delete();
        }
    }

    public function generateSecurityKey()
    {
        return md5(uniqid(mt_rand(), true));
    }

    public function getAddressByCustomerId($customerId)
    {
        $sql = 'SELECT `id_address` FROM ' . _DB_PREFIX_ . "address WHERE id_customer = '" . (int) $customerId . "' and deleted = 0";

        return Db::getInstance()->getValue($sql);
    }

    public function createAddress($customerId, $customerAddress)
    {
        $countryId = ($customerAddress->countrycode) ? Country::getByIso($customerAddress->countrycode) : 0;
        $state_id = ($customerAddress->division) ? State::getIdByName($customerAddress->division) : 0;

        $address = new Address();
        $address->alias = ($customerAddress->companyname) ? $customerAddress->companyname : 'Home';
        $this->addName($address, $customerAddress);
        $address->city = ($customerAddress->place) ? $customerAddress->place : '';
        $address->id_state = ($state_id) ? $state_id : 0;
        $address->id_customer = $customerId;
        $address->id_country = ($countryId) ? $countryId : 0;
        $address->address1 = ($customerAddress->address1) ? $customerAddress->address1 : '';
        $address->address2 = $customerAddress->address2 ? $customerAddress->address2 : '';
        $address->phone = $customerAddress->phone ? $customerAddress->phone : '';
        $address->postcode = $customerAddress->postalcode ? $customerAddress->postalcode : '';
        $address->active = 1;
        $address->add();

        return $address;
    }

    public function isSameAddress($billingAddress, $billingFirstName, $billingLastName, $shippingAddress, $shippingFirstName, $shippingLastName)
    {
        if ($billingFirstName !== $shippingFirstName) {
            return false;
        }

        if ($billingLastName !== $shippingLastName) {
            return false;
        }

        if (isset($billingAddress->address1) && !isset($shippingAddress->address1)) {
            return false;
        }

        if (isset($billingAddress->address2) && !isset($shippingAddress->address2)) {
            return false;
        }

        if (trim($billingAddress->address1) !== trim($shippingAddress->address1)) {
            return false;
        }

        if (trim($billingAddress->address2) !== trim($shippingAddress->address2)) {
            return false;
        }

        if (isset($billingAddress->city, $shippingAddress->city)
            && trim($billingAddress->city) !== trim($shippingAddress->city)) {
            return false;
        }

        return true;
    }

    public function addName($address, $customer_address)
    {
        $firstName = $lastName = 'Noname';
        if (strpos($customer_address->name, ' ') !== false) {
            $name = explode(' ', $customer_address->name, 2);
            $firstName = $name[0];
            $lastName = $name[1];
        } else {
            $firstName = $customer_address->name;
            $lastName = 'Noname';
        }

        $address->firstname = $firstName;
        $address->lastname = $lastName;

        return $address;
    }

    public function getCarrierIdByName($carrier_name)
    {
        $carrierId = 0;

        $sql = 'SELECT `id_carrier` FROM ' . _DB_PREFIX_ . "carrier WHERE `deleted` = 0 AND `name` = '" . pSQL($carrier_name) . "'";

        $carrierId = Db::getInstance()->getValue($sql, false);

        if (!$carrierId) {
            $carrierId = Configuration::get('PS_CARRIER_DEFAULT');
        }

        return $carrierId;
    }

    public function createPrestaShopCarrier($carrier_name)
    {
        $carrier = new Carrier();
        $carrier->name = $carrier_name;
        $carrier->delay[Configuration::get('PS_LANG_DEFAULT')] = $carrier_name;

        if (!$carrier->add()) {
            return false;
        }

        // Associate carrier to all groups
        $groups = Group::getGroups(true);
        foreach ($groups as $group) {
            Db::getInstance()->insert('carrier_group', ['id_carrier' => (int) $carrier->id, 'id_group' => (int) $group['id_group']]);
        }

        // Create price range
        $rangePrice = new RangePrice();
        $rangePrice->id_carrier = $carrier->id;
        $rangePrice->delimiter1 = '0';
        $rangePrice->delimiter2 = '10000';
        $rangePrice->add();

        // Create weight range
        $rangeWeight = new RangeWeight();
        $rangeWeight->id_carrier = $carrier->id;
        $rangeWeight->delimiter1 = '0';
        $rangeWeight->delimiter2 = '10000';
        $rangeWeight->add();

        // Associate carrier to all zones
        $zones = Zone::getZones(true);
        foreach ($zones as $zone) {
            Db::getInstance()->insert('carrier_zone', ['id_carrier' => (int) $carrier->id, 'id_zone' => (int) $zone['id_zone']]);
            Db::getInstance()->insert('delivery', ['id_carrier' => (int) $carrier->id, 'id_range_price' => (int) $rangePrice->id, 'id_range_weight' => null, 'id_zone' => (int) $zone['id_zone'], 'price' => 0]);
            Db::getInstance()->insert('delivery', ['id_carrier' => (int) $carrier->id, 'id_range_price' => null, 'id_range_weight' => (int) $rangeWeight->id, 'id_zone' => (int) $zone['id_zone'], 'price' => 0]);
        }

        // Save the carrier ID in the Configuration table
        Configuration::updateValue($carrier_name, $carrier->id);

        return $carrier->id;
    }

    public function convertOrderStateToPrestaOrderStatus($order_status, $payment_status = '', $shipment_status = '')
    {
        if ($payment_status == 'cancelled') {
            return self::STATE_PAYMENT_FAILED;
        }

        if ($order_status == 'captured' && $payment_status == 'complete') {
            return self::STATE_PAID;
        }

        if ($order_status == 'inprogress' && $payment_status == 'complete') {
            return self::STATE_PROCESSING_PROGRESS;
        }

        if ($order_status == 'complete' && $payment_status == 'complete' && $shipment_status == 'complete') {
            return self::STATE_SHIPPED;
        }

        if ($order_status == 'cancelled') {
            return self::STATE_CANCELED;
        }

        return self::STATE_WAITING_CAPTURE;
    }

    public function getTrackingNumber($orderId)
    {
        $sql = 'SELECT `tracking_number` FROM `' . _DB_PREFIX_ . 'order_carrier` WHERE `id_order` = ' . (int) $orderId;

        $trackingNumber = Db::getInstance()->getValue($sql, false);

        return !empty($trackingNumber) ? $trackingNumber : null;
    }

    public function getCarrier($carrier_id)
    {
        $sql = 'SELECT `name` FROM `' . _DB_PREFIX_ . 'carrier` WHERE `id_carrier` = ' . (int) $carrier_id;

        $carrier = Db::getInstance()->getValue($sql, false);

        return !empty($carrier) ? $carrier : null;
    }

    public function getPaymentDate($order_reference)
    {
        $sql = 'SELECT `date_add` FROM `' . _DB_PREFIX_ . "order_payment` WHERE `order_reference` = '" . pSQL($order_reference) . "'";

        $payDate = Db::getInstance()->getValue($sql, false);

        return !empty($payDate) ? $payDate : null;
    }

    public function getCurrentStatus($id_lang, $current_state)
    {
        return Db::getInstance()->getValue('
            SELECT osl.`name`
            FROM `' . _DB_PREFIX_ . 'order_state` os
            LEFT JOIN `' . _DB_PREFIX_ . 'order_state_lang` osl ON (osl.`id_order_state` = os.`id_order_state`)
            WHERE osl.`id_lang` = ' . (int) $id_lang . ' AND os.`id_order_state` = ' . (int) $current_state);
    }

    public function hasKeyOrderMeta($orderId, $key)
    {
        return Db::getInstance()->getValue('
            SELECT `value`
            FROM `' . _DB_PREFIX_ . 'codisto_order_meta`
            WHERE `id_order` = ' . (int) $orderId . ' AND `key` = "' . pSQL($key) . '"');
    }

    public function updateOrderMeta($orderId, $key, $value)
    {
        $key_exists = $this->hasKeyOrderMeta($orderId, $key);
        $result = true;
        $db = Db::getInstance();
        if ($key_exists) {
            $sqlUpdate = 'UPDATE ' . _DB_PREFIX_ . 'codisto_order_meta SET
                    `value` = "' . pSQL($value) . '"
                    WHERE `id_order` = ' . (int) $orderId . ' AND `key` = "' . pSQL($key) . '"';

            $result &= $db->execute($sqlUpdate);
        } else {
            $sqlInsert = 'INSERT INTO `' . _DB_PREFIX_ . 'codisto_order_meta` (`id_order`, `key`, `value`) VALUES(' . (int) $orderId . ', \'' . pSQL($key) . '\', \'' . pSQL($value) . '\')';

            $result &= $db->execute($sqlInsert);
        }

        return (bool) $result;
    }

    public function getFeatureValue($id_feature_value, $id_lang)
    {
        return Db::getInstance()->getValue('
            SELECT value
            FROM `' . _DB_PREFIX_ . 'feature_value_lang`
            WHERE `id_feature_value` = ' . (int) $id_feature_value . '
            AND `id_lang` = ' . (int) $id_lang . '
        ');
    }

    public function getTaxRuleGroupNameById($id_tax_rules_group)
    {
        return Db::getInstance()->getValue(
            'SELECT `name`
            FROM `' . _DB_PREFIX_ . 'tax_rules_group` rg
            WHERE `id_tax_rules_group` = ' . (int) $id_tax_rules_group . '
        ');
    }

    public function getTaxes($id_lang)
    {
        return Db::getInstance()->executeS(
            '
            SELECT g.`id_tax_rule`,
            tl.`name` AS name,
            trg.`name` AS class,
            c.`iso_code` AS country,
            s.`iso_code` AS state,
            t.`rate`,
            g.`zipcode_from`, g.`zipcode_to`,
            g.`behavior`,
            g.`id_country`,
            g.`id_state`
        FROM `' . _DB_PREFIX_ . 'tax_rule` g
        LEFT JOIN `' . _DB_PREFIX_ . 'country` c ON (g.`id_country` = c.`id_country`)
        LEFT JOIN `' . _DB_PREFIX_ . 'state` s ON (g.`id_state` = s.`id_state`)
        LEFT JOIN `' . _DB_PREFIX_ . 'tax` t ON (g.`id_tax` = t.`id_tax`)
        LEFT JOIN `' . _DB_PREFIX_ . 'tax_lang` tl ON (g.`id_tax` = tl.`id_tax` AND `id_lang` = ' . (int) $id_lang . ')
        LEFT JOIN `' . _DB_PREFIX_ . 'tax_rules_group` trg ON (g.`id_tax_rules_group` = trg.`id_tax_rules_group`)
        WHERE trg.`deleted` = 0
        ORDER BY `country` ASC, `state` ASC, `zipcode_from` ASC, `zipcode_to` ASC'
        );
    }

    public function getProductType($productcode)
    {
        return Db::getInstance()->getValue(
            'SELECT p.`product_type`
            FROM `' . _DB_PREFIX_ . 'product` p
            LEFT JOIN `' . _DB_PREFIX_ . 'product_attribute` pa
            ON p.`id_product` = pa.`id_product`
            WHERE p.`reference` = "' . pSQL($productcode) . '"
        ');
    }

    public function getProductIdByIdProductAttribute($id_product_attribute)
    {
        return Db::getInstance()->getValue(
            'SELECT `id_product`
            FROM `' . _DB_PREFIX_ . 'product_attribute`
            WHERE `id_product_attribute` = ' . (int) $id_product_attribute . '
        ');
    }

    // recursively scan a directory returning an array of all files contained within
    private function files_in_dir($dir, $prefix = '')
    {
        $dir = rtrim($dir, '\\/');
        $result = [];

        try {
            if (is_dir($dir)) {
                $scan = @scandir($dir);

                if ($scan !== false) {
                    foreach ($scan as $f) {
                        if ($f !== '.' and $f !== '..') {
                            if (is_dir("$dir/$f")) {
                                $result = array_merge($result, $this->files_in_dir("$dir/$f", "$f/"));
                            } else {
                                $result[] = $prefix . $f;
                            }
                        }
                    }
                }
            }
        } catch (Exception $e) {
            // Nothing
        }

        return $result;
    }
}
