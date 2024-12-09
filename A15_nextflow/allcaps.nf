#!/usr/bin/env nextflow

params.str = 'Hello World'

process toUpperCase {

	input:
	val inputString

	output:
	path 'outputString.txt'

	script:
	"""
	echo "$inputString" | tr '[:lower:]' '[:upper:]' > outputString.txt
	"""

}

workflow {
	toUpperCase(inputString: params.str)
}	
