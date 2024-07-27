// Validaciones con Jquery y AJAX en el Formulario del Login
$(document).on('submit', '#login', function(e){
    e.preventDefault();
        $.ajax({
            type: 'POST',
            url:$(this).attr('action'),
            data:{
                username: $('#username').val(),
                password: $('#password').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(data){
                console.log(data.messages)
                if (data.result == 'not register'){
                    let msg = data.status1;
                    swal("Error", msg, "error")
                }
                else if (data.result == 'error') {
                    const json_test = data.errors;
                    // Selecciona el elemento <div> donde se mostrarán los mensajes de error

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
                } 
                else {
                    // Muestra el mensaje de éxito...
                    let msg = 'Bienvenido';
                    swal("Perfecto !", msg, "success")
                    setTimeout(function() {
                        window.location.href = '/users/';
                      }, 1000);
                }
            }
      });
  });