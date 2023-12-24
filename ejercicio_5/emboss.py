
import subprocess

fasta_file = 'NM_000463.fasta'
output_file = 'resultados.txt'
prosite_dir = 'prosite'
prosite_file = 'prosite/prosite.dat'

# Set the EMBOSS_DATA environment variable
emboss_data_path = "/usr/share/EMBOSS/data/"
command = f'export EMBOSS_DATA="{emboss_data_path}"'
subprocess.run(command, shell=True)

# Run prosextract: Extracts PROSITE motif data from prosite.dat and creates database files
prosextract_command = f"sudo prosextract -prositedir {prosite_dir}"
subprocess.run(prosextract_command, shell=True)

# Run patmatmotifs: Scans a protein sequence with motifs from the PROSITE database
patmatmotifs_command = f"patmatmotifs -sequence {fasta_file} -outfile {output_file} -sformat1 fasta -sdbname1 prosite -sid1 {prosite_file}"
subprocess.run(patmatmotifs_command, shell=True)

