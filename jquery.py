from dom import Dom
import re
from htmlprase import Myparser
import requests
class MyJquery:

    def __init__(self, doms = []):  
        self.doms = doms
    def select(self,str):  #jq选择器语法('.me #1111 [attr=value]   [target=_top]'-->不能有空格) 
        jq = self
        strlist = str.split(' ')
        for i in strlist:
            if i[0] == '[' and i[-1] == ']':  #[target=blank]
                spi = i[1:-1].split('=')
                if len(spi) == 1:
                    jq = jq.search({spi[0]:[]})
                if len(spi) == 2:
                    jq = jq.search({spi[0]:[spi[1]]})
            if(i[0] == '.'):   # .aa  class选择器
                jq = jq.search({'class':[i[1:]]})
            if(i[0] == '#'):   # #aa id选择器
                jq = jq.search({'id':[i[1:]]})
            if(i[0] not in ['.','#','[']):  #tag选择器
                jq = jq.search2(i[:])
        return jq
    def text(self): #返回tag的data
        strlist = []
        for i in self.doms:
            strlist.append(i.getData())
        return strlist
    def search(self,attrs):  #通过 attrs搜索 返回：MyJquery对象 attrs = [key :value[]]
        doms = []   #return
        stack = []
        for dom in self.doms:
            stack.append(dom)
        while(len(stack) != 0):
            dompop = stack.pop()
            if dompop.hasAttrs(attrs):
                doms.append(dompop)
            for domc in dompop.children:
                stack.append(domc)
        return MyJquery(doms)

    def search2(self, tag): #通过tag搜索，tag:str
        doms = []   #return
        stack = []
        for dom in self.doms:
            stack.append(dom)
        while(len(stack) != 0):
            dompop = stack.pop()
            if dompop.isTag(tag):
                doms.append(dompop)
            for domc in dompop.children:
                stack.append(domc)
        return MyJquery(doms)
    
    


    def feed(self, str): #把html解析为dom数组 input:html字符串 修改属性:self.doms[]
        strlist = self._prase2List(str)
        for i in strlist:
            myparser = Myparser()
            myparser.feed(i)
            self.doms.append(myparser.getDom())
            


    def _prase2List(self,htmlstr): 
        #转化为规范html  诸如 <a>1111<div>1111</div></a> output:list
        #把 <link> <script> <br> <input>  <style>等特殊标签去除
        htmlstr = re.sub(r'<input.*/>', '', htmlstr)
        htmlstr = re.sub(r'<![Dd][Oo][Cc][Tt][Yy][Pp][Ee] html>', '', htmlstr)
        htmlstr = re.sub(r'<link.*>', '', htmlstr)
        htmlstr = re.sub(r'<script.*?>[\s\S]*?</script>', '', htmlstr)
        htmlstr = re.sub(r'<style.*?>[\s\S]*?</style>', '', htmlstr)
        htmlstr = re.sub(r'<!--[\s\S]*?-->', '', htmlstr)
        htmlstr = re.sub(r'<br>', '', htmlstr)
        htmlstr = re.sub(r'<meta.*?>', '', htmlstr)
        return [htmlstr]

url = 'http://www.runoob.com/jquery/jquery-selectors.html'
r = requests.get(url)
my = MyJquery()
my.feed(r.content.decode('utf8'))
jqq = my.select('a [target=_top]')
print(jqq.text())
print(11111)

