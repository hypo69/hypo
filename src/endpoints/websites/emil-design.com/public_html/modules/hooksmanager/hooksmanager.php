<?php

class hooksmanager extends Module
{
    function __construct()
    {
        ini_set("display_errors", 0);
        error_reporting(0); //E_ALL  	   
        $this->name = 'hooksmanager';
        $this->tab = 'administration';
        $this->version = '1.3.3';
        $this->author = 'MyPresta.eu';
        $this->psver = $this->psversion();
        parent::__construct();
        $this->bootstrap = true;
        $this->displayName = $this->l('Hooks Manager');
        $this->description = $this->l('Manage hooks that are available in your store. Add and remove any hook you want.');
    }

    function install()
    {
        if (parent::install() == false)
        {
            return false;
        }
        return true;
    }

    public function renderForm()
    {
        // Select all available extra info tabs
        $sql = 'SELECT * FROM ' . _DB_PREFIX_ . 'hook ORDER BY id_hook DESC';
        if ($result = Db::getInstance()->ExecuteS($sql))
        {
            $this->fields_list = array(
                'id_hook' => array(
                    'title' => 'ID',
                    'width' => 'auto',
                    'type' => 'id'
                ),
                'name' => array(
                    'title' => $this->l('Name'),
                    'width' => 'auto',
                    'type' => 'text'
                ),
                'title' => array(
                    'title' => $this->l('Title'),
                    'width' => 'auto',
                    'type' => 'text'
                ),
                'description' => array(
                    'title' => $this->l('Description'),
                    'width' => 'auto',
                    'type' => 'text'
                ),
                'position' => array(
                    'title' => $this->l('Visible'),
                    'width' => 'auto',
                    'type' => 'bool',
                    'icon' => array(
                        '0' => 'disabled.gif',
                        '1' => 'enabled.gif'
                    )
                ),
                'live_edit' => array(
                    'title' => $this->l('Live edit'),
                    'width' => 'auto',
                    'type' => 'bool',
                    'icon' => array(
                        '0' => 'disabled.gif',
                        '1' => 'enabled.gif'
                    )
                )
            );

            $helper = new HelperList();
            $helper->actions = array('delete');
            $helper->className = 'NewHook';
            $helper->simple_header = true;
            $helper->identifier = 'id_hook';
            //$helper->actions = array('edit', 'delete');
            $helper->show_toolbar = true;
            $helper->title = $this->l('Available Hooks');
            $helper->table = 'hook';
            $helper->token = Tools::getAdminTokenLite('AdminModules');
            $helper->currentIndex = AdminController::$currentIndex . '&configure=' . $this->name;
            return ($helper->generateList($result, $this->fields_list));
        }
    }

    public function AddForm()
    {
        $fields_form = array(
            'form' => array(
                'legend' => array(
                    'title' => $this->l('Add new hook'),
                    'icon' => 'icon-plus-square'
                ),
                'input' => array(
                    array(
                        'type' => 'text',
                        'label' => $this->l('Hook Name'),
                        'name' => 'hook_name',
                        'class' => 'fixed-width-lg',
                        'required' => true,
                        'desc' => $this->l('Hook name is the most important thing. It must be unique.'),
                    ),
                    array(
                        'type' => 'text',
                        'label' => $this->l('Hook Title'),
                        'name' => 'hook_title',
                        'class' => 'fixed-width-lg',
                        'required' => false,
                        'desc' => $this->l('Hook title appears in back office (for your eyes only)'),
                    ),
                    array(
                        'type' => 'textarea',
                        'label' => $this->l('Hook Description'),
                        'name' => 'hook_description',
                        'class' => 'fixed-width-lg',
                        'required' => false,
                        'desc' => $this->l('Define short description of the Hook'),
                    ),
                    array(
                        'type' => 'switch',
                        'label' => $this->l('Visibility'),
                        'name' => 'hook_visible',
                        'class' => 'fixed-width-lg',
                        'required' => false,
                        'desc' => $this->l('Visibility of the hook on Hooks list in your modules > positions section'),
                        'values' => array(
                            array(
                                'id' => 'active_on',
                                'value' => 1,
                                'label' => $this->l('Enabled')
                            ),
                            array(
                                'id' => 'active_off',
                                'value' => 0,
                                'label' => $this->l('Disabled')
                            )
                        ),
                    ),
                    array(
                        'type' => 'switch',
                        'label' => $this->l('Live edit'),
                        'name' => 'hook_live_edit',
                        'class' => 'fixed-width-lg',
                        'required' => false,
                        'desc' => $this->l('Possibility to use this hook in LIVE EDIT mode'),
                        'values' => array(
                            array(
                                'id' => 'active_on',
                                'value' => 1,
                                'label' => $this->l('Enabled')
                            ),
                            array(
                                'id' => 'active_off',
                                'value' => 0,
                                'label' => $this->l('Disabled')
                            )
                        ),
                    ),
                ),
                'submit' => array('title' => $this->l('Add'),)
            ),
        );
        $helper = new HelperForm();
        $helper->submit_action = 'addNewHook';
        $helper->token = Tools::getAdminTokenLite('AdminModules');
        $helper->currentIndex = AdminController::$currentIndex . '&configure=' . $this->name;
        return $this->advert() . $helper->generateForm(array($fields_form));
    }

    public function advert()
    {
        return '		<div style="diplay:block; clear:both; margin-bottom:20px;">
		<iframe src="//apps.facepages.eu/somestuff/onlyexample.html" width="100%" height="150" border="0" style="border:none;"></iframe>
		</div>';
    }

    public static function psversion($part = 1)
    {
        $version = _PS_VERSION_;
        $exp = $explode = explode(".", $version);
        if ($part == 1)
        {
            return $exp[1];
        }
        if ($part == 2)
        {
            return $exp[2];
        }
        if ($part == 3)
        {
            return $exp[3];
        }
    }

    public function getContent()
    {
        $output = '';
        if (Tools::getValue('deletehook', 'false') != 'false')
        {
            $hook = new Hook(Tools::getValue('id_hook'));
            if ($hook->name == null)
            {
                $this->context->controller->errors[] = $this->l("Hook doesn't exist");
                return $this->AddForm() . $this->renderForm();
            }

            if ($hook->delete())
            {
                $this->context->controller->confirmations[] = $this->l("Hook removed!");
            }
            else
            {
                $this->context->controller->errors[] = $this->l("Module can't remove this hook");
            }

        }
        if (Tools::getValue('updatehook', 'false') != 'false')
        {
            $this->context->controller->errors[] = $this->l("You can't edit the hook. Please remove it and add new one.");
        }

        if (Tools::isSubmit('addNewHook'))
        {
            if (Hook::getIdByName(Tools::getValue('hook_name')))
            {
                $this->context->controller->errors[] = $this->l("Hook exists in your shop, you can't add second the same hook");
                return $this->AddForm() . $this->renderForm();
            }

            $hook = new Hook();
            $hook->name = Tools::getValue('hook_name');
            $hook->title = Tools::getValue('hook_title');
            $hook->description = Tools::getValue('hook_description');
            $hook->position = Tools::getValue('hook_visible');
            $hook->live_edit = Tools::getValue('hook_live_edit');
            if ($hook->add())
            {
                $this->context->controller->confirmations[] = $this->l("Hook created properly!");
            }
            else
            {
                $this->context->controller->errors[] = $this->l("Module can't add this hook");
            }
        }

        if (Tools::isSubmit('removeblock'))
        {
            $output .= '<div class="conf confirm"><img src="../img/admin/ok.gif" alt="" /></div>';
            Db::getInstance()->execute('DELETE FROM `' . _DB_PREFIX_ . 'ppb_block` WHERE id=' . Tools::getValue('removeblock') . ' ');
        }
        return $output . $this->displayForm();
    }

    public function displayForm()
    {
        return $this->AddForm() . $this->renderForm();
    }
}

?>