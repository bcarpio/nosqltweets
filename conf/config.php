<?php

$PATH='/home/bcarpio/Projects/nosqltweets/';
$TEMPLATE_NAME='default';
$TEMPLATE_PATH=$PATH . 'templates/' . $TEMPLATE_NAME;
$DATABASE='nosqltweets';

$m =  new Mongo();
$db = $m->selectDB("$DATABASE");
?>
