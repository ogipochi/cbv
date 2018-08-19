from django.shortcuts import render
from django.http import HttpResponse
import json
from . import mixins

class CustomClassView:
    """
    最もシンプルなCBV
    headerをタイトルに入れ,
    contextをbodyに入れたレスポンスを返す
    """
    context = ['content_1','content_2']
    header = 'Happy People'

    def __init__(self,**kwargs):
        """
        キーワード引数を受け取って初期化
        例 CustomeClassView(header='Big News')
        『Big News』というタイトルで初期化
        """
        self.kwargs = kwargs
        for (k,v) in kwargs.items():
            setattr(self,k,v)
    
    def render(self):
        # headerが
        header = self.header
        return """
        <html>
        <body>
        <h1>{header}</h1>
        {body}
        </body>
        </html>
        """.format(
            header=self.header,body='<br>'.join(self.context))

    @classmethod
    def as_view(cls,*args,**kwargs):
        """
        受け取った引数をいれインスタンス化したインスタンスのrenderメソッド
        の結果を返す
        クラスメソッドのためインスタンス化せずに呼ばれる
        例 : CustomeClassView.as_view()
        clsはこのクラスを指す.
        このメソッド内でインスタンス化する.ということは継承しても
        このas_viewメソッドを呼ぶことでその中でうまくインスタンス化できる.
        """
        def view(request,):
            instance = cls(**kwargs)
            return HttpResponse(instance.render())
        return view

class BetterCustomClassView(CustomClassView,):
    def get_header(self,):
        """
        headerがあれば返す
        """
        print('Better Custom Class View')
        return self.header if self.header else ""

    def get_context(self,):
        """
        contextがあれば返す
        なければ空のリストを返す
        """
        return self.context if self.context else []
    def render_context(self):
        """
        contextフィールドを抽出し改行で連結した文字列を返す
        """
        context = self.get_context()
        if context:
            return '<br>'.join(context)
        return ""
    def render(self):
        return """
        <html>
            <body>
                <h1>{header}</h1>
                {body}
            </body>
        </html>
        """.format(
            header=self.get_header(),
            body=self.render_context()
        )

class HeaderPrefixBetterCustomClassView(mixins.HeaderPrefixMixin,BetterCustomClassView):
    header='Hello'

class HeaderPrefixDefaultBetterCustomClassView(mixins.HeaderPrefixMixin,mixins.DefaultHeaderSuperMixin,BetterCustomClassView):
    pass


class ExtraContext12BetterCustomClassView(mixins.ExtraContext1Mixin, mixins.ExtraContext2Mixin, BetterCustomClassView):
    pass

class ExtraContext21BetterCustomClassView(mixins.ExtraContext2Mixin, mixins.ExtraContext1Mixin, BetterCustomClassView):
    pass  
class AllTogetherNowBetterCustomClassView(
        mixins.HeaderPrefixMixin,
        mixins.DefaultHeaderSuperMixin,
        mixins.ExtraContext1Mixin,
        mixins.ExtraContext2Mixin,
        BetterCustomClassView
    ):
    pass