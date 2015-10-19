from foo import Foo
from bar import Bar

if __name__ == '__main__':
    b = Bar()
    print b.get_font()
    f = Foo()
    print f.get_font()
    
    b.set_font('bar')
    print b.get_font()
    print f.get_font()
    pass