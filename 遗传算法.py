'''
在一个长度为n的数组nums中选择10个元素，使得10个元素的和原数组的所有的元素之和的1/10无限接近
如n=50，sun(nms)=1000,选择的元素列表answer要满足|sum(answer)-100|<e,e尽可能小
'''
##遗传算法实例
import random

'''
1.创建随机解集
创建包含100个解的初始解集
def create_answer()
random库
random.sample(list,number)
在list中随机抽取 number个元素
'''

def create_answer(numbers_set,n):
	#创建列表，返回n次遍历
	result = []
	for i in range(n):
		#随机抽取n个遍历
		result.append(random.sample(numbers_set,10))
	return result

def error_level(new_answer,numbers_set):
	error=[]
	#计算正确答案，原始和的十分之一
	right_answer = sum(numbers_set)/10
	#对每个解进行计算误差
	for item in new_answer:
		value = abs(right_answer - sum(item))
		#如果误差等于0
		if value == 0:
		#让误差加上10，否则的话用1/误差
			error.append(10)
		else:
			error.append(1/value)
	return error




#选择并且交换解的部分完成了
def choice_selected(old_answer,numbers_set):
	result = []
	#计算误差系数
	error = error_level(old_answer,numbers_set)
	#误差进行归一化，等于列表元素除以总体元素和，
	error_one = [item/sum(error) for item in error]
	#然后进行叠加法
	for i in range(1,len(error_one)):
		error_one[i]+=error_one[i-1]
		#每次会产生两个不同的解，独立的父体和母体，因此还需要循环
	for i in range(len(old_answer)//2):
		temp = []
		for j in range(2):
			#每次产生一个随机浮点数
			rand = random.uniform(0,1)
			#然后对error_one进行循环保存
			for k in range(len(error_one)):
				#如果随机数等于0或者小于error_one[k]，temp增加一个父体和母体old_answer[k]
				if k==0:
					if rand < error_one[k]:
						temp.append(old_answer[k])
				else:
						##如果随机数等于0或者大于或者等于error_one[k]，temp增加一个父体和母体old_answer[k]
					if rand>=error_one[k-1] and rand < error_one[k]:
							temp.append(old_answer[k])
						
		rand = random.randint(0,6)
		#二进制的片段
		temp_1=temp[0][:rand]+temp[1][rand:rand+3]+temp[0][rand+3:]
        temp_2=temp[1][:rand]+temp[0][rand:rand+3]+temp[1][rand+3:]
		#将最终解集增加上这两个解
 		result.append(temp_1)
        result.append(temp_2)
    return result


#选择信息变异，概率变异，解决某元素随机替换
def variation(old_answer,numbers_set,pro):
	#选择一个变异pro，进行变异
	for i in range(len(old_answer)):
		#随机产生0-1的浮点数
		rand = random.uniform(0,1)
		#如果浮点数小于pro,就发生变异
		if rand < pro:
			#在解中随机选取0-9的数
			rand_num = random.randint(0,9)
			#变异的信息就为这个随机值，下标为O到9，这个信息会产生变异，其他的保持不变，等于本身部分+变异部分
			old_answer[i] = old_answer[i][:rand_num] + random.sample(numbers_set,1)+old_answer[i][rand_num+ 1:]

	return old_answer
#随机抽取50个解
numbers_set = random.sample(range(0,1000),50)
#创建解集这个最初的解
middle_answer = create_answer(numbers_set,100)
# print(middle_answer) #[[22, 870, 296, 676, 424, 4, 167, 474, 86, 703]]
#定义一个原始解
first_answer = middle_answer[0]
great_answer=[]
for i in range(1000):
	middle_answer = choice_selected(middle_answer,numbers_set)
	middle_answer = variation(middle_answer,numbers_set,0.1)
	#选择误差大的
	error = error_level(middle_answer,numbers_set)
	index = error.index(max(error))
	#增加解和系数
	great_answer.append([middle_answer[index],error[index]])
	#信息打印，看下学习效果
	#先将great_answer进行排序，排序的规则是系数，然后是系数的大小，从大到小排序，误差越小，选择概率越大
great_answer.sort(key = lambda x:x[1],reverse = True)
print("正确答案为",sum(numbers_set)/10)
print("给出的最优解为",great_answer[0][0])
print("该和为",sum(great_answer[0][0]))
print("选择系数为",great_answer[0][1])
#原始解和最优秀解的差距
print("最初解的和为",sum(first_answer))


'''
正确答案为 2604.7
给出的最优解为 [407, 923, 407, 144, 32, 98, 315, 82, 167, 32]
该和为 2607
选择系数为 0.4347826086956178
最初解的和为 6270
[Finished in 1.6s]
'''














