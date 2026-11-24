# Classificação de chamados de suporte: regras em Python vs. IA

Projeto pequeno de estudo em Python (pandas) que compara duas formas de classificar chamados de suporte técnico em **rede**, **hardware** ou **software**: um classificador por palavras-chave feito por mim e uma IA generativa (ChatGPT).

## Por que fiz isso

Trabalhei com suporte técnico presencial e quis testar, com números, até onde regras simples chegam e onde uma IA se sai melhor, em vez de apenas usar a IA sem avaliar o resultado.

## Dados

- **45 chamados de desenvolvimento**, usados para criar e ajustar as regras.
- **15 chamados de teste**, novos, usados só para medir (as regras não foram alteradas depois de ver esse resultado).
- Os chamados são curtos e foram escritos em português com ajuda de IA (Claude). As categorias corretas são o critério que adotei.
- Alguns chamados são ambíguos de propósito, por exemplo "O computador está lento".

## Método

1. **Regras:** um dicionário em Python com palavras-chave por categoria. Se nenhuma palavra bate, o chamado cai em "outro" (que conta como erro, pois não existe como categoria correta).
2. **IA:** colei a lista de chamados, sem as categorias, e pedi uma classificação por linha. Repeti com os chamados em **ordem aleatória**, em uma conversa nova, para verificar se a ordem influenciava o resultado.
3. **Medida:** percentual de acertos comparado com a categoria que defini.

## Resultados

| Método | 45 chamados (desenvolvimento) | 15 chamados novos (teste) |
|---|---|---|
| Regras, versão inicial | 51% | não medido |
| Regras, depois dos ajustes | 100% (ajustadas nesses mesmos dados) | 80% (12 de 15) |
| IA (ordem aleatória) | 98% (44 de 45) | 93% (14 de 15) |

- Os 100% das regras mostram **sobreajuste**: eu as ajustei olhando esses mesmos chamados. O número que vale é o do teste.
- Na primeira rodada da IA, os chamados estavam ordenados por categoria: ela acertou 44 de 45 e 15 de 15 no teste. Com a ordem aleatória, acertou 44 de 45 e 14 de 15. A diferença é de um chamado, então a ordem não pareceu inflar o resultado de forma relevante.

## Análise dos erros

**Regras (teste):** os 3 erros foram chamados que caíram em "outro", ou seja, **faltavam palavras-chave**, não houve confusão entre categorias:
- "As páginas demoram uma eternidade para carregar" (rede)
- "Apareceu uma mensagem dizendo que meus arquivos foram bloqueados" (software)
- "O computador demora muito para iniciar" (software)

Um detalhe que limita as regras: "demora" aparece em um chamado de rede e em outro de software. Uma palavra-chave sozinha não separa os dois sem entender o contexto da frase.

**IA:** errou em chamados ambíguos, onde duas pessoas poderiam discordar:
- "O site abre no celular mas não no computador" (marquei rede, a IA disse software)
- "Ninguém aqui do setor consegue abrir o sistema da empresa pela rede" (marquei rede, a IA disse software)
- Na rodada com a lista ordenada: "Não consigo imprimir" (marquei hardware, a IA disse software)

## Limitações

- Poucos dados: com 15 chamados, cada erro muda o resultado em cerca de 7 pontos. A diferença entre 80% e 93% é de 2 chamados, então **não dá para afirmar que uma é claramente melhor**.
- Os chamados são curtos e claros; chamados reais costumam ser mais longos e confusos.
- As categorias são o meu critério; nos casos ambíguos, outra pessoa poderia decidir diferente.
- As respostas de uma IA podem variar de uma tentativa para outra.

## Como usei IA

- Para ajudar a escrever a lista inicial de chamados e a estruturar o código em Python.
- Como um dos classificadores comparados (seção Método).
- Executei o código, ajustei as regras olhando os erros e medi os resultados. A análise dos erros e este README foram escritos com ajuda de IA e revisados por mim.

## Como executar

```
pip install pandas
python classificador_final.py
```

Os arquivos `tickets.csv` e `tickets_teste.csv` devem estar na mesma pasta do script.
