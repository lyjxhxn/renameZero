import os

test_path = 'E:\\py\\文件名补0\\测试文件\\'


# n = 1
# for i in range(50):
#     with open(test_path+str(n)+'_abc'+'.txt','w')as f:
#         f.write(str(n))
#         n+=1



def fenge(test_path,guanjianzi,digit):
    '''分割字符重命名'''
    # weishu = '0'+digit+'d'
    for file_name in os.listdir(test_path):
        # print(file_name)
        try:
            name_1 = file_name.split(guanjianzi)[0]
            name_2= file_name.split(guanjianzi)[1]
            new_name = '%0{}d'.format(digit) % int(name_1)
            os.rename(test_path+'\\'+file_name, test_path+'\\'+ new_name + guanjianzi+ name_2)
            print(test_path+'\\'+file_name+'    重命名   '+ new_name + guanjianzi+ name_2+'  成功！')
        except:
            print(test_path+'\\'+file_name+'  重命名失败！')

guanjian = 'abcd'
weishu = 3
# fenge(test_path,guanjian,weishu)


n = 1
for i in range(20):
    with open(test_path+str(n)+'abcd'+'.txt','w')as f:
        f.write(str(n))
        n+=1


# def guanjianzi(test_path):
#     '''按重复关键字重命名'''
#     for file_name in os.listdir(test_path):
#         # print(file_name)
#         try:
#             name_1 = file_name.split('abcd')[0]
#             name_2= file_name.split('abcd')[1]
#             os.rename(test_path+'\\'+file_name, test_path+'\\'+'%03d' % int(name_1) +'abcd'+ name_2)
#             print(test_path+'\\'+file_name+'重命名'+ '%03d' % int(name_1) +'abcd'+ name_2+'  成功！')
#         except:
#             print(test_path+'\\'+file_name+'  重命名失败！')

# guanjianzi(test_path)


for file_name in os.listdir(test_path):
    print(file_name)