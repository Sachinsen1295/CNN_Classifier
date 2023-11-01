# CNN Classifier Project

## Create Template.py to create one shot skeleton of project

```
python template.py
```

## Shell script

```
bash init_setup.sh
```

### Setup.py + Pyproject.toml to install as package to publish

## Pyproject.toml

```
[build-system]
requires = ['setuptools>=42.0', "wheel"] 
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
testpaths = [
    "tests" #to Test and Test folder is in codes
    ]  

[tool.mypy]
mypy_path = "src"
ignore_missing_imports = true
```

