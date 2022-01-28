$(document).ready(function(){
    $("#updateProfileModal").modal('show');
});

function profilePosts() {
    const container = document.getElementById('profilePosts')

    if(container.classList.contains('d-none')) {
        container.classList.remove('d-none')
    } else {
        container.classList.add('d-none')
    }
}

function profileComments() {
    const container = document.getElementById('profileComments')

    if(container.classList.contains('d-none')) {
        container.classList.remove('d-none')
    } else {
        container.classList.add('d-none')
    }
}