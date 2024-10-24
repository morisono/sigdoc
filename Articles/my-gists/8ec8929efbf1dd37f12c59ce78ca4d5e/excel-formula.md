# Excel 有用な関数と式

- A-ZZを左から右に参照する式

```excel
=SUBSTITUTE(ADDRESS(1,COLUMN(A1),4),1,)
```



- A-ZZを上から下に参照する式

```excel
=SUBSTITUTE(ADDRESS(1,ROW(A1),4),1,)
```



- 現在の列名を取得する式

```excel
=SUBSTITUTE(ADDRESS(1,COLUMN(),4),1,)
```



