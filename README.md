# timeti
Serialize elapsed time of functions, loops and code blocks.

![test](https://github.com/kephircheek/elapsed-time-logger/actions/workflows/main.yml/badge.svg)
[![license: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Development

### Install 
```
pip install -e ".[dev]"
```

### Run linters

- Run [black](https://github.com/psf/black) - code formatter
  ```
  python -m black .
  ```

- Run [mypy](http://mypy-lang.org/) - static type checker
  ```
  python -m mypy .
  ```

- Run [isort](https://pycqa.github.io/isort/) - library to sort imports alphabetically
  ```
  python -m isort .
  ```
  

### Run tests  

- Run tests   
  ```  
  python -m unittest discover -s tests  
  ```  

- Run doctests for clock face  
  ```  
  python -m doctest -v timeti/clockface.py  
  ```  
