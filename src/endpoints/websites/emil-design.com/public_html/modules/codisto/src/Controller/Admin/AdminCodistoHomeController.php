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

namespace PrestaShop\Module\Codisto\Controller\Admin;

if (!defined('_PS_VERSION_')) {
    exit;
}

use Configuration;
use Module;
use PrestaShop\PrestaShop\Adapter\SymfonyContainer;
use PrestaShopBundle\Controller\Admin\FrameworkBundleAdminController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Tools;

if (!defined('_PS_BASE_URL_SSL_')) {
    define('_PS_BASE_URL_SSL_', Tools::getShopDomainSsl(true));
}

class AdminCodistoHomeController extends FrameworkBundleAdminController
{
    const BASE_URL = _PS_BASE_URL_SSL_ . __PS_BASE_URI__ . 'index.php/codisto-proxy/';

    /**
     * Common http status and header output function
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

    /**
     * common function used to render a proxied codisto page that checks
     * for a valid registered Codisto account
     *
     * @param string $url used to render an iframe to hold the locally proxied content
     * @param string $tabclass used to apply a css class to the iframe for specialised frame styling
     */
    private function adminTab($url, $tabclass)
    {
        $response = new Response();
        $merchantId = Configuration::get('CODISTO_MERCHANTID');

        if (!is_numeric($merchantId)) {
            // generate admin url
            $actionUrl = SymfonyContainer::getInstance()->get('router')->generate('admin_codisto_create');
            $html = '';

            $html = '<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:500,900,700,400">
			<link rel="stylesheet" href="http://fonts.googleapis.com/icon?family=Material+Icons">

			<iframe id="dummy-data" frameborder="0" src="http://codisto.com/xpressgriddemo/ebayedit/"></iframe>
			<div id="dummy-data-overlay"></div>
			<div id="create-account-modal">
				<h1>Create your Account</h1>
				<div class="body">
                    <form id="codisto-form" action="' . $actionUrl . '" method="post">
						<p>To get started, enter your email address.</p>
						<p>Your email address and phone number will be used to communicate important account information and to
							provide a better support experience for any enquiries with your Codisto account.</p>

						<input type="hidden" name="method" value="email"/>

                        <div>
							<label for="email"><i class="material-icons">email</i></label> <input type="email" id="email" name="email" required placeholder="Enter Your Email Address" size="40">
							<div class="help-text email-help-text" data-defaultmessage="Email is required" data-invalidmessage="Please enter a valid email"></div>
						</div>
						<div>
							<label for="emailconfirm"><i class="material-icons">email</i></label> <input type="email" id="emailconfirm" name="emailconfirm" required placeholder="Confirm Your Email Address" size="40">
							<div class="help-text emailconfirm-help-text" data-defaultmessage="Confirm Email is required" data-invalidmessage="Please enter a valid confirm email"></div>
						</div>

						<div>
							<label for="phone"><i class="material-icons">phone_in_talk</i></label> <input type="tel" id="phone" name="phone" required placeholder="Enter your Phone Number (incl. country code)" size="40">
							<div class="help-text phone-help-text" data-defaultmessage="Phone is required" data-invalidmessage="Please enter a valid phone number"></div>
						</div>

						<div class="selection" style="display:none">
							<label for="countrycode"><i class="material-icons">language</i></label> <div class="select-html-wrapper"></div>
							<br/>
							This is important for creating your initial store defaults.
							<br/>
							<br/>
						</div>

						<div class="next">
							<button type="submit" class="button btn-lg">Continue <i class="material-icons">keyboard_arrow_right</i></button>
						</div>
						<div class="error-message">
							<strong>Your email addresses do not match.</strong>
						</div>

					</form>
				</div>
				<div class="footer">
					Once you create an account we will begin synchronizing your catalog data.<br>
					Sit tight, this may take several minutes depending on the size of your catalog.<br>
					When completed, you\'ll have the world\'s best eBay & Amazon integration at your fingertips.<br>
				</div>

			</div>';

            $response->setStatusCode(202);
            $response->headers->set('Content-Type', 'text/html');
            $response->setContent($html);

            return $response;
        }

        $response->setStatusCode(200);

        return $response;
    }

    /**
     * Home layout show
     */
    public function homeAction(Request $request)
    {
        $merchantId = Configuration::get('CODISTO_MERCHANTID');
        $proxyUrl = self::BASE_URL . 'ebaytab/0/' . $merchantId . '/';
        $res = $this->adminTab($proxyUrl, 'codisto-bulk-editor');
        $helpLink = $this->generateSidebarLink($request->attributes->get('_legacy_controller'));

        return $this->viewAction($res, $proxyUrl, 'Home', $helpLink);
    }

    /**
     * Listings layout show
     */
    public function listingsAction(Request $request)
    {
        $merchantId = Configuration::get('CODISTO_MERCHANTID');
        $proxyUrl = self::BASE_URL . 'ebaytab/0/' . $merchantId . '/listings/';
        $res = $this->adminTab($proxyUrl, 'codisto-bulk-editor');
        $helpLink = $this->generateSidebarLink($request->attributes->get('_legacy_controller'));

        return $this->viewAction($res, $proxyUrl, 'Listings', $helpLink);
    }

    /**
     * Orders layout show
     */
    public function ordersAction(Request $request)
    {
        $merchantId = Configuration::get('CODISTO_MERCHANTID');
        $proxyUrl = self::BASE_URL . 'ebaytab/0/' . $merchantId . '/orders/';
        $res = $this->adminTab($proxyUrl, 'codisto-bulk-editor');
        $helpLink = $this->generateSidebarLink($request->attributes->get('_legacy_controller'));

        return $this->viewAction($res, $proxyUrl, 'Orders', $helpLink);
    }

    /**
     * Settings layout show
     */
    public function settingsAction(Request $request)
    {
        $merchantId = Configuration::get('CODISTO_MERCHANTID');
        $proxyUrl = self::BASE_URL . 'ebaytab/0/' . $merchantId . '/settings/';
        $res = $this->adminTab($proxyUrl, 'codisto-bulk-editor');
        $helpLink = $this->generateSidebarLink($request->attributes->get('_legacy_controller'));

        return $this->viewAction($res, $proxyUrl, 'Settings', $helpLink);
    }

    /**
     * Account layout show
     */
    public function accountAction(Request $request)
    {
        $merchantId = Configuration::get('CODISTO_MERCHANTID');
        $proxyUrl = self::BASE_URL . 'ebaytab/0/' . $merchantId . '/account/';
        $res = $this->adminTab($proxyUrl, 'codisto-bulk-editor');
        $helpLink = $this->generateSidebarLink($request->attributes->get('_legacy_controller'));

        return $this->viewAction($res, $proxyUrl, 'Account', $helpLink);
    }

    public function viewAction($res, $proxyUrl, $layout_title, $helpLink)
    {
        if ($res->getStatusCode() === 200) {
            return $this->render('@Modules/codisto/views/templates/admin/home.html.twig', [
                'adminUrl' => $proxyUrl,
                'enableSidebar' => true,
                'help_link' => $helpLink,
                'layoutTitle' => $layout_title,
            ]);
        } else {
            return $this->render('@Modules/codisto/views/templates/admin/create_account.html.twig', [
                'html' => $res->getContent(),
                'enableSidebar' => true,
                'help_link' => $helpLink,
                'layoutTitle' => $layout_title,
            ]);
        }
    }

    // POST handler for create account on codisto servers for this prestashop instance
    public function createAccountAction()
    {
        $shop_name = Configuration::get('PS_SHOP_NAME');
        $module = Module::getInstanceByName('codisto');
        $version = $module->version;
        $remoteUrl = 'https://ui.codisto.com/create';
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            if (Tools::getValue('method') == 'email') {
                $signupemail = stripslashes(Tools::getValue('email'));
                $signupcountry = !empty(Tools::getValue('countrycode')) ? stripslashes(Tools::getValue('countrycode')) : '';
                $signupphone = stripslashes(Tools::getValue('phone'));

                $requestHeaders = [
                    'method: POST',
                    'timeout: 60',
                    'httpversion: 1.0',
                    'redirection: 0',
                    'Content-Type: application/json',
                ];

                $body = json_encode(
                    [
                        'type' => 'prestashop',
                        'version' => _PS_VERSION_,
                        'url' => _PS_BASE_URL_SSL_,
                        'email' => $signupemail,
                        'phone' => $signupphone,
                        'country' => $signupcountry,
                        'storename' => $shop_name,
                        'resellerkey' => '',
                        'codistoversion' => $version,
                    ]
                );

                $ch = curl_init();
                curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
                curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
                curl_setopt($ch, CURLOPT_URL, $remoteUrl);
                curl_setopt($ch, CURLOPT_HTTPHEADER, $requestHeaders);
                curl_setopt($ch, CURLOPT_POST, 1);
                curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

                $response = curl_exec($ch);
                $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
                curl_close($ch);

                $result = json_decode($response, true);

                Configuration::updateValue('CODISTO_MERCHANTID', $result['merchantid']);
                Configuration::updateValue('CODISTO_KEY', $result['hostkey']);
            }
        }

        return $this->redirectToRoute('admin_codistohome');
    }

    /**
     * eBay Template layout show
     */
    public function templateAction(Request $request)
    {
        $ext_file = ['html'];
        $current_page_url = SymfonyContainer::getInstance()->get('router')->generate('admin_codistoebay_templates');

        $updated = false;
        $file_error = false;
        $ext_error = false;

        if (!empty(Tools::getValue('updated')) && (Tools::getValue('file') != '_new')) {
            $updated = true;
        }

        if (!empty(Tools::getValue('file_error'))) {
            $file_error = true;
        }

        if (!empty(Tools::getValue('ext_error'))) {
            $ext_error = true;
        }

        if (!empty(Tools::getValue('file'))) {
            $filename = stripslashes(Tools::getValue('file'));
            $info = pathinfo($filename);
            if (((!empty($info['extension']) && !in_array($info['extension'], $ext_file)) || !file_exists(_PS_ROOT_DIR_ . '/upload/codistoebaytemplates/' . $filename)) && (Tools::getValue('file') != '_new')) {
                $filename = 'default.html';
            }
        } else {
            $filename = 'default.html';
        }

        $file = _PS_ROOT_DIR_ . '/upload/codistoebaytemplates/' . $filename;

        if (file_exists($file)) {
            $content = @Tools::file_get_contents($file);
            if (!$content) {
                $content = '';
            }
        } else {
            $content = '';
        }

        $list_files_html = '';
        if (is_dir(_PS_ROOT_DIR_ . '/upload/codistoebaytemplates/')) {
            $files = scandir(_PS_ROOT_DIR_ . '/upload/codistoebaytemplates/');
        } else {
            $files = [];
        }

        $list_files_html .= '<ul class="file-list">';

        foreach ($files as $list_file) {
            if ($list_file[0] === '.') {
                continue;
            }

            if (is_dir(_PS_ROOT_DIR_ . '/upload/codistoebaytemplates/' . $list_file)) {
                continue;
            }

            $list_files_html .= '<li><a href="' . $current_page_url . '&file=' . urlencode($list_file) . '"><span ' . ($list_file == $filename ? 'class="highlight"' : '') . '>' . htmlspecialchars($list_file) . '</span></a></li>';
        }

        $list_files_html .= '<li><button class="button btn btn-primary pointer new-template"><i class="material-icons">add_circle_outline</i> New Template</button></li>';

        $list_files_html .= '</ul>';

        $action_url = SymfonyContainer::getInstance()->get('router')->generate('admin_codisto_update_template');

        $templatepreview = self::BASE_URL . 'ebaytab/templatepreview#1';

        return $this->render('@Modules/codisto/views/templates/admin/templates.html.twig', [
            'filename' => $filename,
            'list_files' => $list_files_html,
            'action_url' => $action_url,
            'content' => htmlspecialchars($content),
            'updated' => $updated,
            'file_error' => $file_error,
            'ext_error' => $ext_error,
            'templatepreview' => $templatepreview,
            'enableSidebar' => true,
            'help_link' => $this->generateSidebarLink($request->attributes->get('_legacy_controller')),
            'layoutTitle' => 'eBay Templates',
        ]);
    }

    // POST handler for saving edits to templates
    public function updateTemplateAccountAction(Request $request)
    {
        $filename = stripslashes(Tools::getValue('file'));
        $ext_file = ['html'];
        $info = pathinfo($filename);

        $file_error = false;
        $ext_error = false;
        if (preg_match('/[^a-z0-9\_\-\.]/i', $filename)) {
            $file_error = true;

            return $this->redirectToRoute('admin_codistoebay_templates', ['file_error' => ($file_error ? '&file_error=true' : ''), 'file' => '_new']);
        }

        $content = stripslashes(Tools::getValue('newcontent'));

        $dir = _PS_ROOT_DIR_ . '/upload/codistoebaytemplates/';
        if (in_array($info['extension'], $ext_file)) {
            $file = _PS_ROOT_DIR_ . '/upload/codistoebaytemplates/' . $filename;
        } else {
            $ext_error = true;

            return $this->redirectToRoute('admin_codistoebay_templates', ['ext_error' => ($ext_error ? '&ext_error=true' : ''), 'file' => '_new']);
        }

        if (!is_dir($dir)) {
            mkdir($dir, 0755, true);
        }

        $updated = false;

        $f = fopen($file, 'w');
        if ($f !== false) {
            fwrite($f, $content);
            fclose($f);

            $updated = true;
        }

        return $this->redirectToRoute('admin_codistoebay_templates', ['file' => urlencode($filename), 'updated' => ($updated ? '&updated=true' : '')]);
    }
}
