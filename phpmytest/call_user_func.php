<?php
    function funa($b, $c)
	{
		echo $b."<br/>",$c;
	}
	
class a 
{
	function b()
	{
		$args = func_get_args();
		$num = func_num_args();
		print_r($args);
		echo '<br/>'.$num;
	}		
}
 call_user_func('funa', 111, 222);
