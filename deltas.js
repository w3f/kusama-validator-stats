const fs = require('fs')

// Stats to show:
//      Total DOT:
//      Bonding Stake
//      Staking Rate
//      Highest-staked validator
//      Lowest-staked validator
//      Average stake of all validators
//      Highest commission validator:
//      Lowest commission validator:
//      Average Average stake per nominator
//      Average Minimum stake per nominator

async function main() {
    let file_1 = process.argv[2]
    let file_2 = process.argv[3]
    let summary_section_1 = read_from_file(file_1)
    let summary_section_2 = read_from_file(file_2)
    compare(summary_section_1, summary_section_2)
}

// Returns an array of lines from the file
// The first line in the file should be the line that says "Summary Data: "
function read_from_file(file_name) {
    let file_input = fs.readFileSync(file_name, 'utf8');
    file_input = file_input.split('\n')
    let total_lines = file_input.length
    let summary_section = file_input.slice(total_lines - 20, total_lines)
    return Array.from(summary_section)
}

// Call helper compare functions
// The helper functions print the stats for a given piece of data
// first and second are lists of strings
// each string is one line in the summary section of the output file
// Might be better to split lines at the : and compare the first string as opposed to hard-coding indices
// but this works for now
function compare(first, second) {
    console.log("Summary Data:\n")
    compare_line(first[1], second[1], "Total Dot: ", 2);
    compare_line(first[2], second[2], "Bonding Stake: ", 2);
    compare_line(first[3], second[3], "Staking Rate: ", 2);
    compare_line(first[5], second[5], "Highest Staked Validator: ", 4);
    compare_line(first[6], second[6], "Lowest Staked Validator: ", 4);
    compare_line(first[15], second[15], "Average Stake Per Validator: ", 4);
    compare_line(first[6], second[6], "Lowest Staked Validator: ", 4);
    compare_line(first[8], second[8], "Highest Commission Validator: ", 5);
    compare_line(first[9], second[9], "Lowest Commission Validator: ", 5);
}

function compare_line(first, second, title, index_in_string) {
    // isolates the value at the index in the string
    // eg. if the line is "Total Stake: 2934 DOT"
    // it would isolate the 2934 (at index 2) as that is the value to compare
    let first_value = first.split(' ')[index_in_string] // After splitting the string into a list, the value of DOT is at index 2
    let second_value = second.split(' ')[index_in_string]
    console.log(title)
    console.log(`File 1: ${first_value}\t\tFile 2: ${second_value}\t\tDifference: ${first_value-second_value}\n`)
}

main()