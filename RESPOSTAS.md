# Respostas — Reflexão sobre os paradigmas

**Nome:** Renatto Gabriel Lira Freire Duarte
**Matrícula:** 2536043

## 1. Orientação a objetos
Quais foram as vantagens e as dificuldades de resolver o problema com classes (semanas 1 e 2)?

**Vantagens:** o problema ficou organizado como no mercado: cada tipo de produto virou uma classe e cada uma sabe a sua alíquota. A validação do preço negativo ficou em um único lugar, no setter da `Produto`, e vale para todos. O `Carrinho` ficou simples, porque só chama `imposto()` sem saber o tipo de cada produto.

**Dificuldades:** foi difícil entender a `property` com setter e por que o `__init__` precisa usar `self.preco = preco` para a validação valer na criação. Também deu trabalho organizar o estado do carrinho e impedir que um erro deixasse o carrinho pela metade.

## 2. Programação funcional
Quais foram as vantagens e as dificuldades de resolver o problema com funções puras, sem classes e sem laços (semanas 3 e 4)?

**Vantagens:** o código ficou mais curto e fácil de testar, pois cada função recebe dados e devolve um resultado sem alterar nada de fora. Como a lista não é modificada, uma função não estraga os dados de outra. A closure `criar_calculadora` e a `compor` mostram que dá para montar comportamentos novos combinando funções pequenas.

**Dificuldades:** foi preciso pensar sem `for` e `while`, usando `map`, `filter`, `sorted` e compreensões. A `compor`, que aplica as funções da direita para a esquerda, e o `reduce` demoraram a fazer sentido.

## 3. Comparação
Se o governo criasse uma nova categoria de produto (por exemplo, "redução de 30%"), o que você precisaria mudar em cada versão? Qual delas seria mais fácil de alterar? Por quê?

**Com objetos:** criaria uma nova subclasse de `Produto` com a nova alíquota, sem mexer na `Produto` nem no `Carrinho`, porque o polimorfismo faz o carrinho funcionar sozinho.

**Na versão funcional:** adicionaria a categoria no dicionário `ALIQUOTAS` e também no dicionário dentro da `criar_calculadora`. O `gerar_relatorio` já pegaria a nova categoria sozinho.

Pra mim, a versão com objetos é mais fácil de alterar, porque a mudança é só acrescentar código novo, sem editar o que já funciona. Na funcional são poucas linhas, mas esquecer um dos dois dicionários causa erro.

## 4. Alíquota zero
Explique, com suas palavras, por que um produto da cesta básica ainda executa o método `imposto()` em vez de "pular" o cálculo.

Porque alíquota zero não é isenção: o imposto existe e é calculado, só que o resultado é zero (preço × 0% = R$ 0,00). Na lei isso importa porque, com alíquota zero, a empresa mantém os créditos do imposto pago nas etapas anteriores. No código, é o polimorfismo: todo produto responde ao mesmo `imposto()`, e o da cesta básica devolve `0.0`, então o carrinho não precisa de nenhum `if` para tratar a cesta básica de forma especial.
