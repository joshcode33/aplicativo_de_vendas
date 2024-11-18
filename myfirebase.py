import requests
from kivy.app import App


class MyFireBase():
    API_KEY = "AIzaSyBmxAWe4quMhFj4OswYKENzZfeXXPP7CFw"
    pass

    def criar_conta(self, email, senha):
        link = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}"
        print(email, senha)
        info = {"email": email,
                "password": senha,
                "returnSecureToken": True}
        requisicao = requests.post(link, data=info)
        requisicao.dic = requisicao.json()

        if requisicao.ok:
            print("usuario criado")
            # requisicao.dic["idToken"]
            # requisicao.dic["refreshToken"]
            # requisicao.dic["localid"]
            refresh_token = requisicao.dic["refreshToken"]
            local_id = requisicao.dic["localId"]
            id_token = requisicao.dic["idToken"]

            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            with open("refreshtoken.txt", "w") as arquivo:
                arquivo.write(refresh_token)

            link = f"https://appdevendas-9e69b-default-rtdb.firebaseio.com/{local_id}.json"
            info_usuario = '{"avatar": "foto1.png", "equipe": "", "total_vendas": "0", "vendas": ""}'
            requisicao_usuario = requests.patch(link, data=info_usuario)

            meu_aplicativo.carregar_infos_usuarios()
            meu_aplicativo.mudar_tela("homepage")
        else:
            mensagem_erro = requisicao.dic["error"]["message"]
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids["loginpage"]
            pagina_login.ids["mansagem_login"].text = mensagem_erro
            pagina_login.ids["mensagem_erro"].color = (1, 0, 0, 1)
        print(requisicao.dic)

    def fazer_login(self, email, senha):
        pass