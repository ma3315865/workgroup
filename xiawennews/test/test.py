# coding = utf-8
import os
import multiprocessing


def copy(que, file_name, old_folder_name, new_folder_name):
    with open(os.path.join(old_folder_name, file_name), "rb") as old_f:
        context = old_f.read()
        old_f.close()
    with open(os.path.join(new_folder_name, file_name), "wb") as new_f:
        new_f.write(context)
        new_f.close()
    que.put(file_name)


def main():
    que = multiprocessing.Manager().Queue()
    path = os.path.abspath("..")
    root = os.path.abspath(os.path.join(path, ".."))
    old_folder_name = os.path.join(root, "test")
    new_folder_name = os.path.join(root, "test2")
    try:
        os.mkdir(new_folder_name)
    except:
        pass
    po = multiprocessing.Pool(5)
    for file_name in os.listdir(old_folder_name):
        po.apply_async(copy, (que, file_name, old_folder_name, new_folder_name))
    po.close()
    flag = 0
    file_num = len(os.listdir(old_folder_name))
    while True:
        que.get()
        flag += 1
        print("\r当前进度为 %.2f %%" % (flag / file_num * 100), end="")
        if flag >= file_num:
            break


if __name__ == "__main__":
    main()
