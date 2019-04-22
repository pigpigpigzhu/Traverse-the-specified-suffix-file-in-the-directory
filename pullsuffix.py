import os
def subdir_list(dirname):
    """获取目录下所有子目录名
    @param dirname: str 目录的完整路径
    @return: list(str) 所有子目录完整路径组成的列表
    """
    return list(filter(os.path.isdir,
        map(lambda filename: os.path.join(dirname, filename),
            os.listdir(dirname))))

def file_list(dirname, ext='.csv'):
    """获取目录下所有特定后缀的文件
    @param dirname: str 目录的完整路径
    @param ext: str 后缀名, 以点号开头
    @return: list(str) 所有子文件名(不包含路径)组成的列表
    """
    return list(filter(
        lambda filename: os.path.splitext(filename)[1] == ext,
        os.listdir(dirname)))
    

outfile = open('guid.txt', 'a')                          # 以追加方式打开输出文件
for dirpath, dirs, files in os.walk(''):                # 递归遍历当前目录和所有子目录的文件和目录
    for name in files:                                   # files保存的是所有的文件名
        if os.path.splitext(name)[1] == '.png' or os.path.splitext(name)[1]=='.jpg' :        
            filename = os.path.join(dirpath, name)+'\n'      # 加上路径，dirpath是遍历时文件对应的路径
            #f = open(filename, 'r')
            #guid = f.readlines()[1].split(': ')[1]       # 获取文件第二行以': '分割的后者
            outfile.write(filename)                          # 写入输出文件
            #f.close()    
outfile.close()