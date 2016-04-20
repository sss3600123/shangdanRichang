<?php

function squares ($start, $end)
{
	if ($start < $end) {
		for ($i = $start; $i <= $end; ++$i) {
			yield $i => $i * $i;
		}
	} else {
		for ($i = $end; $i >= $start; ++$i) {
			yield $i => $i * $i;
		}
	}
}

foreach (squares(3, 15) as $n => $s) {
	printf("%d squared is %d<br/>", $n, $s);
}
