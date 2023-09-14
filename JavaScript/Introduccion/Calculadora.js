
let operador = prompt("Que operacion desea hacer: 1 - sumar || 2 - Restar || 3 - Multiplicar || Dividir");
let numero1 = Number(promp("Ingrese el primer numero"))
let numero2 = Nunmber(promp("Ingrese el segundo numero"))
let total;

if(operador == 1){
    total = numero1+numero2
    alert("El resultado de la suma es de"+ total)
}else if(operador == 2){
    total = numero1-numero2
    alert("El resultado de la resta es de"+ total)
}else if(operador == 3){
    total = numero1*numero2
    alert("El resultado de la multiplicacion es de"+ total)
}else if(operador == 4){
    total = numero1/numero2
    alert("El resultado de la division es de"+ total)
}else{
    alert("Opcion de operacion incorrecta")
}