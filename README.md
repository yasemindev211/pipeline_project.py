# Python Pipeline Project

## Description
This project demonstrates a **data processing pipeline** in Python.  
It showcases several Python concepts including:

- Nested functions  
- Function factories  
- Functions as parameters  
- Decorators (for logging)  
- Iterators  
- Generators  

The pipeline processes a list of numbers by:

1. Filtering even numbers  
2. Squaring them (or applying other transformations)  
3. Logging each operation  
4. Outputting results using both an **iterator** and a **generator**

---

## Features
- **Filter Factory:** Generates functions to filter even or odd numbers  
- **Pipeline Builder:** Combines filtering and transformation functions  
- **Logging Decorator:** Tracks the start and end of each transformation function  
- **Iterator:** Iterates over processed data  
- **Generator:** Yields processed data one by one for memory efficiency  

---

## Example Usage

```python
data = [1, 2, 3, 4, 5, 6]

# Create filter function
filter_func = filter_factory("even")

# Build pipeline
pipeline = pipeline_builder(filter_func, square)

# Run pipeline
result = pipeline(data)
print("Pipeline result:", result)  # [4, 16, 36]

# Iterator
iterator = MyIterator(result)
for item in iterator:
    print(item)

# Generator
gen = data_generator(result)
for item in gen:
    print(item)
