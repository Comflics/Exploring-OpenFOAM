Some changes to the case files might be required to suit the version of OpenFoam you have installed. The current configuration is for OF 2.1.x

Known Issues:

laminarVortexShedding/system/fvSchemes
Line 21: 'CrankNicholson' for version 2.1.x and before
         'CrankNicolson'  for version 2.3.x and later

Line 42: div((nuEff*dev(T(grad(U)))))  for all OF versions
         div((nuEff*dev(grad(U).T()))) for Foam-extend 3.1	

