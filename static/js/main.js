$('.datetimepicker').datetimepicker({format: "YYYY-MM-DD",locale: 'es',});

function OpenInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function buscar_estudiante(id) {
  $.getJSON('/buscar_estudiante/', {cedula: $('#'+id).val()}, function(json, textStatus) {
    if (json.existe==0) {
      confir = confirm('Estudiante no reguistrado desea reguistrarse');
      if (confir) {
        $('#crear_alumno_m').modal('show');
        $('#crear_cedula').val($('#'+id).val())
      };
    } else {
      location.href="/servicio/"+$('#'+id).val();
    };
  });
}

function crear_estudiante() {
  $.ajax({
    url: 'crear_estudiante/',
    type: 'POST',
    dataType: 'json',
    data: $('#crear_alumno_f').serialize(),
    beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));},
  })
  .done(function(data) {
    OmegaNotify.success('Guardado Exitosamente');
  })
  .fail(function() {
  })
  .always(function() {
  });
}
var cupos = 0;

function cupos_disponibles() {
  $.getJSON('/cupos_disponibles/', {id: $("#Intitucion").val(), facultad: $("#facultad").val()}, function(json, textStatus) {
      cupos = json;
      if (json>1) {
        $("#cupos_text").html('Quedan '+json+ ' Cupos Disponibles');
        $("#cupos_class").addClass('panel-primary');
        $("#cupos_class").removeClass('panel-danger');
        $("#cupos_class").removeClass('panel-warning');
      }else if (json==1) {
        $("#cupos_text").html('Queda '+json+ ' Cupo Disponible');
        $("#cupos_class").addClass('panel-warning');
        $("#cupos_class").removeClass('panel-danger');
        $("#cupos_class").removeClass('panel-primary');
      }else {
        $("#cupos_text").html('Ya No Quedan Cupos Disponibles');
        $("#cupos_class").addClass('panel-danger');
        $("#cupos_class").removeClass('panel-warning');
        $("#cupos_class").removeClass('panel-primary');
      };
  });
}

$("#Intitucion").change(function(event) {
  cupos_disponibles();
});

function Inscribirse() {
  if (cupos>0) {
    $(this).attr('disabled', 'disabled');
    $.ajax({
      url: '/Inscribirse/',
      type: 'POST',
      dataType: 'json',
      data: {
        id_estudiante: $("#id_estudiante").val(),
        id_institucion: $("#Intitucion").val(),
        id_facultad: $("#facultad").val(),
      },
      beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));},
    })
    .done(function(data) {
      if (data==1) {
        OmegaNotify.success('Guardado Exitosamente');
        setTimeout(function(){ location.reload(); }, 3000);
      } else if (data==2) {
        OmegaNotify.fail('Se agotaron los cupos para esta institucion');
        setTimeout(function(){ location.reload(); }, 3000);
      }else {
        OmegaNotify.fail('Ya te encuentras inscrito en este corte o ya tienes otro corte como culminado');
        setTimeout(function(){ location.reload(); }, 3000);
      };
    })
    .fail(function() {
    })
    .always(function() {
    });
  }else {
    OmegaNotify.fail('Ya no hay cupos disponible para esta intitucion');
    $("#Intitucion").val("");
  };
}
function obtener_tutor(id) {
  $.ajax({
    url: '/poner_tutor/',
    type: 'POST',
    dataType: 'json',
    data: {
      id: id,
    },
    beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));},
  })
  .done(function(data) {
    if (data.dato==1) {
      OmegaNotify.success('Felicidades Ya Se Te Assigno Un Tutor');
      setTimeout(function(){ location.reload(); }, 3000);
    } else if (data.dato==0) {
      OmegaNotify.fail('Aun No Se Assignado Un Tutor A Esta Institucion');
    };
  })
  .fail(function() {
  })
  .always(function() {
  });
}

function listadoestudianteintituciones() {
  var win = window.open('/InformeEstudiantesEnInstituciones.pdf/'+$("#Periodo").val()+'/'+$("#Intitucion").val()+'/'+$("#Facultad").val(), '_blank');
  if (win) {
      //Browser has allowed it to be opened
      win.focus();
  } else {
      //Browser has blocked it
      alert('Please allow popups for this website');
  }
}