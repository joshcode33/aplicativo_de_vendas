from kivy.app import App
from kivy.lang import Builder
from myfirebase import MyFireBase
from telas import *
from botoes import *
import requests
from bannervenda import BannerVenda
import os
from functools import partial
from myfirebase import MyFireBase





GUI = Builder.load_file("main.kv")
class MainApp(App):
    id_usuario = 1

    def build(self):
        self.firebase = MyFireBase()
        return GUI

    def on_start(self):
        # Listar arquivos de fotos de perfil
        arquivos = os.listdir('icones/fotos_perfil')
        pagina_fotoperfil = self.root.ids['fotoperfil']
        lista_fotos = pagina_fotoperfil.ids['lista_foto_perfil']

        for foto in arquivos:
            # Usar Button com imagem para capturar evento de clique
            image_button = Button(
                background_normal=f"icones/fotos_perfil/{foto}",
                on_release=self.mudar_foto_perfil
            )
            lista_fotos.add_widget(image_button)


        self.carregar_infos_usuario()


    def carregar_infos_usuario(self):

        # pegar informacoes de usuario
        import requests

        try:
            # Fazendo a requisição GET para a API
            requisicao = requests.get(f"https://appdevendas-9e69b-default-rtdb.firebaseio.com/{self.id_usuario}.json")

            # Verificando se a requisição foi bem-sucedida (status code 200)
            requisicao.raise_for_status()

            # Tentando converter a resposta para um dicionário (JSON)
            requisicao_dic = requisicao.json()

        except requests.exceptions.RequestException as e:
            # Captura erros de requisição (ex: problemas de conexão, URL inválida)
            print(f"Erro ao fazer requisição: {e}")

        except ValueError as e:
            # Captura erros caso a resposta não seja um JSON válido
            print(f"Erro ao processar a resposta como JSON: {e}")

        # preencher foto de perfil
        avatar = requisicao_dic['avatar']
        foto_perfil = self.root.ids["foto_perfil"]
        foto_perfil.source = f"icones/fotos_perfil/{avatar}"

        # Preencher listas de vendas
        try:
            print(requisicao_dic)
            vendas = requisicao_dic.get["vendas"][1:]
            pagina_homepage = self.root.ids["homepage"]
            lista_vendas = pagina_homepage.ids["lista_vendas"]
            for id_venda in vendas:
                venda = vendas(id_venda)
                banner = BannerVenda(
                        cliente=venda.get("cliente", ""),
                        foto_cliente=venda.get("foto_cliente", ""),
                        produto=venda.get("produto", ""),
                        foto_produto=venda.get("foto_produto", ""),
                        data=venda.get("data", ""),
                        preco=venda.get("preco", 0),
                        unidade=venda.get("unidade", ""),
                        quantidade=venda.get("quantidade", 0)
                    )

                lista_vendas.add_widget(banner)

        except:
            pass

    def mudar_tela(self, id_tela):
        gerenciar_telas = self.root.ids["screen_manager"]
        gerenciar_telas.current = id_tela

    def mudar_foto_perfil(self, foto, *args):
        print(foto)
        foto_perfil = self.root.ids["foto_perfil"]
        foto_perfil.source = f"icones/fotos_perfil/{foto}"

        info = f'{{"avatar": "{foto}"}}'
        requisicao = requests.get(f"https://appdevendas-9e69b-default-rtdb.firebaseio.com/{self.id_usuario}.json"
                                  , data=info)

        self.mudar_tela("ajustespage")
MainApp().run()

