describe("Consulta", function(){

    it("não deve cobrar se for um retorno", function(){
        var paciente = new Paciente("teste", 50, 80, 1.80);
        var consulta = new Consulta(consulta, [], true, true);

        expect(consulta.preco()).toEqual(0);
    });

    it("deve cobrar 25 para cada procedimento comum", function(){
        var paciente = new Paciente("teste", 50, 80, 1.80);
        var consulta = new Consulta(consulta, ["proc-comum-1","proc-comum-2"], false, false);

        expect(consulta.preco()).toEqual(50);
    });

    it("deve cobrar o preço para cada procecimento específico", function(){
        var paciente = new Paciente("teste", 50, 80, 1.80);
        var consulta = new Consulta(consulta, ["proc-comum-1","raio-x","gesso"], false, false);

        expect(consulta.preco()).toEqual(25+55+32);
    });

    it("deve cobrar o dobro para consultas particulares", function(){
        var paciente = new Paciente("teste", 50, 80, 1.80);
        var consulta = new Consulta(consulta, ["proc-comum-1"], true, false);

        expect(consulta.preco()).toEqual(25*2);
    });

});