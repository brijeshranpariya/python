import importlib


def explore_module_attributes():
    module_name = input("Enter module name to explore: ")
    try:
        module = importlib.import_module(module_name)
        print(f"Available Attributes in {module_name} module: {dir(module)}")
    except ModuleNotFoundError as e:
        print(f"{module_name} does not found! Please enter valid module name.")
