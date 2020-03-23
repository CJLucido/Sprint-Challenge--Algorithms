# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

#I don't know how to minimize the number of eggs dropped, but I can try to see how many floors will break eggs vs how many won't
#also, if we are at the top floor then wouldn't the floor f-1 always be the best floor for our eggs???

#we have plenty of eggs so
eggs = []

def minimize_broken_eggs(n_story_building, eggs):

#if egg gets thrown off floor f or higher, then egg breaks
#we have to check every floor in the building

for f in n_story_building:
#capture the amount of broken eggs (in an array) from the floor and all the floors above it
broken_eggs = n_story_building - f + 1 #plus 1 for the floor that we are on
eggs.append(broken_eggs)

      #now that we have a list of the severity of broken eggs by index we can find the floor by finding the one with the lowest number, retrieving it's index and then adding 1 (since the array is zero indexed)

      #we can make a copy of the array first so that we keep the original indices intact

      ordered_severity_eggs = eggs.copy()
      ordered_severity_eggs.sort()
      minimal_broken_eggs = ordered_severity_eggs[0]

floor = eggs.index(minimal_broken_eggs) + 1

#we are solving for f
return floor
