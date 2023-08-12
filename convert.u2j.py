import os
import sys
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

defaultOTname = bytearray(b'\x8A\x93\x8B\x50\x50\x50')
defaultPMname = bytearray(b'\x8B\x08\xA6\x50\x50\x50')
jpnPMNames = [bytearray(b'\x8A\x81\x13\xAB\x50\x50'), bytearray(b'\x8A\x81\x13\xAB\x50\x50'), bytearray(b'\x05\xA6\xE3\xA5\x50\x50'), bytearray(b'\x95\x13\xA5\xAB\xEF\x50'), bytearray(b'\x41\xAC\x41\x50\x50\x50'), bytearray(b'\x84\x95\x8C\x0C\xA0\x50'), bytearray(b'\x1A\xD8\xD8\x0F\x9D\x50'), bytearray(b'\x95\x13\x86\xAB\x07\x50'), bytearray(b'\xA2\x13\xA5\xAB\x50\x50'), bytearray(b'\x9B\x8B\x06\x8E\x82\x50'), bytearray(b'\x94\xAC\x8B\xE3\x50\x50'), bytearray(b'\x3D\xA8\xD8\xAB\x05\x50'), bytearray(b'\x8F\x9D\x8F\x9D\x50\x50'), bytearray(b'\x3D\x93\x3D\x8F\xE3\x50'), bytearray(b'\x08\xAB\x05\xE3\x50\x50'), bytearray(b'\x95\x13\xA5\xAB\xF5\x50'), bytearray(b'\x95\x13\x87\x81\xAB\x50'), bytearray(b'\x85\xA5\x85\xA5\x50\x50'), bytearray(b'\x8A\x81\x9C\xE3\xAB\x50'), bytearray(b'\xA5\x42\xA5\x8C\x50\x50'), bytearray(b'\x82\x81\xAB\x12\xB0\x50'), bytearray(b'\x9E\xAE\x82\x50\x50\x50'), bytearray(b'\x06\xAD\xA5\x13\x8C\x50'), bytearray(b'\x8B\xEB\xA6\x0F\xE3\x50'), bytearray(b'\xA0\x98\x87\xA5\x08\x50'), bytearray(b'\x09\xE3\x8C\x50\x50\x50'), bytearray(b'\x8C\x93\xA5\x81\x87\x50'), bytearray(b'\x9A\x93\x12\x9D\xAB\x50'), bytearray(b'\x85\xA0\xAC\x87\x8C\x50'), bytearray(b'\x85\x81\xA8\x8C\x50\x50'), bytearray(b'\xA1\xAB\x0B\xAD\xA5\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x05\xE3\x12\xB0\x50\x50'), bytearray(b'\x81\xA9\xE3\x87\x50\x50'), bytearray(b'\x84\x95\x13\xD8\xA6\x50'), bytearray(b'\x43\xAC\x43\x50\x50\x50'), bytearray(b'\xA2\x13\xAB\x50\x50\x50'), bytearray(b'\xA3\xAB\x08\xA5\xE3\x50'), bytearray(b'\x09\xA8\xE3\xAB\x50\x50'), bytearray(b'\xA5\xAC\x86\xE3\x50\x50'), bytearray(b'\x09\xE3\xD8\x86\xE3\x50'), bytearray(b'\x19\xD8\xA2\xE3\x13\x50'), bytearray(b'\x8A\xA9\x9F\xA5\xE3\x50'), bytearray(b'\x83\x1A\xA9\xA5\xE3\x50'), bytearray(b'\x80\xE3\x1C\xAC\x87\x50'), bytearray(b'\x40\xA5\x8D\x87\x93\x50'), bytearray(b'\x89\x0F\xAC\x87\x50\x50'), bytearray(b'\x8C\xD8\xE3\x42\x50\x50'), bytearray(b'\x09\xA8\xE3\x95\xAD\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x1B\xE3\x19\xE3\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x83\xA7\x1B\xE3\x50\x50'), bytearray(b'\xA7\x80\x89\x81\xA6\x50'), bytearray(b'\x13\x05\xE3\x8C\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x9D\xAB\x86\xE3\x50\x50'), bytearray(b'\x40\x82\xA9\x82\x50\x50'), bytearray(b'\x12\xB0\x07\x0F\x50\x50'), bytearray(b'\x88\xAB\x8F\xA8\x8C\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x85\xA1\x97\x06\x50\x50'), bytearray(b'\x89\xAB\x40\xAB\x50\x50'), bytearray(b'\x85\x81\xD8\xAE\xE3\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x13\xE3\x13\xE3\x50\x50'), bytearray(b'\x95\xAF\xA8\xA1\x50\x50'), bytearray(b'\xA6\xE3\x0B\xAE\xA5\x50'), bytearray(b'\x9B\xE9\x81\xA2\xE3\x50'), bytearray(b'\x9B\xD8\xE3\x0A\xE3\x50'), bytearray(b'\x8A\xAB\x0F\xE3\x50\x50'), bytearray(b'\xA0\x8F\xA1\xAB\x50\x50'), bytearray(b'\x95\xAD\xE3\x8C\x50\x50'), bytearray(b'\x87\xA5\x1B\x50\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xA8\x89\xAB\x50\x50\x50'), bytearray(b'\x86\xAE\x82\x89\xAB\x50'), bytearray(b'\x41\x85\x90\xAE\x82\x50'), bytearray(b'\xA5\x81\x90\xAE\x82\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x9E\x95\xD8\xAE\x82\x50'), bytearray(b'\x99\x87\xD8\xAE\xE3\x50'), bytearray(b'\x85\x1B\x93\x50\x50\x50'), bytearray(b'\x85\x1B\x93\x42\x8C\x50'), bytearray(b'\x8F\xAC\x91\xE3\x50\x50'), bytearray(b'\x8B\xE3\x13\xA5\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x8A\xAB\x13\x50\x50\x50'), bytearray(b'\x8A\xAB\x13\x40\xAB\x50'), bytearray(b'\x84\x9F\x94\x81\x93\x50'), bytearray(b'\x84\x9F\x8C\x8F\xE3\x50'), bytearray(b'\x42\xD8\xAB\x50\x50\x50'), bytearray(b'\x42\x87\xD8\xAB\x50\x50'), bytearray(b'\x81\xE3\x1B\x81\x50\x50'), bytearray(b'\x1B\xE3\x8C\x8F\xE3\x50'), bytearray(b'\x8A\xAB\x0F\xE3\x8C\x50'), bytearray(b'\x8B\xAD\xA9\xE3\x0C\x50'), bytearray(b'\xA9\xAB\xD8\x86\xE3\x50'), bytearray(b'\x0C\x19\xAC\x93\x50\x50'), bytearray(b'\x80\xE3\x1C\x50\x50\x50'), bytearray(b'\x40\xA5\x8C\x50\x50\x50'), bytearray(b'\x95\xAF\xA8\x0E\x50\x50'), bytearray(b'\x95\xAF\xA8\x1C\xAB\x50'), bytearray(b'\x1A\xE3\x13\xA6\x50\x50'), bytearray(b'\x89\x87\xE3\xAB\x50\x50'), bytearray(b'\x8C\x41\x80\xE3\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x13\xE3\x13\xD8\x84\x50'), bytearray(b'\x84\x89\xD8\x0A\xA6\x50'), bytearray(b'\x0F\x07\x93\xD8\x84\x50'), bytearray(b'\xA1\xA6\x9B\xF4\xAB\x50'), bytearray(b'\x0B\xAE\x09\xAB\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x86\xAD\x8F\x41\xE3\x50'), bytearray(b'\x93\xA5\xAB\x8D\xA6\x50'), bytearray(b'\x19\x8F\x9B\xD8\xE3\x50'), bytearray(b'\x85\x81\xD8\x86\xE3\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x09\xA6\x0F\xAC\x87\x50'), bytearray(b'\x8C\xD8\xE3\x40\xE3\x50'), bytearray(b'\x09\xA6\x19\xAC\x93\x50'), bytearray(b'\x9E\xAE\x82\x91\xE3\x50'), bytearray(b'\x85\x1A\x09\xAB\x50\x50'), bytearray(b'\x89\x81\x86\xAB\x07\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x3D\x93\x3D\x93\xAB\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x86\xAB\x07\xA5\xE3\x50'), bytearray(b'\x40\xA6\x8B\xEB\xAB\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x9D\xA6\x9D\x81\xAB\x50'), bytearray(b'\x41\x87\x8B\xE3\x50\x50'), bytearray(b'\x9D\x8F\x13\x05\x8C\x50'), bytearray(b'\x47\xA6\x8B\x80\xAB\x50'), bytearray(b'\x05\xA5\x05\xA5\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x09\xE3\x8C\x93\x50\x50'), bytearray(b'\x88\xE3\x8B\xB0\x50\x50'), bytearray(b'\x9B\xE3\x12\xB0\xAB\x50'), bytearray(b'\x41\x0B\xAF\xAB\x50\x50'), bytearray(b'\x41\x0B\xAF\xAC\x93\x50'), bytearray(b'\x8C\x8F\xE3\x9E\xE3\x50'), bytearray(b'\x9B\x8B\x06\x0F\x97\x50'), bytearray(b'\x9B\x8B\x06\x19\x94\x50'), bytearray(b'\x13\x87\x87\xA5\x08\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x93\x8A\x86\xAB\x93\x50'), bytearray(b'\x80\x0C\x9D\x84\x82\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x43\x95\xE3\x8F\x50\x50'), bytearray(b'\x06\xAD\xA8\xAC\x42\x50'), bytearray(b'\x89\xA5\xAC\x8F\x50\x50'), bytearray(b'\xA5\xAC\x8F\x50\x50\x50'), bytearray(b'\x95\x13\xD8\xE3\x98\x50'), bytearray(b'\x95\x13\xD8\xE3\x94\x50'), bytearray(b'\x81\x8B\x91\x1B\x92\x50'), bytearray(b'\x43\xD8\x09\xAB\x50\x50'), bytearray(b'\x42\x92\xA5\x50\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x89\x81\xA6\x50\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x9A\x93\x85\x08\x50\x50'), bytearray(b'\x0D\x95\x05\xA0\x50\x50'), bytearray(b'\xD8\x0A\xE3\x13\x50\x50'), bytearray(b'\x85\xA0\xE3\xA6\x50\x50'), bytearray(b'\xD8\x0A\xE3\x13\xAB\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x09\xE3\x8C\x93\x50\x50'), bytearray(b'\x94\x0E\x98\x87\x8A\x50'), bytearray(b'\x87\x8A\x81\x99\x94\x50'), bytearray(b'\xA5\x9B\xA7\x8B\x80\x50'), bytearray(b'\x9D\x0F\x91\x1C\x9E\x50'), bytearray(b'\x82\x91\x13\xAB\x50\x50'), bytearray(b'\x82\x91\x1C\xAC\x93\x50')]
class PokemonData:
    speciesID = 0
    pkmnData = bytearray(0)
    otName = bytearray(0)
    pkmnName = bytearray(0)



def readFileAsByteArray(file_path):
    with open(file_path, 'rb') as file:
        byte_array = file.read()
        file.close()
    return bytearray(byte_array)

def writeValueAt(array,offset,value,count):
    for i in range(count):
        array[offset + i] = value

def writeArrayAt(array,offset,inputArray):
    for i in range(len(inputArray)):
        char = inputArray[i]
        array[offset + i] = char

def copyArray(jpOffset,usOffset,usDestination):
    for i in range(usDestination - usOffset):
        # print(inSaveArray[jpOffset + i])
        outSaveArray[usOffset + i] = inSaveArray[jpOffset + i]

def copyArrayByLength(jpOffset,usOffset,length):
    for i in range(length):
        outSaveArray[usOffset + i] = inSaveArray[jpOffset + i]

def calculateChecksum(start,end):
    array = []
    for i in range(start,end + 1):
        array.append(outSaveArray[i])
    checksum =(~(sum(array) & 0xFF)) & 0xFF
    return checksum

def setChecksum(start,end,setOffset,desc):
    checksum = calculateChecksum(start,end)
    print(desc + ' Checksum 是：' + hex(checksum))
    outSaveArray[setOffset] = checksum
    print()

def writeByteArrayAsFile(file_path, byte_array):
    with open(file_path, 'wb') as file:
        file.write(byte_array)

def setBoxChecksums():
    origOffset = 0x4000
    for k in range(2):
        offset = origOffset + k * 0x2000
        for i in range(4):
            boxOffset = offset + i * 0x566
            singleBoxChecksumOffset = offset + 0x1599 + i
            setChecksum(boxOffset,boxOffset + 0x566,singleBoxChecksumOffset,'盒子 ' + str(i + 1 + 6 * k))
        setChecksum(offset,offset + 0x1597,offset + 0x1598,'Bank ' + str(1 + k))

extraBox = []


def getBoxOffsets():
    origOffset = 0x4000
    offsetsJPN = []
    for k in range(2):
        offset = origOffset + k * 0x2000
        for i in range(4):
            offsetsJPN.append(offset + i * 0x566)

    offsetsUS = []
    for k in range(2):
        offset = origOffset + k * 0x2000
        for i in range(6):
            offsetsUS.append(offset + i * 0x462)

    return (offsetsUS,offsetsJPN)
    
extraBox = []
def parseUSABoxData(offset,mode):
    speciesIDs = []
    OTNames = []
    pkmnDatas = []
    pkmnCount = inSaveArray[offset]
    if pkmnCount > 20:
        pkmnCount = 0
    for i in range(pkmnCount):
        speciesIDs.append(inSaveArray[offset + 1 + i])

        pkmnData = []
        for k in range(33):
            pkmnData.append(inSaveArray[offset + 0x16 + k + i * 33])
        pkmnDatas.append(pkmnData)

        OTName = []
        for j in range(6):
            OTName.append(inSaveArray[offset + 0x2AA + j + i * 0xB])
        OTNames.append(OTName)

    outputBox = []
    for i in range(pkmnCount):
        tmpPKMN = PokemonData()
        tmpPKMN.speciesID = speciesIDs[i]
        tmpPKMN.otName = OTNames[i]
        tmpPKMN.pkmnData = pkmnDatas[i]
        if mode == 1:
            outputBox.append(tmpPKMN)
        else:
            extraBox.append(tmpPKMN)
    return outputBox

def writeBoxData(boxData,offset):
    global option
    tmpBoxData = bytearray(0x566)
    tmpBoxData[0] = len(boxData)
    writeValueAt(tmpBoxData, 1, 0xFF, 31)
    for i in range(len(boxData)):
        currPKMN:PokemonData = boxData[i]
        tmpBoxData[1 + i] = currPKMN.speciesID
        writeArrayAt(tmpBoxData, 0x20 + 33 * i,currPKMN.pkmnData)
        writeArrayAt(tmpBoxData, 0x3FE + 0x6 * i,defaultOTname)
        writeArrayAt(tmpBoxData, 0x4B2 + 0x6 * i,jpnPMNames[currPKMN.speciesID])
    writeArrayAt(outSaveArray,offset,tmpBoxData)

file_path = os.path.abspath(os.path.dirname(__file__))
print()
print(' 宝可梦第一世代 美版存档 -> 日版存档 转换工具(测试版)')
print('')
print('-------------------------------------------------------------')
print('由于新版汉化版都是基于美版汉化，日文版无法直接使用，故开发此工具将美版存档转换成日版存档')
print()
print('！！！在开始之前，请确认要转换的存档已经在精灵中心门口的垫子处存档，若死机请在其他地方多次尝试！！！')
print('！！！在确认新版存档能使用前请注意备份存档！！！')
print('！！！不保证 100% 可用！！！宝可梦昵称会被还原成默认名字！')
print('！！！主角/所有宝可梦初训家会被重命名为：サトシ，劲敌会被重命名为：シゲル！！！')
print('！！！存档选择的当前盒子将原样迁移，若美版存档剩余11个盒子（最大220只宝可梦）的宝可梦超过210只，将只迁移其中的前210只。')
print('！！！不会迁移名人堂数据！！！')
print()
print('当前目录：' + file_path)
print('即将打开选择文件对话框')
print('按 Enter/Return 键继续')
print('若按下键盘后没反应，请先用鼠标点击窗口，然后再按下键盘')
dummy = input('')
path = filedialog.askopenfilename(title="选择 .sav 文件", filetypes=(("sav 文件", "*.sav"), ("All files", "*.*")))

# inSaveArray = readFileAsByteArray('red.en.sav')
inSaveArray = readFileAsByteArray(path)
outSaveArray = bytearray(len(inSaveArray))

writeArrayAt(outSaveArray,0x2598,defaultOTname)
copyArray(0x25A3,0x259E,0x25F1)
writeArrayAt(outSaveArray,0x25F1,defaultPMname)
copyArray(0x2601,0x25F7,0x2B2A)
copyArray(0x2CE4,0x2C97,0x2CA8)
dayCareSpecies = inSaveArray[0x2D0B]
if dayCareSpecies <= 190:
    writeArrayAt(outSaveArray,0x2CA8,jpnPMNames[dayCareSpecies])    
writeArrayAt(outSaveArray,0x2CAE,defaultOTname)
copyArray(0x2D0B,0x2CB4,0x2ED5)

copyArrayByLength(0x2F2C,0x2ED5,0x110)
index = 0x2ED5 + 0x110
for i in range(6):
    writeArrayAt(outSaveArray,index + i * 0x6 ,defaultOTname)
index = 0x2ED5 + 0x134
for i in range(6):
    if outSaveArray[0x2ED5 + 1 + i] <= 190:
        writeArrayAt(outSaveArray,index + i * 0x6 ,jpnPMNames[outSaveArray[0x2ED5 + 1 + i]])


currentBoxNo = inSaveArray[0x284C] & 0x7F
print('Current Box No. ' + str(currentBoxNo + 1))
currentPKMNBox = parseUSABoxData(0x30C0,1)
writeBoxData(currentPKMNBox,0x302D)
setChecksum(0x2598,0x3593,0x3594,'Main Data')

boxOffsets = getBoxOffsets()
for boxno in range(12):
    parseUSABoxData(boxOffsets[0][boxno],2)

for boxno in range(8):
    if currentBoxNo == boxno:
        continue
    count = 0
    tmpPKMNBox = []
    # print(extraBox)
    while len(extraBox)!= 0 and count < 30:
        tmpPKMNBox.append(extraBox.pop(0))
        count += 1
    writeBoxData(tmpPKMNBox,boxOffsets[1][boxno])

# for boxno in range(8):
#     currentPKMNBox = parseJPNBoxData(boxOffsets[1][boxno])
#     writeBoxData(currentPKMNBox,boxOffsets[0][boxno])

# for boxno in range(8,12):




setBoxChecksums()


save_path = filedialog.asksaveasfilename(title="请选择保存位置", defaultextension=".sav", filetypes=(("sav 文件", "*.sav"), ("All files", "*.*")))
# writeByteArrayAsFile('red.jp.sav',outSaveArray)
writeByteArrayAsFile(save_path,outSaveArray)
# writeByteArrayAsFile(os.path.join(file_path,'YellowNew.sav'),newArray)
print('新存档已经写入到：')
print(save_path)
print()
print('-------------------------------------------------------------')
print('如果转换后在新版中启动死机')
print('请在 CKN 版本中携带会飞翔的宝可梦，前往精灵中心门口（室外）然后存档')
print('然后再重新执行本操作，进入游戏后使用飞翔前往其他地方即可')

if sys.platform == 'win32':
    print('按 Enter/Return 键关闭')
    dummy2 = input('')