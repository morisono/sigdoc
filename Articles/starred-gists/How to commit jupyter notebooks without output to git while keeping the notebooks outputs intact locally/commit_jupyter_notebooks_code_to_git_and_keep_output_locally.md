### Commit jupyter notebooks code to git and keep output locally  

1. Add a filter to git config by running the following command in bash inside the repo:  
```
git config filter.strip-notebook-output.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR'  
```
2. Create a `.gitattributes` file inside the directory with the notebooks  

3. Add the following to that file:   
```
*.ipynb filter=strip-notebook-output  
```

After that, commit to git as usual. The notebook output will be stripped out in git commits, but it will remain unchanged locally.  

[Source: StackOverflow](https://stackoverflow.com/a/58004619/3861922)  


### How to override the above for a specific notebook  
This is useful if you sometimes want to add specific notebooks with their cell outputs intact to git, while still having the default behavior of clearing out cells.  

1. When adding to git a notebook whose cell outputs you want to keep, instead of the usual `git add <path to your notebook>`  command, use this: `git -c filter.strip-notebook-output.clean= add <path to your notebook>`  

[Source: StackOverflow](https://stackoverflow.com/a/78475631/3861922)  
