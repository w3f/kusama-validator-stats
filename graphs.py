import matplotlib.pyplot as plt

def isolateStake(line):
    tokens = line.split()
    return float(tokens[2])



def read_in_file(file_name):
    with open(file_name) as f:
        for line in f:
            if line.startswith('\tTotal stake:'):
                stake = isolateStake(line)
                stakes.append(stake)
  

stakes = []

def main():
    file_to_read = str(input("Enter the name of the input file(eg. polkadot_out.txt): "))
    number_of_bars = int(input("Enter the number of bars in the graph: "))
    file_name = str(input("Enter an output file name(eg. validator_graph.png): "))
    read_in_file(file_to_read)
    stakes.sort()
    min_stake = stakes[0]
    max_stake = stakes[len(stakes)-1]
    diff = (max_stake - min_stake)
    bucket_size = (diff / number_of_bars)
    counts = []
    for i in range(0, number_of_bars):
        counts.append(0)

    for stake in stakes:
        for i in range(0, number_of_bars):
            if stake <= min_stake + (bucket_size * (i+1)):
                counts[i] += 1
                break
    print(counts)
    
    ranges = []
    for i in range(0, number_of_bars):
        low = str(int(min_stake + bucket_size*(i+1)))
        label = '<=' + low
        ranges.append(label)


    plt.xlabel("Stake (in DOT/KSM)", fontsize=10)
    plt.ylabel("Number of Validators")
    plt.title("Validators by Stake")
    plt.bar(ranges, counts, color='#E6007A')
    plt.xticks(rotation=15)
    # plt.setp(plt, rotation=30, horizontalalignment='right')

    print(ranges)

    plt.savefig('validator_graph.png', bbox_inches='tight', pad_inches=.25)


main()


