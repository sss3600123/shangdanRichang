<?php

$book_collection = [
	'Emma', 
	'Pride and Prejudice',
	'Northhanger Abbey'
];

var_dump($book_collection);

/* --------------------------------------------------------------------------*/
/**
	* @tianxiaolong  
	*
	* @Param $book_collection
	* array_filp()  反转数组中的键和值
	* @Returns   
 */
/* ----------------------------------------------------------------------------*/
$book_collection = array_flip($book_collection);

var_dump($book_collection);

$book = 'Sense and Sensibility';

if (isset($book_collection[$book])) {
	echo 'Own it.';
} else {
	echo 'Need it.';
}
