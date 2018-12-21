实验楼第二周



### 数据集成方法

##### 键合并数据 

[pandas.DataFrame.merge()](http://pandas.pydata.org/pandas-docs/version/0.16.2/generated/pandas.DataFrame.merge.html):通过一个或多个键将DataFrame链接起来。

##### 索引合并数据：按照索引进行合并，更好的保留了索引的序号

[pandas.DataFrame.join](http://pandas.pydata.org/pandas-docs/version/0.16.2/generated/pandas.DataFrame.join.html)

##### 轴堆叠数据：按照指定的轴对不同的DataFrame进行链接，

[pandas.concat](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html)

###数据映射：

###map



```python
name_to_gender = {'amy': 'girl', 'david': 'boy', 'jam': 'boy'}  # 建立映射字典

df['gender'] = df['name'].map(name_to_gender)

df

```

##### cut

[pandas.cut](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.cut.html)

### 分组聚合：分组后在执行求和，平均等运算

[pandas.DataFrame.groupby](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html)

