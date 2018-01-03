describe("Paciente", function(){

    it("deve calcular imc", function (){
        var teste = new Paciente("teste", 50, 80, 1.80);

        expect(teste.imc()).toEqual(80 / (1.80 * 1.80));
    });

    it("deve calcular batimentos", function(){
        var teste = new Paciente("teste", 50, 80, 1.80);

        expect(teste.batimentos()).toEqual(50 * 365 * 24 * 60 * 80);
    });
});