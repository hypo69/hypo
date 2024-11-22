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

class CodistoProxyModuleFrontController extends AbstractCodistoController
{
    private function sendHttpHeaders($status, $headers)
    {
        $statusheader = preg_split('/ /', $status, 2);
        http_response_code((int) $statusheader[0]);
        foreach ($headers as $header => $value) {
            header($header . ': ' . $value);
        }
    }

    protected function processGetRequest()
    {
        $this->proxy();
    }

    protected function processPostRequest()
    {
        $this->proxy();
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

    public function proxy()
    {
        $cookie = new Cookie('psAdmin');
        if (!$cookie->id_employee) {
            exit('Unauthorized');
        }

        $merchantid = Configuration::get('CODISTO_MERCHANTID');
        $db = Db::getInstance();
        $idLang = (int) Context::getContext()->language->id;
        $proxy = Tools::getValue('link_rewrite');
        $hostKey = Configuration::get('CODISTO_KEY');
        $module = Module::getInstanceByName('codisto');
        $version = $module->version;
        $querystring = preg_replace('/q=[^&]*&/', '', $_SERVER['QUERY_STRING']);
        $path = $proxy;
        $storeId = '0';
        $merchantid = Configuration::get('CODISTO_MERCHANTID');
        $bodyStr = '';

        if (!empty(Tools::getValue('merchantid'))) {
            $merchantid = (int) Tools::getValue('merchantid');
        } else {
            $storematch = [];

            if (preg_match('/^ebaytab\/(\d+)\/(\d+)(?:\/|$)/', $path, $storematch)) {
                $storeId = (int) $storematch[1];
                $merchantid = (int) $storematch[2];

                $path = preg_replace('/(^ebaytab\/)(\d+\/?)(\d+\/?)/', '$1', $path);
            }

            if (preg_match('/^ebaytab\/(\d+)(?:\/|$)/', $path, $storematch)) {
                if (isset($storematch[2])) {
                    $merchantid = (int) $storematch[2];
                }

                $path = preg_replace('/(^ebaytab\/)(\d+\/?)/', '$1', $path);
            }
        }

        if (!$merchantid) {
            $this->sendHttpHeaders(
                '404 Not Found',
                [
                    'Content-Type' => 'text/html',
                    'Cache-Control' => 'no-cache, no-store',
                    'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                    'Pragma' => 'no-cache',
                ]
            );

            ?>
            <h1>Resource Not Found</h1>
            <?php
            exit;
        }

        $remoteUrl = 'https://ui.codisto.com/' . $merchantid . '/' . $path . ($querystring ? '?' . $querystring : '');

        // generate admin url
        $base_url = _PS_BASE_URL_SSL_ . __PS_BASE_URI__ . 'index.php/codisto-proxy/';
        $adminUrl = $base_url . 'ebaytab/' . $storeId . '/' . $merchantid . '/';

        $requestHeaders = [
            'X-Codisto-Cart: prestashop',
            'X-Codisto-Version:' . $version,
            'X-HostKey:' . $hostKey,
            'X-Admin-Base-Url:' . $adminUrl,
            'Accept-Encoding: ',
            'method:' . $_SERVER['REQUEST_METHOD'],
            'timeout: 120',
            'httpversion: 1.0',
            'decompress: false',
            'redirection: 0',
        ];

        if (array_key_exists('CONTENT_TYPE', $_SERVER)) {
            $requestHeaders[] = 'Content-Type: ' . $_SERVER['CONTENT_TYPE'];
        }

        for ($retry = 0;; $retry = $retry + 1) {
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
            curl_setopt($ch, CURLOPT_URL, $remoteUrl);
            curl_setopt($ch, CURLOPT_HTTPHEADER, $requestHeaders);
            curl_setopt($ch, CURLOPT_HEADER, true);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

            if (strtolower($_SERVER['REQUEST_METHOD']) == 'post') {
                $remoteUrl = 'https://ui.codisto.com/' . $merchantid . '/';
                curl_setopt($ch, CURLOPT_POST, true);
                $body = Tools::file_get_contents('php://input');
                if (preg_match("/application\/json/i", $_SERVER['CONTENT_TYPE'])) {
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
                } else {
                    parse_str($body, $data);
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
                }
            }

            $result = curl_exec($ch);
            $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            $curlErr = curl_error($ch);

            if ($curlErr) {
                if ($retry >= 3) {
                    $this->sendHttpHeaders(
                        '500 Server Error',
                        [
                            'Content-Type' => 'text/html',
                            'Cache-Control' => 'no-cache, no-store',
                            'Expires' => 'Thu, 01 Jan 1970 00:00:00 GMT',
                            'Pragma' => 'no-cache',
                        ]
                    );
                    echo '<h1>Error processing request</h1><p>' . htmlspecialchars($curlErr) . '</p>';
                    exit;
                }

                sleep(2);
                continue;
            }

            // how big are the headers
            $headerSize = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
            $headerStr = substr($result, 0, $headerSize);
            $bodyStr = substr($result, $headerSize);

            // convert headers to array
            $headerArr = explode(PHP_EOL, $headerStr);
            foreach ($headerArr as $headerRow) {
                preg_match('/([a-zA-Z\-]+):\s(.+)$/', $headerRow, $matches);
                if (!isset($matches[0])) {
                    continue;
                }
                $headers[$matches[1]] = $matches[2];
            }
            curl_close($ch);
            break;
        }

        if ($httpcode > 300 || $httpcode <= 400) {
            $filterHeaders = ['server', 'content-length', 'transfer-encoding', 'date', 'connection', 'x-storeviewmap', 'content-encoding'];

            if (!empty($headers)) {
                foreach ($headers as $header => $value) {
                    if (!in_array(strtolower($header), $filterHeaders, true)) {
                        if (is_array($value)) {
                            header($header . ': ' . $value[0], true);
                            for ($i = 1; $i < count($value); $i = $i + 1) {
                                header($header . ': ' . $value[$i], false);
                            }
                        } else {
                            header($header . ': ' . $value, true);
                        }
                    }
                }
            }
        }

        file_put_contents('php://output', $bodyStr);
        exit;
    }
}
