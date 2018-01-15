<?php
    header('Content-Type: application/json');
    $json = file_get_contents('http://simple-python/');
    $obj = json_decode($json);
    $prof = $obj->Profile;
    echo json_encode($prof);
?>
