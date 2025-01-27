def display(tauarlar):
    for id, data in tauarlar.items():
        print(f"{id} | {data["name"]} | бағасы: {data["bagasy"]}теңгеден | {data["zapas"]} {data["olshemi"]} бар")

def cart(tauarlar):
    korzina = []
    korzina_sany = []
    stock_dec_dynamics = {1:[tauarlar[1]["zapas"]],2:[tauarlar[2]["zapas"]],3:[tauarlar[3]["zapas"]]}
    total_sum = 0
    while True:
        id = int(input("Алғыңыз келген тауардың айдиін енгізіңіз: "))
        if id == 0:
            for x in range(len(korzina)):
                print(f"{tauarlar[korzina[x]]["name"]} {tauarlar[korzina[x]]["bagasy"]}тг * {korzina_sany[x]} {tauarlar[korzina[x]]["olshemi"]}")
            print(f"Итого: {total_sum}")
        else:
            korzina.append(id)
            quantity = int(input(f"Қанша {tauarlar[id]["olshemi"]} алғыңыз келеді: "))
            tauarlar[id]["zapas"]-=quantity
            stock_dec_dynamics
            korzina_sany.append(quantity)
            baga = tauarlar[id]["bagasy"]
            summa = baga * quantity
            total_sum = total_sum + summa
            print(total_sum)
            print(korzina)
            print(korzina_sany)
            display(tauarlar)
