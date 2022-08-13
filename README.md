# timeti
Serialize elapsed time of functions, loops and code blocks.

![test](https://github.com/kephircheek/elapsed-time-logger/actions/workflows/main.yml/badge.svg)
[![license: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


### Experience

### Install 
```
pip install timeti
```

### Usage
- Profile function with decorator
  ```python
  >>> @timeti.profiler
  ... def ultimative_question(*args, **kwargs):
  ...     sum(range(100_000))
  ... 
  >>> ultimative_question()
  Elapsed time of 'ultimative_question' function: 4 ms
  ```

- Profile loop with wrap
  ```python
  >>> for i in timeti.profiler(range(2)):
  ...     _ = sum(range(100_000))
  ... 
  Elapsed time of loop iteration 0: 4 ms
  Elapsed time of loop iteration 1: 3 ms
  Elapsed time of loop: 8 ms
  ```

- Profile code blocks with context manager 
  ```python
  >>> with timeti.profiler():
  ...     _ = sum(range(100_000))
  ... 
  Elapsed time of block: 5 ms
  ```


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
