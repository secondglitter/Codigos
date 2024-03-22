function toggleCajas() {
    var cajas = document.querySelectorAll('.caja');
    var mostrarButton = document.getElementById('mostrar-button');
    var ocultarButton = document.getElementById('ocultar-button');

    cajas.forEach(function(caja) {
        if (caja.style.display === 'none' || caja.style.display === '') {
            caja.style.display = 'block';
            mostrarButton.style.display = 'none';
            ocultarButton.style.display = 'inline-block';
        } else {
            caja.style.display = 'none';
            mostrarButton.style.display = 'inline-block';
            ocultarButton.style.display = 'none';
        }
    });
}