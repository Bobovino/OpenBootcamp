import {suma,multiplica} from "./modulos/controller.js";
import chalk from 'chalk';

//Crea un nuevo proyecto de Node
//- Configura el proyecto para utilizar los módulos de ES6
//- En el entrypoint index.js, importa el módulo controller.js
//- El entrypoint index.js debe utilizar las funciones del módulo para devolver la multiplicación de suma(1, 2) y suma(4, 5)
console.log(multiplica(suma(1, 2),suma(4, 5)))
//- Instala e importa la librería chalk (https://www.npmjs.com/package/chalk)

//- Modifica el último console.log del entrypoint index.js para devolver el resultado en color verde
console.log(chalk.green(multiplica(suma(1, 2),suma(4, 5))))

console.log(chalk.blue('Me gusta el azul.'));