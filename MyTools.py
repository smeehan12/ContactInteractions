from ROOT import TH1F

def GetMaxFromHists( allHists, debug=False):

    maxbin = 0
    maxloc = 0
    maxval = 0
    
    for hist in allHists:
        temp_maxbin = hist.GetMaximumBin()
        temp_maxloc = hist.GetXaxis().GetBinCenter(temp_maxbin)
        temp_maxval = hist.GetBinContent(temp_maxbin)
        
        if debug:
            print("Testing Max Hist : ",hist)
            print("Values : ",temp_maxbin,temp_maxloc,temp_maxval)

        if temp_maxval>maxval:
            maxbin = temp_maxbin
            maxloc = temp_maxloc
            maxval = temp_maxval

    return maxbin,maxloc,maxval
    
def GetMinMaxFromSetList( allSets, debug=False):
    myMin = 100000
    myMax = -1
    
    for thisSet in allSets:
    
        if len(thisSet)==0:
            continue
        
        thisMin = min(thisSet)
        thisMax = max(thisSet)
        
        if thisMin<myMin:
            myMin=thisMin
        if thisMax>myMax:
            myMax = thisMax
          
    if debug==True:
        print("Set min,max : ",myMin,myMax)
          
    return myMin,myMax



    
def SetTitleStyle(input,mcolor,msize,mstyle,lcolor,lsize,lstyle,title,xaxis,yaxis):
    input.SetDirectory(0)

    input.SetMarkerColor(mcolor)
    input.SetMarkerSize(msize)
    input.SetMarkerStyle(mstyle)
    
    input.SetLineColor(lcolor)
    input.SetLineWidth(lcolor)
    input.SetLineStyle(lcolor)
    
    input.SetTitle(title)
    input.GetXaxis().SetTitle(xaxis)
    input.GetYaxis().SetTitle(yaxis)

    return input
    
    
def SetGraphTitleStyle(input,mcolor,msize,mstyle,lcolor,lsize,lstyle,title,xaxis,yaxis):

    input.SetMarkerColor(mcolor)
    input.SetMarkerSize(msize)
    input.SetMarkerStyle(mstyle)
    
    input.SetLineColor(lcolor)
    input.SetLineWidth(lcolor)
    input.SetLineStyle(lcolor)
    
    input.SetTitle(title)
    input.GetXaxis().SetTitle(xaxis)
    input.GetYaxis().SetTitle(yaxis)

    return input
