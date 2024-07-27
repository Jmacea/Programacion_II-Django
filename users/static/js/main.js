// Funcion DataTable para la mejora de tablas

$(function(){
    var table = $('#test').DataTable({
        paging: true, //pagination
        pageLength: 10, // data per page
        lengthChange: true, //show entries per page
        autoWidth: true, //control the auto width on clumns
        searching: true, // Input search
        bInfo: true, // Info on footer
        bSort: true, // Filter A to Z and Z to A (and numbers)
    });

    
});  


// Funciones para los modales
var $ = jQuery.noConflit();
function OpenModalAdd(url){
    $('#addModal').load(url,function(){
    $(this).modal('show');
    });
}
function OpenModalEdit(url){
    $('#editModal').load(url,function(){
    $(this).modal('show');
    });
}
function OpenModalDelete(url){
    $('#deleteModal').load(url,function(){
    $(this).modal('show');
    });
}

function editPerfil(url){
    $('#EditPerfil').load(url,function(){
    $(this).modal('show');
    });
}

function addAdmin(url){
    $('#AddAdmin').load(url,function(){
    $(this).modal('show');
    });
}
