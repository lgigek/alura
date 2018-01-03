describe("Maior e Menor", function(){

    it("deve retornar maior e menor com os números ordem não sequencial", function(){
        var algoritmo = new MaiorMenor();
        algoritmo.encontra([10,5,15,2]);

        expect(algoritmo.pegaMaior()).toEqual(15);
        expect(algoritmo.pegaMenor()).toEqual(2);
    });

    it("deve retornar maior e menor com os números ordem crescente", function(){
        var algoritmo = new MaiorMenor();
        algoritmo.encontra([1,2,3,4]);

        expect(algoritmo.pegaMaior()).toEqual(4);
        expect(algoritmo.pegaMenor()).toEqual(1);
    });

    it("deve retornar maior e menor com os números ordem decrescente", function(){
        var algoritmo = new MaiorMenor();
        algoritmo.encontra([9,8,7,6]);

        expect(algoritmo.pegaMaior()).toEqual(9);
        expect(algoritmo.pegaMenor()).toEqual(6);
    });

    it("deve retornar maior e menor com apenas um número",function(){
        var algoritmo = new MaiorMenor();
        algoritmo.encontra([9]);

        expect(algoritmo.pegaMaior()).toEqual(9);
        expect(algoritmo.pegaMenor()).toEqual(9);
    });

});