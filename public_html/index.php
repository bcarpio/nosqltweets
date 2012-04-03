<?php
// load up your config file
    require_once("../conf/config.php");
	require_once($TEMPLATE_PATH . "/header.php");
?>

<?php
$list = $db->listCollections();

foreach ($list as $collection){
	$collection = preg_replace("/".$DATABASE."/", $replace, $collection);
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
	Number: <?php echo $cursor->count(); ?>

<?php
}
?>
<?php
	require_once($TEMPLATE_PATH . "/footer.php");
?>
