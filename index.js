const{ ApiPromise, WsProvider } = require('@polkadot/api')
const { isHex } = require('@polkadot/util')
const DOT_DECIMAL_PLACES = 1000000000000;
let lowest = "no one";
let highest = "no one";
let highestAmount = NaN;
let lowestAmount = NaN;
let highestCommission = "no one";
let lowestCommission = "no one";
let highestCommissionAmount = NaN;
let lowestCommissionAmount = NaN;

(async () => {
    const provider = new WsProvider('wss://kusama-rpc.polkadot.io/')
    const api = await ApiPromise.create({ provider })
    const [ currentValidators, totalIssuance, currentEra ] = await Promise.all([
      api.query.session.validators(),
      api.query.balances.totalIssuance(),
      api.query.staking.currentEra(),
    ]);

    const totalKSM = parseInt(totalIssuance.toString())
    const totalBondingStake = await api.query.staking.erasTotalStake(currentEra.toString())
    
    for (let i=0; i<currentValidators.length; i++) {
      const validatorStake = await api.query.staking.erasStakers(currentEra.toString(), currentValidators[i])
      const validatorComissionRate = await api.query.staking.erasValidatorPrefs(currentEra.toString(), currentValidators[i])
      const validatorTotalStake = validatorStake['total'].toString() / DOT_DECIMAL_PLACES
      const validatorOwnStake = validatorStake['own'].toString() / DOT_DECIMAL_PLACES
      const validatorNominators = validatorStake['others'].toJSON()
      
      check(currentValidators[i].toString(), parseInt(validatorTotalStake), parseInt(validatorComissionRate['commission'].toString()))

      console.log(`Stash Address: ${currentValidators[i].toString()}.\n\tTotal stake: ${validatorTotalStake}\n\tSelf stake: ${validatorOwnStake}`)
      for (let j=0; j<validatorNominators.length; j++) {
        console.log(`\tAddress: ${validatorNominators[j].who}, Stake: ${validatorNominators[j].value / DOT_DECIMAL_PLACES}`)
      }
      console.log(`\tCommission: ${validatorComissionRate['commission'].toString() / 10000000}%`)
      console.log('\tNominators:', validatorNominators.length)
    }

		console.log()
    console.log("\nSummary Data:")
    console.log(`Total KSM: ${totalKSM / DOT_DECIMAL_PLACES}`)
    console.log(`Bonding Stake: ${totalBondingStake.toString() / DOT_DECIMAL_PLACES} KSM`)
    console.log(`Staking Rate: ${totalBondingStake.toString() / totalKSM * 100} %`)

    console.log(`Highest-staked validator: ${highest} : ${highestAmount} KSM`)
    console.log(`Lowest-staked validator: ${lowest} : ${lowestAmount} KSM`)
    console.log(`Highest commission validator: ${highestCommission} : ${highestCommissionAmount / 10000000}%`)
    console.log(`Lowest commission validator: ${lowestCommission} : ${lowestCommissionAmount / 10000000}%`)

    process.exit()
})()


const check = (currentValidator, stake, commission) => {
	if (isNaN(highestAmount)) {
	    // If highest_amount is NaN, this must be the
	    // first.  Set this validator to highest and lowest everything.
	    lowest = highest = currentValidator
	    lowestAmount = highestAmount = stake
	    lowestCommission = highestCommission = currentValidator
	    lowestCommissionAmount = highestCommissionAmount = commission
	} else {
	    // Check total stake

	    if (stake > highestAmount) {
        highest = currentValidator
        highestAmount = stake
      } else if (stake < lowestAmount) {
        lowest = currentValidator
        lowestAmount = stake
	    }

	    // Check commissions

	    if (commission > highestCommissionAmount) {
        highestCommission = currentValidator
        highestCommissionAmount = commission
      } else if (commission < lowestCommissionAmount) {
        lowestCommission = currentValidator
        lowestCommissionAmount = commission
	    }
	}
}