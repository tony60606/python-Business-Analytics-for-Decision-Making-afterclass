import numpy as np
#1.建立一維陣列
np1 = np.array([1,3,5,7,9])
#2.建立二維陣列,含int ,float ,str
np2 = np.array([[2,4,6,8,10],[2.2,4.4,6.6,8.8,10.1],['2','4','6','8','10']])
#3.印出一維陣列內容,形狀,資料型態
print(f'np1={np1}')
print(f'shape={np1.shape}')
print(f'dtype={np1.dtype}')
print("="*30)
#4.印出二維陣列內容,形狀,資料型態
print(f'np2={np2}')
print(f'shape2={np2.shape}')
print(f'dtype2={np2.dtype}')


#5.向量化運算,對每個元素同時操作,將陣列1*2+1
print(np1*2+1)
#廣播,不同形狀的陣列自動對齊
#6.宣告 price為ndarry,內容為100,200,300
price = np.array([100,200,300])
#7.宣告 discount=0.1 #純量會自動擴展為[0.1,0.1,0.1]
discount = 0.1
#8.宣告final為 price*(1-discount)
final = price * (1-discount)
#9.印出final內容
print(f'final={final}')
price2 = np.array([[100,200,300],[300,500,700],[1000,2000,30000],[15000,35000,50000]])
final2 = price2 * (1-discount)
print(f'final2={final2}')

#常用統計函式
data=np.array([120,350,280,95,410])
#10.印出平均值
print(np.mean(data))
#11.印出中位數
print(np.median(data))

#12.印出標準差
print(np.std(data))

#13.印出總和
print(np.sum(data))

#14.印出最大值
print(np.max(data))

#15.印出最小值
print(np.min(data))


#布林索引
#16.印出大於200元素
print(f'大於200的值={data[data>200]}')
#17.計算大於200的元素總和為
print(f'大於200的值和={data[data>200].sum()}')
#18.計算大於200的元素數目為
print(f'大於200的值和={(data>200).sum()}')

#19.將大於200的元素,值改為0
data[data>200]=0
print(data)