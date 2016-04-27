<?php

class guest_book
{
	public $comments;
	public $last_visitor;

	public function __construct ($user)
	{
		$dbh = mysqli_connect('localhost', 'root', 'root', 'shangdan');
		$user = mysqli_real_escape_string($dbh, $user);
		$sql = "select "
	}
}
