<?php
$memcached = new Memcached();
$memcached->addServer('localhost', 11211);

$key = 'test';
$value = 'Hello, Memcached!';

$memcached->set($key, $value, 60);

$result = $memcached->get($key);

echo $result;
?>
