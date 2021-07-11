# TODO: find api to convert path to list of avaiable modules
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
import os,sys
import pathlib as ___pl
# print(___pl.sys.path('~/Users/jules/opt/anaconda3/lib/python3.8/site-packages'))

class Dr:#directory
    def __init__(s,nm):s.nm,s.fs=nm,[]
def test_get_module_files(path):
    '''
    when api is found, this gets the files in the path,
    based on the curr path

    for now, dummy
    :param path:
    :return:
    '''
    if path == '~':
        j=[str(i) for i in range(9)]
    elif 'x' in path:
        j=[[]if i%2 else 'x'+str(i) for i in range(9)]
    return j
def test_build_dir():
    root=Dr('~')
    # -
    #    o
    #    o
    #        x
    #        x
    #        x
    #    ...
    #    4 o x-z0,z1,z2 x-z0, x

    #pop root

    for o in test_get_module_files(root.nm):
        root.fs+=[Dr(root.nm+'/'+Dr(o).nm)]
    dn = lambda o: o.split('/')[-1]  # dirname
    for f in root.fs:
        if int(dn(f.nm))%2:
            f.fs+=[Dr(root.nm+'/'+dn(f.nm)+'/'+str(chr(i))) for i in range(65,69)]
    return root
    # for f in root.fs:
    #     if int(dn(f.nm))%2:
    #         for e in root.fs[int(dn(f.nm))].fs:
    #             e.fs+=[Dr(''+j) for j in range(3)]
    #
    # return root

def a(a:int,c:str,b:bool):
    '''
    does somethin
    :param a:
    :param c:
    :param b:
    :return:
    '''
    return bool
'''
<ul>
  <li>Fruit
    <ul>
      <li>Bananas</li>
      <li>Apples</li>
      <li>Pears</li>
    </ul>
  </li>
  <li>Vegetables</li>
  <li>Meat</li>
</ul>
'''''

class A:
    def b(self):
        # if line has _3quote
        '''
        sadfasdfad
        :return:
        """

        """
                        ''' '''
                        
        '''
        rrrr=0
        """ docs1
""" ''' """ ''' """ '''docs2
            ''' """
        '''
        ddd
        ''' """'''"""

        exception = "" \
                    "''' "\
                    "" \
                    "not in docuemntaiton" \
                    "'''" \
                    "" \
                    ""
        f= ['"""'
            '"""'
            ]
        #parse escaped threequotes
        print
        def f(): # assert len(line.split('\t'))==2
            print
            def g(): # assert len(line.split('\t'))==3
                print
                #4
    def c(self):
        bool


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
    print(line,'has',tablature)
    return tablature
def snooper(path):
    '''
    consumes path and produces html depth 1

    This is not a full-on python interpreter

    methods and classes are only revealed if
    depth is 1

    use document at your own risk!
    1. 'directory'
    2. 'classes'
    3a c.mrthds
    3b. 'loose methods'
    :param path:
    :return:
    '''
    html = ''
    if path[-3:]!='.py':return None # this aint python
    c='class'
    d='def'
    indx = 0 #tablature
    _1quotes = "'''"
    _2quotes = '"""'
    _quotez = [_1quotes,_2quotes]
    with open(path,'r') as ro_module:
        print('opening',path)
        in_doc=False
        html=str()
        class_ix = 0
        in_class = False
        for ix,line in enumerate(ro_module.readlines()[:100]):
            if get_ix(line) <= class_ix:
                if in_class:
                    html+='</ul>'
                in_class = False
            if not in_doc:
                if line.strip()[:len(d)]==d: # method-line
                    cix = get_ix(line)

                    if cix > class_ix: #class method
                        html += (f'<p><li><u><b>{line}</b></u></li></p>')
                    else:
                        html += (f'<p><b>{line}</b></p>')
                elif line.strip()[:len(c)] == c: #class-line
                    html += (f'<p><i>{line}</i><ul>')
                    class_ix = get_ix(line)
                    in_class = True

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
from os import listdir
if __name__=='__main__':
    in_path='/Users/jules/opt/anaconda3/lib/python3.8/site-packages/flask'
    out_path='/Users/jules/Desktop/minasgerais/docs'

    result = (snooper(in_path+'/ctx.py'))
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




