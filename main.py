import numpy as np
import matplotlib.pyplot as plt

num_bins = 1000

def part1(display=True):
    # Part 1 ---------------------------------------------------------------
    part1_mean = 0.0
    part1_std_dev = 1.0
    part1_N = 10000
    part1_samples = np.random.default_rng().normal(part1_mean, part1_std_dev, part1_N)
    part1_means = [sum(part1_samples[0:i])/(i+1) for i in range (0,10000)]
    
    if display:
        plt.hist(part1_samples, num_bins, density=True)
        plt.title('Normal Distribution Samples')
        plt.xlabel('Samples')
        plt.ylabel('Relative Frequency')
        plt.show()
        
        plt.hist(part1_means, num_bins, density=True)
        plt.title('Normal Distribution Sample Means')
        plt.xlabel('Sample Means')
        plt.ylabel('Relative Frequency')
        plt.show()
    
    return part1_samples
    # ----------------------------------------------------------------------

def part2(display=True):
    # Part 2 ---------------------------------------------------------------
    lower_bound = -1.0
    upper_bound = 1.0
    uniform_N = 10000
    normal_samples = np.random.default_rng().uniform(lower_bound,upper_bound,uniform_N)
    
    part2_samples = np.tan(np.pi * normal_samples)
    part2_means = [sum(part2_samples[0:i])/(i+1) for i in range (0,10000)]

    
    part2_samples1 = part2_samples[::100]
    part2_samples2 = part2_samples[::10]
    part2_samples3 = part2_samples[::1]
    
    if display:
        plt.hist(part2_samples1, num_bins, density=True)
        plt.title('100-Sample Distribution')
        plt.xlabel('Samples')
        plt.ylabel('Relative Frequency')
        plt.show()
        
        plt.hist(part2_samples2, num_bins, density=True)
        plt.title('1000-Sample Distribution')
        plt.xlabel('Samples')
        plt.ylabel('Relative Frequency')
        plt.show()
        
        plt.hist(part2_samples3, num_bins, density=True)
        plt.title('10000-Sample Distribution')
        plt.xlabel('Samples')
        plt.ylabel('Relative Frequency')
        plt.show()
        
        plt.hist(part2_means, num_bins, density=True)
        plt.title('Part 2 Sample Means')
        plt.xlabel('Sample Means')
        plt.ylabel('Relative Frequency')
        plt.show()
    
    return part2_samples
    # ----------------------------------------------------------------------

def part3(display1=True, display2=True, display3=True):
     # Part 3 ---------------------------------------------------------------
    X_n = part1(display1)
    Y_n = part2(display2)
    
    part3_samples = X_n / Y_n
    part3_means = [sum(part3_samples[0:i])/(i+1) for i in range (0,10000)]
    part3_samples1 = part3_samples[::100]
    part3_samples2 = part3_samples[::10]
    part3_samples3 = part3_samples[::1]
    
    if display3:
        plt.hist(part3_samples1, num_bins, density=True)
        plt.title('100-Sample Cauchy Distribution')
        plt.xlabel('Samples')
        plt.ylabel('Relative Frequency')
        plt.show()
        
        plt.hist(part3_samples2, num_bins, density=True)
        plt.title('1000-Sample Cauchy Distribution')
        plt.xlabel('Samples')
        plt.ylabel('Relative Frequency')
        plt.show()
        
        plt.hist(part3_samples3, num_bins, density=True)
        plt.title('10000-Sample Cauchy Distribution')
        plt.xlabel('Samples')
        plt.ylabel('Relative Frequency')
        plt.show()
        
        plt.hist(part3_means, num_bins, density=True)
        plt.title('Cauchy Distribution Sample Means')
        plt.xlabel('Sample Means')
        plt.ylabel('Relative Frequency')
        plt.show()
    
    return part3_samples
    # ----------------------------------------------------------------------


def main():
    part3(True,True,True)
    
        
if __name__ == "__main__":
    main()