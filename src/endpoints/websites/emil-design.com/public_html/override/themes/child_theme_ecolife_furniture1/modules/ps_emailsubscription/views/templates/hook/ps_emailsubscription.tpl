{**
* 2007-2018 PrestaShop
*
* NOTICE OF LICENSE
*
* This source file is subject to the Academic Free License 3.0 (AFL-3.0)
* that is bundled with this package in the file LICENSE.txt.
* It is also available through the world-wide-web at this URL:
* https://opensource.org/licenses/AFL-3.0
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
* @author    PrestaShop SA <contact@prestashop.com>
* @copyright 2007-2018 PrestaShop SA
* @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
* International Registered Trademark & Property of PrestaShop SA
*}

<div class="block_newsletter ft_newsletter col-footer" id="blockEmailSubscription_{$hookName}" style="margin:0;"> 
	<p>{$conditions}</p>
	<div class="col col_form">
		<form action="{$urls.current_url}#blockEmailSubscription_{$hookName}" method="post">
			<input
			class="btn btn-primary"
			name="submitNewsletter"
			type="submit"
			value="{l s='Sign up' d='Shop.Theme.Actions'}"
			>
			<div class="input-wrapper">
			<input
			name="email"
			type="email"
			value="{$value}"
			placeholder="{l s='Your email address' d='Shop.Forms.Labels'}"
			>
			</div>
			<input type="hidden" name="action" value="0">
			<div class="clearfix"></div>
			{if $msg}
			<p class="alert {if $nw_error}alert-danger{else}alert-success{/if}">
			{$msg}
			</p>
			{/if}
			{if isset($id_module)}
			{hook h='displayGDPRConsent' id_module=$id_module}
			{/if}
		</form>
	</div>
</div>
<style>
.ft_newsletter form {
	overflow:visible;
}
.block_newsletter_alert {
	position:absolute;
	bottom:-30px;
}
.block_newsletter form input[type=email]:focus {
    border: none;
    padding: 10px 120px 10px 10px;
}
</style>