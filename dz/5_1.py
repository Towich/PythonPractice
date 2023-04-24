import inspect
import importlib

def generate_documentation(module_name):
    module = importlib.import_module(module_name)#берем
    module_doc = inspect.getdoc(module) #информация
    module_title = f'Markdown\n# Модуль {module_name}\n\n{module_doc}\n\n' #заголовок
    class_docs = []

    for name, obj in inspect.getmembers(module, inspect.isclass): #берем информацию
        class_doc = inspect.getdoc(obj)
        class_title = f'## Класс {name}\n\n{class_doc}\n'
        method_docs = []

        for method_name, method_obj in inspect.getmembers(obj, inspect.isfunction): #для методов

            if method_name.startswith('__') and method_name.endswith('__'): #пропускаем невкусные методы
                continue

            method_doc = inspect.getdoc(method_obj)
            signature = inspect.signature(method_obj) #сигнатура - слово та какое забавное
            signature_str = str(signature)

            method_str = f'* **Метод** `{method_name}{signature_str}`\n{method_doc}\n'

            method_docs.append(method_str)


        class_str = class_title + '\n'.join(method_docs) + '\n'#создаем строку
        class_docs.append(class_str)

    function_docs = []

    for name, obj in inspect.getmembers(module, inspect.isfunction):
        function_doc = inspect.getdoc(obj)
        signature = inspect.signature(obj)
        signature_str = str(signature)

        function_str = f'## Функция {name}\n\nСигнатура: `{name}{signature_str}`\n\n{function_doc}\n'
        function_docs.append(function_str)

    docs_str = module_title + '\n'.join(class_docs) + '\n'.join(function_docs)

    return docs_str

print(generate_documentation("mymodule"))