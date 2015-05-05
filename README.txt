Author:	Tami Hong Le

This is a document to specify how the “Input.txt” file should be formatted in order to make this application work correctly.

1)	The question frame must be in the following format:

EXAMPLE:

Question: Is the experimental result credible and reliable?:Credible and reliable, Acceptable credibility and reliability, Not credible nor reliable.

a)	The colons “:” are for the purpose of splitting when parsing the information.
b)	The line must begin with “Question” in order for the program to recognize that it is a question frame.
c)	“Is the experimental result credible and reliable?” is the question that you are trying to explore.
d)	Next, are the answers to the question you are exploring.
i)	 For example:
(1)	Credible and reliable
(2)	Acceptable credibility and reliability
(3)	Not credible or reliable.

2)	The frame must be in the following format:

EXAMPLE:

Frame :EN: Environment sterility and cleanliness: Sterile environment and cleanliness/ Sterile environment and average cleanliness/ Sterile environment and poor cleanliness/ Moderately sterile environment and good cleanliness/ Moderately sterile environment and average cleanliness/ Moderately sterile environment and poor cleanliness/ Dirty environment and good cleanliness/ Dirty environment and average cleanliness/ Dirty environment and poor cleanliness

a)	The line must begin with “Frame” in order for the application to recognize that it is a frame.
b)	The colons “:” are for the purpose of splitting when parsing the information.
c)	“Environment sterility and cleanliness:” is the name of the frame.
d)	“Sterile environment and cleanliness/” is the proposition to the frame. Note that it must be followed by a forward slash “/” in order to parse correctly. Every answer must have a ‘/’after it until you have reached the end. The last proposition does NOT have ‘/’, otherwise, it would incorrectly parse.

3)	The compatibility relations must begin with ‘CR:’followed by a colon.

EXAMPLE:

CR1:EN X PA:EN1/PA1,PA2,PA4,PA5,PA6:EN2/PA1,PA3,PA4,PA5,PA6:EN3/PA5,PA6,PA7,PA8,PA9:EN4/PA1,PA2,PA4,PA5,PA6,PA7,PA8:EN5/PA2,PA3,PA4,PA5,PA6,PA7:EN6/PA6,PA7,PA8,PA9:EN7/PA3,PA6,PA7,PA8,PA9:EN8/PA7,PA8,PA9:EN9/PA6,PA7,PA8,PA9

a)	The next piece of information is the frame you are crossing. Here, we are crossing the frame ‘EN’ with the frame PA, shown as EN X PA. The ‘X’ must be capitalized. ‘EN X PA’ must be spaced correctly in order for the application to represent it in a nicer format.
b)	“EN1/PA1,PA2,PA4,PA5,PA6:EN2/PA1,PA3,PA4,PA5,PA6,” where EN1 is the proposition that is compatible to “PA1,PA2,PA4,PA5,PA6:EN2/PA1,PA3,PA4,PA5,PA6.” This is a shortcut to represent that EN1  is crossed with all the PA propositions that it is compatible to.
c)	Each proposition must be separated with ‘/’ in order to correctly parse it. Otherwise the application would not be able to parse it correctly, rendering the wrong answer.

4)	‘FOD:’ represents the frames of discernment.

EXAMPLE:

FOD:EN:YES: 0.10: 0.70:EN1 U EN2:0.10: EN3: EN: EN1,EN2,EN3,EN4,EN5,EN6,EN7,EN8,EN9
a)	Here, the colons “:” are for the purpose of splitting when parsing the information.
b)	‘EN:’ represent the frame abbreviation.
c)	‘YES:’ is a flag for the discount operation.
d)	 ‘: 0.10:’is the discount number (known as the alpha value).
e)	‘0.70:EN1 U EN2’where 0.70 represents the mass to the proposition ‘EN1 U EN2’. The ‘U’ indicates the union of both proposition.
f)	‘0.10: EN3’ represents the next proposition (EN3) that has an initial mass of 0.10.
g)	‘: EN: EN1,EN2,EN3,EN4,EN5,EN6,EN7,EN8,EN9’ where EN is the abbreviated form of the frame and  ‘EN1,EN2,EN3,EN4,EN5,EN6,EN7,EN8,EN9’ are the propositions to the frame EN. Note that it must be separated by “,”in order to parse correctly.
h)	The FOD does not have to be a union (U). It can also be separated. Say for instance, this FOD could have been represented as:

FOD:EN:YES: 0.10: 0.70:EN1:0.10: EN2: EN: EN1,EN2,EN3,EN4,EN5,EN6,EN7,EN8,EN9
i)	The last CR must be represent with a ‘Q’ in order for the application to recognize that the last frame is for making compatibility relations with the question frame. An example is the following:

CR5:PR X EN X PA X Q:Good credibility and reliability/PR1 v [EN1 v PA1,PA2,PA4,PA5,PA6, EN2 v PA1,PA2,PA3,PA4,PA5,PA6, EN3 v PA5,PA6,PA7,PA8,PA9, EN4 v PA1,PA2,PA4,PA5,PA6,PA7,PA8, EN5 v PA1,PA2,PA3,PA4,PA5,PA6,PA7, EN6 v PA6,PA7,PA8,PA9], PR2 v [EN1 v  PA1,PA2,PA4,PA5,PA6, EN2 v PA1,PA3,PA4,PA5,PA6, EN3 v PA5,PA6,PA7,PA8,PA9, EN4 v PA1,PA2,PA4,PA5,PA6,PA7, EN5 v PA2,PA3,PA4,PA5,PA6,PA7, EN6 v PA6,PA7,PA8,PA9], PR5 v [EN2 v PA1,PA2,PA3,PA4,PA5,PA6, EN4 v PA1,PA2,PA4,PA5,PA6,PA7,PA8, EN5 v PA2,PA3,PA4,PA5,PA6,PA7]:Acceptable credibility and reliability/PR5 v [EN2 v PA1,PA2,PA3,PA4,PA5,PA6, EN4 v PA1,PA2,PA4,PA5,PA6,PA7,PA8, EN5 v PA2,PA3,PA4,PA5,PA6,PA7], PR6 v [EN5 v PA2,PA3,PA4,PA5,PA6,PA7, EN6 v PA6,PA7,PA8,PA9, EN7 v PA3,PA6,PA7,PA8,PA9], PR9 v [EN1 v PA1,PA2,PA4,PA5,PA6, EN2 v PA1,PA2,PA3,PA4,PA5,PA6, EN3 v PA5,PA6,PA7,PA8,PA9, EN4 v PA1,PA2,PA4,PA5,PA6,PA7,PA8, EN5 v PA1,PA2,PA3,PA4,PA5,PA6,PA7], PR10 v [EN2 v PA1,PA2,PA3,PA4,PA5,PA6, EN4 v PA1,PA2,PA4,PA5,PA6,PA7,PA8, EN5 v PA1,PA2,PA3,PA4,PA5,PA6,PA7, EN6 v PA6,PA7,PA8,PA9], PR13 v [EN3 v PA5,PA6,PA7,PA8,PA9, EN5 v PA2,PA3,PA4,PA5,PA6,PA7, EN6 v PA6,PA7,PA8,PA9, EN7 v PA3,PA6,PA7,PA8,PA9]:Poor credibility and reliability/ PR4 v [EN3 v PA5,PA6,PA7,PA8,PA9, EN4 v PA1,PA2,PA4,PA5,PA6,PA7,PA8, EN5 v PA2,PA3,PA4,PA5,PA6,PA7, EN6 v PA6,PA7,PA8,PA9, EN7 v PA3,PA6,PA7,PA8, EN8 v PA7,PA8,PA9], PR7 v [EN3 v PA5,PA6,PA7,PA8,PA9, EN6 v PA6,PA7,PA8,PA9, EN7 v PA3,PA6,PA7,PA8,PA9, EN8 v PA7,PA8,PA9, EN9 v PA6,PA7,PA8,PA9], PR8 v [EN3 v PA5,PA6,PA7,PA8,PA9, EN6 v PA6,PA7,PA8,PA9, EN7 v PA3,PA6,PA7,PA8,PA9, EN8 v PA7,PA8,PA9, EN9 v PA6,PA7,PA8,PA9], PR12 v [EN7 v PA3,PA6,PA7,PA8, EN8 v PA7,PA8,PA9, EN9 v PA6,PA7,PA8,PA9], PR15 v [EN7 v PA3,PA6,PA7,PA8, EN8 v PA7,PA8,PA9, EN9 v PA6,PA7,PA8,PA9], PR16 v [EN8 v PA7,PA8,PA9, EN9 v PA6,PA7,PA8,PA9]
 Where ‘PR X EN X PA X Q’ is the frame name with emphasis on ‘Q’. All the answer to the question frame are sandwiched in between a ‘:’ and ‘/’as shown ‘Good credibility and reliability/’.

“PR1 v [EN1 v PA1,PA2,PA4,PA5,PA6, EN2 v PA1,PA2,PA3,PA4,PA5,PA6, EN3 v PA5,PA6,PA7,PA8,PA9, EN4 v PA1,PA2,PA4,PA5,PA6,PA7,PA8, EN5 v PA1,PA2,PA3,PA4,PA5,PA6,PA7, EN6 v PA6,PA7,PA8,PA9]” proceeding the answer represents the proposition PR1 crossed with EN1 which has compatibility relations with the PA frame.



