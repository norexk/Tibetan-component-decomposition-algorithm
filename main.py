#!/usr/bin/python
# -*- coding: UTF-8 -*-

class componentAnalysis():
    __afterOptions = {
        'ག': ['ཅ', 'ཏ', 'ཙ', 'ཉ', 'ད', 'ན', 'ཞ', 'ཟ', 'ཡ', 'ཤ'],
        'ད': ['ཀ', 'པ', 'ག', 'ང', 'བ', 'མ'],
        'བ': ['ཀ', 'ཅ', 'ཏ', 'ཙ', 'ག', 'ང', 'ཇ', 'ཉ', 'ད', 'ན', 'ཛ', 'ཞ', 'ཟ', 'ར', 'ཤ', 'ས'],
        'མ': ['ཁ', 'ཆ', 'ཐ', 'ཚ', 'ག', 'ཇ', 'ད', 'ཛ', 'ང', 'ཉ', 'ན'],
        'འ': ['ག', 'ཇ', 'ད', 'བ', 'ཛ', 'ཁ', 'ཆ', 'ཐ', 'ཕ', 'ཚ'],
    }
    __upOptions = [
        'རྐ', 'རྒ', 'རྔ', 'རྗ', 'རྙ', 'རྟ', 'རྡ', 'རྣ', 'རྦ', 'རྨ', 'རྩ', 'རྫ',
        'སྐ', 'སྒ', 'སྔ', 'སྙ', 'སྟ', 'སྡ', 'སྣ', 'སྤ', 'སྦ', 'སྨ', 'སྩ',
        'ལྐ', 'ལྒ', 'ལྔ', 'ལྕ', 'ལྗ', 'ལྟ', 'ལྡ', 'ལྤ', 'ལྦ', 'ལྷ'
    ]
    __downOptions = [ 'ྲ', 'ླ', 'ྱ', 'ྭ']
    __vowelOptions = ['ི', 'ུ', 'ེ', 'ོ']

    __char = None

    compUp = None
    compDown = None
    compAfter = None
    compBefor = None
    compBefors = None
    compBase = None
    compVowel = None

    compIndex = {
        'up': None,
        'down': None,
        'after': None,
        'befor': None,
        'befors': None,
        'base': None,
        'vowel': None,
    }

    def __init__(self,char):
        self.__char = char

        #遍历上加字找到基字
        for letter in self.__upOptions:
            if(self.__char.find(letter) > -1):
                compUpIndex = self.__char.find(letter)
                self.compIndex['up'] = compUpIndex
                self.compIndex['base'] = compUpIndex + 1
                self.compUp = self.__char[compUpIndex]
                self.compBase = self.__char[compUpIndex + 1]
                break
        
        #遍历下加字找到基字
        for letter in self.__downOptions:
            if(self.__char.find(letter) > -1):
                compUpIndex = self.__char.find(letter)
                self.compIndex['down'] = compUpIndex
                self.compIndex['base'] = compUpIndex - 1
                self.compDown = self.__char[compUpIndex]
                self.compBase = self.__char[compUpIndex - 1]
                break
        
        #未能通过上加字与下加字查询判定基字的情况下
        #判断第一个字符是否为前加字
        if self.compIndex['base'] is None :
            afterOptions = self.__afterOptions.keys()
            queryAfter = self.__char[0] in afterOptions
            if queryAfter == False :
                self.compIndex['base'] = 0      #第一个字丁为基字
                self.compBase = self.__char[0]  #标记字丁的下标
            else:
                if self.__char[1] in self.__afterOptions[self.__char[0]]:   #如果第二个字丁在前加字可用的基字列表中
                    self.compIndex['base'] = 1
                    self.compBase = self.__char[1]
                    self.compIndex['after'] = 0      
                    self.compAfter = self.__char[0]
                else:
                    self.compIndex['base'] = 0      
                    self.compBase = self.__char[0]
        
        #判断有没有音元符
        for letter in self.__vowelOptions:
            if(self.__char.find(letter) > -1):
                compVowelIndex = self.__char.find(letter)
                self.compIndex['vowel'] = compVowelIndex
                self.compVowel = self.__char[compVowelIndex]
                break
        
        #判断是否有音元符
        #判断音元符后面是否还有字丁
        #如果音元符后面还有字丁 那么音元符后面的第一个字符是后加字 第二个则是再后加字

        if self.compIndex['vowel'] is not None:
            if self.compIndex['vowel'] < len(self.__char):
                remaining = len(self.__char) - 1 - self.compIndex['vowel']
                self.compIndex['befor'] = self.compIndex['vowel'] + 1
                self.compBefor = self.__char[self.compIndex['vowel'] + 1]
                if remaining == 2:
                    self.compIndex['befors'] = self.compIndex['vowel'] + 2
                    self.compBefors = self.__char[self.compIndex['vowel'] + 2]
        elif self.compIndex['down'] is not None:
            if self.compIndex['down'] < len(self.__char):
                remaining = len(self.__char) - 1 - self.compIndex['down']
                self.compIndex['befor'] = self.compIndex['down'] + 1
                self.compBefor = self.__char[self.compIndex['down'] + 1]
                if remaining == 2:
                    self.compIndex['befors'] = self.compIndex['down'] + 2
                    self.compBefors = self.__char[self.compIndex['down'] + 2]
        else:
            if self.compIndex['base'] < len(self.__char):
                remaining = len(self.__char) - 1 - self.compIndex['base']
                self.compIndex['befor'] = self.compIndex['base'] + 1
                self.compBefor = self.__char[self.compIndex['base'] + 1]
                if remaining == 2:
                    self.compIndex['befors'] = self.compIndex['base'] + 2
                    self.compBefors = self.__char[self.compIndex['base'] + 2]

        








        
char = 'མཛུབ'
C = componentAnalysis(char)

charArray = [
    'ཨར',   'ཅི',     'རི',   'ཡར',   'བསྐྱོད', 'མཁན',
    'ཀྲུང', 'གོའི',   'རིམས', 'འགོག', 'སྨན',    'བཅོས',
    'རིགས', 'གཅིག',   'མཁས',  'ཅན',   'ཚོགས',   'ཆུང',
    'ཀྲུང', 'གོ',     'ལྕགས', 'ལམ',   'འཛུགས',  'སྐྲུན',
    'ལས',   'གྲྭ',    'ཚོགས', 'པ',    'ཨར',     'ཅི',
    'ཨར',   'པ',      'ལ',    'ཅིའི', 'ལུས',    'རྩལ',
    'ཐང',   'གི',     'རྣམ',  'གྲངས', 'ལས',     'ཡུལ',
    'དུ',   'བསྐྱོད', 'དེ',   'ཀྲུང', 'གོ',     'དང',
    'ཨར',   'ཅི',     'རི',   'ཡའི',  'ལས',     'མིར',
    'ཏོག',  'གསར',    'གློ',  'ཚད',   'རིམས',   'ནད',
    'སྔོན', 'འགོག',   'དང',   'ཚོད',  'འཛིན',   'གྱི',
    'ལས',   'དོན',    'ལ',    'མཛུབ', 'ཁྲིད',   'བྱས',
    'པ',    'རེད'
] 

# for item in charArray:
#     C = componentAnalysis(item)
#     print(item)
#     print(C.compAfter)
#     print('------------------')


print(C.compAfter)
print(C.compUp)
print(C.compBase)
print(C.compDown)
print(C.compVowel)
print(C.compBefor)
print(C.compBefors)