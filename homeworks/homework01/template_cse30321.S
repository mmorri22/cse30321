//  Template file for use with QtRVSim simulator 
//  (https://github.com/cvut/qtrvsim/)
//
//  template_cse30321.S       - template/skeleton file
//
//  Created by @adingler for CSE30321,
//  based on simple-lw-sw-ia.S, (C) 2021 by Pavel Pisa
//      e-mail:   pisa@cmp.felk.cvut.cz
//      homepage: http://cmp.felk.cvut.cz/~pisa
//      work:     http://www.pikron.com/
//      license:  public domain

// Directives to make interesting windows visible
#pragma qtrvsim show registers
#pragma qtrvsim show memory

.globl _start
.option norelax

.text

_start:
	//your code for "main" should go here

	// this will stop the simulation, but note you can still single-step
	// past this point (it will throw errors)
	ebreak

	
	//define all functions after "main"

.data

// you can optionally specify a location to show in memory window by
// uncommenting this pragma and updating LABEL (see simple-ls-sw-ia.S)
//#pragma qtrvsim focus memory LABEL
