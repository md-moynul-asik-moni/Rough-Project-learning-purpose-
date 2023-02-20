


outer:
for (var i = 0; i<3; i++){
    document.write(i + '<br/>')
    for (var j = 0; j<5; j++){

        document.write(j + '<br/>');
        if(j == 3) 
            break outer;
    }
}