<?php
echo memory_get_usage()."\n";
$var = str_repeat('tianxiaolong', 10000);
echo memory_get_usage()."\n";
unset($var);
echo memory_get_usage();
