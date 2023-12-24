"""
Escribir un script para analizar (parsear) un reporte de salida de blast que identifique los hits 
que en su descripción aparezca un Pattern determinado que le damos como parámetro de entrada. 
El pattern puede ser una palabra.

https://biopython.org/docs/1.76/api/Bio.Blast.html

Nota: el archivo blast.out debe estar en formato XML
"""

from Bio.Blast import NCBIXML
import sys

def search_pattern_blast(pattern, blast_outfile):
    # Leer el archivo de salida de BLAST
    with open(blast_outfile, 'r') as f:
        blast_records = NCBIXML.parse(f)

        # Recorrer los resultados de BLAST
        for record in blast_records:
            for alignment in record.alignments:
                for hsp in alignment.hsps:
                    # Verificar si el patrón está presente en la descripción del hit
                    if pattern in alignment.title:
                        # Imprimir información del hit
                        print("Hit ID:", alignment.hit_id)
                        print("Descripción:", alignment.title)
                        print("Secuencia:", alignment.hit_def)
                        print("Score:", hsp.score)
                        print("E-value:", hsp.expect)
                        print("")

# Obtener el patrón de búsqueda como argumento de línea de comandos
if len(sys.argv) < 3:
    print("Usage: python blast_analysis.py [blast.out] [pattern]")
    sys.exit(1)

blast_outfile = sys.argv[1]
search_pattern = sys.argv[2]

# Llamar a la función para buscar el patrón en el archivo de salida de BLAST
search_pattern_blast(search_pattern, blast_outfile)
