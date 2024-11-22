<?php

if(!defined('_PS_VERSION_')
	OR !defined('_CAN_LOAD_FILES_')
)
{
	exit;
}

class ecm_richeditor extends Module
{
	protected $_errors = false;

	public
	function __construct()
	{
		$this->name = 'ecm_richeditor';
		$this->tab = 'administration';
		$this->version = 0.2;
		$this->author = 'Elcommerce';
		$this->ps_versions_compliancy = array('min'=> '1.6','max'=> '1.6.20');
		$this->need_instance = 0;

		parent::__construct();

		$this->displayName = $this->l('tinyMCE rich editor');
		$this->description = $this->l('extends the functionality of the built in tinyMCE editor');
	}

	public
	function install()
	{

		if(!parent::install()
			OR !$this->backup_files()
			OR !$this->override_file()
			OR !$this->copy_plugin(dirname(__FILE__)."/plugins/",_PS_ROOT_DIR_."/js/tiny_mce/plugins/",true)

		){
			return FALSE;
		}
		return TRUE;
	}

	public
	function uninstall()
	{
		if(!parent::uninstall()
			OR !$this->backup()
			OR !$this->unlink_file()
		){
			return FALSE;
		}
		return TRUE;
	}
	private function backup_files(){
		if( _PS_VERSION_ < "1.6.0.13"){
		if (file_exists(_PS_ROOT_DIR_."/js/tinymce.inc.js"))
		@rename(_PS_ROOT_DIR_."/js/tinymce.inc.js",_PS_ROOT_DIR_."/js/tinymce.inc_bak.js");
		}else{
		if (file_exists(_PS_ROOT_DIR_."/js/admin/tinymce.inc.js"))
		@rename(_PS_ROOT_DIR_."/js/admin/tinymce.inc.js",_PS_ROOT_DIR_."/js/admin/tinymce.inc_bak.js");
			}
		return TRUE;
	}
	private function copy_plugin ($from, $to, $rewrite = true) {
if (is_dir($from)) {
@mkdir($to);
$d = dir($from);
while (false !== ($entry = $d->read())) {
if ($entry == "." || $entry == "..") continue;
$this->copy_plugin("$from/$entry", "$to/$entry", $rewrite);
}
$d->close();
} else {
if (!file_exists($to) || $rewrite)
copy($from, $to);
}
return TRUE;
}
	private function backup(){
		if( _PS_VERSION_ < "1.6.0.13"){
		@unlink(_PS_ROOT_DIR_."/js/tinymce.inc.js");
		if (file_exists(_PS_ROOT_DIR_."/js/tinymce.inc_bak.js"))
		@rename(_PS_ROOT_DIR_."/js/tinymce.inc_bak.js",_PS_ROOT_DIR_."/js/tinymce.inc.js");}
		else{
		@unlink(_PS_ROOT_DIR_."/js/admin/tinymce.inc.js");
		if (file_exists(_PS_ROOT_DIR_."/js/admin/tinymce.inc_bak.js"))
		@rename(_PS_ROOT_DIR_."/js/admin/tinymce.inc_bak.js",_PS_ROOT_DIR_."/js/admin/tinymce.inc.js");
		}

		return TRUE;
	}
	public
	function unlink_file(){
		//@unlink(_PS_ROOT_DIR_."/override/classes/Validate.php");
		@unlink(_PS_ROOT_DIR_."/cache/class_index.php");
		return TRUE;
	}

	public
	function override_file()
	{
		$src = dirname(__FILE__)."/_override/js/tinymce.inc.js";
		if( _PS_VERSION_ < "1.6.0.13"){
		$dst =      _PS_ROOT_DIR_."/js/tinymce.inc.js";}
		else{
		$dst =      _PS_ROOT_DIR_."/js/admin/tinymce.inc.js";
		}
		@copy($src, $dst);
		@unlink(_PS_ROOT_DIR_."/cache/class_index.php");
		return TRUE;
	}
}
