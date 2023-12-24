import subprocess

# Comando para ejecutar el BLAST
blast_cmd "-query .\NM_000463.fasta -db .\swissprot -out blast.out"
subprocess.run(blast_cmd, shell=True)