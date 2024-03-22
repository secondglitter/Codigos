const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

// Creamos la instancia de express
const app = express();
app.use(express.json());
app.use(cors());

// Creamos la conexión a la base de datos
const conexion = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "tablas",
});

// Verificamos la conexión
conexion.connect(function (error) {
  if (error) {
    console.log(error);
  } else {
    console.log("Conexión exitosa");
  }
});

// Iniciamos el servidor
app.listen(3000, () => {
  console.log("Servidor iniciado");
});

// Consultar todos los fotoresistores
app.get("/valores", (peticion, respuesta) => {
    const sql = "SELECT * FROM valores";
    conexion.query(sql, (error, resultado) => {
      if (error) return respuesta.json({ mensaje: "Error" });
      return respuesta.json({ Estatus: "exitoso", contenido: resultado });
    });
});

// Obtener datos por rango de valor
app.get("/valoresRango", (req, res) => {
  const { minimo, maximo } = req.query; // Usa req.query para acceder a los parámetros de consulta

  if (isNaN(minimo) || isNaN(maximo)) {
    return res.status(400).json({ Estatus: "Error", mensaje: "Los parámetros deben ser numéricos" });
  }
  const valorMinimo = parseInt(minimo, 10);
  const valorMaximo = parseInt(maximo, 10);

  const sql = "SELECT * FROM valores WHERE mensaje BETWEEN ? AND ?";

  conexion.query(sql, [valorMinimo, valorMaximo], (error, resultado) => {
    if (error) {
      return res.status(500).json({ Estatus: "Error", mensaje: error.message });
    }
    return res.json({ Estatus: "Exitoso", contenido: resultado });
  });
});


// Crear un nuevo registro de fotoresistor
app.post("/crear", (peticion, respuesta) => {
    const { id_puerto_serial, valor, intensidad } = peticion.body;
    const sql = "INSERT INTO valores (mensaje, valor) VALUES (?, ?)";
    conexion.query(sql, [id_puerto_serial, valor, intensidad], (error, resultado) => {
      if (error) return respuesta.json({ Estatus: "Error", mensaje: error.message });
      return respuesta.json({ Estatus: "exitoso", id: resultado.insertId });
    });
});

// Actualizar un registro de fotoresistor existente
app.put("/actualizar/:id", (peticion, respuesta) => {
    const { id } = peticion.params;
    const { valor, intensidad } = peticion.body;
    const sql = "UPDATE valores SET mensaje = ?, valor = ? WHERE id = ?";
    conexion.query(sql, [valor, intensidad, id], (error, resultado) => {
      if (error) return respuesta.json({ Estatus: "Error", mensaje: error.message });
      if (resultado.affectedRows === 0) return respuesta.json({ Estatus: "Error", mensaje: "Fotoresistor no encontrado" });
      return respuesta.json({ Estatus: "exitoso" });
    });
});

// Eliminar un registro de fotoresistor
app.delete("/eliminar/:id", (peticion, respuesta) => {
    const { id } = peticion.params;
    const sql = "DELETE FROM valores WHERE id = ?";
    conexion.query(sql, [id], (error, resultado) => {
      if (error) return respuesta.json({ Estatus: "Error", mensaje: error.message });
      if (resultado.affectedRows === 0) return respuesta.json({ Estatus: "Error", mensaje: "Fotoresistor no encontrado" });
      return respuesta.json({ Estatus: "exitoso" });
    });
});
