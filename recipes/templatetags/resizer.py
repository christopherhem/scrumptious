from django import template

register = template.Library()


@register.filter()
def resize_to(ingredient, target):
    servings = int(ingredient.recipe.servings)
    if servings != None and target != None:
        user = int(target)
        ratio = user / servings
        return ratio * servings
    return ingredient


register.filter(resize_to)


# Get the number of servings from the ingredient's
# recipe using the ingredient.recipe.servings
# properties

# If the servings from the recipe is not None
#   and the value of target is not None
# try
# calculate the ratio of target over
#   servings
# return the ratio multiplied by the
#   ingredient's amount
# catch a possible error
# pass
# return the original ingredient's amount since
#   nothing else worked
