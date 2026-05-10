import numpy as np
#1.宣告二個列表 list1 內容為1,2,3,4 list 內容為 5,6,7,8
list1 = [1,2,3,4]
list2 = [5,6,7,8]
#2.宣告 list3為 list1+list2
list3 = list1 + list2
#3.宣告 list4 為 list2*3
list4 = list2 * 3
#4.以fstring印出list3與list4的結果
print(f'list1={list1}\nlist2={list2}\nlist3={list3}\nlist4={list4}')
print("="*30)
#5.利用np.array將list1與list2轉換為ndarray
#5.名稱分別為 nd1,nd2
nd1 = np.array(list1)
nd2 = np.array(list2)
#6.宣告 nd3 為 nd1+nd2
nd3 = nd1 + nd2
#7.宣告 nd4 為 nd2*3
nd4 = nd2 * 3
#8.以fstring印出nd3與nd4的結果
print(f'nd3={nd3}\nnd4={nd4}')
