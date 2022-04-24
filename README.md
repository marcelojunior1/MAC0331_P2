# Segundo Projeto: Detectar interseção de segmentos

O segundo projeto detecta a intecessão de quaisquer dois segmentos em uma lista fornecida como entrada, conforme o enunciado, o algoritmo de Shamos e Hoey foi implementado.

A resolução do problema utiliza uma linha de varredura que trata os pontos dos segmentos como eventos. O ponto de menor coordenada X é um *ponto de inicio* do segmento, enquanto o seu semelhante é o *ponto final*. Quando a linha de varredura intercepta um *ponto de inicio* ou um *ponto final*, respectivamente, o segmento é inserido ou removido em uma árvore de busca e em ambos os casos é feito um teste de intercessão entre o segmento e seus dois vizinhos próximos. Apesar do enunciado solicitar um árvore de busca binária simples, foi utilizado um árvore de busca binária balanceada rubro negra com suas devidas adaptações.

A orientação ao percorrer a árvore não é definida do modo usual, ou seja, se a *chave* é maior ou menor que outro elemento, e sim, se o segmento está a esquerda ou não de outro. Ao mudar o modo de orientação na árvore, também é necessário garantir a consistência nos resultados, cuja tarefa é exercida pela função *Esquerda*(A,B). O segmento **B** está a esquerda de **A** se o determinate, cuja a matriz é a junção das coordenadas de **A** com o ponto de inicio de **B**, é maior do que zero. Essa definição pode funcionar para casos gerais, porém falha em outros, que são:

> O segmento **B** tem as pontas de cada lado em relação à **A**: Esse pode ser um problema, pois a árvore de busca mantem a ordem do conjunto que ela ordena, porém pode inverter a ordem em que eles foram inseridos, por isso, o resultado de *Esquerda*(A,B) e *Esquerda*(B,A) podem ser os mesmos, o que faz com que algum segmento não seja encontrado apartir 
