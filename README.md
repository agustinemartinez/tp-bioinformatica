# TP Bioinformática

El presente trabajo práctico tiene por objetivo adquirir las primeras habilidades en el campo de la
Bioinformática. Se incluyen cuatro ejercicios donde deberán desarrollar pequeños scripts para
resolver problemas específicos. Los mismos pueden ser desarrollados utilizando cualquiera de los
lenguajes de programación bioinformática de código abierto como BioPerl, BioJava y BioRuby, que
son ampliamente utilizados en la investigación bioinformática y de biología computacional,
aunque se sugiere la utilización de BioPerl para facilitar la resolución de los ejercicios. Las
herramientas computacionales escritas en estos lenguajes proporcionan múltiples funcionalidades
para crear soluciones personalizadas y realizar análisis de datos biológicos. Un quinto ejercicio esta
relacionado con la comprensión de la información en bases de datos de biología molecular.

## Ejercicio 1 – Procesamiento de secuencias 
Escribir un script que lea una o más secuencias (de
nucleótidos) de un archivo que contenga la información en formato GenBank de un mRNA de su gen (o
genes) de interés, las traduzca a sus secuencias de amino ácidos posibles (tener en cuenta los Reading
Frames) y escriba los resultados en un archivo en formato FASTA. Ustedes deben generarse su archivo
GenBank de secuencias input, por ejemplo realizando una consulta de los mRNA del gen INS (que está
asociado a la Diabetes) en la base de datos de NCBI-Gene y obtener uno o más resultados en formato
GenBank en un archivo de texto. Si no desean seguir trabajando con las seis secuencias de aa posibles,
pueden utilizar alguna función o programa que les permita saber cual el es marco de lectura correcto y
seguir con esa secuencia.

* Input: Archivo de secuencias Genbank (ej. NMxxxx.gbk con una o más secuencias).
* Output: Archivo de secuencias Fasta de cada ORF (ej. Xxxxx.fas con una o más secuencias de
aminoácidos).

## Ejercicio 2 - BLAST
Escribir un script que realice un BLAST de una o varias secuencias (si son varias se
realiza un Blast por cada secuencia input) y escriba el resultado (blast output) en un archivo. Nota: Pueden
ejecutar BLAST de manera remota o bien localmente (si hacen ambos tienen más puntos!), para esto deben
instalarse BLAST localmente del FTP del NCBI, luego bajarse la base de datos

ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/swissprot.gz y descomprimirla en un dir por ej. ncbi-blast-
2.3.0+/data/, luego usar el comando ncbi-blast-2.3.0+/bin/makeblastdb sobre el archivo swissprot (el
original ya está en formato FASTA) para darle formato de BLAST DB. Dependiendo de la versión de Blast
suite que tengan instalado puede que en vez de makeblastdb deban utilizar el comando formatdb.

* Input: Secuencia Fasta (ej. Xxxx.fas con una o más secuencias de aminoácidos obtenidas en Ej.1).
* Output: Reporte Blast (ej. blast.out, si deciden hacer múltiples pueden generar un único o varios
archivos).

## Ejercicio 3 – Multiple Sequence Alignment (MSA)
Descargar las secuencias (en formato fasta) de 3 o más
organismos distintos pertenecientes a otras especies que hayan salido en los resultados del Blast y realizar
un alineamiento múltiple con tu secuencia de consulta más estas otras encontradas. Si no pueden hacerlo
localmente pueden utilizar algún programa de MSA online. Intenten realizar una interpretación del
resultado del alineamiento múltiple. Entregar información del MSA.


## Ejercicio 4 – BLAST OUTPUT 
Escribir un script para analizar (parsear) un reporte de salida de blast que
identifique los hits que en su descripción aparezca un Pattern determinado que le damos como parámetro
de entrada. El pattern puede ser una palabra. Punto extra: pueden a su vez parsear cuál es el ACCESSION
del hit identificado (donde hay una coincidencia del Pattern) y con el módulo Bio::DB::GenBank obtener la
secuencia completa del hit en formato FASTA y escribirla a un archivo, es decir, levantar las secuencias
originales completas de los hits seleccionados.

* Input: Reporte Blast (blast.out del ej. 2) y un Pattern (por ej. “Mus Musculus”).
* Output: Lista de los hits que coincidan con el pattern (por ej. solo los hits de Ratones).

## Ejercicio 5 - EMBOSS
Instalar EMBOSS. Escribir un script que llame a algún programa EMBOSS para que
realice algún análisis sobre la una secuencia de nucleótidos fasta (del Ej. 1).
Por ejemplo, pueden correr un programa que calcule los ORFs y obtenga las secuencias de proteínas
posibles. Luego bájense la bases de datos PROSITE (archivo prosite.dat) de dominios/motivos funcionales
conocidos, por medio del llamado a otro programa EMBOSS realizar el análisis de dominios de las
secuencias de aminoácidos obtenidas y escribir los resultados en un archivo de salida.

* Input : Archivo de secuencias Fasta (por ej. Xxxxx.fas con una o más secuencias de aa).
* Output: Archivo de resultados del dominios funcionales encontrados en las secuencias de aa.
