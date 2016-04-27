<?php

function logf ()
{
	$date = date(DATE_RSS);
	$args = func_get_args();

	return print "$date: ". call_user_func_array('sprintf', $args). "<br/>";
}

logf('<a href="%s">%s</a>','http://developer.ebay.com','eBay Developer Program');

