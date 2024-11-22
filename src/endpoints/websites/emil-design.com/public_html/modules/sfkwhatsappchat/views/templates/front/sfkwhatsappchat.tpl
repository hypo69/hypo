{*
* The module helps to add whats app chat support on online store and turn visitors into customers.This helps to build relationship with customers,provide personalized service and increase in sales.
*
* NOTICE OF LICENSE
* 
* Each copy of the software must be used for only one production website, it may be used on additional
* test servers. You are not permitted to make copies of the software without first purchasing the
* appropriate additional licenses. This license does not grant any reseller privileges.
* 
* @author    Shahab
* @copyright 2007-2022 Shahab-FK Enterprises
* @license   Prestashop Commercial Module License
*}

<style>
div.fixed {
    position: fixed;
    width: 50%;
    bottom: 15px;
} 
</style>

{if $PS7_FLAG==""}
    
{if $SFKNUMBER != ''}

<div class="fixed">

    <a href="https://{$DEVICE}.whatsapp.com/send?l=en&phone={$SFKNUMBER}&text={$SFKMESSAGE}" target="_blank">
        <img src="{$SFKIMAGEPATH}" alt="Whats App Chat Support">
    </a>

</div>

{/if}

{else}
    
{if $SFKNUMBER != ''}

<div class="fixed">

    <a href="https://{$DEVICE|escape nofilter}.whatsapp.com/send?l=en&phone={$SFKNUMBER|escape nofilter}&text={$SFKMESSAGE|escape nofilter}" target="_blank">
         <img src="{$SFKIMAGEPATH|escape nofilter}" alt="Whats App Chat Support">
    </a>

</div>

{/if}

{/if}    

