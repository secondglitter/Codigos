// archivo que contiene los algoritmos de ordenamiento

function obtieneArreglo(){
    //idea de la página https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/trim
      var contenidoarr = document.getElementById("arreglodesord").value.trim();
      var idalgoritmo = document.getElementById("algoritmos").value.trim();
      var arreglosinespacio=contenidoarr.split(',').map(element => parseInt(element.trim()));
      var arregloord=[];
    switch(idalgoritmo){
          case '1': arregloord=ebuuble(arreglosinespacio); 
          document.getElementById("resultado").textContent ="Arreglo Ordenado [ " + arregloord.join(", ") + " ]" ;
          break;
          case '2': arregloord=quicksort(arreglosinespacio); 
          document.getElementById("resultado").textContent ="Arreglo Ordenado [ " + arregloord.join(", ") + " ]" ;
          break;
          case '3': arregloord=insertionsort(arreglosinespacio); 
          document.getElementById("resultado").textContent ="Arreglo Ordenado [ " + arregloord.join(", ") + " ]" ;
          break;
          case '4': arregloord=mergeshort(arreglosinespacio);
          document.getElementById("resultado").textContent ="Arreglo Ordenado [ " + arregloord.join(", ") + " ]" ;
          break;
          case '5': arregloord=selectionsort(arreglosinespacio); 
          document.getElementById("resultado").textContent ="Arreglo Ordenado [ " + arregloord.join(", ") + " ]" ;
          break;
      }
  }
  
// ebuuble
 function ebuuble(arreglo){
        console.log(arreglo)
        long = arreglo.length;
    do {
        ordenado = false;
        for (i = 0; i < long - 1; i++) {
            if (arreglo[i] > arreglo[i + 1]) {
                temp = arreglo[i];
                arreglo[i] = arreglo[i + 1];
                arreglo[i + 1] = temp;
                ordenado = true
            }
        }
    } while (ordenado);
    return arreglo;
}

// quicksort

function quicksort (cadena){
    console.log(cadena)
    if(cadena.length<1){
        return[];
    }
    var left = [];
    var right = [];
    var pivote = cadena [0];
    for (i=1; i < cadena.length; i++){
        if(cadena[i]<pivote){
            left.push(cadena[i])
        }else{
            right.push(cadena[i])
        }
    }
    return[].concat(quicksort(left),pivote,quicksort(right));
} 

// insertion

function insertionsort(arr) {
    console.log(arr)
    const length = arr.length;

    for (let i = 1; i < length; i++) {
        let j = i;
        const currentElement = arr[i];

        while (j > 0 && arr[j - 1] > currentElement) {
            arr[j] = arr[j - 1];
            j--;
        }

        arr[j] = currentElement;
    }

    return arr;
} 

// merge

function combinar (izquierda, derecha){
	let resultado = [] ;
	let indiceizquierdo = 0;
	let indicederecho = 0;

	while (indiceizquierdo < izquierda.length && indicederecho < derecha.length) {
	  if (izquierda[indiceizquierdo] < derecha [indicederecho]) {
	     resultado.push(izquierda[indiceizquierdo]);
	     indiceizquierdo++;
	  } else{
	     resultado.push(derecha[indicederecho]);
	     indicederecho++;
	  }
	}

	 return resultado.concat(
		izquierda.slice(indiceizquierdo),
		derecha.slice(indicederecho)
	);
}

function mergeshort(merge) {
    console.log(merge)
	const longitud = merge.length;
	
	if (longitud <= 1) {
	  return merge;
	}

	const medio = Math.floor(longitud / 2);
	const izquierda = merge.slice(0, medio);
	const derecha = merge.slice(medio);

	return combinar(mergeshort(izquierda), mergeshort(derecha));
} 

//selection

function selectionsort(selection) {
    console.log(selection)
    const n = selection.length;
    for (let i = 0; i < n - 1; i++) {
        let minIndex = i;
    for (let j = i + 1; j < n; j++) {
        if (selection[j] < selection[minIndex]){
            minIndex = j;
        }
    }
    if (minIndex !== i) {
        const temp = selection[i];
        selection[i] = selection[minIndex];
        selection[minIndex] = temp
    }
    }
    return selection;
}

