<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInitc6aff386259a05dc6136fda79ebedaed
{
    public static $classMap = array (
        'Ps_Shoppingcart' => __DIR__ . '/../..' . '/ps_shoppingcart.php',
        'Ps_ShoppingcartAjaxModuleFrontController' => __DIR__ . '/../..' . '/controllers/front/ajax.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->classMap = ComposerStaticInitc6aff386259a05dc6136fda79ebedaed::$classMap;

        }, null, ClassLoader::class);
    }
}
