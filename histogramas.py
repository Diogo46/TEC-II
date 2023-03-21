import ROOT 

file = ROOT.TFile("teste.root","READ")
fileToWrite = ROOT.TFile("canvas.root","RECREATE")

tree = file.Get("eventos")

#tree.Scan("*")
#histogram = tree.Draw("Nep", "FlagFluo==0")

Xmin = tree.GetMinimum("Nep")
Xmax = tree.GetMaximum('Nep')

nBins = int(Xmax-Xmin+1)

canvas1 = ROOT.TCanvas("FlagFluoCanvas", "FlagFluoCanvas")
canvas2 = ROOT.TCanvas("NoFlagFluoCanvas", "NoFlagFluoCanvas")
canvas3 = ROOT.TCanvas("BothFlagFluoCanvas", "BothFlagFluoCanvas")



histogram = ROOT.TH1I('FlagFluo', 'FlagFluo', nBins, Xmin, Xmax)

tree.Draw("Nep >> FlagFluo","FlagFluo==0","goff")

#histogram2 = tree.Draw("Nep", "FlagFluo!=0")

histogram2 = ROOT.TH1I('NoFlagFluo', 'NoFlagFluo', nBins, Xmin, Xmax)

tree.Draw("Nep >> NoFlagFluo","FlagFluo!=0","goff")

histogram.SetLineColor(ROOT.kBlack)
histogram.SetFillColor(ROOT.kRed)

histogram2.SetLineColor(ROOT.kBlack)
histogram2.SetFillColor(ROOT.kBlue)


histogram.GetYaxis().SetTitle("Counts")
histogram.GetYaxis().CenterTitle(True)
histogram.GetXaxis().SetTitle("Nep")
histogram.GetXaxis().CenterTitle(True)

histogram2.GetYaxis().SetTitle("Counts")
histogram2.GetYaxis().CenterTitle(True)
histogram2.GetXaxis().SetTitle("Nep")
histogram2.GetXaxis().CenterTitle(True)

legend1 = ROOT.TLegend(0.1,0.7, 0.34,0.9)
legend1.AddEntry(histogram, "FlagFluo")

legend2 = ROOT.TLegend(0.1,0.7, 0.34,0.9)
legend2.AddEntry(histogram2,"NoFlagFluo")

legend3 = ROOT.TLegend(0.1,0.7, 0.34,0.9)
legend3.AddEntry(histogram, "FlagFluo")
legend3.AddEntry(histogram2,"NoFlagFluo")

canvas1.cd()
histogram.Draw("hist")
legend1.Draw()

canvas2.cd()
histogram2.Draw("hist")
legend2.Draw()

canvas3.cd()
histogram.Draw("hist")
histogram2.Draw("same")
legend3.Draw()

canvas1.Write()
canvas2.Write()
canvas3.Write()

