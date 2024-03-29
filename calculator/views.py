from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_servings(recipe, servings):
    recipe_new = {k: v * servings for k, v in recipe.items()}
    return recipe_new


def omlet_view(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA['omlet']
    recipe_serv = recipe_servings(recipe, servings)
    context = {
        'recipe': recipe_serv,
    }
    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA['pasta']
    recipe_serv = recipe_servings(recipe, servings)
    context = {
        'recipe': recipe_serv,
    }
    return render(request, 'calculator/index.html', context)


def butter_view(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA['butter']
    recipe_serv = recipe_servings(recipe, servings)
    context = {
        'recipe': recipe_serv,
    }
    return render(request, 'calculator/index.html', context)
