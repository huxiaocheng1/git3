 
def bubblt_sort(items):
    """冒泡排序"""
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
               


def main():
    """主函数"""
    items = [35, 12, 99, 78, 65, 47, 52, 80]
    bubblt_sort(items)
    print(items)


if __name__ == '__main__':
    main() 


# gitee.com/jackfrued