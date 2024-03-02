#### Quiz

ask1 = "5 + 3 = "                #PRIMEIRA PERGUNTA
ques1 = "8"               #PRIMEIRA RESPOSTA

ask2 = "12 + 12 = "                #SEGUNDA PERGUNTA
ques2 = "24"               #SEGUNDA RESPOSTA

ask3 = "5 + 5 = "                #TERCEIRA PERGUNTA
ques3 = "10"               #TERCEIRA RESPOSTA

ask4 = "55 + 55 = "                #QUARTA PERGUNTA
ques4 = "110"               #QUARTA RESPOSTA

maxpo = 0
points = 0


maxpo += 1
answer = ""
answer = input(f"{ask1}")
print("\n")

if answer.lower() == ques1.lower():
    print(f"Você acertou, a resposta era \"{ques1}\"")
    print("\n")
    points += 1
else:
    answer = input("Resposta errada. ")
    print("\n")
  
maxpo += 1  
answer = ""
answer = input(f"{ask2}")
print("\n")

if answer.lower() == ques2.lower():
    print(f"Você acertou, a resposta era \"{ques2}\"")
    print("\n")
    points += 1
else:
    answer = input("Resposta errada. ")
    print("\n")


maxpo += 1
answer = ""
answer = input(f"{ask3}")
print("\n")

if answer.lower() == ques3.lower():
    print(f"Você acertou, a resposta era \"{ques3}\"")
    print("\n")
    points += 1
else:
    answer = input("Resposta errada. ")
    print("\n")

maxpo += 1
answer = ""
answer = input(f"{ask4}")
print("\n")

if answer.lower() == ques4.lower():
    print(f"Você acertou, a resposta era \"{ques4}\"")
    print("\n")
    points += 1
else:
    answer = input("Resposta errada. ")
    print("\n")
    
percentpo = (points / maxpo) * 100

if points == maxpo:
    print(f"Parabéns, você acertou todas as perguntas ({maxpo}/{maxpo})! {percentpo}%! ")
elif points != maxpo:
    print(f"Você fez {points} pontos! O maximo de pontos era {maxpo} pontos! ")
    print(f"Você acertou {percentpo}%! ")

dontleavemenow = input("")