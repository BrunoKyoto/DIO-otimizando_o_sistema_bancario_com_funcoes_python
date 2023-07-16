# [Lab Project] Otimizando o Sistema Bancário com Funções Python

## Nesse projeto fomos instigados à aperfeiçoar o último algoritmo, referente ao sistema bancário.

## Foi bastante desafiador, pois dessa vez tivemos que obedecer alguns critérios e regras de processamento, como o uso de funções e o modo em que os argumentos são passados para essas mesmas funções, onde alguns deveriam ser inseridos como posicionais e outros referenciados pelo conjunto chave/valor.

## Eu tomei a liberdade de modificar levemente o projeto. Em dado momento, há a criação de uma função que lista todas as contas cadastradas no sistema; eu modifiquei essa função e a renomeei para "acessar_conta". O nome é autoexplicativo, mas o que ela realmente faz é filtrar apenas a conta referente ao CPF informado. Esse mecanismo poderia ser aprimorado e filtrar também os dados por número de conta, para possibilitar o acesso à múltiplas contas, mas por falta de tempo, não pude implementar a melhoria, pelo menos, por enquanto. Então, a função encerra ao encontrar a primeira conta cadastrada com o CPF informado.

## Caso a conta seja localizada, encerram-se igualmente a função e o laço de repetição atual (via comando "break") e inicia-se o segundo laço, simulando o acesso à referida conta, onde é possível realizar as movimentações de depósito, saque e impressão de extrato.

## Tanto a função de depósito quanto saque realizam a verificação do valor informado para assegurar que trata-se de um número válido (> 0). A função de saque verifica se há fundos para concluir a operação, mas também verifica se o número máximo diário de saques foi ou não atingido (= 3 saques diários) e se o valor solicitado para retirada é menor que R$500,00. Ambas funções, se devidamente executadas, incrementam a variável extrato com uma nova string, que registra a natureza da operação e a quantia movimentada.

## A função "exibe_extrato" é igualmente autoexplicativa; exibe o saldo atual e as movimentações executadas. Vale lembrar que essa função também poderia sofrer melhorias, como identificar a conta e o cliente, por exemplo. Mas, por questões de disponibilidade de tempo, tal implementação ainda não foi realizada.

## O projeto foi, sim, desafiador, porém, posso dizer que também foi muito recompensador perceber o resultado final. Sim, é um algoritmo muito simples e nem é realmente funcional, mas é muito prazeroso observar a lógica por trás de tudo e como tudo funciona ordenadamente. A programação e o que pode ser construído a partir dela é maravilhosamente belo!

## O código pode ser acessado através do arquivo: "sistema_bancario_v2.py".

### Potência Tech powered by iFood | Ciências de Dados com Python | Dominando o Python Para Ciência de Dados | [Lab Project] Criando um Sistema Bancário com Python