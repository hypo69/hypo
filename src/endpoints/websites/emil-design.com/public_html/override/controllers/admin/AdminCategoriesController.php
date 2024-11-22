<?php

/** from https://www.choosepizzi.net/prestashop-add-custom-field-in-category/ */

//
//class AdminCategoriesController extends AdminCategoriesControllerCore
//{
//
//    public function renderForm()
//    {
//        $this->fields_form_override = array(
//            /*
//            array(
//                'type' => 'text',
//                'label' => $this->l('Canonical URL'),
//                'name' => 'canonical_url',
//                'lang' => true,
//                'autoload_rte' => true,
//                'hint' => $this->l('Invalid characters:') . ' <>;=#{}',
//            ),
//            array(
//                'type' => 'switch',
//                'label' => $this->trans('Visible', array(), 'Admin.Global'),
//                'name' => 'visible_url',
//                'lang' => false,
//                'required' => false,
//                'is_bool' => true,
//                'values' => array(
//                    array(
//                        'id' => 'visible_url_on',
//                        'value' => 1,
//                        'label' => $this->trans('Enabled', array(), 'Admin.Global')
//                    ),
//                    array(
//                        'id' => 'visible_url_off',
//                        'value' => 0,
//                        'label' => $this->trans('Disabled', array(), 'Admin.Global')
//                    )
//                )
//            ),
//            */
//            array(
//                'type' => 'html',
//                'label' => $this->l('Category Long description'),
//                'name' => 'category_description_long',
//                'lang' => true,
//                'autoload_rte' => true,
//                'hint' => $this->l('Description HTML for category') . ' HTML tags',
//            ),
//        );
//
//        return parent::renderForm();
//    }
//}
