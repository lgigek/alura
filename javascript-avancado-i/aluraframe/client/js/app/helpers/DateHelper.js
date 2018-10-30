class DateHelper {

    constructor() {

        throw new Error('Essa classe não pode ser instanciada');
    }

    static textoParaData(texto) {
        /*
         criando um date no padrão "new Date(yyyy, MM, dd)", o mês vai de 0 à 11
         quando cria uma arrow function inline, não precisa de `return`
        */

        if (!/\d{4}-\d{2}-\d{2}/.test(texto))
            throw new Error('Deve estar no formato yyyy-MM-dd');

        return new Date(...texto
            .split('-')
            .map((item, indice) => item - indice % 2)
        );
    }

    static dataParaTexto(data) {

        return `${data.getDate()}/${data.getMonth() + 1}/${data.getFullYear()}`;
    }

}