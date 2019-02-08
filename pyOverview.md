# Self Study Overview

## Data Types

### Strings
```python
>>> print("I am a string.")
I am a string.
>>> type("I am a string.")
<class 'str'>

>>> print('I am too.')
I am too.
>>> type('I am too.')
<class 'str'>

>>> print("This string contains a single quote (') character.")
This string contains a single quote (') character.

>>> print('This string contains a double quote (") character.')
This string contains a double quote (") character.
```
### Collection Types

There are four data collection types in Python -- Lists, Tuples, Sets, and Dictionaries.

| Type       | Structure | Immutability | Duplicates         | 
|------------|-----------|--------------|--------------------|
| List       | Ordered   | Changeable   | Duplicates Allowed |
| Tuple      | Ordered   | Unchangeable | Duplicates Allowed | 
| Set        | Unordered | Add Only     | No Duplicates      | 
| Dictionary | Unordered | Changeable   | Duplicates Allowed | 

We will be focusing on ``Lists`` and ``Dictionaries`` for this exercise.

#### Lists
```python
>>> thislist = ["apple", "banana", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']

>>> print(thislist[1])
banana
```

#### Dictionaries
```python
>>> thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

>>> x = thisdict["model"]
>>> print(x)
Mustang
```

## Functions

A function is a block of code which runs _when it is called_. Data can be passed into a function in the form of ``parameters``. A function can then perform some task or ``return`` some data. Define a function with the ``def`` keyword.

```python
>>> def HelloWorld():
...   print('Hello World!')
... 
>>> HelloWorld
<function HelloWorld at 0x103bd48c8>
>>> HelloWorld()
Hello World!
>>> def HelloPerson(person):
...   print('Hello ' + person + '!')
... 
>>> HelloPerson('kevin')
Hello kevin!
>>> def HelloMoon(moon):
...   x = 'Hello ' + moon + '!'
...   return x
... 
>>> y = HelloMoon('ganymede')
>>> print(y)
Hello ganymede!
```

## Modules

Think of a module as a code library -- a file containing a set of functions you'd like to use in your application.

```python
>>> import platform
>>> # Check what functions are available in this module
>>> dir(platform)
['DEV_NULL', '_UNIXCONFDIR', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture', '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_parse_release_file', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_release_filename', '_release_version', '_supported_dists', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'warnings', 'win32_ver']
>>> x = platform.system()
>>> print(x)
Darwin
```

