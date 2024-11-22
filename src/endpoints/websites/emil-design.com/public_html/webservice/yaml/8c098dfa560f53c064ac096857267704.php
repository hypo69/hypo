<?php return array (
  'name' => 'theme_ecolife_furniture1',
  'display_name' => 'Ecolife Furniture1',
  'version' => '1.0.0',
  'author' => 
  array (
    'name' => 'Posthemes',
    'email' => '',
    'url' => 'http://posthemes.com/',
  ),
  'meta' => 
  array (
    'compatibility' => 
    array (
      'from' => '1.7.0.0',
      'to' => NULL,
    ),
    'available_layouts' => 
    array (
      'layout-full-width' => 
      array (
        'name' => 'Full Width',
        'description' => 'No side columns, ideal for distraction-free pages such as product pages.',
      ),
      'layout-both-columns' => 
      array (
        'name' => 'Three Columns',
        'description' => 'One large central column and 2 side columns.',
      ),
      'layout-left-column' => 
      array (
        'name' => 'Two Columns, small left column',
        'description' => 'Two columns with a small left column',
      ),
      'layout-right-column' => 
      array (
        'name' => 'Two Columns, small right column',
        'description' => 'Two columns with a small right column',
      ),
    ),
  ),
  'assets' => NULL,
  'global_settings' => 
  array (
    'configuration' => 
    array (
      'PS_IMAGE_QUALITY' => 'png',
    ),
    'modules' => 
    array (
      'to_disable' => 
      array (
        0 => 'welcome',
        1 => 'ps_customtext',
        2 => 'ps_featuredproducts',
        3 => 'ps_bestsellers',
        4 => 'ps_imageslider',
        5 => 'ps_mainmenu',
        6 => 'ps_banner',
        7 => 'ps_searchbar',
      ),
      'to_enable' => 
      array (
        0 => 'ps_socialfollow',
        1 => 'ps_contactinfo',
        2 => 'ps_linklist',
        3 => 'ps_advertising',
        4 => 'ps_categoryproducts',
        5 => 'blockreassurance',
        6 => 'blocktags',
        7 => 'blockwishlist',
        8 => 'poscompare',
        9 => 'productcomments',
        10 => 'posrotatorimg',
        11 => 'possearchproducts',
        12 => 'posstaticblocks',
        13 => 'posstaticfooter',
        14 => 'posthemeoptions',
        15 => 'posmegamenu',
        16 => 'posslideshows',
        17 => 'poslistcategories',
        18 => 'posnewproducts',
        19 => 'poslogo',
        20 => 'posfeaturedproducts',
        21 => 'posspecialproducts',
        22 => 'poscountdown',
        23 => 'xipblog',
        24 => 'xipblogdisplayposts',
      ),
    ),
    'hooks' => 
    array (
      'modules_to_hook' => 
      array (
        'displayBannersequence' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayHome' => 
        array (
          0 => 'poslistcategories',
          1 => 'posstaticblocks',
          2 => 'posnewproducts',
        ),
        'displayContainertop' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayContainertop2' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayFulltop' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayFulltop2' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayContainerbottom' => 
        array (
          0 => 'posstaticblocks',
          1 => 'posspecialproducts',
          2 => 'poslogo',
          3 => 'posfeaturedproducts',
          4 => 'xipblogdisplayposts',
        ),
        'displayContainerbottom2' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayFullbottom' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayFullbottom2' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayProductListFunctionalButtons' => 
        array (
          0 => 'blockwishlist',
        ),
        'displayBeforeBodyClosingTag' => 
        array (
          0 => 'poscompare',
        ),
        'displayProductListCompare' => 
        array (
          0 => 'poscompare',
        ),
        'displayNav1' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayNav2' => 
        array (
          0 => 'posstaticblocks',
        ),
        'displayTopColumn' => 
        array (
          0 => 'posslideshows',
          1 => 'posstaticblocks',
        ),
        'displayNav' => 
        array (
          0 => 'ps_languageselector',
          1 => 'ps_currencyselector',
          2 => 'ps_customersignin',
          3 => 'posstaticblocks',
          4 => 'ps_contactinfo',
        ),
        'displayTop' => 
        array (
          0 => 'posstaticblocks',
          1 => 'ps_shoppingcart',
          2 => 'blockwishlist',
          3 => 'poscompare',
          4 => 'possearchproducts',
        ),
        'displayFooter' => 
        array (
          0 => 'posstaticfooter',
        ),
        'displayFooterBefore' => 
        array (
          0 => 'posstaticfooter',
        ),
        'displayFooterAfter' => 
        array (
          0 => 'posstaticfooter',
        ),
        'displayLeftColumn' => 
        array (
          0 => 'ps_categorytree',
          1 => 'ps_facetedsearch',
          2 => 'blocktags',
          3 => 'ps_advertising',
        ),
        'displayProductAdditionalInfo' => 
        array (
          0 => 'blockwishlist',
          1 => 'poscompare',
          2 => 'ps_sharebuttons',
        ),
        'displayFooterTop' => 
        array (
          0 => 'posstaticfooter',
        ),
        'displayFooterBottom' => 
        array (
          0 => 'posstaticfooter',
        ),
        'displayFooterProduct' => 
        array (
          0 => 'ps_categoryproducts',
        ),
        'displayReassurance' => 
        array (
          0 => 'blockreassurance',
        ),
      ),
    ),
    'image_types' => 
    array (
      'cart_default' => 
      array (
        'width' => 125,
        'height' => 125,
        'scope' => 
        array (
          0 => 'products',
        ),
      ),
      'small_default' => 
      array (
        'width' => 98,
        'height' => 98,
        'scope' => 
        array (
          0 => 'products',
          1 => 'categories',
          2 => 'manufacturers',
          3 => 'suppliers',
        ),
      ),
      'medium_default' => 
      array (
        'width' => 452,
        'height' => 452,
        'scope' => 
        array (
          0 => 'products',
          1 => 'manufacturers',
          2 => 'suppliers',
        ),
      ),
      'home_default' => 
      array (
        'width' => 360,
        'height' => 360,
        'scope' => 
        array (
          0 => 'products',
        ),
      ),
      'large_default' => 
      array (
        'width' => 800,
        'height' => 800,
        'scope' => 
        array (
          0 => 'products',
          1 => 'manufacturers',
          2 => 'suppliers',
        ),
      ),
      'category_default' => 
      array (
        'width' => 1050,
        'height' => 350,
        'scope' => 
        array (
          0 => 'categories',
        ),
      ),
      'stores_default' => 
      array (
        'width' => 170,
        'height' => 115,
        'scope' => 
        array (
          0 => 'stores',
        ),
      ),
    ),
  ),
  'theme_settings' => 
  array (
    'default_layout' => 'layout-full-width',
    'layouts' => 
    array (
      'category' => 'layout-left-column',
      'best-sales' => 'layout-left-column',
      'new-products' => 'layout-left-column',
      'prices-drop' => 'layout-left-column',
      'contact' => 'layout-left-column',
      'manufacturers' => 'layout-left-column',
      'search' => 'layout-left-column',
      'module-xipblog-archive' => 'layout-left-column',
      'module-xipblog-single' => 'layout-left-column',
    ),
  ),
  'dependencies' => 
  array (
    'modules' => 
    array (
      0 => 'ps_advertising',
      1 => 'ps_categoryproducts',
      2 => 'blocktags',
      3 => 'blockwishlist',
      4 => 'poscompare',
      5 => 'productcomments',
      6 => 'posrotatorimg',
      7 => 'possearchproducts',
      8 => 'posmegamenu',
      9 => 'posslideshows',
      10 => 'posstaticblocks',
      11 => 'posstaticfooter',
      12 => 'posthemeoptions',
      13 => 'poslistcategories',
      14 => 'posnewproducts',
      15 => 'poslogo',
      16 => 'posfeaturedproducts',
      17 => 'posspecialproducts',
      18 => 'poscountdown',
      19 => 'xipblog',
      20 => 'xipblogdisplayposts',
    ),
  ),
);
