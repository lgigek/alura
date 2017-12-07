var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista"

var peso = document.querySelector("#primeiro-paciente .info-peso");
var altura = document.querySelector("#primeiro-paciente .info-altura");
var imc = document.querySelector("#primeiro-paciente .info-imc");

var pesoEValido = true;
var alturaEValido = true;

if (peso.textContent <= 0 || peso.textContent >= 500){
    pesoEValido = false;
    imc.textContent = "Peso inválido";
}

if (altura.textContent <= 0 || altura.textContent >= 3.00){
    alturaEValido = false;
    imc.textContent = "Altura inválida";
}

if (pesoEValido && alturaEValido){
    var valorImc = peso.textContent / (altura.textContent * altura.textContent );
    imc.textContent = valorImc;
}
