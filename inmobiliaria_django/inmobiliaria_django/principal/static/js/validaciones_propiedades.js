// validaciones_propiedades.js

document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.querySelector('form');
    if (!formulario) return;

    const titulo = document.getElementById('titulo');
    const descripcion = document.getElementById('descripcion');
    const ubicacion = document.getElementById('ubicacion');
    const precio = document.getElementById('precio');

    function mostrarError(input, mensaje) {
        let error = input.nextElementSibling;
        if (!error || !error.classList.contains('error-mensaje')) {
            error = document.createElement('div');
            error.className = 'error-mensaje';
            error.style.color = 'red';
            error.style.fontSize = '13px';
            error.style.marginTop = '4px';
            input.parentNode.appendChild(error);
        }
        error.textContent = mensaje;
    }

    function limpiarError(input) {
        const error = input.parentNode.querySelector('.error-mensaje');
        if (error) {
            error.textContent = '';
        }
    }

    titulo.addEventListener('input', () => {
        if (titulo.value.trim() === '') {
            mostrarError(titulo, 'El título es obligatorio');
        } else {
            limpiarError(titulo);
        }
    });

    descripcion.addEventListener('input', () => {
        if (descripcion.value.trim() === '') {
            mostrarError(descripcion, 'La descripción es obligatoria');
        } else {
            limpiarError(descripcion);
        }
    });

    ubicacion.addEventListener('input', () => {
        if (ubicacion.value.trim() === '') {
            mostrarError(ubicacion, 'La ubicación es obligatoria');
        } else {
            limpiarError(ubicacion);
        }
    });

    precio.addEventListener('input', () => {
        if (precio.value <= 0 || isNaN(precio.value)) {
            mostrarError(precio, 'Introduce un precio válido');
        } else {
            limpiarError(precio);
        }
    });

    formulario.addEventListener('submit', function (e) {
        let hayError = false;

        if (titulo.value.trim() === '') {
            mostrarError(titulo, 'El título es obligatorio');
            hayError = true;
        }
        if (descripcion.value.trim() === '') {
            mostrarError(descripcion, 'La descripción es obligatoria');
            hayError = true;
        }
        if (ubicacion.value.trim() === '') {
            mostrarError(ubicacion, 'La ubicación es obligatoria');
            hayError = true;
        }
        if (precio.value <= 0 || isNaN(precio.value)) {
            mostrarError(precio, 'Introduce un precio válido');
            hayError = true;
        }

        if (hayError) {
            e.preventDefault();
            alert('Por favor, corrige los errores antes de enviar el formulario.');
        }
    });
});
