#con3con2con1 = 100  IO0 = Tx -- esp32:RX
#盘符：USB:00 SD:01 FLASH:02 NO_DEVICE：FF

# ##串口播放
# from machine import UART
# com = UART(2,9600)
# com.write(b'\xaa\x02\x00\xac')

#软串口
# >>> from serial_uart import uart
# >>> import time
# >>>
# >>> com = uart(27, 34, False, 512)  #tx=27, rx=34
# >>> com.open(9600)
# 0
# >>> com.write(b'abc')
# 3
# >>> com.read()
# b'qwe'


from serial_uart import uart
import time

com = uart(22, 23, False, 512)  #tx=22, rx=23
com.open(9600)

#播放当前
com.write(b'\xaa\x02\x00\xac')


#上一曲
com.write(b'\xaa\x05\x00\xaf')


#下一曲
com.write(b'\xaa\x06\x00\xb0')


#结束播放
com.write(b'\xaa\x10\x00\xba')


#播放模式 *
com.write(b'\xaa\x18\x01\x02\xc5')
 播放模式定义：上电默认为单曲停止。
# ※ 全盘循环(00)：按顺序播放全盘曲目,播放完后循环播放。 
# ※ 单曲循环(01)：一直循环播放当前曲目。  
# ※ 单曲停止(02)：播放完当前曲目一次停止。
# ※ 全盘随机(03)：随机播放盘符内曲目。  
# ※ 目录循环(04)：按顺序播放当前文件夹内曲目,播放完后循环播放，目录不包含子目录。 
# ※ 目录随机(05): 在当前目录内随机播放，目录不包含子目录。
# ※ 目录顺序播放(06)：按顺序播放当前文件夹内曲目，播放完后停止，目录不包含子目录。
# ※ 顺序播放(07)：按顺序播放全盘曲目，播放完后停止。 


#音量设置[0,30] 16进制  默认20级
com.write(b'\xAA\x13\x01\x14\xD2')  #20级=\x14

#组合播放（放在ZH文件夹下 01.mp3+02.mp3）
com.write(b'\xaa\x1b\x04\x30\x31\x30\x32\x8c') # 04 长度，'0'=\x30  曲目1高字节+曲目1低字节+曲目2...
##可以组合两首，立刻结束第一首 从而只播放第二首
com.write(b'\xaa\x1b\x04\x30\x31\x30\x32\x8c')  #其他名字有bug，暂时不推荐
com.write(b'\xaa\x10\x00\xba')#结束播放
com.write(b'\xaa\x1b\x04\x30\x32\x30\x31\x8c')
com.write(b'\xaa\x10\x00\xba')#结束播放


####################################################


#查询当前盘符
com.write(b'\xaa\x09\x00\xb3')


#查询总曲目
com.write(b'\xaa\x12\x00\xbc')

