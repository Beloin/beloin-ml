# Hyperparameter Tuning

É o caso de mudar os valores do hiper para metros de um Modelo de Machine Learning.

Quando estamos treinando um modelo (principalmente de RNA) precisamos prestar atenção nos erros. como <i MSE />.

- Learning Rate:
    Valor para se alterar como se fossem os passos de cada epoch. O valor que o gradiente vai multipliar a cada iteração para modificar os pesos.

- Epochs:
    Quantidades de interações que seu algortimo efetuará sobre os dados.

- Batch Size:
    Quantidade de itens do `batch`, que são os "blocos" de dados. Os pesos e <i bias/> serão alterados a cada iteração de um batch.

OBS: Caso haja 100 dados, com batch de 10, cada Epochs terá 10 iterações (100 % 10 = 10).
