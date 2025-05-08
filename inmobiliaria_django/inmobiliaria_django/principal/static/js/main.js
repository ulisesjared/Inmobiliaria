function abrirCalculadora() {
    const modal = document.getElementById('modalCalculadora');
    modal.classList.add('mostrar');

    // Reinicia el resultado al abrir
    const resultado = document.getElementById('resultadoHipoteca');
    resultado.classList.remove('mostrar');
    resultado.innerHTML = '';
}

function cerrarCalculadora() {
    const modal = document.getElementById('modalCalculadora');
    modal.classList.remove('mostrar');
}

function calcularHipoteca() {
    const precio = parseFloat(document.getElementById('precio').value);
    const enganche = parseFloat(document.getElementById('enganche').value);
    const plazo = parseFloat(document.getElementById('plazo').value);
    const interes = parseFloat(document.getElementById('interes').value) / 100;

    if (!precio || !enganche || !plazo || !interes) {
        alert('Por favor completa todos los campos.');
        return;
    }

    const montoPrestamo = precio - (precio * (enganche / 100));
    const numeroPagos = plazo * 12;
    const tasaMensual = interes / 12;
    const pagoMensual = (montoPrestamo * tasaMensual) / (1 - Math.pow(1 + tasaMensual, -numeroPagos));

    const resultado = document.getElementById('resultadoHipoteca');
    resultado.innerHTML = `Pago mensual aproximado: <strong>$${pagoMensual.toFixed(2)} MXN</strong>`;
    resultado.classList.add('mostrar');
}

// Detecta clic fuera del modal para cerrarlo
window.addEventListener('click', function(event) {
    const modal = document.getElementById('modalCalculadora');
    if (event.target === modal) {
        cerrarCalculadora();
    }
});
