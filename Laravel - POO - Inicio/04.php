<?php
include 'includes/header.php';

//Constructores
//Crear una clase
class Empleado {
    public $nombre;
    public $apellido;
    public $departamento;
    public $email;
    public $codigo;

    //Contructor
    public function __construct($nombre, $apellido, $departamento, $email, $codigo)
    {
        //Atributos del constructor
        $this->nombre = $nombre;
        $this->apellido = $apellido;
        $this->departamento = $departamento;
        $this->email = $email;
        $this->codigo = $codigo;
    }
};

$juan = new Empleado('Juan', 'Perez', 'Estadias', 'juan@gmail.com', 22931);
$karen = new Empleado('Karen', 'Perez', 'Ti', 'karen@gmail.com', 4453);


//Esto nos servira para estar probando nuestro objetos
echo "<pre>";
var_dump($juan,$karen);
echo "</pre>";