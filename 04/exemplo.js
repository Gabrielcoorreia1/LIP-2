// 1. Tipagem dinâmica: 'valor' é um número.
let valor = 10;
console.log(`O valor é ${valor} e o tipo é ${typeof valor}`);

// 2. Agora a mesma variável guarda um texto.
valor = "dez";
console.log(`O valor agora é '${valor}' e o tipo mudou para ${typeof valor}`);

// 3. Tipagem fraca em ação (coerção de tipo).
// O JavaScript converte o número 10 para string e concatena,
// em vez de lançar um erro.
let somaInesperada = 10 + "5";

console.log(`\nJavaScript é fracamente tipado:`);
console.log(`O resultado de 10 + "5" é: ${somaInesperada}`);
console.log(`O tipo do resultado é: ${typeof somaInesperada}`);