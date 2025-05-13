document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.querySelector('form');
    const titulo = document.getElementById('titulo');
    const descripcion = document.getElementById('descripcion');
    const ubicacion = document.getElementById('ubicacion');
    const precio = document.getElementById('precio');

    function mostrarError(input, mensaje) {
        Swal.fire({
            icon: 'error',
            title: 'Campo inválido',
            text: mensaje,
            confirmButtonColor: '#4AA1EF'
        });
        input.focus();
    }

    function validarCampo(input, mensaje) {
        if (input.value.trim() === '') {
            mostrarError(input, mensaje);
            return false;
        }
        return true;
    }

    // Opcional: validación en vivo con borde de color
    function validarInput(input, mensaje) {
        input.addEventListener('input', () => {
            if (input.value.trim() !== '') {
                input.style.borderColor = 'green';
            } else {
                input.style.borderColor = 'red';
            }
        });
    }

    // Activamos validación en vivo
    validarInput(titulo, 'El título es obligatorio');
    validarInput(descripcion, 'La descripción es obligatoria');
    validarInput(ubicacion, 'La ubicación es obligatoria');
    validarInput(precio, 'El precio es obligatorio');

    formulario.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevenimos envío para validar

        const tituloValido = validarCampo(titulo, 'El título es obligatorio');
        const descripcionValida = validarCampo(descripcion, 'La descripción es obligatoria');
        const ubicacionValida = validarCampo(ubicacion, 'La ubicación es obligatoria');
        const precioValido = validarCampo(precio, 'El precio es obligatorio');

        if (tituloValido && descripcionValida && ubicacionValida && precioValido) {
            // Todo está bien, podemos enviar el formulario
            Swal.fire({
                icon: 'success',
                title: 'Formulario válido',
                text: 'La propiedad será registrada correctamente.',
                confirmButtonColor: '#0CDDC7'
            }).then(() => {
                formulario.submit(); // Ahora sí se envía el formulario
            });
        }
    });
});
