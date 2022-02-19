( function (window) {
 var hellogreeter = {};
 var greeting = "Hello";
  hellogreeter.sayHello = function(name) {
      console.log(greeting + " " + name);
  }
  window.hellogreeter = hellogreeter;
}) (window);