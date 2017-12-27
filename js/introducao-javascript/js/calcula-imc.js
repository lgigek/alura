var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista"

var pacientes = document.querySelectorAll(".paciente");

for (var i = 0; i < pacientes.length; i++) {

    var paciente = pacientes[i];

    var pesoTd = paciente.querySelector(".info-peso");
    var alturaTd = paciente.querySelector(".info-altura");
    var imcTd = paciente.querySelector(".info-imc");

    var peso = pesoTd.textContent;
    var altura = alturaTd.textContent;

    var pesoEValido = true;
    var alturaEValido = true;

    if (pesoTd.textContent <= 0 || pesoTd.textContent >= 500) {
        pesoEValido = false;
        imcTd.textContent = "Peso inválido";
        paciente.classList.add("paciente-invalido");
    }

    if (alturaTd.textContent <= 0 || alturaTd.textContent >= 3.00) {
        alturaEValido = false;
        imcTd.textContent = "Altura inválida";
        paciente.classList.add("paciente-invalido");
    }

    if (pesoEValido && alturaEValido) {
        var imc = calculaImc(peso, altura);
        imcTd.textContent = imc;
    }
}

function calculaImc(peso, altura){
    var imc = 0
    imc = peso / (altura * altura);
    return imc.toFixed(2)
}
