import matplotlib.pyplot as plt

plt.rc('xtick',labelsize=6)
plt.rc('ytick',labelsize=6)

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
    prompt = "Make a selection from the following options:"
    prompt += "\n\t[1] Validator Stake Graph"
    prompt += "\n\t[2] Minimal Nominator Graph"
    prompt += "\n\t[3] Average Nominator Graph\n\tSelection: "
    selection = int(input(prompt))
    if selection == 1:
        gen_validator_graph()
    elif selection == 2:
        gen_min_nominator_graph()
    elif selection == 3:
        gen_avg_nominator_graph()
    else:
        print("Invalid option")

def gen_validator_graph():
    file_to_read = str(input("Enter the name of the input file(eg. polkadot_out.txt): "))
    number_of_bars = int(input("Enter the number of bars in the graph: "))
    output_file = str(input("Enter an output file name(eg. validator_graph.png): "))
    if(output_file) == '':
        output_file = 'validator_graph.png' # default to this file name if omitted
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
        low = "{:,}".format(int(min_stake + bucket_size*(i+1)))
        label = '< ' + low
        ranges.append(label)


    plt.xlabel("Stake (in DOT/KSM)")
    plt.ylabel("Number of Validators")
    plt.title("Validators by Stake", fontsize=15)
    plt.bar(ranges, counts, color='#E6007A')
    plt.xticks(rotation=20)
    # plt.setp(plt, rotation=30, horizontalalignment='right')

    print(ranges)

    plt.savefig(output_file, bbox_inches='tight', pad_inches=.25)

main()


