<?php

class Itest
{
	public static $arr = [
		'Apple' => 'test1.php',
		'Pears' => 'test2.php',
		'Banana' => 'test3.php'
	];
	
	public function __construct ()
	{
		echo "";
	}
	

	/* --------------------------------------------------------------------------*/
	/**
		* @tianxiaolong  
		*
		* @Param $name
		* $name 就是 调用时的类名
		* 先加载当前文件
		* $a = new Apple(); 这是，$name 就是 Apple
		* 
		* @Returns   
	 */
	/* ----------------------------------------------------------------------------*/
	public static function autoLoads ($name)
	{
		if (array_key_exists($name, self::$arr)) {
			require_once self::$arr[$name];
			return true;
		} else {
			echo "no {$name} class";
			return false;
		}
	}
}

//向栈中注册这个类的方法
spl_autoload_register(['Itest', 'autoLoads']);
