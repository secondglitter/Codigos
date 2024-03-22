<?php
include 'includes/header.php';

//Atributos de una clase
//Crear una clase
class Empleado {
    public $nombre;
    public $apellido;
    public $departamento;
    public $email;
    public $codigo;
};

//Instataciar una clase
//De esta forma se instancia una clase
$empleado = new Empleado;

$empleado->nombre = "Juan";
$empleado->apellido = "De la cruz";


//Esto nos servira para estar probando nuestro objetos
echo "<pre>";
var_dump($empleado);
echo "</pre>";