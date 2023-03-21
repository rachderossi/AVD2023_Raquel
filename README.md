# AVD2023_Raquel

## 20/02
- Na pasta crawlercamilo criei um script Python que faz a extração automática das 54 obras de Camilo Castelo Branco.
- Na pasta obras temos as obras em formato mobi. Ainda preciso converter os arquivos mobi em txt.
- Na pasta markdowns temos o arquivo em html e markdown das obras: A espada de Alexandre e A senhora Rattazzi.

## 02/03
- Atualizado o campo de data das obras em markdown.
- Adicionado arquivo csv com a estrtura das duas obras escolhidas: A espada de Alexandre e A senhora Rattazzi.

## 13/03
- Procurei as obras que não constavam na lista de obras e encontrei versões no Gutemberg e no Open Library.
- Anexei o link na coluna de notas do sheets.

## 21/03
- Utilizei o comando linguakit tagger pt -nec Camilo-Amor_de_Perdicao.txt > Camilo-Amor_de_Perdicao.tag para fazer a leitura do documento de interesse (Camilo-Amor_de_Perdicao.txt)e faz a classificação de cada palavra do texto e salva a saída em um novo documento (Camilo-Amor_de_Perdicao.tag).
- Após utilizei o comando grep NP Camilo-Amor_de_Perdicao.tag | sort | uniq -c | sort -n > NP_resultados.csv que faz a busca (utilizando o grep) de todas as entidades (NP) no arquivo Camilo-Amor_de_Perdica.tag, as ordena (sort) em ordem crescente e salva a saída em um novo documento (NP_resultados.csv).
- Por fim, utilizando o Google sheets, dividi o texto em colunas e usei como separador os espaços em branco conseguindo assim deixar o resultado final em 4 colunas.
