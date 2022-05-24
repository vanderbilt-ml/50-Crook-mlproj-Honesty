# 50-Crook-mlproj-Honesty
Predict whether religious affiliation and personality type have a correlation with Machivallian personality traits.
The data set for this project will be the Machivallianism Test set from Kaggle which features the results of a Mach-IV survey administered to a group of people.
The survey featured 20 questions, which scores a person's Machivallian personality indicators using a score of 20-100, with 60 and over equated to a high
percentage. Survey takers were asked to further participate in additional questions and demographic data, but it was purely optional. For the purposes of this project, only entries that feature the optional results will be vetted.

The data that will be weighed is indicated in the Data Items section of this README, but will basically involve calculating the Mach-IV score and leveraging answers to certain questions as indicators of dishonest traits. The project will then evaluate the demographic data of the data set in order to predict specific groupings.

# Project Data

Data Dictionary contains the following elements:
The main body of the consisted of 20 questions. The text of those questions is below.

"Q1" : "Never tell anyone the real reason you did something unless it is useful to do so."
"Q2" : "The best way to handle people is to tell them what they want to hear."
"Q3" : "One should take action only when sure it is morally right."
"Q4" : "Most people are basically good and kind."
"Q5" : "It is safest to assume that all people have a vicious streak and it will come out when they are given a chance."
"Q6" : "Honesty is the best policy in all cases."
"Q7" : "There is no excuse for lying to someone else."
"Q8" : "Generally speaking, people won't work hard unless they're forced to do so."
"Q9" : "All in all, it is better to be humble and honest than to be important and dishonest."
"Q10" : "When you ask someone to do something for you, it is best to give the real reasons for wanting it rather than giving reasons which carry more weight."
"Q11" : "Most people who get ahead in the world lead clean, moral lives."
"Q12" : "Anyone who completely trusts anyone else is asking for trouble."
"Q13" : "The biggest difference between most criminals and other people is that the criminals are stupid enough to get caught."
"Q14" : "Most people are brave."
"Q15" : "It is wise to flatter important people."
"Q16" : "It is possible to be good in all respects."
"Q17" : "P.T. Barnum was wrong when he said that there's a sucker born every minute."
"Q18" : "It is hard to get ahead without cutting corners here and there."
"Q19" : "People suffering from incurable diseases should have the choice of being put painlessly to death."
"Q20" : "Most people forget more easily the death of their parents than the loss of their property."

The questions were presented one at a time in a random order. Users responded to each item on a five point scale: 1=Disagree, 2=Slightly disagree, 3=Neutral, 4=Slightly agree, 5=Agree.

Three values are recorded for each question. e.g.

Q1A - the user's answer
Q1I - the position of that item in the survey
Q1E - the time spend on that question in milliseconds

After the test body, users were asked if they would be willing to complete an additional research survey. This data only includes those who agreed to.

The optional survey included a variety of questions:

The Ten Item Personality Inventory was administered (see Gosling, S. D., Rentfrow, P. J., & Swann, W. B., Jr. (2003). A Very Brief Measure of the Big Five Personality Domains. Journal of Research in Personality, 37, 504-528.):

TIPI1	Extraverted, enthusiastic.
TIPI2	Critical, quarrelsome.
TIPI3	Dependable, self-disciplined.
TIPI4	Anxious, easily upset.
TIPI5	Open to new experiences, complex.
TIPI6	Reserved, quiet.
TIPI7	Sympathetic, warm.
TIPI8	Disorganized, careless.
TIPI9	Calm, emotionally stable.
TIPI10	Conventional, uncreative.

The TIPI items were rated "I see myself as:" _____ such that

1 = Disagree strongly
2 = Disagree moderately
3 = Disagree a little
4 = Neither agree nor disagree
5 = Agree a little
6 = Agree moderately
7 = Agree strongly

The following items were presented as a check-list and subjects were instructed "In the grid below, check all the words whose definitions you are sure you know":

VCL1	boat
VCL2	incoherent
VCL3	pallid
VCL4	robot
VCL5	audible
VCL6	cuivocal
VCL7	paucity
VCL8	epistemology
VCL9	florted
VCL10	decide
VCL11	pastiche
VCL12	verdid
VCL13	abysmal
VCL14	lucid
VCL15	betray
VCL16	funny

A value of 1 is checked, 0 means unchecked. The words at VCL6, VCL9, and VCL12 are not real words and can be used as a validity check.

A bunch more questions were then asked:

education			"How much education have you completed?", 1=Less than high school, 2=High school, 3=University degree, 4=Graduate degree
urban				"What type of area did you live when you were a child?", 1=Rural (country side), 2=Suburban, 3=Urban (town, city)
gender				"What is your gender?", 1=Male, 2=Female, 3=Other
engnat				"Is English your native language?", 1=Yes, 2=No
age					"How many years old are you?"
hand				"What hand do you use to write with?", 1=Right, 2=Left, 3=Both
religion			"What is your religion?", 1=Agnostic, 2=Atheist, 3=Buddhist, 4=Christian (Catholic), 5=Christian (Mormon), 6=Christian (Protestant), 7=Christian (Other), 8=Hindu, 9=Jewish, 10=Muslim, 11=Sikh, 12=Other
orientation			"What is your sexual orientation?", 1=Heterosexual, 2=Bisexual, 3=Homosexual, 4=Asexual, 5=Other
race				"What is your race?", 10=Asian, 20=Arab, 30=Black, 40=Indigenous Australian, 50=Native American, 60=White, 70=Other
voted				"Have you voted in a national election in the past year?", 1=Yes, 2=No
married				"What is your marital status?", 1=Never married, 2=Currently married, 3=Previously married
familysize			"Including you, how many children did your mother have?"		
major				"If you attended a university, what was your major (e.g. "psychology", "English", "civil engineering")?"

The following value were calculated by the server:

country		the user's network location

screenw		width of user's device in pixels
screenh		width of user's device in pixels

The time spend on each page was recorded in seconds:

introelapse
testelapse
surveyelapse

# Data Items of Interest:
1. Overall Mach-IV score (20-100)
2. Answer to Question 6
3. Answer to Question 7
4. religion answer in data range 3-7

# Data Items for Further Analysis
1. Scores on TIPI1
2. Scores on TIPI6
3. education
4. race
5. age
6. gender
7. religions choice

# Expected Output
1. A percentage of entries that meet the following criteria: Overall Mach-IV score of 60+, Answer to question 6 is a value of < 3, Answer to question 7 is < 3, religion value is in data range 3-7.
2. Statistical measure of item 1 broken down by Scores on TIPT1
3. Statistical measure of item 1 broken down by Scores on TIPT6
4. Statistical measure of item 1 broken down by Scores on eduction
5. Statistical measure of item 1 broken down by Scores on race
6. Statistical measure of item 1 broken down by Scores on age
7. Statistical measure of item 1 broken down by Scores on gender
8. Statistical measure of item 1 broken down by Scores on religious choice
9. percentage of item 1 entries that have the same values for Scores on Data Items for Further Analysis

# Expected Costs
No costs are expected for data. One developer will be used for the application development and only open source tools will be used for statistical analysis.

# Molly's 1st Comment 
Need to explain how you're going to take the user's data and correlate it to Machiavellian personality traits

# Molly's 2nd Comment
Need to explain the point of the optional survey 
