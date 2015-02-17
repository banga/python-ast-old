class ASTBase(object):
    # TODO: figure out what information we want from the AST
    pass


class Name(ASTBase):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id


class Attribute(ASTBase):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __str__(self):
        return '%s.%s' % (self.parent, self.name)


class ArgumentList(ASTBase):
    def __init__(self, names):
        self.names = names

    def __str__(self):
        return '(%s)' % (', '.join(str(name) for name in self.names))


class Decorator(ASTBase):
    def __init__(self, name, arglist=None):
        self.name = name
        self.arglist = arglist

    def __str__(self):
        ret = '@' + str(self.name)
        if self.arglist is not None:
            ret += str(self.arglist)
        return ret

    __repr__ = __str__
