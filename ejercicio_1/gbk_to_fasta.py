"""
Escribir un script que lea una o más secuencias (de nucleótidos) de un archivo que contenga la información 
en formato GenBank de un mRNA de su gen (o genes) de interés, las traduzca a sus secuencias de aminoácidos posibles 
(tener en cuenta los Reading Frames) y escriba los resultados en un archivo en formato FASTA

https://biopython.org/wiki/Converting_sequence_files
"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

RNA = "NM_000463"


def translate_reading_frames(sequence):
    reading_frames = []
    # Reading Frames (+1, +2 y +3)
    for i in range(3):
        frame_sequence = sequence[i:]
        if len(frame_sequence) % 3 != 0:
            # Se descartan los nucleotidos sobrantes
            frame_sequence = frame_sequence[:-(len(frame_sequence) % 3)]
        aminoacid_sequence = frame_sequence.translate(to_stop=True)
        reading_frames.append(aminoacid_sequence)
    # Reading Frames complementarios (-1, -2 y -3)
    for i in range(3):
        frame_sequence = sequence.reverse_complement()[i:]
        if len(frame_sequence) % 3 != 0:
            frame_sequence = frame_sequence[:-(len(frame_sequence) % 3)]
        aminoacid_sequence = frame_sequence.translate(to_stop=True)
        reading_frames.append(aminoacid_sequence)
    return reading_frames




# Abrir el archivo GenBank y leer la secuencia de nucleotidos
filename = RNA + ".gb"
with open(filename, "r") as handle:
    record = SeqIO.read(handle, "genbank")
    nucleotide_seq = record.seq

"""
Las características (features) en un archivo GenBank describen diferentes elementos de la secuencia, como genes, exones, intrones, regiones promotoras, etc.
En el formato GenBank, las secuencias de ADN o ARN que codifican proteínas suelen estar etiquetadas como features de tipo "CDS". 
El atributo strand '-1' indica que la secuencia de nucleótidos se encuentra en la cadena complementaria o inversa.
"""
# Identificar las secuencias de nucleotidos correspondientes a los genes
gene_seqs = []
for feature in record.features:
    if feature.type == "CDS":
        gene_seq = feature.extract(nucleotide_seq)
        if feature.strand == -1:
            gene_seq = gene_seq.reverse_complement()
        gene_seqs.append(gene_seq)

print("Secuencia de nucleotidos:")
for seq in gene_seqs :
  print(seq)

# Traducir cada secuencia de nucleotidos a su secuencia de aminoacidos correspondiente
aminoacid_seqs = []
for gene_seq in gene_seqs:
    reading_frames = translate_reading_frames(gene_seq)
    aminoacid_seqs.extend(reading_frames)

print("\nSecuencia de aminoacidos:")
for seq in aminoacid_seqs :
  print("> " + seq)

# Escribir los resultados en un archivo en formato FASTA
output_filename = RNA + ".fasta"
output_records = []
for i, aminoacid_seq in enumerate(aminoacid_seqs):
    output_record = SeqRecord(Seq(str(aminoacid_seq)), id="{}_{}".format(record.id, i+1), description="")
    output_records.append(output_record)

with open(output_filename, "w") as output_handle:
    SeqIO.write(output_records, output_handle, "fasta")
