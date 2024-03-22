<?php
include 'includes/header.php';

//Instanciar una clase
class Empleado {
    
};

//De esta forma se instancia una clase
$empleado = new Empleado;
$empleado2 = new Empleado;
$empleado3 = new Empleado;

//Esto nos servira para estar probando nuestro objetos
echo "<pre>";
var_dump($empleado);
echo "</pre>";

echo "<pre>";
var_dump($empleado2);
echo "</pre>";

echo "<pre>";
var_dump($empleado3);
echo "</pre>";