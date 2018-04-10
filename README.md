## wxPython 从入门到放肆

pass
e61 获取鼠标位置较pdf有改动

```python
event.GetPositionTuple()
```

改为
```python
(x,y) = (event.GetX(), event.GetY())
newPos = (x,y)
```

因为，貌似现在没有GetPositionTuple这个函数了

# issues

1. wxPython.png 图片不能正确显示
2. part1 chapter2 toolbar.py 里images不能用
3. e35 运行后报错


wxPython in Action [pdf](http://docs.autolook.top/pdf/python/wxPython%E5%AE%9E%E6%88%98%28%E4%B8%AD%E6%96%87%E7%89%88%EF%BC%89.pdf)
