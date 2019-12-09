from ROOT import TFile,TTree,TH1D,TH2D,TCanvas,gDirectory

# import the necessary local tools
import sys
import os
from MyTools import *
from AtlasStyleTools import *
SetAtlasStyle()


os.system("mkdir plots")


outtype="png"

nevents=10000

f_0 = TFile("config_sm_"+str(nevents)+".root")
t_0 = f_0.Get("tree")

f_1 = TFile("config_ci_"+str(nevents)+".root")
t_1 = f_1.Get("tree")

f_2 = TFile("config_sm_ci_"+str(nevents)+".root")
t_2 = f_2.Get("tree")

c1 = TCanvas("c1","c1",500,500)
c2 = TCanvas("c2","c2",580,500)
c2.SetRightMargin(0.20)










c1.cd()
t_0.Draw("mjj >> h0(100,0,1000)","","hist")
t_1.Draw("mjj >> h1(100,0,1000)","","hist")
t_2.Draw("mjj >> h2(100,0,1000)","","hist")

h0 = gDirectory.Get("h0")
h1 = gDirectory.Get("h1")
h2 = gDirectory.Get("h2")


h0.SetStats(0)
h0.GetXaxis().SetTitle("m(jj) [GeV]")
h0.GetYaxis().SetTitle("NEvents")
h0.SetMaximum(1.5*GetMaxFromHists([h0])[2])
h0.SetLineColor(1)
h0.Draw("hist")

h1.SetLineColor(2)
h1.Draw("histsame")

h2.SetLineColor(4)
h2.Draw("histsame")

ATLASLabel(0.2, 0.9, 0.25, 1, 0.05, "Internal")
#myText(0.2,0.85,1,0.04,""")
myLineText(0.7, 0.80, 0.1, 1, 1, 0.03, "SM Only")
myLineText(0.7, 0.75, 0.1, 2, 1, 0.03, "CI Only")
myLineText(0.7, 0.70, 0.1, 4, 1, 0.03, "SM+CI")
c1.SetLogy()
c1.SaveAs("plots/mjj."+outtype)


# c2.cd()
# t.Draw("abs(neutrino_eta):neutrino_e >> h2(100,0,1000,150,0,15)","abs(neutrino_flav)=="+type["id"]+" && par1_has!=0","colz")
# h2 = gDirectory.Get("h2")
# h2.SetStats(0)
# h2.GetXaxis().SetTitle("Energy [GeV]")
# h2.GetYaxis().SetTitle("abs[eta]")
# h2.GetZaxis().SetTitle("N(neutrinos)")
# h2.Draw("colz")
# 
# ATLASLabel(0.2, 0.9, 0.25, 1, 0.05, "Internal")
# myText(0.2,0.85,1,0.04,"Neutrino Flavor : "+type["flavor"])
# c2.SaveAs("plots/neutrino_eta_energy_"+type["flavor"]+"."+outtype)




  
  
  
  
  
  
  
  
  
  
  