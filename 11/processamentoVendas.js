// --- 1. DADOS INICIAIS ---
// Lista de vendas representando um problema real.
const vendas = [150.00, 80.50, 210.25, 50.00, 300.00, 120.75];

console.log(`Lista de vendas original: [${vendas.join(', ')}]\n`);


// --- 2. USO DE FUNÇÕES DE ALTA ORDEM ---

// a) .filter(): Cria uma nova lista apenas com vendas acima de R$ 100.
// A função filter recebe uma "arrow function" como argumento.
const vendasFiltradas = vendas.filter(v => v > 100);
console.log(`Vendas filtradas (acima de R$ 100): [${vendasFiltradas.join(', ')}]`);

// b) .map(): Aplica uma função de desconto de 10% a cada item da lista filtrada.
const vendasComDesconto = vendasFiltradas.map(v => v * 0.9);
// Formatando a saída para melhor visualização.
const vendasFormatadas = vendasComDesconto.map(v => v.toFixed(2));
console.log(`Vendas com desconto de 10%: [${vendasFormatadas.join(', ')}]\n`);


// --- 3. USO DE RECURSÃO ---

const somaRecursiva = (listaDeValores) => {
  /**
   * Soma os valores de uma lista de forma recursiva.
   */
  if (listaDeValores.length === 0) {
    return 0;
  }
  // Passo recursivo: soma o primeiro elemento com o resultado
  // da soma do resto da lista (criado com .slice(1)).
  else {
    const [primeiroElemento, ...restoDaLista] = listaDeValores;
    return primeiroElemento + somaRecursiva(restoDaLista);
  }
};

const totalFinal = somaRecursiva(vendasComDesconto);

console.log("--- Calculando o total final com recursão ---");
console.log(`A soma total das vendas processadas é: R$ ${totalFinal.toFixed(2)}`);