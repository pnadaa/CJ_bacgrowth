This is a super barebones program written in 2 hours to estimate bacterial optical density for exponential growth.\
I recommend checking the OD at around 75% of the time that the program estimates it to ensure the cultures do not overgrow (might add this calculation in the future).\
The program is based on the exponential growth formula: A = P<sub>0</sub>e<sup>rt</sup>, where A = current OD, P<sub>0</sub> = original OD, r = growth constant, and t = time.\
It calcualtes the r constant using the intermediate OD measurement and uses it to calculate the time t.