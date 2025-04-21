# Kullanılacak semboller
symbols = ['@', ':', ';', '|', '#', '%', '!', '*']

# Giriş ve çıkış dosyalarının isimleri
input_file = 'combo.txt'
output_file = 'filtered.txt'

# Dosyaları oku ve filtrele
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        line = line.strip()
        if ':' in line:
            email, password = line.split(':', 1)
            if any(symbol in password for symbol in symbols):
                outfile.write(line + '\n')