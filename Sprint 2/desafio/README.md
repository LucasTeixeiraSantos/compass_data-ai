## Antes da Normalização
<img src="https://github.com/LucasTeixeiraSantos/compass_data-ai/blob/main/Sprint%202/desafio/tb_locacao.png" alt="tb_locacao.png" />

## Normalização da Base de Dados do Sistema de Gerenciamento de Pedidos

Este documento descreve os passos seguidos para a normalização da base de dados de um sistema de alugueis de carros. A normalização foi realizada para minimizar redundâncias e manter a integridade dos dados.

### Passos de Normalização

1. **Identificação das Entidades**
   - As principais entidades do sistema foram identificadas: `clientes`, `vendedores`, `carros` e `combustiveis`.

2. **Criação de Tabelas Separadas**
   - Para cada entidade identificada, foi criada uma tabela separada para armazenar seus dados.
   - As tabelas criadas são: `clientes`, `vendedores`, `carros` e `combustiveis`.

3. **Definição de Chaves Primárias**
   - Cada tabela possui uma chave primária (`PK`) que identifica unicamente cada registro dentro da tabela.
   - As chaves primárias definidas são:
     - `clientes`: `idCliente`
     - `vendedores`: `idVendedor`
     - `carros`: `idCarro`
     - `combustiveis`: `idCombustivel`

4. **Definição de Chaves Estrangeiras**
   - As relações entre tabelas foram definidas usando chaves estrangeiras (`FK`).
   - As chaves estrangeiras definidas são:
     - `locacoes`: `idCliente` (referencia `clientes`), `idCarro` (referencia `carros`),`idVendedor` (referencia `vendedores`)
     - `carros`: `idcombustivel` (referencia `combustiveis`).

## Locacoes após a Normalização

<img src="https://github.com/LucasTeixeiraSantos/compass_data-ai/blob/main/Sprint%202/desafio/locacoes_fato.png" alt="locacoes_fato.png" />

## Modelo Dimensional

<img src="https://github.com/LucasTeixeiraSantos/compass_data-ai/blob/main/Sprint%202/desafio/modelo-dimensional.png" alt="modelo-dimensional.png" />
