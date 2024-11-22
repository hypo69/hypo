{if $contact_infos.phone}
<div id="_desktop_contact_link">
  <div class="contact-nav">
	<div class="phone">
		{l s='Call us:' d='Shop.Theme.Global'} <a href="tel:{$contact_infos.phone}">{$contact_infos.phone}</a>
		
	</div>
  </div>
</div>
{/if}