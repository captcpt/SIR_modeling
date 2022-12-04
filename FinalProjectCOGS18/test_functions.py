import pytest
from IPython import display

# Testing the SIR() function
assert SIR('AZ','10/18/2021') == [1, 0.15608832821444257, 0]
assert SIR('IL', '10/18/2021') == [1, 0.13189275844813259, 0]
assert SIR('NY', '10/18/2022') == [1, 0.16511117990888546, 0]
assert SIR('FL','10/18/2022') == [1, 0.32807451478178723, 0]

# Testing the deriv() function
assert deriv([(732673 - 284076),284076,0],10) == [-127435641372, 127435499334.0, 142038.0] # For AK, 10/18/2022
assert deriv([(5039877 - 810974),810974,0],10) == [-3429530381522, 3429529976035.0, 405487.0] # For AL 10/18/2021

# Examples/tests of sir_model()
display.Image('sir_model_CA21.png')
display.Image('sir_model_CA22.png')
display.Image('sir_model_TX21.png')
display.Image('sir_model_TX22.png')
display.Image('sir_model_NY21.png')
display.Image('sir_model_NY22.png')
