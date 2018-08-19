
class DefaultHeaderMixin:
    """
    Header定義のMixin
    """
    def get_header(self,):
        return self.header if self.header else "DEFAULT HEADER"
    
class DefaultContextMixin:
    """
    context定義のMixin
    """
    def get_context(self,):
        return self.context if self.context else ["DEFAULT CONTEXT"]

class HeaderPrefixMixin:
    def get_header(self,):
        """
        親クラスのget_headerメソッドから子クラスのheaderフィールドを受り,
        PREFIXをつけて返す
        """
        return "PREFIX: " + super().get_header()


class DefaultHeaderSuperMixin:
    def get_header(self,):
        """
        親クラスのget_headerメソッドから
        子クラスのheaderフィールドをかえす.
        なければデフォルト値を返す
        """
        return super().get_header() if super().get_header() else "DEFAULT HEADER"

class ExtraContext1Mixin:
    def get_context(self,):
        """
        親クラスのcontextデータを受取り,
        'data1'を最後尾に追加する
        """
        ctx = super().get_context()
        ctx.append('data1')
        return ctx

class ExtraContext2Mixin:
    def get_context(self,):
        """
        親クラスのcontextデータを受取り,
        'data2'を0番目に挿入する
        """
        ctx = super().get_context()
        ctx.insert(0,'data2')
        return ctx


 