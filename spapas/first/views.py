from django.shortcuts import render
from django.http import HttpResponse

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
