# AVD2023_Raquel

## 20/02
- Na pasta **crawlercamilo** criei um script Python que faz a extração automática das 54 obras de Camilo Castelo Branco.
- Na pasta obras temos as obras em formato mobi. 
- Na pasta **markdowns** temos o arquivo em html e markdown das obras: A espada de Alexandre e A senhora Rattazzi.

## 02/03
- Atualizado o campo de data das obras em markdown.
- Adicionado arquivo **estrutura_obras.csv** com a estrtura das duas obras escolhidas: A espada de Alexandre e A senhora Rattazzi.

## 13/03
- Procurei as obras que não constavam na lista de obras e encontrei versões no Gutemberg e no Open Library.
- Anexei o link na coluna de notas do sheets.

## 21/03
- Utilizei o comando **linguakit tagger pt -nec Camilo-Amor_de_Perdicao.txt > Camilo-Amor_de_Perdicao.tag** para fazer a leitura do documento de interesse (Camilo-Amor_de_Perdicao.txt)e faz a classificação de cada palavra do texto e salva a saída em um novo documento (Camilo-Amor_de_Perdicao.tag).
- Após utilizei o comando **grep NP Camilo-Amor_de_Perdicao.tag | sort | uniq -c | sort -n > NP_resultados.csv** que faz a busca (utilizando o grep) de todas as entidades (NP) no arquivo Camilo-Amor_de_Perdica.tag, as ordena (sort) em ordem crescente e salva a saída em um novo documento (NP_resultados.csv).
- Por fim, utilizando o Google sheets, dividi o texto em colunas e usei como separador os espaços em branco conseguindo assim deixar o resultado final em 4 colunas.

## 27/03
- Utilizando o *software R* criei gráficos de barras com as informações do arquivo **NP_resultados.csv**.
- Foram criados 4 gráficos de barras, um para cada tipo de entidade nomeada, adicionei também a frequência realtiva (%) aos gráficos.
- Para a criação dos gráficos de barras, considerei apenas palvras com 10 ocorrências ou mais.
- Alguns grupos de palavras não foram agrupadas nas entidades nomeadas corretamente, então para que não houvesse perda de dados fiz a etiquetação correta em cada grupo.
- O script da criação das visualizações se encontra no arquivo **amor_viz.Rmd**.

## 03/04
- Com o linguakit, utilizei o parâmetro *seg* para fazer a segmentação de frases **linguakit seg pt Camilo-Amor_de_Perdicao.txt**,  que retornou uma frase por linha. E o parâmetro *sent* para fazer a análise de sentimento de cada frase **linguakit sent pt Camilo-Amor_de_Perdicao.csv**.
- Inclui na base de dados uma coluna com a informação do capítulo do livro, isso foi feito a partir da filtragem pelo número da linha que contnha a palavra CAPÍTULO. Escolhi os três primeiros capítulos.
- Com a base de dados completa (capítulos, texto e sentimento), construi gráficos de barras e nuvem de palavras para cada capítulo.
- O script da criação das visualizações se encontra no arquivo **viz_capitulos.Rmd**.

## 20/04
- Utilizando o script em python *script_sentlex.py* criado na última aula com o professor, foi gerado uma base de dados com as informações de número de caracteres, número de palavras e polarização do sentimento de cada um dos 17 capítulos do livro *harry potter e a pedra filosofal*.
- A seguir criei duas colunas com frequências relativas do número de caracteres e do número de palavras. 
- Foram criados 3 gráficos de barras, um para cada tipo de variável da base de dados, adicionei também a frequência realtiva (%) aos gráficos.
- Por fim, coonforme discutido na aula anterior realizei uma análise de cluster para classificar os capítulos em grupos com similaridades utilizando o método de clusterização *K-means*.
- O script da criação das visualizações se encontra no arquivo **viz_harrypotter.Rmd** e o gráfico de clusterização em **cluster.R**.
