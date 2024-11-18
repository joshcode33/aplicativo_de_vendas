from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color


class BannerVenda(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Inicializa o GridLayout corretamente
        self.rows = 1  # Define rows após o init

        with self.canvas:
            Color(rgba=(0, 0, 0, 1))  # Use rgba para incluir a transparência
            self.rec = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.atualizar_rec, size=self.atualizar_rec)

        cliente = kwargs.get("cliente", "")
        foto_cliente = kwargs.get("foto_cliente", "")
        produto = kwargs.get("produto", "")
        foto_produto = kwargs.get("foto_produto", "")
        data = kwargs.get("data", "")
        unidade = kwargs.get("unidade", "")
        quantidade = float(kwargs("quantidade", 1))
        preco = float(kwargs("preco", 0))

        # Seção esquerda
        esquerda = FloatLayout()
        esquerda_image = Image(pos_hint={"right": 1, "top": 0.95}, size_hint=(1, 0.75),
                               source=f"icones/fotos_clientes/{foto_cliente}")
        esquerda_label = Label(text=cliente, size_hint=(1, 0.2), pos_hint={"right": 1, "top": 0.2})
        esquerda.add_widget(esquerda_image)
        esquerda.add_widget(esquerda_label)

        # Seção meio
        meio = FloatLayout()
        meio_image = Image(pos_hint={"right": 1, "top": 0.95}, size_hint=(1, 0.75),
                           source=f"icones/fotos_produtos/{foto_produto}")
        meio_label = Label(text=produto, size_hint=(1, 0.2), pos_hint={"right": 1, "top": 0.2})
        meio.add_widget(meio_image)
        meio.add_widget(meio_label)

        # Seção direita
        direita = FloatLayout()
        direita_label_data = Label(text=f"Data: {data}", size_hint=(1, 0.33), pos_hint={"right": 1, "top": 0.9})
        direita_label_preco = Label(text=f"Preço: R${preco}", size_hint=(1, 0.33), pos_hint={"right": 1, "top": 0.65})
        direita_label_quantidade = Label(text=f"{quantidade} {unidade}", size_hint=(1, 0.33), pos_hint={"right": 1, "top": 0.4})
        direita.add_widget(direita_label_data)
        direita.add_widget(direita_label_preco)
        direita.add_widget(direita_label_quantidade)

        # Adicionando as seções ao layout principal
        self.add_widget(esquerda)
        self.add_widget(meio)
        self.add_widget(direita)

    def atualizar_rec(self, *args):
        self.rec.pos = self.pos
        self.rec.size = self.size
