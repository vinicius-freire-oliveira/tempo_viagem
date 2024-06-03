# Solicita ao usuário a distância em quilômetros e a velocidade média em quilômetros por hora
distancia = float(input("Digite a distância em km: "))
velocidade_media = float(input("Digite a velocidade média em km/h: "))

# Calcula o tempo estimado em horas para percorrer a distância com a velocidade média fornecida
tempo = distancia / velocidade_media

# Imprime o tempo estimado em horas
print("O tempo estimado é de %.2f horas" % tempo)

# Converte o tempo estimado de horas para segundos para facilitar a manipulação
tempo_s = int(tempo * 3600)  # convertemos de horas para segundos

# Calcula o número de horas (parte inteira)
horas = int(tempo_s / 3600)

# Calcula o resto em segundos após a conversão das horas
tempo_s = int(tempo_s % 3600)

# Calcula o número de minutos
minutos = int(tempo_s / 60)

# Calcula o número de segundos
segundos = int(tempo_s % 60)

# Imprime o tempo estimado no formato HH:MM:SS
print("%02d:%02d:%02d" % (horas, minutos, segundos))


