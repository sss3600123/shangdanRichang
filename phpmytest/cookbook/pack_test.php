<?php

/* --------------------------------------------------------------------------*/
/**
 * @tianxiaolong  
 * pack 把数据装入二进制
 */
/* ----------------------------------------------------------------------------*/
$books = [
	['Elmer Gantry', 'Sinclair Lewis', 1927],
	['The Scarlatti Inheritance', 'Robert Ludlum', 1971],
	['The Parsifal Mosaic', 'William Sytron', 1979]
];

foreach ($books as $book) {
	print pack('A25A15A4', $book[0], $book[1], $book[2]). "<br/>";
}
