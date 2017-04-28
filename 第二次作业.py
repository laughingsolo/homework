# _*_coding:utf-8_*_
import re
taikong = []
fanpai = {}
juese  = {}
qita = {}
nanzhu = {}
nvzhu = {}
peijue = {}
fazhan = {}
jieju = {}
juqing = {}
kaitou = {}
leidian = {}
xiaodian = {}
dongzuo = {}
huamian = {}
jingtou = {}
shitingqt = {}
shiting = {}
yinyue = {}
bianju ={}
chupin = {}
daoyan = {}
xuanjing = {}
zhizuo = {}
fengge = {}
ticai = {}
zhuti = {}
with open('/home/laughingsolo/PycharmProjects/chapter 1/太空旅者.txt', 'r',encoding = 'utf-8') as readFile:
    txt = readFile.read()
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/角色/反派.txt', 'r', encoding = 'utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        fanpai[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt','w') as writeFile:
    for line in fanpai:
        writeFile.write(str(fanpai[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/角色/角色.txt', 'r', encoding='utf-8') as readFile:
        for line in readFile.readlines():
            line = line.strip('\n')
            reg = re.findall(line, txt)
            num = len(reg)
            juese[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
        for line in juese:
            writeFile.write(str(juese[line]))
            writeFile.write(' ')
            writeFile.write(line)
            writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/角色/角色中的其他.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        qita[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in qita:
        writeFile.write(str(qita[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/角色/男主角.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        nanzhu[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in nanzhu:
        writeFile.write(str(nanzhu[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/角色/女主角.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        nvzhu[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in nvzhu:
        writeFile.write(str(nvzhu[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/角色/配角.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        peijue[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in peijue:
        writeFile.write(str(peijue[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/剧情/发展.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        fazhan[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in fazhan:
        writeFile.write(str(fazhan[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/剧情/结局.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        jieju[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in jieju:
        writeFile.write(str(jieju[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/剧情/剧情.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        juqing[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in juqing:
        writeFile.write(str(juqing[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/剧情/开头.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        kaitou[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in kaitou:
        writeFile.write(str(kaitou[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/剧情/泪点.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        leidian[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in leidian:
        writeFile.write(str(leidian[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/剧情/笑点.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        xiaodian[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in xiaodian:
        writeFile.write(str(xiaodian[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/视听/动作.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        dongzuo[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in dongzuo:
        writeFile.write(str(dongzuo[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/视听/画面.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        huamian[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in huamian:
        writeFile.write(str(huamian[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/视听/镜头.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        jingtou[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in jingtou:
        writeFile.write(str(jingtou[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/视听/试听效果中的其他.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        shitingqt[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in shitingqt:
        writeFile.write(str(shitingqt[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/视听/视听.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        shiting[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in shiting:
        writeFile.write(str(shiting[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/视听/音乐.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        yinyue[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in yinyue:
        writeFile.write(str(yinyue[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/制作/编剧.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        bianju[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in bianju:
        writeFile.write(str(bianju[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/制作/出品公司.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        chupin[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in chupin:
        writeFile.write(str(chupin[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/制作/导演.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        daoyan[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in daoyan:
        writeFile.write(str(daoyan[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/制作/选景.txt', 'r', encoding='gbk') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        xuanjing[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in xuanjing:
        writeFile.write(str(xuanjing[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/制作/制作.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        zhizuo[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in zhizuo:
        writeFile.write(str(zhizuo[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/主题/风格.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        fengge[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in fengge:
        writeFile.write(str(fengge[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/主题/题材内容.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        ticai[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in ticai:
        writeFile.write(str(ticai[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
with open('/home/laughingsolo/PycharmProjects/chapter 1/dict/主题/主题.txt', 'r', encoding='utf-8') as readFile:
    for line in readFile.readlines():
        line = line.strip('\n')
        reg = re.findall(line, txt)
        num = len(reg)
        zhuti[line] = num
with open('/home/laughingsolo/PycharmProjects/chapter 1/关注点.txt', 'w') as writeFile:
    for line in zhuti:
        writeFile.write(str(zhuti[line]))
        writeFile.write(' ')
        writeFile.write(line)
        writeFile.write('\n')
