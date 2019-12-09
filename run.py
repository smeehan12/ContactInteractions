# https://github.com/scikit-hep/numpythia
from numpythia import Pythia

# for making the proper output
import ROOT
from ROOT import TH1F,TH2F,TH3F,TFile,TLorentzVector,TTree
import sys
from array import array

runtypes=[]
runtypes.append('config_sm')
runtypes.append('config_ci')
runtypes.append('config_sm_ci')

nevents=10000

for runtype in runtypes:

  # setting up the output ntuple

  fout = TFile(runtype+"_"+str(nevents)+".root", "RECREATE")
  t = TTree( 'tree', 'tree with stuff' )

  ptj1    = array( 'f', [ 0 ] )
  etaj1   = array( 'f', [ 0 ] )
  phij1   = array( 'f', [ 0 ] )
  ej1     = array( 'f', [ 0 ] )  
  ptj2    = array( 'f', [ 0 ] )
  etaj2   = array( 'f', [ 0 ] )
  phij2   = array( 'f', [ 0 ] )
  ej2     = array( 'f', [ 0 ] )
  mjj     = array( 'f', [ 0 ] )
  ystarjj = array( 'f', [ 0 ] )

  t.Branch( 'ptj1'     ,  ptj1   ,    'ptj1/F' )
  t.Branch( 'etaj1'    ,  etaj1  ,    'etaj1/F' )
  t.Branch( 'phij1'    ,  phij1  ,    'phij1/F' )
  t.Branch( 'ej1'      ,  ej1    ,    'ej1/F' )
  t.Branch( 'ptj2'     ,  ptj2   ,    'ptj2/F' )
  t.Branch( 'etaj2'    ,  etaj2  ,    'etaj2/F' )
  t.Branch( 'phij2'    ,  phij2  ,    'phij2/F' )
  t.Branch( 'ej2'      ,  ej2    ,    'ej2/F' )
  t.Branch( 'mjj'      ,  mjj    ,    'mjj/F' )
  t.Branch( 'ystarjj'  ,  ystarjj,    'ystarjj/F' )

  # generate events
  pythia = Pythia(config=runtype+'.cmd')
  events = pythia(events=nevents)
  #print(type(events))

  # loop over events 
  for e in events:  

    # get the event record
    allparts = e.all(return_hepmc=True)
  
    # get the two outgoing partons
  
    j1 = ROOT.TLorentzVector()
    j2 = ROOT.TLorentzVector()
  
    count=0
    for p in allparts:    
      # status 23 denotes outgoing particle from subprocess
      if p.status==23:
        # print("Particle:")
        # print("count=",count,"  p=",p)
      
        if count==0:
          j1.SetPxPyPzE(p.px, p.py, p.pz, p.e)
          count+=1
        else:
          j2.SetPxPyPzE(p.px, p.py, p.pz, p.e)
          break
        
    ptj1[0]    = j1.Pt()
    etaj1[0]   = j1.Eta()
    phij1[0]   = j1.Phi()
    ej1[0]     = j1.E()

    ptj2[0]    = j2.Pt()
    etaj2[0]   = j2.Eta()
    phij2[0]   = j2.Phi()
    ej2[0]     = j2.E()

    mjj[0]     = (j1+j2).M()
    ystarjj[0] = abs(j1.Eta()-j2.Eta())/2
  
#    print("ptj1[0]    : ",ptj1[0]   )
#    print("etaj1[0]   : ",etaj1[0]  )
#    print("phij1[0]   : ",phij1[0]  )
#    print("ej1[0]     : ",ej1[0]    )
#
#    print("ptj2[0]    : ",ptj2[0]   )
#    print("etaj2[0]   : ",etaj2[0]  )
#    print("phij2[0]   : ",phij2[0]  )
#    print("ej2[0]     : ",ej2[0]    )
#
#    print("mjj[0]     : ",mjj[0]    )
#    print("ystarjj[0] : ",ystarjj[0])

  
    t.Fill()

      
  fout.cd()
  t.Write()
  fout.Close()      
    
      
      
      
    
