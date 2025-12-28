def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return 'Pls go away and stop eating my sheep'
    else:
        return f"Oi! Sheep number {len(queue) - queue.index('wolf') - 1}! You are about to be eaten by a wolf!"

print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))
# Oi! Sheep number 2! You are about to be eaten by a wolf!