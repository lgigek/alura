var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista"

var pacientes = document.querySelectorAll(".paciente");

for (var i = 0; i < pacientes.length; i++) {

    var paciente = pacientes[i];

    var peso = paciente.querySelector(".info-peso");
    var altura = paciente.querySelector(".info-altura");
    var imc = paciente.querySelector(".info-imc");

    var pesoEValido = true;
    var alturaEValido = true;

    if (peso.textContent <= 0 || peso.textContent >= 500) {
        pesoEValido = false;
        imc.textContent = "Peso inválido";
        paciente.classList.add("paciente-invalido");
    }

    if (altura.textContent <= 0 || altura.textContent >= 3.00) {
        alturaEValido = false;
        imc.textContent = "Altura inválida";
        paciente.classList.add("paciente-invalido");
    }

    if (pesoEValido && alturaEValido) {
        var valorImc = peso.textContent / (altura.textContent * altura.textContent);
        imc.textContent = valorImc.toFixed(2);
    }
}


var botaoAdicionar = document.querySelector("#adicionar-paciente")


console.log(botaoAdicionar);

botaoAdicionar.addEventListener("click", function(){
    console.log("botao clicado")
});


