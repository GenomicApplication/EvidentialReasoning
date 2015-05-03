Author: Tami Hong Le

This is a read me documentations for various input functions required to make the evidential reasoning package.

For input.txt file, the input should be in the following format:

1) The first line should be  hypothesis separated by ":" for the split function to parse the strings.

For example:

Hypothesis: H1: Is the experimental result credible and reliable?: Very credible and reliable, Good credibility and reliability, Acceptable credibility and reliability, Not credible or reliable

Hypothesis can be named anything you prefer, however, it is easier to identify it if it is named "Hypothesis". The first line are ALWAYS considered a hypothesis frame. This is always stored in an array with index of 0.

H1 is the abbreviated string for "hypothesis" frame. This is always stored in an array with index of 1.


The Question " Is the experimental result credible and reliable?:" is always stored in an array with index of 2.

The trailing strings for every "," separation are propositions

2) Follow the following procedure to name all frames, determine it's abbreviation, followed by propositions. These frames will not have the question format as required for 'H1.'

Ror example:

B1: ENVC: TRUE: Procedure: PM: Effective, Ineffective

B1 is the branch number in the gallery. Stored in array index 0.

ENVC is the abbreviation for the branch number. Stored in array index 1.

TRUE is a flag to turn on the discount function if needed. Stored in array index 2.

Procedure is the name of the frame. Stored in array index 3.

PM1 is the frame abbreviation. Stored in array index 4.

Effective is a proposition. Stored in array index 5.

Ineefective is a proposition. Stored in array index 5.

Notice that the propositions are all stored in index 5. The proposition will be splitted again into another array in the program with the ',' as the identifier for splitting.

3) To define credibility relations, the start of the line must begin with 'CR' followed by a number (incremental numbering starting from 1 is an organized way of representing this).

For example:

CR1: EN: CL: 0.2: {(EN1), (CL1,CL2,CL3)} ; {(EN2), (CL1, CL2, CL3)} ; {(EN3), (CL2, CL3, CL4)} ; {(EN4), (CL3,CL4)}

CR1 is the compatibility relation 1. Stored in array index 0.

'EN: CL' are the two frames that are being translated. Stored in index 1 and index 2.

'0.2:' represents the degrees of belief with ':' indicating the end of the string. Stored in index 3.

"{(EN1),(CL1,CL2,CL3)} ; " where '{}' is the set propositions of one frame to the propositions of another frame. Here, EN is the ENVIRONMENT frame and CL is the cleaniliness frame. The numbers trailing after EN and CL are the proposition numbers that are organized in the same manner as the declaration of EN and CL under branch (B1). Every ';'  that are after '}' seperates the relationships.

Testing






