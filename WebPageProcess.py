import io, os, os.path
import urllib.request

def file_rm(filename):
    if(os.path.exists(filename)):
        os.remove(filename)


# 初始化文件名
file_name = input('请输入要生成的文件名：\n')
file_html = file_name + '.html'
file_clean = file_name + 'clean.html'


# 连续读取网页，生成html文件
file1 = open(file_html, 'a', encoding='utf-8')
address0 = input('请输入网页首页地址:\n')
page_start = input('请输入开始页码：\n')
if page_start == '':
    page_start = 1
else:
    page_start = int(page_start)
page_end = int(input('请输入总页数（大于2）:\n'))
for i in range(page_start, page_end):
    address_final = address0[:-7] + str(i)+ '.shtml'
    webpage1 = urllib.request.urlopen(address_final, timeout=20)
    webpage1_code = webpage1.read().decode('utf-8')
#    print(webpage1_code)
    file1.write(webpage1_code)
file1.close()

# 对html文件进行处理，
file_html_process = open(file_html, 'r', encoding='utf-8')
file_clean_process = open(file_clean, 'a', encoding='utf-8')
for line in file_html_process:
#    linestrip = line.strip() #去除行首空格
    if 'bbs-content' in line: #去除网页框架
#        print(line)
        file_clean_process.write(line)
file_html_process.close()
file_clean_process.close()

# 去除剩余的html标记及回复贴，生成txt文件
file_final = file_name + str(page_start) + '-' + str(page_end-1) + '.txt'
file_clean_read = open(file_clean, 'r', encoding='utf-8')
file_final_process = open(file_final, 'a', encoding='utf-8')
for line in file_clean_read:
    while '<' in line:
        start = line.find('<')
        end = line.find('>')
        line = line[:start]+line[(end+1):]
        line = line.strip()
    if len(line) < 250:
        pass
    elif '@' in line:
        pass
    elif u'&#' in line:
        pass
    elif u'回复日期：' in line:
        pass
    else:
        print(line,'\n')
        file_final_process.write(line)
        file_final_process.write('\n')
file_clean_read.close()
file_final_process.close()

#删除临时文件，remove temp files
file_rm(file_html)
file_rm(file_clean)
