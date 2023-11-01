# CNN Classifier Project

## Workflow
#### 1.reserach/trils 
#### 2.config.yaml 
#### 3.entity 
#### 4.component 
#### 5.pipeline 
#### 6.training 
#### 7.predeiction 
#### 8.test your package 
#### 9.dvc for the reprodcuing the pipeline




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

