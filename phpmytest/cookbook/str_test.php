<?php
$username = substr('thadqy3434', 0, 8);
print($username."<br/>");
print substr('watch out for that tree', 6, 5);
echo "<br/>";
print substr_replace('My pet is a blue dog.','fish.', 12);
echo "<br/>";
print substr_replace('My pet is a blue dog.', 'green', 12, 4);
echo "<br/>";
print substr_replace('My pet is a blue dog.', 'Title: ', 0, 0);
echo "<br/>";
print strrev('This is not a palindrome');
echo "<br/>";
$s = 'Once upon a time there was a turtle.';
$words = explode(' ', $s);
var_dump($words);
echo "<br/>";
$s = implode(' ', $words);
print $s;
