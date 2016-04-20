<?php
ob_start();
for ($number = 1; $number <= 100; $number++) {
	$url = "http://www.google.com.hk <br/>";
	echo $url;
}
ob_end_flush();
