def distinct_averages(species_populations):
    averages = set()
    species_populations.sort()
    left = 0
    right = len(species_populations) - 1
    while(left < right):
        averages.add((species_populations[left] + species_populations[right]) / 2)
        left += 1
        right -= 1

    return len(averages)

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 