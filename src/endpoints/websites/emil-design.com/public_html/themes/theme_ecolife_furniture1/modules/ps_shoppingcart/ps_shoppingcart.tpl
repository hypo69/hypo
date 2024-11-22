<div id="_desktop_cart_block">
	<div class="blockcart cart-preview" data-refresh-url="{$refresh_url}" data-cartitems="{$cart.products_count}">
		<div class="button_cart">
			<a rel="nofollow" href="{$cart_url}" class="desktop hidden-md-down">
				 <span class="item_count">{$cart.products_count}</span>
				 <span class="item_total">{$cart.totals.total.value}</span>
			</a>
			<a rel="nofollow" href="{$cart_url}" class="mobile hidden-lg-up">
				<span class="item_count">{$cart.products_count}</span>
			</a>
		</div>
		<div class="popup_cart">
			<div class="content-cart">
				<div class="mini_cart_arrow"></div>
				<ul>
				  {foreach from=$cart.products item=product}
					<li>{include 'module:ps_shoppingcart/ps_shoppingcart-product-line.tpl' product=$product}</li>
				  {/foreach}
				</ul>
				<div class="price_content">
					<div class="cart-subtotals">
					   {foreach from=$cart.subtotals item="subtotal"}
						  {if $subtotal && $subtotal.value|count_characters > 0 && $subtotal.type !== 'tax'}
							<div class="cart-summary-line" id="cart-subtotal-{$subtotal.type}">
							  <span class="label{if 'products' === $subtotal.type} js-subtotal{/if}">
								{if 'products' == $subtotal.type}
								  {$cart.summary_string}
								{else}
								  {$subtotal.label}
								{/if}
							  </span>
							  <span class="value">
								{if 'discount' == $subtotal.type}-&nbsp;{/if}{$subtotal.value}
							  </span>
							  {if $subtotal.type === 'shipping'}
								  <div><small class="value">{hook h='displayCheckoutSubtotalDetails' subtotal=$subtotal}</small></div>
							  {/if}
							</div>
						  {/if}
						{/foreach}
					</div>
					<div class="cart-total price_inline">
					  <span class="label" style="font-weight:700;">{$cart.totals.total.label}</span>
					  <span class="value" style="font-weight:700;">{$cart.totals.total.value}</span>
					</div>
				</div>
				<div class="checkout">
					<a href="{$cart_url}" class="btn btn-primary">{l s='Checkout' d='Shop.Theme.Actions'}</a> 
				</div>
			</div>
		</div>
	</div>
</div>
