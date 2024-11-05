import matplotlib.pyplot as plt
import statistics

CRIM_values = []
RM_values = []
MEDV_values = []
LSTAT_values = []

with open('Boston-Housing.txt', 'r') as file:
    for line in file:
        values = line.split() 

        CRIM_values.append(float(values[0])) 
        RM_values.append(float(values[5]))  
        LSTAT_values.append(float(values[12]))
        MEDV_values.append(float(values[13])) 
        
plt.figure(figsize=(18,5))

# 1. Histogram 
plt.subplot(1, 3, 1)
plt.hist(CRIM_values, bins=20)
plt.title('Histogram of CRIM')
plt.xlabel('Per Capita Crime Rate')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(RM_values, bins=20)
plt.title('Histogram of RM')
plt.xlabel('Average Number of Rooms')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(MEDV_values, bins=20)
plt.title('Histogram of MEDV')
plt.xlabel('Median Value of Homes ($1000\'s)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('Boston_Housing_Histograms.png')
plt.show()

# 2. Scatter plots 
plt.subplot(1,3,1)
plt.scatter(CRIM_values, MEDV_values) 
plt.title('MEDV vs. DRIM')
plt.xlabel('CRIM')
plt.ylabel('MEDV')

plt.subplot(1,3,2)
plt.scatter(RM_values, MEDV_values)
plt.title('MEDV vs. LSTAT')
plt.xlabel('% LSTAT')
plt.ylabel('MEDV')

plt.tight_layout()
plt.savefig('Boston_Housing_ScatterPlots.png')
plt.show()


# 3. Minimum and Maximum MEDV of a house 
min_MEDV_index = MEDV_values.index(min(MEDV_values))
max_MEDV_index = MEDV_values.index(max(MEDV_values))

min_MEDV = MEDV_values[min_MEDV_index]
max_MEDV = MEDV_values[max_MEDV_index]

corresponding_CRIM_min = CRIM_values[min_MEDV_index]
corresponding_RM_min = RM_values[min_MEDV_index]

corresponding_CRIM_max = CRIM_values[max_MEDV_index]
corresponding_RM_max = RM_values[max_MEDV_index]

print(f'Minimum MEDV: {min_MEDV}, CRIM: {corresponding_CRIM_min}, RM: {corresponding_RM_min}')
print(f'Maximum MEDV: {max_MEDV}, CRIM: {corresponding_CRIM_max}, RM: {corresponding_RM_max}')

# 4. Compute median and standard deviation of MEDV and CRIM 
median_MEDV = statistics.median(MEDV_values)
median_CRIM = statistics.median(CRIM_values)

std_dev_MEDV = statistics.stdev(MEDV_values)
std_dev_CRIM = statistics.stdev(CRIM_values)

print(f'Median of MEDV: {median_MEDV}, Standard Deviation of MEDV: {std_dev_MEDV}')
print(f'Median of CRIM: {median_CRIM}, Standard Deviation of CRIM: {std_dev_CRIM}')