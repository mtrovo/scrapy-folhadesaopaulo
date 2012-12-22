scrapy-folhadesaopaulo
======================

Projeto de exemplo em scrapy para leitura dos artigos publicados no site do
jornal da Folha de São Paulo para estudos referentes a NLP.

Ambiente
========

Para usar o projeto você precisa do scrapy instalado, para isso basta seguir as
instruções em http://doc.scrapy.org/en/latest/intro/install.html.

Se você possui easy_install ou pip é tão simples quanto rodar:

        easy_install Scrapy

ou para no pip

        pip install Scrapy

Executando
==========

Com o scrapy instalado basta entrar na pasta do projeto e rodar o comando:

        scrapy crawl -o out.json folha


Com esse comando será gerado um arquivo out.json,cada linha desse arquivo correspondendo
a um objeto JSON referente a um artigo do site. O objeto JSON contém os campos:
* url: url do artigo;
* nome: título do artigo;
* conteudo: conteúdo do artigo (só texto, sem links ou formatação HMTL).

Abaixo uma linha de exemplo da saída:

``` json
{"url": "http://www1.folha.uol.com.br/folha/informatica/ult124u558717.shtml", "conteudo": "\nA Apple est\u00e1 \u00e0 procura de novos empregados da ind\u00fastria de semicondutores, e tamb\u00e9m est\u00e1 desenvolvendo a sua capacidade de desenvolver chips pr\u00f3prios. As informa\u00e7\u00f5es est\u00e3o na edi\u00e7\u00e3o de quarta-feira (29) do di\u00e1rio econ\u00f4mico \"Wall Street Journal\".\n\nA fabricante do iPhone e do iPod espera que seus esfor\u00e7os fa\u00e7am com que se desenvolvam novas funcionalidades para os seus dispositivos, e que habilite a empresa a manter mais segredo, em rela\u00e7\u00e3o aos vendedores de chips, sobre os detalhes tecnol\u00f3gicos dos seus equipamentos.\n\nUm porta-voz da Apple confirmou que a companhia contratou Bob Drebin, executivo de produtos gr\u00e1ficos da fabricante de chips Advanced Micro Devices, e Raja Koduri, que ocupou a mesma posi\u00e7\u00e3o antes de Drebin.\n\nNo entanto, o porta-voz n\u00e3o deu mais detalhes sobre o assunto. A p\u00e1gina de Drebin em uma rede social o indica como diretor-s\u00eanior da Apple.\n\nA Apple tem contratado engenheiros, a fim de criar chips multifuncionais para que sejam usados em seus telefones, diz o \"WSJ\". A tecnologia dos chips estaria dispon\u00edvel j\u00e1 no come\u00e7o do ano que vem.\n\ncom ag\u00eancia Reuters\n", "nome": "Apple quer desenvolver chips pr\u00f3prios, diz jornal"}
```

Por padrão o projeto está feito para ler somente artigos do caderno de mercado
mas pode ser modificado facilmente para monitorar artigos de todo o site alterando
o arquivo folha.py.

Estatísticas
============

Com base no conteúdo mineirado pelo scrapy foi feita uma análise com as palavras
mais utilizadas nos artigos.

Utilizando o script extract_content.py extrai o conteúdo dos artigos salvos e em seguida
o comando tr do Linux é utilizado para contar a frequência das palavras utilizadas
nos arquivos. O comando utilizado é o seguinte:

        python extract_content.py < out.json | tr -sc 'a-zA-ZÁáÉéÍíÓóÚúÂâÊêÔô\-çÃãÕõÀà' '\n' | sort | uniq -c | sort -n -r | less

o comando irá gerar uma saída parecida com o abaixo (gerado a partir de um out.json com 9MB):

          68187 de
          45922 a
          38174 o
          24206 que
          24052 do
          23747 e
          20923 em
          20508 da
          16735 para
          14232 no
          11544 com
          10505 os
           9346 na
           8178 um
           8004 as
           6884 é
           6719 uma
           6476 dos
           6118 não
           5819 por
           5034 mais
           4785 ano
           4709 r
           4695 ao
           4425 das
           4038 se
           3718 segundo
           3676 bilhões
           3521 foi
           3273 como
           3058 à
           3040 us
           2982 pelo
           2896 milhões
           2883 pela
           2852 nos
           2644 já
           2549 empresa
           2490 mercado
           2467 são
           2448 entre
           2409 mas
           2385 brasil
           2373 governo
           2335 sobre
           2324 disse
           2301 também
           2296 nesta
           2205 até
           2197 está
