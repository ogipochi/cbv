
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

