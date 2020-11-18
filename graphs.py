import matplotlib.pyplot as plt

# Set the font size of the axis labels for graphs
plt.rc('xtick',labelsize=6)
plt.rc('ytick',labelsize=6)

input_file = None

# returns the total stake from the "Total stake: <stake>" line in the input file
def isolate_total_stake(line):
    tokens = line.split()
    return float(tokens[2])

# Reads in the file (used for the first graph option)
def read_in_file_1(file_name):
    total_stakes = []
    with open(file_name) as f:
        for line in f:
            if line.startswith('\tTotal stake:'):
                stake = isolate_total_stake(line)
                total_stakes.append(stake)
    return total_stakes


# returns the min stake from the line passed in from the file
def isolate_min_stake(line):
    tokens = line.split()
    return float(tokens[4])

# Reads in the file and returns a list of the minimum stake for all validators
def read_in_file_2(file_name):
    min_stakes = []
    with open(file_name) as f:
        for line in f:
            if line.startswith('\tMin Nominator:'):
                min_stake = isolate_min_stake(line)
                min_stakes.append(min_stake)
    return min_stakes

# returns the avg stake from the line passed in from the file
def isolate_avg_stake(line):
    tokens = line.split()
    return float(tokens[3])

def read_in_file_3(file_name):
    avg_stakes = []
    with open(file_name) as f:
        for line in f:
            if line.startswith('\tAverage Nominator Stake:'):
                avg_stake = isolate_avg_stake(line)
                avg_stakes.append(avg_stake)
    return avg_stakes


  




def main():
    prompt = "Make a selection from the following options:"
    prompt += "\n\t[1] Validator Total Stake Graph"
    prompt += "\n\t[2] Minimum Nomination Per Validator Graph"
    prompt += "\n\t[3] Average Nomination Per Validator Graph"
    prompt += "\n\t[4] Generate All Graphs"
    prompt += "\n\tSelection: "
    selection = int(input(prompt))
    if selection == 1:
        gen_validator_total_stake()
    elif selection == 2:
        gen_min_nomination_graph()
    elif selection == 3:
        gen_avg_nomination_graph()
    elif selection ==4:
        gen_validator_total_stake()
        plt.clf()
        gen_min_nomination_graph()
        plt.clf()
        gen_avg_nomination_graph()
    else:
        print("Invalid option")

def gen_validator_total_stake():
    global input_file
    if not input_file:
        input_file = str(input("Enter the name of the input file(eg. polkadot_out.txt): "))
    number_of_bars = int(input("Enter the number of bars in the Total Stake graph: "))
    output_file = str(input("Enter an output file name(eg. validator_total_stake_graph.png): "))
    if(output_file) == '':
        output_file = 'validator_total_stake_graph.png' # default to this file name if omitted
    stakes = read_in_file_1(input_file)
    stakes.sort()
    # print(stakes)
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
    angle = min(number_of_bars//9, 6)
    plt.xticks(rotation=15*angle)
    print(ranges)
    plt.savefig(output_file, dpi=300, bbox_inches='tight', pad_inches=.25)
    print("Saved Validator Total Stake Graph as", output_file)

def gen_min_nomination_graph():
    global input_file
    if not input_file:
        input_file = str(input("Enter the name of the input file(eg. polkadot_out.txt): "))
    number_of_bars = int(input("Enter the number of bars in the Min Stake graph: "))
    output_file = str(input("Enter an output file name(eg. min_nomination_graph.png): "))
    if(output_file) == '':
        output_file = 'min_nomination_graph.png' # default to this file name if omitted
    min_stakes = read_in_file_2(input_file)
    min_stakes.sort()
    # print(min_stakes)
    min_stake = min_stakes[0]
    max_stake = min_stakes[len(min_stakes)-1]
    diff = (max_stake - min_stake)
    bucket_size = (diff / number_of_bars)
    counts = []
    for i in range(0, number_of_bars):
        counts.append(0)

    for stake in min_stakes:
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
    plt.title("Minimum Nomination Per Validator", fontsize=15)
    plt.bar(ranges, counts, color='#E6007A')
    angle = min(number_of_bars//9, 6)
    plt.xticks(rotation=15*angle)
    print(ranges)
    plt.savefig(output_file, dpi=300, bbox_inches='tight', pad_inches=.25)
    print("Saved Minimum Nomination Per Validator graph as", output_file)

def gen_avg_nomination_graph():
    global input_file
    if not input_file:
        input_file = str(input("Enter the name of the input file(eg. polkadot_out.txt): "))
    number_of_bars = int(input("Enter the number of bars in the Average Stake graph: "))
    output_file = str(input("Enter an output file name(eg. avg_nomination_graph.png): "))
    if(output_file) == '':
        output_file = 'avg_nomination_graph.png' # default to this file name if omitted
    avg_stakes = read_in_file_3(input_file)
    avg_stakes.sort()
    # print(min_stakes)
    min_stake = avg_stakes[0]
    max_stake = avg_stakes[len(avg_stakes)-1]
    diff = (max_stake - min_stake)
    bucket_size = (diff / number_of_bars)
    counts = []
    for i in range(0, number_of_bars):
        counts.append(0)

    for stake in avg_stakes:
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
    plt.title("Average Nomination Per Validator", fontsize=15)
    plt.bar(ranges, counts, color='#E6007A')
    angle = min(number_of_bars//9, 6)
    plt.xticks(rotation=15*angle)
    print(ranges)
    plt.savefig(output_file, dpi=300, bbox_inches='tight', pad_inches=.25)
    print("Saved Average Nomination Per Validator graph as", output_file)


main()


