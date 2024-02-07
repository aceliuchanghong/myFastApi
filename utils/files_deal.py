# 定义一个自定义排序函数
def custom_sort(filename):
    # 如果文件名以'a'开头，给予最高优先级
    if filename.startswith('a'):
        # 返回一个元组，第一个元素确保所有以'a'开头的文件排在前面
        # 第二个元素是原始文件名，用于'a'开头的文件之间的排序
        return 0, filename
    else:
        # 对于不以'a'开头的文件，返回另一个元组，确保它们排在后面
        # 同样，第二个元素用于这些文件之间的排序
        return 1, filename
