<?php

function gen_one_to_three ()
{
	for ($i = 1; $i <= 3; ++$i) {
		yield $i;
	}
}

//$aa = gen_one_to_three();

//foreach ($aa as $v) {
//	echo $v, "<br/>";
//}
//for ($j = 1; $j <= 3; ++$j) {
	//echo $aa->;
	//echo gen_one_to_three();
//}

$input = <<<EOF
1;PHP;Likes dollar signs
2;Python;Likes whitespace
3;Ruby;Likes blocks
EOF;

//var_dump(explode("\n", $input));
function input_parser ($input)
{
	foreach (explode("\n", $input) as $line) {
		$fields = explode(";", $line);
		$id = $fields[0];
		yield $id => $fields;
	}
}

foreach (input_parser($input) as $id => $fields) {
	echo "$id: <br/>", "&nbsp;&nbsp;$fields[1]<br/>", "&nbsp;&nbsp;$fields[2]<br/>";
}
