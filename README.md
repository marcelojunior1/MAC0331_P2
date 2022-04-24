# Segundo Projeto: Detectar interseção de segmentos

O segundo projeto detecta a intecessão de quaisquer dois segmentos em uma lista fornecida como entrada, conforme o enunciado, o algoritmo de Shamos e Hoey foi implementado.

A resolução do problema utiliza uma linha de varredura que trata os pontos dos segmentos como eventos. O ponto de menor coordenada X é um *ponto de inicio* do segmento, enquanto o seu semelhante é o *ponto final*. Quando a linha de varredura intercepta um *ponto de inicio* ou um *ponto final*, respectivamente, o segmento é inserido ou removido em uma árvore de busca e em ambos os casos é feito um teste de intercessão entre o segmento e seus vizinhos próximos. Apesar do enunciado solicitar um árvore de busca binária simples, foi utilizado um árvore de busca binária balanceada rubro negra com suas devidas adaptações.

