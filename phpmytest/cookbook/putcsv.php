<?php
$sales = [
	['Northeast', '2005-01-01', '2005-02-01', 12.54], 
	['Northwest', '2005-01-01', '2005-02-01', 546.33],
	['All Regions', '--', '--', 1507.34]
];

$filename = './sales.csv';
$fh = fopen($filename, 'ww') or die("Can't open $filename");
foreach ($sales as $sales_line) {
	if (fputcsv($fh, $sales_line) === false) {
		die("Can't write CSV line");
	}
}
fclose($fh) or die("Can't close $filename");

