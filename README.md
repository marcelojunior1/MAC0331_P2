## Detectar interseção de segmentos

O segundo projeto detecta a intecessão de quaisquer dois segmentos em uma lista fornecida como entrada. Conforme o enunciado, o algoritmo de Shamos e Hoey foi implementado.

A resolução do problema utiliza uma linha de varredura que trata os pontos dos segmentos como eventos. O ponto de menor coordenada X é um *ponto de início* do segmento, enquanto o seu semelhante é o *ponto final*. Quando a linha de varredura intercepta um *ponto de início* ou um *ponto final*, respectivamente, o segmento é inserido ou removido em uma árvore de busca e em ambos os casos é feito um teste de interseção entre o segmento e seus dois vizinhos mais próximos. Apesar do enunciado solicitar uma árvore de busca binária simples, foi utilizado uma árvore de busca binária balanceada rubro negra com suas devidas adaptações.

A orientação ao percorrer a árvore não é definida do modo usual, ou seja, se a *chave* é maior ou menor que outro elemento, e sim, se o segmento está a esquerda ou não de outro. Ao mudar o modo de orientação na árvore, também é necessário garantir a consistência nos resultados, cuja tarefa é exercida pela função *Esquerda*(A,B). O segmento **B** está a esquerda de **A** se o determinate, cuja matriz é a junção das coordenadas de **A** com o ponto de início de **B** e o vetor coluna [1,1,1], é menor do que zero. Essa definição pode funcionar para casos gerais, porém falha em outros três, que são:

> O segmento **B** tem as pontas de cada lado em relação à **A**: Esse pode ser um problema, pois a árvore de busca mantem a ordem do conjunto que ela ordena, porém pode inverter a ordem em que eles foram inseridos, por isso, ao percorrer a árvore, os resultados de *Esquerda*(A,B) na inserção e *Esquerda*(B,A) na remoção podem ser os mesmos, o que faz que a busca de um elemento seja incorreta. A solução aplicada foi inverter a ordem dos segmentos ao detectar que **A** está mais a direta em X do que **B**.

>O ponto de início de **B** é colinear à **A**: Se um ponto de início pertence à reta de **A**, basta realizar o teste *Esquerda* em relação ao ponto final de **B**.

>Os dois pontos de **B** são colineares à **A**: Aqui o teste define quem está a esquerda pela coordenada X de seus pontos iniciais, em caso de empate, a posição em *l* torna-se o critério de desempate.

A linha de varredura é simulada percorrendo a fila de eventos e executando as operações já descritas, a cada operação a parte gráfica é acionada, seja alterando a posição da linha de varredura, ou mostrando os testes de interseção que são realizados. Ao final, os dois segmentos que se intersessionam aparecem marcados.

Os testes realizados foram feitos com os arquivos fornecidos na pasta *dados* e com segmentos aleatórios, sempre comparados ao algoritmo de força bruta, também fornecido no *front end*. O único caso que não foi tratado foi quando o segmento tem seus pontos coincidentes (*Ponto de início* = *Ponto final*), apesar do algoritmo não quebrar, também não retorna o resultado correto, sendo esse um caso degenerado.
