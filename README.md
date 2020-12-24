# kusama-validator-stats

To run the script, make sure you have `yarn` and `nodejs` installed.

run `yarn` to install yarn dependencies

run `yarn add @polkadot/api` to install the necessary polkadot api packages


If no command line args are included, it defaults to the Polkadot network
`node index-polkadot.js`

Include "kusama" as a command line argument to run this script on the Kusama network
`node index-polkadot.js kusama`

## Result

![Kusama Staking Stat](https://i.imgur.com/ucKNVw4.png)

# Graphs

Make sure you have Python 3 installed.

run `pip install matplotlib` to install the graphing library used

Before running the python script to create the graphs, you must save the output of `node index-polkadot.js` to a text file.

eg. `node index-polkadot.js > polkadot_out.txt`

To run the script to create graphs:
`python graphs.py [input_file]`

eg. `python graphs.py polkadot_out.txt`

- input_file is an optional parameter, without it you will be prompted to enter the file name when the program runs
- output file name can be omitted when prompted, the default name for each graph is shown as an example and will be used if no file name is provided
- output file name must end with one of the following extensions, or be omitted:
    - eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
    - if no extension is provided, matplotlib defaults to .png


