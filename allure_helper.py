import allure

def apply_allure_metadata(data):
    def decorator(func):
        @allure.title(data['title'])
        @allure.description(data['description'])
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator