import string
from tokenize import String


##======= LEXICAL ANALYZER ======##

print(" ")
print("=========Program Lexical Analizer Bahasa Portugis===========")
print(" ")
print("subjek   : - ela")
print("           - ele")
print(" ")
print("Predikat : - vejo")
print("           - comer")
print("           - beber")
print("           - trazer")
print(" ")
print("Objek    : - mar")
print("           - pao")
print("           - suco")
print("           - livro")
print(" ")
kalimat = input('Masukkan Kalimat : ')
inputString = kalimat.lower()+'#'

# inisialisasi
listAbjad = string.ascii_lowercase
listState = [
    'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 
    'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
    'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 
    'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28'
]

tabelTransisi = {}

for state in listState:
    for huruf in listAbjad:
        tabelTransisi[(state, huruf)] = 'error'
    tabelTransisi[(state, '#')] = 'error'
    tabelTransisi[(state, ' ')] = 'error'

# Tabel transisi untuk q0 jika menerima spasi
tabelTransisi['q0', ' '] = 'q0'

# update tabel transisi untuk token : Ela
tabelTransisi[('q0', 'e')] = 'q1'
tabelTransisi[('q1', 'l')] = 'q2'
tabelTransisi[('q2', 'a')] = 'q3'
tabelTransisi[('q3', ' ')] = 'q5'
tabelTransisi[('q3', '#')] = 'accept'

tabelTransisi[('q5', ' ')] = 'q5'
tabelTransisi[('q5', '#')] = 'accept'

# update tabel transisi untuk token : Ele
tabelTransisi[('q2', 'e')] = 'q4'
tabelTransisi[('q4', ' ')] = 'q5'
tabelTransisi[('q4', '#')] = 'accept'

# update tabel transisi untuk token : Vejo
tabelTransisi[('q0', 'v')] = 'q6'
tabelTransisi[('q6', 'e')] = 'q7'
tabelTransisi[('q7', 'j')] = 'q8'
tabelTransisi[('q8', 'o')] = 'q9'
tabelTransisi[('q9', ' ')] = 'q5'
tabelTransisi[('q9', '#')] = 'accept'

# update tabel transisi untuk token : Trazer
tabelTransisi[('q0', 't')] = 'q10'
tabelTransisi[('q10', 'r')] = 'q11'
tabelTransisi[('q11', 'a')] = 'q12'
tabelTransisi[('q12', 'z')] = 'q13'
tabelTransisi[('q13', 'e')] = 'q14'
tabelTransisi[('q14', 'r')] = 'q15'
tabelTransisi[('q15', ' ')] = 'q5'
tabelTransisi[('q15', '#')] = 'accept'

# update tabel transisi untuk token : Comer
tabelTransisi[('q0', 'c')] = 'q16'
tabelTransisi[('q16', 'o')] = 'q17'
tabelTransisi[('q17', 'm')] = 'q13'

# update tabel transisi untuk token : Beber
tabelTransisi[('q0', 'b')] = 'q18'
tabelTransisi[('q18', 'e')] = 'q19'
tabelTransisi[('q19', 'b')] = 'q13'

# update tabel transisi untuk token : Mar
tabelTransisi[('q0', 'm')] = 'q20'
tabelTransisi[('q20', 'a')] = 'q14'

# update tabel transisi untuk token : Pao
tabelTransisi[('q0', 'p')] = 'q21'
tabelTransisi[('q21', 'a')] = 'q22'
tabelTransisi[('q22', 'o')] = 'q23'
tabelTransisi[('q23', ' ')] = 'q5'
tabelTransisi[('q23', '#')] = 'accept'

# update tabel transisi untuk token : Suco
tabelTransisi[('q0', 's')] = 'q24'
tabelTransisi[('q24', 'u')] = 'q25'
tabelTransisi[('q25', 'c')] = 'q22'

# update tabel transisi untuk token : Livro
tabelTransisi[('q0', 'l')] = 'q26'
tabelTransisi[('q26', 'i')] = 'q27'
tabelTransisi[('q27', 'v')] = 'q28'
tabelTransisi[('q28', 'r')] = 'q22'

# tabel transisi untuk token baru/token selanjutnya
tabelTransisi[('q5', 'e')] = 'q1'
tabelTransisi[('q5', 'v')] = 'q6'
tabelTransisi[('q5', 't')] = 'q10'
tabelTransisi[('q5', 'c')] = 'q16'
tabelTransisi[('q5', 'b')] = 'q18'
tabelTransisi[('q5', 'm')] = 'q20'
tabelTransisi[('q5', 'p')] = 'q21'
tabelTransisi[('q5', 's')] = 'q24'
tabelTransisi[('q5', 'l')] = 'q26'

# Lexical Analysis
idChar = 0
idToken = 0
state = 'q0'
currentToken = ''
while state != 'accept':
    currentChar = inputString[idChar]
    currentToken += currentChar
    state = tabelTransisi[(state, currentChar)]
    if(state == 'q3') or (state == 'q4') or (state == 'q9') or (state == 'q15') or (state == 'q23'):
        idToken += 1
        print(f"Token {idToken}, {currentToken} : VALID")
        currentToken = ''
    if state == 'error':
        idToken += 1
        print(f"Token {idToken} : INVALID")
        break
    idChar += 1

# Kesimpulan Lexical Analysis
if state == 'accept':
    print(f"Semua Token di input : {kalimat} : VALID")
else:
    print(f"Token di input : {kalimat} : INVALID")

#===================================================================================================================================

##====== PARSER ======##

print()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("===========================================================")
print()
tokens = kalimat.lower().split()
tokens.append('EOS')

# Pendefinisian Symbol
nonTerminal = ['S', 'NN', 'VB']
terminal = ['ela', 'ele', 'vejo', 'comer', 'beber', 
            'trazer', 'mar', 'pao', 'suco', 'livro'
    ]

# Pendefisinisian Parse Table
tabelParser = {}

tabelParser[('S', 'ela')] = ['NN', 'VB', 'NN']
tabelParser[('S', 'ele')] = ['NN', 'VB', 'NN']
tabelParser[('S', 'mar')] = ['NN', 'VB', 'NN']
tabelParser[('S', 'pao')] = ['NN', 'VB', 'NN']
tabelParser[('S', 'suco')] = ['NN', 'VB', 'NN']
tabelParser[('S', 'livro')] = ['NN', 'VB', 'NN']
tabelParser[('S', 'vejo')] = ['error']
tabelParser[('S', 'comer')] = ['error']
tabelParser[('S', 'beber')] = ['error']
tabelParser[('S', 'trazer')] = ['error']
tabelParser[('S', 'EOS')] = ['error']

tabelParser[('NN', 'ela')] = ['ela']
tabelParser[('NN', 'ele')] = ['ele']
tabelParser[('NN', 'mar')] = ['mar']
tabelParser[('NN', 'pao')] = ['pao']
tabelParser[('NN', 'suco')] = ['suco']
tabelParser[('NN', 'livro')] = ['livro']
tabelParser[('NN', 'vejo')] = ['error']
tabelParser[('NN', 'comer')] = ['error']
tabelParser[('NN', 'beber')] = ['error']
tabelParser[('NN', 'trazer')] = ['error']
tabelParser[('NN', 'EOS')] = ['error']

tabelParser[('VB', 'ela')] = ['error']
tabelParser[('VB', 'ele')] = ['error']
tabelParser[('VB', 'mar')] = ['error']
tabelParser[('VB', 'pao')] = ['error']
tabelParser[('VB', 'suco')] = ['error']
tabelParser[('VB', 'livro')] = ['error']
tabelParser[('VB', 'vejo')] = ['vejo']
tabelParser[('VB', 'comer')] = ['comer']
tabelParser[('VB', 'beber')] = ['beber']
tabelParser[('VB', 'trazer')] = ['trazer']
tabelParser[('VB', 'EOS')] = ['error']

# inisialisasi stack
stack = []
stack.append('#')
stack.append('S')

# membaca input inisialisasi
idToken = 0
symbol = tokens[idToken]


# Pengecekan apakah kalimat valid di Lexical analyzer
if state == 'accept':
    # Proses Parsing
    while len(stack) > 0:
            top = stack[len(stack)-1]
            print('top = ', top)
            print('symbol = ', symbol)
            if top in terminal:
                    print(top, 'merupakan simbol terminal')
                    if top == symbol:
                            stack.pop()
                            idToken += 1
                            symbol = tokens[idToken]
                            if symbol == 'EOS':
                                    print('isi stack: ', stack)
                                    stack.pop()
                    else:
                            print('ERROR')
                            break
            elif top in nonTerminal:
                    print(top, 'merupakan non-terminal')
                    if tabelParser[(top, symbol)][0] != 'error':
                            stack.pop()
                            pushSymbol = tabelParser[(top, symbol)]
                            for i in range(len(pushSymbol)-1, -1, -1):
                                    stack.append(pushSymbol[i])
                    else:
                            print('ERROR')
                            break
            else:
                    print('ERROR')
                    break
            print('isi stack: ', stack, '\n')

    # conclusion
    if symbol == 'EOS' and len(stack) == 0:
            print(f'Input : {kalimat.title()} --> DITERIMA Karena Sesuai Grammar')
    else:
            print(f'\nInput : {kalimat.title()} --> DITOLAK Karena Tidak Sesuai Grammar')

else:
    print(f'\nInput : {kalimat.title()} --> DITOLAK Karena Pilihan Kata Tidak Sesuai')