var express = require('express');
// inicializando o express
var app = express();

app.set('view engine', 'ejs');

app.get('/produtos', function(req, res){
    console.log("testando o nodemon");
    res.render("produtos/lista");
});

app.listen(3000,function(){
    console.log("Servidor rodando");
});
