'''
/******************************************************************************
* Copyright (C) 1996-2021 suli.org, Booljawn.
*
* Permission is hereby granted, free of charge, to any person obtaining
* a copy of this software and associated documentation files (the
* "Software"), to deal in the Software without restriction, including
* without limitation the rights to use, copy, modify, merge, publish,
* distribute, sublicense, and/or sell copies of the Software, and to
* permit persons to whom the Software is furnished to do so, subject to
* the following conditions:
*
* The above copyright notice and this permission notice shall be
* included in all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
* IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
* CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
* TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
* SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
******************************************************************************/
'''
import os,random
# random.seed(23)
def get_ix(line: str)->int:
    '''
    consumes a line of python and returns
    the number of tab-spaces in front of line

    if empty, returns -1
    :param line:
    :return:
    '''
    if len(line.strip())==0:return -1
    _4space = ' ' * 4
    _tab = '\t'
    tablature = 0
    for c in line:
        if c=='\t':
            tablature+=1
        if c!='\t':
            break
    for elem in line.split(_4space):
        if not elem:
            tablature+=1
        else:
            break
    print(tablature,str(chr(33))*5, line[:-2],)
    return tablature
def snooper(path:str)->str:
    '''
    Snoops into a python module, and returns html describing it.
    consumes path and produces html depth 1

    This is not a full-on python interpreter

    methods and classes are only revealed if
    depth is 1

    use document at your own risk!
    1. 'directory'
    2. 'classes'
    3a c.mrthds
    3b. 'loose methods'
    :param path: python-raw.py
    :return: str: html-raw.html
    '''
    if path[-3:]!='.py':return None # this aint python
    c='class'
    d='def'
    _quotez = ["'''",'"""']
    with open(path,'r') as ro_module:
        print('opening',path)
        in_doc=False
        html=str()
        class_ix = 0
        in_class = False
        for ix,line in enumerate(ro_module.readlines()[:10000]):
            if get_ix(line) <= class_ix:
                if in_class:
                    html+='</ul>'
                in_class = False
            if not in_doc:
                if line.strip()[:len(d)]==d: # method-line
                    cix = get_ix(line)
                    if cix > class_ix: #class method
                        html += (f'<li><font color={rand_color}><u><b>{line}</b></u></font></li>')
                    else:
                        html += (f'<p><b>{line}</b></p>')
                elif line.strip()[:len(c)] == c: #class-line
                    in_class = True
                    rand_color = str(hex(random.getrandbits(32)))[2:8]
                    html += (f'<p><font size=24 color={rand_color}><i>{line}</font></i><ul>')
                    class_ix = get_ix(line)
            # Interpret line if contains triquotes
            if (card:=sum(map(lambda q:len(line.split(q)),_quotez)))==2:
                if in_doc:
                    for q in _quotez:
                        line = line.replace(q,'')
                    html += line + '<br>'
            if card==3:
                in_doc= not in_doc
                if in_doc:
                    for q in _quotez:
                        line = line.replace(q,'')
                    html+='<p>'+line+'<br>'
            if card==4:
                for q in _quotez:
                    line=line.replace(q,'')
                html+='<p>' + line + '</p>'
    return html
def inorder_search(dr,yogg=0):
    '''
    inorder search
    to consume root and print, recursively print
    later, this will populate html of following form
    1. 'directory'
    2. 'classes'
    3a clsthds
    3b. 'loose methods'

    :param dr:
    :return:
    '''
    # make this directory. if terminal
    print('\t'*yogg,dr.nm,''if dr.fs else'.html')
    #moreover, call snooper to build docs html
    [inorder_search(f,yogg=yogg+1) for f in dr.fs]

if __name__=='__main__':
    in_path='/Users/jules/opt/anaconda3/lib/python3.8/site-packages/flask'+ '/ctx.py'
    out_path='/Users/jules/Desktop/minasgerais/docs'
    # in_path =  '/Users/jules/Desktop/minasgerais/swag.py'
    result = (snooper(in_path))
    with open('/Users/jules/Desktop/minasgerais/windex.html','w+') as a:
        a.write(result)
    # print(listdir(in_path))
    # from the in_path, recurse through all python modules
    # for each python file, iterate lines of python code
    # case 1: entering loose method
    # case 2: entering class
    # case 3: entering class method
    # We know a class or method ends when the indentation drops
    # os.mkdir
    # os.rmdir




