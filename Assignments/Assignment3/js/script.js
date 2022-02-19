( function() {
    var names = [ "John", "Eanna", "Raj", "jai", "Anky", "Hari", "Shiva"];

    for(var i = 0; i < names.length; i++){
        var firstCharacter = names[i].charAt(0).toLowerCase();

        if(firstCharacter === 'j')
        goodbyegreeter.sayGoodBye(names[i]);
        else
        hellogreeter.sayHello(names[i]);
    }
})();