from operator import truediv
import os 
import time
while True:
    login= input("Deseja fazer login? ou cadastrar?")
    if not "login" in login and not "Login" in login and not "cadastrar" in login:
        continue
    break
if login == "login":
    with open("login.txt","r") as logando:
        ler = [tr[0:-1]for tr in logando.readlines()]
        dicio={}
        for k,_ in enumerate(ler):
            ls=ler[k].split("//")
            dicio[ls[0]]=ls[1:]
        os.system("clear")
        username = input("Digite seu nome de login: ")
        for k,v in dicio.items():
            while True:
                if username  == k:
                    print(k)
                    print(v)
                    while True:
                        os.system("clear")
                        passw=input("Sua senha: ")
                        if passw == v[0]:
                            print("Login feito com sucesso")
                            escolha=1
                            break
                        else:
                            print("senha errada")
                        continue 
                    break
                else:
                    break
    logando.close
else:
    with open("login.txt","r+") as logando:
        ler = [tr[0:]for tr in logando.readlines()]
        dicio={}
        for k,_ in enumerate(ler):
            ls=ler[k].split("//")
            dicio[ls[0]]=ls[1:]
        username = input("Digite seu nome de login: ")
        for k,v in dicio.items():
            if username != k:
                passw = input("Digite sua senha: ")
                logando.write(f"\n{username}//{passw}\n")
            else:
                print("ja existe este nome de usuario, tente outro")
    logando.close
if escolha==1:
    while True:
        acao=input("Deseja continuar de onde parou? 1-Sim ou 2-Nao: ")
        if not "1" in acao and not "2" in acao:
            continue
        break
    if acao == "1":
        jogo=1
    else:
        itens={
            "maca":("alimento","1"),
            "wood espada":("body arma","4")
        }
        with open("bagrpg.txt", "w") as bag:
            for k,v in itens.items():
                bag.write(k)
                bag.write("//")
                bag.write(v[0])
                bag.write(" : ")
                bag.write(v[1])
                bag.write("\n")
        bag.close
        jogo=1
while jogo==1:
    os.system("clear")
    with open("bagrpg.txt", "r+") as bag:
        ler = [tr[0:-1]for tr in bag.readlines()]
        dicio={}
        for k,_ in enumerate(ler):
            ls=ler[k].split("//")
            dicio[ls[0]]=ls[1:]
        print("Esta aqui e sua mochila com seus items: ")
        for k,v in dicio.items():
            print(k)
            print(v)
        bag.close
        time.sleep(1)
        os.system("clear")
        while True:
            atitu = input("O que deseja fazer?\n1-dropar um item\n2-adicionar um item\n3-editar um item\n4-visualizar o que ha a na mochila\n5-pesquisar o valor de um item\n6-sair: ")
            if not "1" in atitu and not "2" in atitu and not "3" in atitu and not "4" in atitu and not "5" in atitu and not "6" in atitu:
                continue
            break
        while True:
            if atitu == "1":
                os.system("clear")
                for k,v in dicio.items():
                    print(k)
                    print(v)
                ativ=input("Qual item deseja dropar?")
                with open("bagrpg.txt", "a+") as bag:
                    for k,v in dicio.items():
                        if ativ == k:
                            del dicio[k]
                            del v[0]
                            print(dicio)
                            bag.write(f"{dicio}")
                        else:
                            continue
                        break
                bag.close
            elif atitu =="2":
                os.system("clear")
                item=input("Qual item deseja adicionar? ")
                classe=input("Classe do item: ")
                quant=input("Quantidade: ")
                with open("bagrpg.txt", "a") as bag:
                    bag.write(f"{item}//{classe} : {quant}")
                bag.close
            elif atitu == "3":
                os.system("clear")
                with open("bagrpg.txt", "a") as bag:
                    for k,v in dicio.items():
                        print(k)
                        print(v)
                    edit=input("Qual item deseja editar? ")
                    for k,v in dicio.items():
                        item=k
                        if edit == k:
                            del dicio[k]
                            del v[0]
                            classe=input("Classe do item: ")
                            quant=input("Quantidade: ")
                            v=(f"{classe} : {quant}")
                            bag.write(f"\n{item}//{v}")
                            bag.close
                            break
                        else:
                            break
            elif atitu == "4":
                os.system("clear")
                for k,v in dicio.items():
                    print(k)
                    print(v)
                break
            elif atitu =="5":
                os.system("clear")
                pesq=input("Qual item deseja saber? ")
                for k,v in dicio.items():
                    if pesq ==  k:
                        print(v)
                        time.sleep(2)
                        break
                    else:
                        continue
                break
            else:
                exit()
    