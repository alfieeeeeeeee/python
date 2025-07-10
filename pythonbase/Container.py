# -*- coding: utf-8 -*-
# 可变类型和不可变类型在于是否发生局部修改，全局修改相当于重新赋值，所有类型都可以
# 可变类型：列表
# 不可变类型：字符串、元组、数字

tuple1 = (1, 2, 3)
# tuple1[0] = 1
tuple2 = (1, 2)
print(tuple2)

# List的append和insert

# del和pop
# 如果不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：如果要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果要在删除元素后继续使用它，就使用pop()方法。

# sort和sorted排序
# sort永久排序，sorted临时排序，且都可设置倒序

# reverse 永久反向排序

# 列表推导式
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 使用切片复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# 不可变的列表叫元组


print("hellopython")
import sys

list1 = ["alfie", "thomas", "ada", "author"]
list1.append("Mary")  # ['alfie', 'thomas', 'ada', 'author', 'Mary']
print(list1)
list1.insert(0, "john")  # ['john', 'alfie', 'thomas', 'ada', 'author', 'Mary']
print(list1)

list1 = ["alfie", "thomas", "ada", "author", "grace"]
list1.pop(0)
print(list1)  # ['thomas', 'ada', 'author']
list1.remove("ada")
print(list1)  # ['thomas', 'author']

squares1 = [i ** 3 for i in range(1, 5)]
print(f"列表推导式: {squares1}")

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

fruits = ['苹果', '香蕉', '橙子', '葡萄', '草莓']
print(f"步长为2: {fruits[::2]}")

# enumerate()函数
for index, fruit in enumerate(['苹果', '香蕉', '橙子']):
    print(f"索引 {index}: {fruit}")
print("\n")

# 去重
duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(duplicates))
print(f"原始列表: {duplicates}")
print(f"去重后: {unique}")

numbers = (1, 2, 3, 4, 5, 3, 6, 3)
print(f"原始元组: {numbers}")

count = numbers.count(3)
print(f"元素3出现的次数: {count}")

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(f"列表内存使用: {sys.getsizeof(list_data)} 字节")  # 列表内存使用: 104 字节
print(f"元组内存使用: {sys.getsizeof(tuple_data)} 字节")  # 元组内存使用: 80 字节

# zip() 将多个可迭代对象（如列表、元组、字符串等）中的元素“按位置一一配对”，返回一个可迭代的
# 对象，其中每个元素是一个元组。
names = ['张三', '李四', '王五']
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(f"使用zip合并: {combined}")

# namedtuple是 collections模块提供的工厂函数，用于生成一个“带字段名”的不可变类，
# 其实质上仍是tuple的子类，但你可以像访问对象属性一样访问元素。命名元组 - 使用collections.namedtuple创建带字段名的元组
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])  # 定义命名元组类型
person1 = Person('张三', 25, '北京')  # 创建命名元组实例
print(f"命名元组: {person1}")
print(f"访问字段: {person1.name}, {person1.age}, {person1.city}")  # 通过字段名访问

fruits = {'苹果', '香蕉', '橙子'}
print(f"原始集合: {fruits}")

# add() - 添加单个元素
fruits.add('葡萄')
print(f"add('葡萄')后: {fruits}")

# update() - 添加多个元素
fruits.update(['草莓', '蓝莓'])
print(f"update(['草莓', '蓝莓'])后: {fruits}")

# remove() - 删除指定元素，如果不存在会报错
fruits.remove('香蕉')
print(f"remove('香蕉')后: {fruits}")

# discard() - 删除指定元素，如果不存在不会报错
fruits.discard('西瓜')  # 元素不存在，不会报错
print(f"discard('西瓜')后: {fruits}")

# pop() - 随机删除并返回一个元素
popped = fruits.pop()
print(f"pop()后: {fruits}, 弹出的元素: {popped}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"集合1: {set1}")
print(f"集合2: {set2}")
# 并集 (union)
union_set = set1.union(set2)
print(f"并集: {union_set}")
print(f"使用|运算符: {set1 | set2}")

# 交集 (intersection)
intersection_set = set1.intersection(set2)
print(f"交集: {intersection_set}")
print(f"使用&运算符: {set1 & set2}")

# 差集 (difference)
difference_set = set1.difference(set2)
print(f"差集(set1 - set2): {difference_set}")
print(f"使用-运算符: {set1 - set2}")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {6, 7, 8}
print(f"集合A: {set_a}")
print(f"集合B: {set_b}")
print(f"集合C: {set_c}")

# issubset() - 判断是否为子集
print(f"A是B的子集: {set_a.issubset(set_b)}")
print(f"使用<=运算符: {set_a <= set_b}")

# issuperset() - 判断是否为超集
print(f"B是A的超集: {set_b.issuperset(set_a)}")
print(f"使用>=运算符: {set_b >= set_a}")

# isdisjoint() - 判断是否不相交
print(f"A和C不相交: {set_a.isdisjoint(set_c)}")
print(f"A和B不相交: {set_a.isdisjoint(set_b)}")

# 多个集合的运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# 多个集合的并集
union_all = set1.union(set2, set3)
print(f"三个集合的并集: {union_all}")

# 多个集合的交集
intersection_all = set1.intersection(set2, set3)
print(f"三个集合的交集: {intersection_all}")

"""
我们将__init__()方法定义成包含三个形参：self、name和age。在这个方法的定义中，形参self必不可少，
而且必须位于其他形参的前面。为何必须在方法定义中包含形参self呢？因为当Python调用这个方法来创建Dog实例时，
将自动传入实参self。每个与实例相关联的方法调用都会自动传递实参self，该实参是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
当我们创建Dog实例时，Python将调用Dog类的__init__()方法。我们将通过实参向Dog()传递名字和年龄；self则会自动传递，
因此不需要我们来传递。每当我们根据Dog类创建实例时，都只需给最后两个形参（name和age）提供值。
在__init__()方法内定义的两个变量都有前缀self（见❸）。以self为前缀的变量可供类中的所有方法使用，可以通过类的任意实例来访问。
self.name = name获取与形参name相关联的值，并将其赋给变量name，然后该变量被关联到当前创建的实例。
self.age = age的作用与此类似。像这样可通过实例访问的变量称为属性(attribute)。
"""


class Car:
    """一次模拟汽车的简单尝试"""


def __init__(self, make, model, year):
    """初始化描述汽车的属性"""
    self.make = make
    self.model = model
    self.year = year


def get_descriptive_name(self):
    """返回格式规范的描述性信息"""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# 在❶处，定义__init__()方法。与前面的Dog类中一样，这个方法的第一个形参为self。此外，这个方法还包含三个形参：make、model和year。
# __init__()方法接受这些形参的值，并将它们赋给根据这个类创建的实例的属性。在创建新的Car实例时，需要指定其制造商、型号和生产年份。


"""
在使用代码模拟实物时，你可能会发现自己给类添加了太多细节：属性和方法越来越多，文件越来越长。
在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。将大型类拆分成多个协同工作的小类，
这种方法称为组合(composition)。例如，在不断给ElectricCar类添加细节时，我们可能会发现其中包含很多专门针对汽车电池的属性和方法。
在这种情况下，可将这些属性和方法提取出来，放到一个名为Battery的类中，并将一个Battery实例作为ElectricCar类的属性：

"""


# class Car:
class Battery:
    """一次模拟电动汽车电池的简单尝试"""


def __init__(self, battery_size=40):
    """初始化电池的属性"""
    self.battery_size = battery_size


def describe_battery(self):
    """打印一条描述电池容量的消息"""
    print(f"This car has a {self.battery_size}-kWh battery.")

    class ElectricCar(Car):
        """电动汽车的独特之处"""

        def __init__(self, make, model, year):
            """
           先初始化父类的属性，再初始化电动汽车特有的属性
            """
            super().__init__(make, model, year)

    self.battery = Battery()

    my_leaf = ElectricCar('nissan', 'leaf', 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.battery.describe_battery()


"""
我们定义了一个名为Battery的新类，它没有继承任何类。
__init__()方法在self之外还有一个形参battery_size。这个形参是可选的：如果没有给它提供值，电池容量将被设置为40。
describe_battery()方法也被移到了这个类中。
在ElectricCar类中，添加一个名为self.battery的属性。
这行代码让Python创建一个新的Battery实例（因为没有指定容量，所以为默认值40），并将该实例赋给属性self.battery。
每当__init__()方法被调用时，都将执行该操作，因此现在每个ElectricCar实例都包含一个自动创建的Battery实例。
我们创建一辆电动汽车，并将其赋给变量my_leaf。在描述电池时，需要使用电动汽车的属性battery：
my_leaf.battery.describe_battery()

这行代码让Python在实例my_leaf中查找属性battery，并对存储在该属性中的Battery实例调用describe_battery()方法。
输出与你在前面看到的相同：

2024 Nissan Leaf
This car has a 40-kWh battery.
这看似做了很多额外的工作，但是现在想多详细地描述电池都可以，且不会导致ElectricCar类混乱不堪。下面再给Battery类添加一个方法，它根据电池容量报告汽车的续航里程：

"""


# class Car:
class Battery:

    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


# class ElectricCar(Car):
    # my_leaf = ElectricCar('nissan', 'leaf', 2024)
    # print(my_leaf.get_descriptive_name())
    # my_leaf.battery.describe_battery()
    # my_leaf.battery.get_range()


"""
新增的方法get_range()做了一些简单的分析：如果电池的容量为40千瓦时，就将续航里程设置为150英里；
如果容量为65千瓦时，就将续航里程设置为225英里。然后，它会报告这个值。为了使用这个方法，也需要通过汽车的属性battery来调用（见❶）
输出已经可以根据电池的容量显示对应的续航里程了：

2024 Nissan Leaf
This car has a 40-kWh battery.
This car can go about 150 miles on a full charge.
"""



"""
9.3.5 模拟实物
在模拟较复杂的事物（如电动汽车）时，需要思考一些有趣的问题。续航里程是电池的属性还是汽车的属性呢？如果只描述一辆汽车，将get_range()方法放在Battery类中也许是合适的，但如果要描述一家汽车制造商的整条产品线，也许应该将get_range()方法移到ElectricCar类中。在这种情况下，get_range()依然根据电池容量来确定续航里程，但报告的是一款汽车的续航里程。也可以这样做：仍将get_range()方法留在Battery类中，但向它传递一个参数，如car_model。此时，get_range()方法将根据电池容量和汽车型号报告续航里程。
这让你进入了程序员的另一个境界：在解决上述问题时，从较高的逻辑层面（而不是语法层面）思考。你考虑的不是Python，而是如何使用代码来表示实际事物。达到这种境界后，你会经常发现，对现实世界的建模方法没有对错之分。有些方法的效率更高，但要找出效率最高的表示法，需要一定的实践。只要代码能够像你希望的那样运行，就说明你已经做得很好了！即便发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁。要编写出高效、准确的代码，这是必经之路。
=======
# -*- coding: utf-8 -*-
# 可变类型和不可变类型在于是否发生局部修改，全局修改相当于重新赋值，所有类型都可以
# 可变类型：列表
# 不可变类型：字符串、元组、数字

tuple1 = (1, 2, 3)
# tuple1[0] = 1
tuple2 = (1, 2)
print(tuple2)

# List的append和insert

# del和pop
# 如果不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：如果要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果要在删除元素后继续使用它，就使用pop()方法。

# sort和sorted排序
# sort永久排序，sorted临时排序，且都可设置倒序

# reverse 永久反向排序

# 列表推导式
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 使用切片复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# 不可变的列表叫元组


print("hellopython")
import sys

list1 = ["alfie", "thomas", "ada", "author"]
list1.append("Mary")  # ['alfie', 'thomas', 'ada', 'author', 'Mary']
print(list1)
list1.insert(0, "john")  # ['john', 'alfie', 'thomas', 'ada', 'author', 'Mary']
print(list1)

list1 = ["alfie", "thomas", "ada", "author", "grace"]
list1.pop(0)
print(list1)  # ['thomas', 'ada', 'author']
list1.remove("ada")
print(list1)  # ['thomas', 'author']

squares1 = [i ** 3 for i in range(1, 5)]
print(f"列表推导式: {squares1}")

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

fruits = ['苹果', '香蕉', '橙子', '葡萄', '草莓']
print(f"步长为2: {fruits[::2]}")

# enumerate()函数
for index, fruit in enumerate(['苹果', '香蕉', '橙子']):
    print(f"索引 {index}: {fruit}")
print("\n")

# 去重
duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(duplicates))
print(f"原始列表: {duplicates}")
print(f"去重后: {unique}")

numbers = (1, 2, 3, 4, 5, 3, 6, 3)
print(f"原始元组: {numbers}")

count = numbers.count(3)
print(f"元素3出现的次数: {count}")

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(f"列表内存使用: {sys.getsizeof(list_data)} 字节")  # 列表内存使用: 104 字节
print(f"元组内存使用: {sys.getsizeof(tuple_data)} 字节")  # 元组内存使用: 80 字节

# zip() 将多个可迭代对象（如列表、元组、字符串等）中的元素“按位置一一配对”，返回一个可迭代的
# 对象，其中每个元素是一个元组。
names = ['张三', '李四', '王五']
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(f"使用zip合并: {combined}")

# namedtuple是 collections模块提供的工厂函数，用于生成一个“带字段名”的不可变类，
# 其实质上仍是tuple的子类，但你可以像访问对象属性一样访问元素。命名元组 - 使用collections.namedtuple创建带字段名的元组
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])  # 定义命名元组类型
person1 = Person('张三', 25, '北京')  # 创建命名元组实例
print(f"命名元组: {person1}")
print(f"访问字段: {person1.name}, {person1.age}, {person1.city}")  # 通过字段名访问

fruits = {'苹果', '香蕉', '橙子'}
print(f"原始集合: {fruits}")

# add() - 添加单个元素
fruits.add('葡萄')
print(f"add('葡萄')后: {fruits}")

# update() - 添加多个元素
fruits.update(['草莓', '蓝莓'])
print(f"update(['草莓', '蓝莓'])后: {fruits}")

# remove() - 删除指定元素，如果不存在会报错
fruits.remove('香蕉')
print(f"remove('香蕉')后: {fruits}")

# discard() - 删除指定元素，如果不存在不会报错
fruits.discard('西瓜')  # 元素不存在，不会报错
print(f"discard('西瓜')后: {fruits}")

# pop() - 随机删除并返回一个元素
popped = fruits.pop()
print(f"pop()后: {fruits}, 弹出的元素: {popped}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"集合1: {set1}")
print(f"集合2: {set2}")
# 并集 (union)
union_set = set1.union(set2)
print(f"并集: {union_set}")
print(f"使用|运算符: {set1 | set2}")

# 交集 (intersection)
intersection_set = set1.intersection(set2)
print(f"交集: {intersection_set}")
print(f"使用&运算符: {set1 & set2}")

# 差集 (difference)
difference_set = set1.difference(set2)
print(f"差集(set1 - set2): {difference_set}")
print(f"使用-运算符: {set1 - set2}")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {6, 7, 8}
print(f"集合A: {set_a}")
print(f"集合B: {set_b}")
print(f"集合C: {set_c}")

# issubset() - 判断是否为子集
print(f"A是B的子集: {set_a.issubset(set_b)}")
print(f"使用<=运算符: {set_a <= set_b}")

# issuperset() - 判断是否为超集
print(f"B是A的超集: {set_b.issuperset(set_a)}")
print(f"使用>=运算符: {set_b >= set_a}")

# isdisjoint() - 判断是否不相交
print(f"A和C不相交: {set_a.isdisjoint(set_c)}")
print(f"A和B不相交: {set_a.isdisjoint(set_b)}")

# 多个集合的运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# 多个集合的并集
union_all = set1.union(set2, set3)
print(f"三个集合的并集: {union_all}")

# 多个集合的交集
intersection_all = set1.intersection(set2, set3)
print(f"三个集合的交集: {intersection_all}")
"""

"""
我们将__init__()方法定义成包含三个形参：self、name和age。在这个方法的定义中，形参self必不可少，
而且必须位于其他形参的前面。为何必须在方法定义中包含形参self呢？因为当Python调用这个方法来创建Dog实例时，
将自动传入实参self。每个与实例相关联的方法调用都会自动传递实参self，该实参是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
当我们创建Dog实例时，Python将调用Dog类的__init__()方法。我们将通过实参向Dog()传递名字和年龄；self则会自动传递，
因此不需要我们来传递。每当我们根据Dog类创建实例时，都只需给最后两个形参（name和age）提供值。
在__init__()方法内定义的两个变量都有前缀self（见❸）。以self为前缀的变量可供类中的所有方法使用，可以通过类的任意实例来访问。
self.name = name获取与形参name相关联的值，并将其赋给变量name，然后该变量被关联到当前创建的实例。
self.age = age的作用与此类似。像这样可通过实例访问的变量称为属性(attribute)。
"""


class Car:
    """一次模拟汽车的简单尝试"""


def __init__(self, make, model, year):
    """初始化描述汽车的属性"""
    self.make = make
    self.model = model
    self.year = year


def get_descriptive_name(self):
    """返回格式规范的描述性信息"""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# 在❶处，定义__init__()方法。与前面的Dog类中一样，这个方法的第一个形参为self。此外，这个方法还包含三个形参：make、model和year。
# __init__()方法接受这些形参的值，并将它们赋给根据这个类创建的实例的属性。在创建新的Car实例时，需要指定其制造商、型号和生产年份。


"""
在使用代码模拟实物时，你可能会发现自己给类添加了太多细节：属性和方法越来越多，文件越来越长。
在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。将大型类拆分成多个协同工作的小类，
这种方法称为组合(composition)。例如，在不断给ElectricCar类添加细节时，我们可能会发现其中包含很多专门针对汽车电池的属性和方法。
在这种情况下，可将这些属性和方法提取出来，放到一个名为Battery的类中，并将一个Battery实例作为ElectricCar类的属性：

"""


# class Car:
class Battery:
    """一次模拟电动汽车电池的简单尝试"""


def __init__(self, battery_size=40):
    """初始化电池的属性"""
    self.battery_size = battery_size


def describe_battery(self):
    """打印一条描述电池容量的消息"""
    print(f"This car has a {self.battery_size}-kWh battery.")

    class ElectricCar(Car):
        """电动汽车的独特之处"""

        def __init__(self, make, model, year):
            """
           先初始化父类的属性，再初始化电动汽车特有的属性
            """
            super().__init__(make, model, year)

    self.battery = Battery()

    my_leaf = ElectricCar('nissan', 'leaf', 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.battery.describe_battery()


"""
我们定义了一个名为Battery的新类，它没有继承任何类。
__init__()方法在self之外还有一个形参battery_size。这个形参是可选的：如果没有给它提供值，电池容量将被设置为40。
describe_battery()方法也被移到了这个类中。
在ElectricCar类中，添加一个名为self.battery的属性。
这行代码让Python创建一个新的Battery实例（因为没有指定容量，所以为默认值40），并将该实例赋给属性self.battery。
每当__init__()方法被调用时，都将执行该操作，因此现在每个ElectricCar实例都包含一个自动创建的Battery实例。
我们创建一辆电动汽车，并将其赋给变量my_leaf。在描述电池时，需要使用电动汽车的属性battery：
my_leaf.battery.describe_battery()

这行代码让Python在实例my_leaf中查找属性battery，并对存储在该属性中的Battery实例调用describe_battery()方法。
输出与你在前面看到的相同：

2024 Nissan Leaf
This car has a 40-kWh battery.
这看似做了很多额外的工作，但是现在想多详细地描述电池都可以，且不会导致ElectricCar类混乱不堪。下面再给Battery类添加一个方法，它根据电池容量报告汽车的续航里程：

"""


# class Car:
class Battery:

    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    my_leaf = ElectricCar('nissan', 'leaf', 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.battery.describe_battery()
    my_leaf.battery.get_range()


"""
新增的方法get_range()做了一些简单的分析：如果电池的容量为40千瓦时，就将续航里程设置为150英里；
如果容量为65千瓦时，就将续航里程设置为225英里。然后，它会报告这个值。为了使用这个方法，也需要通过汽车的属性battery来调用（见❶）
输出已经可以根据电池的容量显示对应的续航里程了：

2024 Nissan Leaf
This car has a 40-kWh battery.
This car can go about 150 miles on a full charge.
"""



"""
9.3.5 模拟实物
在模拟较复杂的事物（如电动汽车）时，需要思考一些有趣的问题。续航里程是电池的属性还是汽车的属性呢？如果只描述一辆汽车，将get_range()方法放在Battery类中也许是合适的，但如果要描述一家汽车制造商的整条产品线，也许应该将get_range()方法移到ElectricCar类中。在这种情况下，get_range()依然根据电池容量来确定续航里程，但报告的是一款汽车的续航里程。也可以这样做：仍将get_range()方法留在Battery类中，但向它传递一个参数，如car_model。此时，get_range()方法将根据电池容量和汽车型号报告续航里程。
这让你进入了程序员的另一个境界：在解决上述问题时，从较高的逻辑层面（而不是语法层面）思考。你考虑的不是Python，而是如何使用代码来表示实际事物。达到这种境界后，你会经常发现，对现实世界的建模方法没有对错之分。有些方法的效率更高，但要找出效率最高的表示法，需要一定的实践。只要代码能够像你希望的那样运行，就说明你已经做得很好了！即便发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁。要编写出高效、准确的代码，这是必经之路。
>>>>>>> 1ee27c175f430901a0371b8efc021416cc340850
"""