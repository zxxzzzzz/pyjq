from html.parser import HTMLParser
from dom import Dom
class Myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.dom = Dom()
        self.stack = []  #dom堆栈 顶层对象为当前dom,用来实现子dom的添加

    def handle_data(self, data):
        if(len(self.stack) > 0):
            self.stack[len(self.stack) - 1].data = data

    def handle_starttag(self, tag, attrs):
        
        if len(self.stack) == 0:
            self.dom.type = tag
            for i in attrs:
                if i[1]:
                    self.dom.attrs[i[0]] = i[1].split(' ')
            self.stack.append(self.dom)
        else:
            dom = Dom()
            dom.type = tag
            for i in attrs:
               
                if i[1]:
                    dom.attrs[i[0]] = i[1].split(' ')
            
            self.stack[-1].children.append(dom)
            self.stack.append(dom)
        # self.stack[len(stack) - 1].type = tag  #写入目前的dom
        # for i in attrs:
        #     self.stack[len(stack) - 1].attrs[i[0]] = i[1].split(' ')
        # self.stack.append()
        
    def handle_endtag(self,tag):
        if len(self.stack) > 0:
            self.stack.pop()

    def getDom(self):
        return self.dom

# myparser = Myparser()
# myparser.feed('<a id = "111" class = "2222 333">111<div>222</div><a>333<a1>eee</a1><a2>a222</a2></a></a>')
# print(111)
