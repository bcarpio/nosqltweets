<?php
	require_once("../conf/config.php");
	require_once($TEMPLATE_PATH . "/header.php");

$years = array('2012-01-01', '2013', '2014');
$list = $db->listCollections();

foreach ($list as $collection){
	$collection = preg_replace("/".$DATABASE."/", "", $collection);
	$collection = preg_replace("/\.+/i", "", $collection); 
	if(!isset($_GET['nosql'])) {
?>

<a href="./index.php?nosql=<?php echo "$collection" ?>"><?php echo "$collection"?></a> 

<?php
}
}

if(isset($_GET['nosql'])) {
	$s = $_GET["nosql"];
	$cursor = $db->$s;
?>
	<B><?php print $s ?></B><BR>
	Total Number: <?php echo $cursor->count(); ?><BR>
	<?php
	foreach ($years as $year){
	$start = $year;
	$end = $year;
	$count = $cursor->count(array("created_at" => array('$gt' => "2012", '$lte' => "2013")));
	?>
	Year: <?php echo $count; ?> <BR>
	

<?php
}
}
?>
<?php
	require_once($TEMPLATE_PATH . "/footer.php");
?>
