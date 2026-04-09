# 1️ Decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} çalışıyor...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} tamamlandı\n")
        return result
    return wrapper

# 2️ Fonksiyon parametre olarak gönderme
def apply_operation(data, func):
    return [func(x) for x in data]

# 3️ Fonksiyon döndüren factory
def filter_factory(type):
    def even(x):
        return x % 2 == 0

    def odd(x):
        return x % 2 != 0
    
    return even if type == "even" else odd

# 4️ Pipeline builder
def pipeline_builder(filter_func, transform_func):
    def pipeline(data):
        filtered = [x for x in data if filter_func(x)]
        transformed = [transform_func(x) for x in filtered]
        return transformed
    return pipeline

# 5️ Iterator sınıfı
class MyIterator:
    def __init__(self, data):
        self.data = data 
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            val = self.data[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

# 6️ Generator fonksiyonu (sınıf dışında)
def data_generator(data):
    for item in data:
        yield item

# 7️ Transform fonksiyonu (decorator ile)
@log_decorator
def square(x):
    return x*x

#  MAIN
data = [1,2,3,4,5,6]

# factory ile filter oluştur
filter_func = filter_factory("even")

# pipeline oluştur
pipeline = pipeline_builder(filter_func, square)

# pipeline çalıştır
result = pipeline(data)
print("Pipeline sonucu:", result)

# Iterator ile
print("\nIterator ile:")
iterator = MyIterator(result)
for item in iterator:
    print(item)

# Generator ile
print("\nGenerator ile:")
gen = data_generator(result)
for item in gen:
    print(item)