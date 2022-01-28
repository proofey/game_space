$(document).ready(function(){
    $("#loginModal").modal('show')
    $("#registrationModal").modal('show')
});

// Login form

$('#login-form').on('submit', function(e){

    e.preventDefault();
    var login_form = $('#login-form');
    var action = login_form.attr('action');
    var method = login_form.attr('method');
    var data_ = login_form.serialize();
    var token = document.getElementsByName("csrfToken").value

    $.ajax({
        type: method,
        url: action,
        data: data_,
        headers:{ 
            'X-CSRFToken': token
         },
        success: function(data){
            if ($(data).find('.alert-danger').length > 0) {
                document.getElementById('modalHeader').innerHTML = `<h5 class="text-danger" >Invalid 'Username' or 'Password'</h5>`
            }else{
                window.location.href = "/"  
            }
        },
        error: function(error){
            console.log(error)
        }
    });
});


// Registration form

$('#registration-form').on('submit', function(e){

    e.preventDefault();
    var registration_form = $('#registration-form');
    var action = registration_form.attr('action');
    var method = registration_form.attr('method');
    var data_ = registration_form.serialize();
    var token = document.getElementsByName("csrfToken").value

    $.ajax({
        type: method,
        url: action,
        data: data_,
        headers:{ 
            'X-CSRFToken': token
         },
        success: function(data){
            if ($(data).find('.alert-danger').length > 0) {
                document.getElementById('registrationModalLabel').innerHTML = `<h5 class="text-danger" >Some of the fields are incorrect</h5>`
            }else{
                document.getElementById('registrationModalLabel').innerHTML = `<h5 class="text-success" >Congratulations!You can now Sign In</h5>`
                setTimeout(function(){
                    window.location.href = "/login/"
                },2500)
            }
        },
        error: function(error){
            console.log(error)
        }
    });
});
