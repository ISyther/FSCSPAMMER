#!/usr/bin/env python
# -*- coding: utf-8 -*-

def banner():
    print('''
        
                              /$$$$$$$$ /$$$$$$   /$$$$$$        
                             | $$_____//$$__  $$ /$$__  $$      
                             | $$     | $$  \__/| $$  \__/      
                             | $$$$$  |  $$$$$$ | $$            
                             | $$__/   \____  $$| $$            
                             | $$      /$$  \ $$| $$    $$      
                             | $$     |  $$$$$$/|  $$$$$$/      
                             |__/      \______/  \______/ 

 /$$      /$$  /$$$$$$  /$$$$$$ /$$              /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$ /$$      /$$ /$$$$$$$$ /$$$$$$$ 
| $$$    /$$$ /$$__  $$|_  $$_/| $$             /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$| $$$    /$$$| $$_____/| $$__  $$
| $$$$  /$$$$| $$  \ $$  | $$  | $$            | $$  \__/| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$$$  /$$$$| $$      | $$  \ $$
| $$ $$/$$ $$| $$$$$$$$  | $$  | $$   /$$$$$$  |  $$$$$$ | $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$ $$/$$ $$| $$$$$   | $$$$$$$/
| $$  $$$| $$| $$__  $$  | $$  | $$  |______/   \____  $$| $$____/ | $$__  $$| $$  $$$| $$| $$  $$$| $$| $$__/   | $$__  $$
| $$\  $ | $$| $$  | $$  | $$  | $$             /$$  \ $$| $$      | $$  | $$| $$\  $ | $$| $$\  $ | $$| $$      | $$  \ $$
| $$ \/  | $$| $$  | $$ /$$$$$$| $$$$$$$$      |  $$$$$$/| $$      | $$  | $$| $$ \/  | $$| $$ \/  | $$| $$$$$$$$| $$  | $$
|__/     |__/|__/  |__/|______/|________/       \______/ |__/      |__/  |__/|__/     |__/|__/     |__/|________/|__/  |__/
    

                                        By: Felipe Mandioca
                                 
                            [Grupo] www.facebook.com/groups/fsocietybrasil         
                            [Forum] www.forum.fsocietybrasil.org   
                            [Site]  www.fsocietybrasil.org 
                            [Link da Postagem] www.forum.fsocietybrasil.org/topic/609-fsc-mail-spammer/
                                (Na postagem ensino a permitir logins que não sejam pelo site na conta do gmail)
    
    ''')

#=================================================================================================#

def confirmar():
    print('''
|   
|[EMAIL] %s [SENHA] %s
|   
|   [REMENTENTE] %s
|
|[MENSAGEM] %s 
|[VEZES] %d
|
    
    '''%(email,senha,receber,mensagem,vezes))

    sair=False

    while sair==False:
        continuar=input("Você confirma? Esta tudo correto para o envio do email? S/N ")

        if(continuar.lower() == "s"):
            return True

        else:
            print("Vamos fazer novamente então!")
            return  False
#==================================================================================================#

def limpa():
    print(50*"\n")

def send_mail(email, senha, receber, mensagem, vezes):
    try:
        from smtplib import SMTP
        import time

        x = 1
        gmail = SMTP('smtp.gmail.com:587')
        gmail.ehlo()
        gmail.starttls()
        gmail.login(email, senha)
        while x <= vezes:
            gmail.sendmail(email, receber, mensagem)
            print("[%d]Enviado!" % x)
            x += 1

        gmail.close()
        time.sleep(2)


    except KeyboardInterrupt:
        print("\n\n[!] Interrompendo o envio de emails!")
        time.sleep(3)

    except ImportError:
        print("[!] Erro de importação, biblioteca: smtplib,time")

    except:
        print("\n[!] Erro de Autenticação! (Logins externos não estão permitidos no seu gmail ou Login incorreto ou Rementente não encontrado")
        print("\nEspere 10 segundos")
        time.sleep(10)

#=================================================================================================#

while True:
    banner()
    email = input("Digite Seu email: ")
    senha = input("Digite Sua senha: ")
    receber = input("Digite o email remente: ")
    mensagem = input("Digite sua mensagem: ")
    vezes = int(input("Digite a quantidade de emails para serem enviados: "))

    if(confirmar() == False):
        continue

    else:

        send_mail(email,senha,receber,mensagem,vezes)
        limpa()
