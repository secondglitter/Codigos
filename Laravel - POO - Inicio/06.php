<?php
include 'includes/header.php';

//Constructor property promotion
//Crear una clase
class Empleado {
    /* Esto igual se elimina, pero se pega dentro de los argumentos del constructor
    public $nombre;
    public $apellido;
    public $departamento;
    public $email;
    public $codigo; */

    //Contructor                    Igual esto
    public function __construct(/* string $nombre, string $apellido, string $departamento, string $email, int $codigo */
        public $nombre,
        public $apellido,
        public $departamento,
        public $email,
        public $codigo,
        )
    {
        //Atributos del constructor
        /*Esto se elimina cuando se ocupa el Constructor property promotion
        $this->nombre = $nombre;
        $this->apellido = $apellido;
        $this->departamento = $departamento;
        $this->email = $email;
        $this->codigo = $codigo; */
    }
};

$juan = new Empleado('Juan', 'Perez', 'Estadias', 'juan@gmail.com', 22931);
$karen = new Empleado('Karen', 'Perez', 'Ti', 'karen@gmail.com', 4453);


//Esto nos servira para estar probando nuestro objetos
echo "<pre>";
var_dump($juan);
echo "</pre><br>";

echo "<pre>";
var_dump($karen);
echo "</pre>";