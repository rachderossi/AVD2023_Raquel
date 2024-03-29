library(factoextra)
library(dplyr)
library(ggplot2)

## Análise de cluster

# classificar os objetos em grupos
# objetos dentro do mesmo grupo sejam mais similares
# grupos sejam mais diferentes

dados <- read.csv("/Users/raquelrossi/Desktop/aula7/sentlex - sentlex.csv")

# selecionando apenas as colunas que irão nos ajudar a defnir os grupos
dados2 <- dados %>% select(caracteres, palavras, sentimento)

# o escalonamento dos dados nos ajuda a padronizar os dados de modo que cada variável 
# apresente média zero e variância unitária.
df=scale(dados2)


# gráfico para nos ajudar a definir o número de clusters

# utilizando a noção da soma dos quadrados intra cluster é possível verificar que o 
# número ótimo de clusters para a amostra é 4. Isto porque novos clusters acima de 4 possuem
# baixo ganho para aumentar a diferenciação dos demais.
fviz_nbclust(df, kmeans, method = "wss")

# clusterização k-means
set.seed(123)
km.res=kmeans(df, 4, nstart=3)
print(km.res)


# verificando características de cada aglomeração
aggregate(dados2, by=list(cluster=km.res$cluster), mean)

# informações dos clusters calculados
cluster=cbind(dados2, cluster=km.res$cluster)
head(cluster)

# distância dos centros
km.res$centers


# cluster plot
fviz_cluster(km.res, data=cluster,
             palette = c("#2E9FDF", "#00AFBB", "#E7B800", "#FC4E07"),
             ellipse.type="euclid",
             star.plot=TRUE,
             repel=TRUE,
             ggtheme=theme_minimal()
)