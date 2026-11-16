# Respostas — Reflexão sobre os paradigmas

**Nome: Renatto Gabriel Lira Freire Duarte**
**Matrícula: 2536043**

## 1. Orientação a objetos
Quais foram as vantagens e as dificuldades de resolver o problema com classes (semanas 1 e 2)?

**Vantagens:** o problema ficou organizado do jeito que a gente pensa no mercado. Cada tipo de produto virou uma classe (`ProdutoCestaBasica`, `ProdutoReduzido`, `ProdutoPadrao`) e cada uma sabe a sua própria alíquota. A validação do preço negativo ficou em um único lugar, no setter da `Produto`, e vale para todos. O `Carrinho` também ficou simples, porque ele só chama `imposto()` e não precisa saber de que tipo é cada produto.

**Dificuldades:** no começo foi difícil entender a `property` com o setter e por que o `__init__` precisa usar `self.preco = preco`, e não `self._preco`, para a validação funcionar na criação. Também deu mais trabalho organizar o estado do carrinho (o dicionário de nome para produto e quantidade) e cuidar para que um erro ao adicionar não deixasse o carrinho pela metade.

## 2. Programação funcional
Quais foram as vantagens e as dificuldades de resolver o problema com funções puras, sem classes e sem laços (semanas 3 e 4)?

**Vantagens:** o código ficou mais curto e mais fácil de testar, porque cada função só recebe dados e devolve um resultado, sem alterar nada de fora. Como a lista não é modificada, não há risco de uma função estragar os dados de outra. A `criar_calculadora` (closure) e a `compor` mostraram que dá para montar comportamentos novos combinando funções pequenas.

**Dificuldades:** foi preciso pensar sem `for` e sem `while`, usando `map`, `filter`, `sorted` e compreensões. A `compor`, que aplica as funções da direita para a esquerda, e o `reduce` demoraram para fazer sentido. Também é mais difícil ler uma sequência de funções encadeadas do que um passo a passo com laço.

## 3. Comparação
Se o governo criasse uma nova categoria de produto (por exemplo, "redução de 30%"), o que você precisaria mudar em cada versão? Qual delas seria mais fácil de alterar? Por quê?

**Na versão com objetos:** criaria uma nova subclasse de `Produto` com a alíquota da nova categoria. Não precisaria mexer na `Produto` nem no `Carrinho`, porque o polimorfismo faz o carrinho funcionar sozinho com a classe nova.

**Na versão funcional:** teria que adicionar a categoria no dicionário `ALIQUOTAS` e também no dicionário de dentro da `criar_calculadora`. O `gerar_relatorio` já pegaria a nova categoria sozinho, porque percorre o `ALIQUOTAS`.

Para mim a versão com objetos seria mais fácil de alterar, porque a mudança é só acrescentar código novo, sem editar o que já funciona. Na funcional são poucas linhas, mas é preciso lembrar de alterar dois lugares, e esquecer um deles dá erro.

## 4. Alíquota zero
Explique, com suas palavras, por que um produto da cesta básica ainda executa o método `imposto()` em vez de "pular" o cálculo.

Porque alíquota zero não é isenção. Na alíquota zero o imposto existe e é calculado, só que o resultado é zero (preço × 0% = R$ 0,00). Na isenção a operação sairia da cobrança. Na lei, isso importa porque com alíquota zero a empresa mantém os créditos do imposto pago nas etapas anteriores.

No código, isso também é o polimorfismo funcionando: todo produto responde ao mesmo método `imposto()`, e o da cesta básica simplesmente devolve `0.0`. Assim o carrinho não precisa de nenhum `if` para tratar a cesta básica de forma especial.
