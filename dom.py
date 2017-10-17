class Dom:
    def __init__(self):  # 
        self.attrs ={} #key:value
        self.data = ''
        self.children = [] # class:dom
        self.type = '' #div img标签名
    def getData(self):
        return self.data
    def hasAttrs(self,attrs): # dom是否有某些attr input:attrs = [] output : True/False
        for key in attrs:
            if key not in self.attrs:  #dom没有该属性key
                return False
            else:
                for value in attrs[key]:
                    if value not in self.attrs[key]:  #dom 属性值不包含
                        return False
        return True
    def isTag(self,tag):
        if tag == self.type:
            return True
        return False


