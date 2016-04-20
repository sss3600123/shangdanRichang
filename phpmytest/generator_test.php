<?php
function aa()
{
	for ($i = 0; $i < 100000; ++$i) {
		yield $i;
	}	
}
//for ($j = 0; $j < 100000; ++$j) {
//	 var_dump(aa());
//}

function printer()
{
	while (true) {
		printf("receive: %s<br/>", yield);
	}
}

$printer = printer();

$printer->send('hello');
$printer->send('world');

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>";

function printer2()
{
	$i = 0;
	while (true) {
		printf("receive: %s<br/>", (yield ++$i));
	}
}

$p2 = printer2();

printf("%d<br/>", $p2->current());
$p2->send('hello');
printf("%d<br/>", $p2->current());
$p2->send('world');
printf("%d<br/>", $p2->current());

