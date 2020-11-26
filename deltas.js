const { compactStripLength } = require('@polkadot/util')
const { Console } = require('console')
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

function read_from_file(file_name) {
    let file_input = fs.readFileSync(file_name, 'utf8');
    file_input = file_input.split('\n')
    let total_lines = file_input.length
    let summary_section = file_input.slice(total_lines - 20, total_lines)
    return Array.from(summary_section)
}

function compare(first, second) {
    console.log("Summary Data:\n")
    compare_total(first[1], second[1])
    compare_bonding_stake(first[2], second[2])
    compare_rate(first[3], second[3])
    compare_highest(first[5], second[5])
    compare_lowest(first[6], second[6])
    compare_average(first[15], second[15])
    compare_commission_high(first[8], second[8])
    compare_commission_low(first[9], second[9])

}

function compare_total(first, second) {
    let first_value = first.split(' ')[2]
    let second_value = second.split(' ')[2]
    console.log(`Total Dot:`)
    console.log(`File 1: ${first_value}\t\tFile 2: ${second_value}\t\tDifference: ${first_value-second_value}\n`)
}

function compare_bonding_stake(first, second) {
    let first_value = first.split(' ')[2]
    let second_value = second.split(' ')[2]
    console.log(`Bonding Stake: `);
    console.log(`File 1: ${first_value}\t\tFile 2: ${second_value}\t\tDifference: ${first_value-second_value}\n`)
}

function compare_rate(first, second) {
    let first_value = first.split(' ')[2]
    let second_value = second.split(' ')[2]
    console.log(`Staking Rate: `);
    console.log(`File 1: ${first_value}%\t\tFile 2: ${second_value}%\t\tDifference: ${first_value-second_value}\n`)
}

function compare_highest(first, second) {
    let first_value = first.split(' ')[4]
    let second_value = second.split(' ')[4]
    console.log(`Highest Staked Validator: `);
    console.log(`File 1: ${first_value}\t\tFile 2: ${second_value}\t\tDifference: ${first_value-second_value}\n`)
}

function compare_lowest(first, second) {
    let first_value = first.split(' ')[4]
    let second_value = second.split(' ')[4]
    console.log(`Lowest Staked Validator: `);
    console.log(`File 1: ${first_value}\t\tFile 2: ${second_value}\t\tDifference: ${first_value-second_value}\n`)
}

function compare_average(first, second) {
    let first_value = first.split(' ')[4]
    let second_value = second.split(' ')[4]
    console.log(`Average Stake Per Validator: `);
    console.log(`File 1: ${first_value}\t\tFile 2: ${second_value}\t\tDifference: ${first_value-second_value}\n`)
}

function compare_commission_high(first, second) {
    let first_value = first.split(' ')[5]
    let second_value = second.split(' ')[5]
    console.log(`Highest Commission Validator: `);
    console.log(`File 1: ${first_value}\t\tFile 2: ${second_value}\t\tDifference: ${first_value-second_value}\n`)
}

function compare_commission_low(first, second) {
    let first_value = first.split(' ')[5]
    let second_value = second.split(' ')[5]
    console.log(`Lowest Commission Validator: `);
    console.log(`File 1: ${first_value}\t\tFile 2: ${second_value}\t\tDifference: ${first_value-second_value}\n`)
}

main()