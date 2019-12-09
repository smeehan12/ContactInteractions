!beam parameters
Beams:idA = 2212 ! first incoming beam is a 2212, i.e. a proton.
Beams:idB = 2212 ! second beam is also a proton.
Beams:eCM = 13000. ! the cm energy of collisions.

!processes
!HardQCD:gg2gg = on
!HardQCD:gg2qqbar = on
!HardQCD:qg2qg = on
HardQCD:qqbar2gg = on
!PhaseSpace:pTHatMin = 50.

! turn off underlying event
PartonLevel:ISR = off
PartonLevel:FSR = off
PartonLevel:MPI = off