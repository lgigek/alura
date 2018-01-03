describe("Consulta", function(){

    var paciente;

    beforeEach(function(){
        // paciente = new PacienteBuilder.comPeso(90).constroi();
        paciente = new PacienteBuilder().constroi();
    })
    
    describe("consultas com tipo retorno", function(){
        it("não deve cobrar se for um retorno", function(){
            var consulta = new Consulta(paciente, [], true, true);

            expect(consulta.preco()).toEqual(0);
        });
    });

    describe("consultas com procedimento", function(){

        it("deve cobrar 25 para cada procedimento comum", function(){
            var consulta = new Consulta(paciente, ["proc-comum-1","proc-comum-2"], false, false);

            expect(consulta.preco()).toEqual(50);
        });

        it("deve cobrar o preço para cada procecimento específico", function(){
            var consulta = new Consulta(paciente, ["proc-comum-1","raio-x","gesso"], false, false);

            expect(consulta.preco()).toEqual(25+55+32);
        });

        it("deve cobrar o dobro para consultas particulares", function(){
            var consulta = new Consulta(paciente, ["proc-comum-1"], true, false);

            expect(consulta.preco()).toEqual(25*2);
        });

    });

});