#!/usr/bin/python
'''
I wanted to keep this in here.  My self-talk about this problem.

If there are no recipes, we can still make something.  But then why 
would there be no recipes?  Dumb thought.  It's more likely 
that we could have the recipes but no ingredients.  
Also, if we run out of ingredients, we'd have to stop. 
So maybe if there are no ingredients that should be a condition.  

OK, so if we're trying to figure out how
many batches we can make, we can only run them until the
ingredients run out.  This sounds like a while loop.  "While
the ingredients are greater than 0...make something"

OK...just re-read the instructions.  I have to count how many
batches were made.  I need some sort of count.  Just inserted count
to the solution.

So now I have this condition for ingredients, a count, and a while
loop.  I'm going to have to iterate through these ingredients. 
A 'for' loop sounds like something to use. Besides, aren't we
always using a for loop? I don't know what to put in the 
for loop though.

Re-read the instructions and saw this: 
The keys will be the ingredient names, with their 
associated values being the amounts.  
Takeaway -- This will need amounts but I don't know where.

I need to figure out how to work with the amounts.
Thirty minutes later and I'm still looking at this statement
about amounts.  Christ ass.

***I need to make a connection between the ingredient items and the
the recipe items.***  This has to impact the amounts in some way.

Maybe if I loop through the recipes and follow each item
and the amount of the item that is used.

Great, so now I'm looping through the recipe items, counting
the items and amounts.  I need to pick up the ingredient items 
though. Hmm...if the items are in ingredients.

So if I'm picking up the recipe items and the ingredient items,
I'll need to subtract the ingredients as they are used by the
recipe. But, what if there are not enough ingredients on a pass?
If it is, then I'll have to return whatever count I have.  If not, then
I need to subtract the ingredients from the recipe and update the
ingredients.

I'm walking through the ingredients and I've reached the point to 
where I don't have any ingredients left and it returns the count.
Fine, but then what?

OK, what if it spins through the process and there are no
recipe items in the ingredients?  I think I'm losing my mind.
'''


import math

def recipe_batches(recipe, ingredients):
    
    if len(ingredients) == 0:
        return 0
        
    count = 0
    
    while len(ingredients) > 0:
        for item, amount in recipe.items():
            if item in ingredients:
                # i did have this at <= 0, still no difference
                if ingredients[item] - recipe[item] < 0:
                    return count

                else:
                    ingredients[item] = ingredients[item] - recipe[item]
                    # count = count + 1  worked with test below, but not attached test
            
            #what if item isn't in ingredients? return 0?
            else:
                return 0

        count = count + 1
        
    return count


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))