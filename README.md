This repository contains code that can be used to prepare an
input dark current exposure for use in the NIRCam Data
Simulator.

The input dark current exposure will be reorganized into the
requested readout pattern (if possible). If the input is not
a linearized exposure, then it will be run through the
initial stages of the JWST calibration pipeline in order to
linearize the data. This includes superbias subtraction and
reference pixel subtraction, followed by the linearization
step.

The signal associated with the superbias and reference pixels
is saved along side the linearized dark ramp such that it
can be added back in later, if the user requests a raw output
ramp from the NIRCam Data Simulator.

Dependencies:

If the:

Inst:
  use_JWST_pipeline

input is set to true, then the JWST calibration pipeline is needed.


Output:

The linearized dark current and zeroth frame as saved to a fits file
that uses the name from the Output:file entry in the input yaml file
and ending with '_linearizedDark.fits'.

These are also available as self.linDark and self.zeroModel


To use:

python dark_prep.py myinputs.yaml

or:

from dark_prep.scripts import dark_prep
dark = dark_prep.DarkPrep()
dark.paramfile = 'myinputs.yaml'
dark.run()
