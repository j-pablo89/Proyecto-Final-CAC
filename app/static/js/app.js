// verificarLogin();
// document.getElementById('authButtonOut').addEventListener('click', () =>{
//     sessionStorage.removeItem('usuario');
//     const authButtonOut = document.getElementById('authButtonOut');
//     authButtonOut.className.add('d-none');
//     const authButton = document.getElementById('authButton');
//     authButton.className.remove('d-none');
//     const labelLoginContainer = document.getElementById('labelLoginContainer');
//     labelLoginContainer.classList.remove('d-none');
//     const itemAdmin = document.getElementById('itemAdmin');
//     itemAdmin.classList.add('d-none');
    
// });


// const usuarioPredefinido = 'Administrador';
// const clavePredefinida = 'adm123456';

// function loguearse(){
//     const inputUsuario = document.getElementById('inputUsuario').value;
//     const inputClave = document.getElementById('inputClave').value;
//     if(inputUsuario === usuarioPredefinido && inputClave === clavePredefinida){
//         sessionStorage.setItem('usuario','login');
//         const labelLoginContainer = document.getElementById('labelLoginContainer');
//         labelLoginContainer.classList.add('d-none');
//         const itemAdmin = document.getElementById('itemAdmin');
//         itemAdmin.classList.remove('d-none');
//         const authButton = document.getElementById('authButton');
//         authButton.classList.add('d-none');
//         const authButtonOut = document.getElementById('authButtonOut');
//         authButtonOut.classList.remove('d-none');
//         window.location="/";
//     }
// };


// function verificarLogin(){
//     const user = sessionStorage.getItem('usuario');
//     if( user === 'login'){
//         const labelLoginContainer = document.getElementById('labelLoginContainer');
//         labelLoginContainer.classList.add('d-none');
//         const itemAdmin = document.getElementById('itemAdmin');
//         itemAdmin.classList.remove('d-none');
//         const authButton = document.getElementById('authButton');
//         authButton.classList.add('d-none');
//         const authButtonOut = document.getElementById('authButtonOut');
//         authButtonOut.classList.remove('d-none');
//     }
// }
function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var message = document.getElementById("message").value;
    var plan = document.getElementById("plan").value;
    var gender = document.querySelector('input[name="gender"]:checked');
    var image = document.getElementById("image").value;
    var isValid = true;

    if (name.trim() === "") {
        document.getElementById("nameError").innerText = "Por favor, ingrese su nombre.";
        isValid = false;
    } else {
        document.getElementById("nameError").innerText = "";
    }


    if (email.trim() === "") {
        document.getElementById("emailError").innerText = "Por favor, ingrese su email.";
        isValid = false;
    } else if (!isValidEmail(email)) {
        document.getElementById("emailError").innerText = "Por favor, ingrese un email válido.";
        isValid = false;
    } else {
        document.getElementById("emailError").innerText = "";
    }


    if (phone.trim() === "") {
        document.getElementById("phoneError").innerText = "Por favor, ingrese su número de teléfono.";
        isValid = false;
    } else {
        document.getElementById("phoneError").innerText = "";
    }


    if (message.trim() === "") {
        document.getElementById("messageError").innerText = "Por favor, ingrese su mensaje.";
        isValid = false;
    } else {
        document.getElementById("messageError").innerText = "";
    }


    if (plan === "") {
        document.getElementById("planError").innerText = "Por favor, seleccione un departamento.";
        isValid = false;
    } else {
        document.getElementById("planError").innerText = "";
    }



    if (!gender) {
        document.getElementById("genderError").innerText = "Por favor, seleccione su género.";
        isValid = false;
    } else {
        document.getElementById("genderError").innerText = "";
    }


    if (image === "") {
        document.getElementById("imageError").innerText = "Por favor, seleccione una imagen.";
        isValid = false;
    } else {
        document.getElementById("imageError").innerText = "";
    }

 
    if (isValid) {
        var modal = document.getElementById("myModal");
        modal.style.display = "block";
        setTimeout(function() {
            modal.style.display = "none";
            window.location.reload();
        }, 3000);
    }


    return false;
}

function isValidEmail(email) {
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}