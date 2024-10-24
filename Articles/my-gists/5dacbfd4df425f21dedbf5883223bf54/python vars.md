# Python vars, dir, __dict__ について

Pythonのプログラミングにおいて、オブジェクトの属性やメソッドにアクセスし、操作する際に便利なビルトイン関数と属性があります。それぞれの概要を以下に示します。

## `vars` 関数

`vars`関数は、オブジェクトの`__dict__`属性を返すためのビルトイン関数です。`__dict__`属性はオブジェクトの属性と値を格納する辞書です。例えば：

```python
class Example:
    def __init__(self):
        self.x = 10
        self.y = 20

obj = Example()
print(vars(obj))  # {'x': 10, 'y': 20}
```

## dir

Pythonのdir関数は、指定したオブジェクトの属性とメソッドをリストとして返すビルトイン関数です。引数を指定しない場合、現在のスコープの属性とメソッドをリストアップします。
```
print(dir(obj))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'x', 'y']
```
## dict 属性

__dict__属性は、Pythonクラスのインスタンスの属性とその値を格納する辞書です。この属性を直接操作することで、オブジェクトの属性を追加、削除、または変更できます。

```
class Example:
    def __init__(self):
        self.x = 10
        self.y = 20

obj = Example()
print(obj.__dict__)  # {'x': 10, 'y': 20}

```

- https://docs.python.org/3/library/functions.html#vars
- https://docs.python.org/3/library/functions.html#dir
- https://docs.python.org/3/reference/datamodel.html#object.__dict__
