<?php

$str = "?name=lili&";
$len = strlen(trim($str));
echo $str.'<br/>';
echo $len.'<br/>';
echo strripos($str, '&').'<br/>';
if (strripos($str, '&') == $len) {
    echo "nice";
} else {
    echo 'no';
}