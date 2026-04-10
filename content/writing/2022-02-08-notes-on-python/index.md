---
title: Cheatsheet on Python
subtitle: Some things that I'll likely forget
summary: Some things that I'll likely forget
author: Harshvardhan
date: '2022-02-08'
slug: notes-on-python
tags:
- python
cover:
  image: og.png
  hidden: true
---
# Installing Packages

The process to install package depends on the Python environment you are using.

There are two possibilities: `pip`, `conda` and within Jupyter Hub.
If you are using Anaconda (Navigator), use `conda`.
`pip` will install for all environments; `conda` will install for (activated) conda environment only.
See <a href="#python-environments">7</a> for details on Python environments.

**Generally, always use `conda` for handling environments and `pip` to install packages**.


```python
pip install <package>
```

For a specific version, you can use `pip install pandas==2.0.1`.

Here are some common pip commands that'll come in handy.
You can get the full list with `pip help`.

1.  **pip freeze** or **pip list** will give a list of all packages that are installed along with their version numbers
2.  **pip check** will list all packages that have conflicted or broken requirements
3.  **pip show numpy** will show all details of that package, including package version and location where it is installed. (**numpy** is an example, replace accordingly).

To uninstall a package, use `pip uninstall <package>`.

# Terminal in Jupyter

Terminal commands can be passed within the Jupyter notebook.
Any command starting with `!` would be run like a terminal command within the Jupyter notebook.


```python
# list all files in current directory
!ls

# delete all files in the current folder
!rm -r *
```

# Debugging in the Current State

Many a time our code crashes and we would like to investigate the environment at that moment.
Running `%debug` in Jupyter Notebook immediately after the code crashes would open a debugging environment where you can see variables' values, etc.


```python
# some code that crashed
x = some_function(y)

# in the next Jupyter cell, run this command
%debug
```

# Printing

There are two methods: `print()` and `pprint()`.
They both serve the save cause but `pprint()` is better at displaying complex data structures such as list of lists or JSON files.

It is worthwhile to mention `f`-strings.
They are usually more compact than writing full print statements.
Furthermore, if you want to print value of a variable, they're really short.


```python
# enclose the variable in curly braces
print(f"Value of x is {x}")

# if you want to just print the value of, use {x=}
print(f"{x=}")
```

# Adding Rows

It is more efficient to create a list of rows first and then convert it to a pandas data frame.
As qmeeus [said](https://stackoverflow.com/questions/55967976/python-panda-append-dataframe-in-loop?noredirect=1&lq=1) on SO,

> Pandas dataframes do not work as a list, they are much more complex data structures and appending is not really considered the best approach.


```python
data = []
for row in some_function_that_yields_data():
    data.append(row)

# either this
df = pd.DataFrame(data)

# or this
df = pd.concat([results, df], axis=0).reset_index(drop=True)
```

# Function

## Getting Help

To see details of a function in a Jupyter notebook, use `??` operator.
It will show you the body and the associated documentation (if available).


```python
??my_function()
```

## Modify Inplace

When you modify a value passed to a function, it modifies that object inplace.
For example, the following function would change the value.

# Python Environments

-   See [Managing environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) for details.
    Use `conda` for managing environments and packages.

-   Generally, avoid messing up with `base` environment.
    Create a new one and use that.

-   Once you create a new environment, remember to [refresh](https://code.visualstudio.com/docs/python/environments#:~:text=If%20you%20create%20a%20new%20conda%20environment%20while%20VS%20Code%20is%20running%2C%20use%20the%20refresh%20icon%20on%20the%20top%20right%20of%20the%20Python%3A%20Select%20Interpreter%20window%3B%20otherwise%20you%20may%20not%20see%20the%20environment%20there.) Visual Studio Code's list of Python interpreters.

## List all environments


```zsh
conda env list
```

Here is how it looks for me.


```python
(base) harshvardhan@harshmac17 ~ % conda env list
# conda environments:
#
base                  *  /Users/harshvardhan/opt/anaconda3
env_oct22                /Users/harshvardhan/opt/anaconda3/envs/env_oct22
```

## Create an environment

This will create an environment called `new_env`.


```python
conda create --name new_env
```

Conda will ask you for permission `proceed ([y]/n)?`.
Type `y`.

## Activate an environment

This will activate the environment called `new_env`.
Remember that you can list all environment with `conda env list`.


```python
conda activate new_env
```

> **VS Code Note:** By default, the Python extension looks for and uses the first Python interpreter it finds in the system path.
> To select a specific environment, use the **Python: Select Interpreter** command from the **Command Palette** (⇧⌘P).

## Clone an environment

This will create a new environment `new_env` with the exact same packages as `old_env`.


```python
conda create --clone old_env --name new_env
```

## Remove an environment

This will remove a Python environment called `old_env`.


```python
conda env remove --name old_env
```

## List all packages

This will list all packages in the current environment.


```python
conda list
```

## Update all packages

This will update all packages in the **activated** Python environment.
See above to list environments and select an environment.
Once you are in the activated environment, execute the following.


```python
conda update --all
```

## Using `pip` in Conda

**This is not recommended.** If you are feeling adventurous, give it a try!
See [Using pip in an environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#using-pip-in-an-environment).
Also see a note on [dependency conflicts](https://stackoverflow.com/a/44072944/8057777).
