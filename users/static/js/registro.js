// Validaciones con Jquery y AJAX en el Formulario del Login

$(document).on('submit', '#registro', function(e){
    e.preventDefault();
    var data = new FormData();
    data.append('username', $('#username').val());
    data.append('last_name', $('#last_name').val());
    data.append('first_name', $('#first_name').val());
    data.append('password1', $('#password1').val());
    data.append('password2', $('#password2').val());
    data.append('email', $('#email').val());
    data.append('photo', $('#photo')[0].files[0]);
    data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({
        type: 'POST',
        url:$(this).attr('action'),
        processData: false,
        contentType: false,
        mimeType: "multipart/form-data",
        dataType: 'json',

        data: data,

        success: function(data){
            if (data.status == 'error') {
                const json_test = data.errors;
                console.log('paso');              

                // Selecciona el elemento <div> donde se mostrarán los mensajes de error
                let msg = 'Error al crear usuario por favor valide los campos';
                swal("Error", msg, "error")
                var $errorDiv = $('#errores');
                $errorDiv.html("")
                // Itera sobre las entradas del objeto JSON
                $.each(json_test, function(clave, mensajes) {
                    // Itera sobre los mensajes de error para esa clave
                    $.each(mensajes, function(index, mensaje) {
                        // Crea un elemento <p> para cada mensaje de error
                        var $messageElement = $('<p>').text('- '+mensaje);
                        $errorDiv.append($messageElement).addClass("alert alert-danger");
                    });
                });
                // Muestra los mensajes de error en el lugar apropiado...
                // ...
            } else if (data.status == 'good'){

                let msg = data.mensaje
                swal("Perfecto !", msg, "success")
                setTimeout(function() {
                    window.location.href = '/';
                    }, 1000);
                
                } 
            
            else{
                let msg = 'Usuario Creado Satisfactoriamente';
                swal("Perfecto !", msg, "success")
                setTimeout(function() {
                    window.location.href = '/';
                    }, 1000);
                

            }
        },
      });
  });