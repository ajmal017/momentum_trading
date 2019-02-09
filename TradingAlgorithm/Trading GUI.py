
from ib.ext.Contract import Contract
from ib.ext.EWrapper import EWrapper
from ib.ext.EClientSocket import EClientSocket
from ib.opt import Connection, message
from tkinter import * # imports Tkinter
from tkinter import ttk

class Application(Frame):

    def __init__(self, master):
        """Initialize the Frame"""
        ttk.Frame.__init__(self, master)

        self.port=7497
        self.client_id = 88 # this can be any number
        self.grid()
        self.create_widgets()

    def create_widgets(self): # Method or function
        """Create the window layout"""

        myFont = ('Lucida Grande', 12)

        #**************************************** Connect / Disconnect Frames *****************************************

        # create tab for Connect / Disconnect Info
        n = ttk.Notebook(root)
        f0 = ttk.Frame(n)  # frame with Connect / Disconnect widgets gridded to it
        n.add(f0, text='Connection to TWS')
        n.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=W)

        # create connect / disconnect button widget
        self.btnConnect = ttk.Button(f0, text='Connect', command=self.connect_to_tws).grid(row=0, column=0, sticky = W)
        self.btnDisconnect = ttk.Button(f0, text="Disconnect", command=self.disconnect_it).grid(row=0, column=1, sticky = W)

        # create placeholder box for TWS to return time of successful connection
        self.eventLogMessages = Text(f0, font=myFont, width=120, height=2)
        self.eventLogMessages.pack()
        self.eventLogMessages.insert(END, EventLogMessagesPlaceholder)
        self.eventLogMessages.grid(row=1, column=0, columnspan=20, sticky=N)


        #*********************************************** Market Data **************************************************

        # create tab for market data to be displayed
        n = ttk.Notebook(root)
        f1 = ttk.Frame(n)   # frame with market data widgets gridded to it
        n.add(f1, text='Market Data')
        n.grid(row=1, column=0, padx=5, sticky = N)

        # create Market Depth table labels
        self.marketDataLabel1 = Label(f1, font=myFont, width = 30, text="Bid").grid(row=0, column=0, columnspan=3, pady=5)
        self.marketDataLabel2 = Label(f1, font=myFont, width = 10, text="Deviation").grid(row=0, column=3, pady=5)
        self.marketDataLabel3 = Label(f1, font=myFont, width = 30, text="Ask").grid(row=0, column=4, columnspan=3, pady=5)
        self.marketDataLabel4 = Label(f1, font=myFont, width = 10, text="Price").grid(row=1, column=0, pady=1)
        self.marketDataLabel5 = Label(f1, font=myFont, width = 10, text="Size").grid(row=1, column=1, pady=1)
        self.marketDataLabel6 = Label(f1, font=myFont, width = 10, text="Cum Size").grid(row=1, column=2, pady=1)
        self.marketDataLabel7 = Label(f1, font=myFont, width = 10, text="Cum Size").grid(row=1, column=4, pady=1)
        self.marketDataLabel8 = Label(f1, font=myFont, width = 10, text="Size").grid(row=1, column=5, pady=1)
        self.marketDataLabel9 = Label(f1, font=myFont, width = 10, text="Price").grid(row=1, column=6, pady=1)

        # create deviation labels for Market Data
        self.devLabel1 = Label(f1, font=myFont, width = 2, text="1").grid(row=2, column=3)
        self.devLabel2 = Label(f1, font=myFont, width = 2, text="2").grid(row=3, column=3)
        self.devLabel3 = Label(f1, font=myFont, width = 2, text="3").grid(row=4, column=3)
        self.devLabel4 = Label(f1, font=myFont, width = 2, text="4").grid(row=5, column=3)
        self.devLabel5 = Label(f1, font=myFont, width = 2, text="5").grid(row=6, column=3)
        self.devLabel6 = Label(f1, font=myFont, width = 2, text="6").grid(row=7, column=3)
        self.devLabel7 = Label(f1, font=myFont, width = 2, text="7").grid(row=8, column=3)
        self.devLabel8 = Label(f1, font=myFont, width = 2, text="8").grid(row=9, column=3)
        self.devLabel9 = Label(f1, font=myFont, width = 2, text="9").grid(row=10, column=3)
        self.devLabel10 = Label(f1, font=myFont, width = 2, text="10").grid(row=11, column=3)

        # placeholders for market data outputs
        self.bidPriceOne = Entry(f1, font=myFont, width=10).grid(row=2, column=0)
        self.bidPriceTwo = Entry(f1, font=myFont, width=10).grid(row=3, column=0)
        self.bidPriceThree = Entry(f1, font=myFont, width=10).grid(row=4, column=0)
        self.bidPriceFour = Entry(f1, font=myFont, width=10).grid(row=5, column=0)
        self.bidPriceFive = Entry(f1, font=myFont, width=10).grid(row=6, column=0)
        self.bidPriceSix = Entry(f1, font=myFont, width=10).grid(row=7, column=0)
        self.bidPriceSeven = Entry(f1, font=myFont, width=10).grid(row=8, column=0)
        self.bidPriceEight = Entry(f1, font=myFont, width=10).grid(row=9, column=0)
        self.bidPriceNine = Entry(f1, font=myFont, width=10).grid(row=10, column=0)
        self.bidPriceTen = Entry(f1, font=myFont, width=10).grid(row=11, column=0)

        self.bidSizeOne = Entry(f1, font=myFont, width=10).grid(row=2, column=1)
        self.bidSizeTwo = Entry(f1, font=myFont, width=10).grid(row=3, column=1)
        self.bidSizeThree = Entry(f1, font=myFont, width=10).grid(row=4, column=1)
        self.bidSizeFour = Entry(f1, font=myFont, width=10).grid(row=5, column=1)
        self.bidSizeFive = Entry(f1, font=myFont, width=10).grid(row=6, column=1)
        self.bidSizeSix = Entry(f1, font=myFont, width=10).grid(row=7, column=1)
        self.bidSizeSeven = Entry(f1, font=myFont, width=10).grid(row=8, column=1)
        self.bidSizeEight = Entry(f1, font=myFont, width=10).grid(row=9, column=1)
        self.bidSizeNine = Entry(f1, font=myFont, width=10).grid(row=10, column=1)
        self.bidSizeTen = Entry(f1, font=myFont, width=10).grid(row=11, column=1)

        self.bidCumSizeOne = Entry(f1, font=myFont, width=10).grid(row=2, column=2)
        self.bidCumSizeTwo = Entry(f1, font=myFont, width=10).grid(row=3, column=2)
        self.bidCumSizeThree = Entry(f1, font=myFont, width=10).grid(row=4, column=2)
        self.bidCumSizeFour = Entry(f1, font=myFont, width=10).grid(row=5, column=2)
        self.bidCumSizeFive = Entry(f1, font=myFont, width=10).grid(row=6, column=2)
        self.bidCumSizeSix = Entry(f1, font=myFont, width=10).grid(row=7, column=2)
        self.bidCumSizeSeven = Entry(f1, font=myFont, width=10).grid(row=8, column=2)
        self.bidCumSizeEight = Entry(f1, font=myFont, width=10).grid(row=9, column=2)
        self.bidCumSizeNine = Entry(f1, font=myFont, width=10).grid(row=10, column=2)
        self.bidCumSizeTen = Entry(f1, font=myFont, width=10).grid(row=11, column=2)

        self.askPriceOne = Entry(f1, font=myFont, width=10).grid(row=2, column=6)
        self.askPriceTwo = Entry(f1, font=myFont, width=10).grid(row=3, column=6)
        self.askPriceThree = Entry(f1, font=myFont, width=10).grid(row=4, column=6)
        self.askPriceFour = Entry(f1, font=myFont, width=10).grid(row=5, column=6)
        self.askPriceFive = Entry(f1, font=myFont, width=10).grid(row=6, column=6)
        self.askPriceSix = Entry(f1, font=myFont, width=10).grid(row=7, column=6)
        self.askPriceSeven = Entry(f1, font=myFont, width=10).grid(row=8, column=6)
        self.askPriceEight = Entry(f1, font=myFont, width=10).grid(row=9, column=6)
        self.askPriceNine = Entry(f1, font=myFont, width=10).grid(row=10, column=6)
        self.askPriceTen = Entry(f1, font=myFont, width=10).grid(row=11, column=6)

        self.askSizeOne = Entry(f1, font=myFont, width=10).grid(row=2, column=5)
        self.askSizeTwo = Entry(f1, font=myFont, width=10).grid(row=3, column=5)
        self.askSizeThree = Entry(f1, font=myFont, width=10).grid(row=4, column=5)
        self.askSizeFour = Entry(f1, font=myFont, width=10).grid(row=5, column=5)
        self.askSizeFive = Entry(f1, font=myFont, width=10).grid(row=6, column=5)
        self.askSizeSix = Entry(f1, font=myFont, width=10).grid(row=7, column=5)
        self.askSizeSeven = Entry(f1, font=myFont, width=10).grid(row=8, column=5)
        self.askSizeEight = Entry(f1, font=myFont, width=10).grid(row=9, column=5)
        self.askSizeNine = Entry(f1, font=myFont, width=10).grid(row=10, column=5)
        self.askSizeTen = Entry(f1, font=myFont, width=10).grid(row=11, column=5)

        self.askCumSizeOne = Entry(f1, font=myFont, width=10).grid(row=2, column=4)
        self.askCumSizeTwo = Entry(f1, font=myFont, width=10).grid(row=3, column=4)
        self.askCumSizeThree = Entry(f1, font=myFont, width=10).grid(row=4, column=4)
        self.askCumSizeFour = Entry(f1, font=myFont, width=10).grid(row=5, column=4)
        self.askCumSizeFive = Entry(f1, font=myFont, width=10).grid(row=6, column=4)
        self.askCumSizeSix = Entry(f1, font=myFont, width=10).grid(row=7, column=4)
        self.askCumSizeSeven = Entry(f1, font=myFont, width=10).grid(row=8, column=4)
        self.askCumSizeEight = Entry(f1, font=myFont, width=10).grid(row=9, column=4)
        self.askCumSizeNine = Entry(f1, font=myFont, width=10).grid(row=10, column=4)
        self.askCumSizeTen = Entry(f1, font=myFont, width=10).grid(row=11, column=4)


        # ******************************************** Market Weightings ***********************************************

        # create tab for market weightings to be displayed
        n = ttk.Notebook(root)
        f2 = ttk.Frame(n)  # frame with marketing weighting widgets gridded to it
        n.add(f2, text='Weighting')
        n.grid(row=1, column=1, padx=5, sticky=N)

        # create Market Weighting table labels
        self.marketWeightLabel1 = Label(f2, font=myFont, width=20, text="Weighting").grid(row=0, column=1, columnspan=2, pady=5)
        self.marketWeightLabel2 = Label(f2, font=myFont, width=10, text="Deviation").grid(row=1, column=0, pady=1)
        self.marketWeightLabel3 = Label(f2, font=myFont, width=10, text="Bid").grid(row=1, column=1, pady=1)
        self.marketWeightLabel4 = Label(f2, font=myFont, width=10, text="Ask").grid(row=1, column=2, pady=1)

        # create deviation labels for Market Weightings
        self.devLabel1 = Label(f2, font=myFont, width=2, text="1").grid(row=2, column=0)
        self.devLabel2 = Label(f2, font=myFont, width=2, text="2").grid(row=3, column=0)
        self.devLabel3 = Label(f2, font=myFont, width=2, text="3").grid(row=4, column=0)
        self.devLabel4 = Label(f2, font=myFont, width=2, text="4").grid(row=5, column=0)
        self.devLabel5 = Label(f2, font=myFont, width=2, text="5").grid(row=6, column=0)
        self.devLabel6 = Label(f2, font=myFont, width=2, text="6").grid(row=7, column=0)
        self.devLabel7 = Label(f2, font=myFont, width=2, text="7").grid(row=8, column=0)
        self.devLabel8 = Label(f2, font=myFont, width=2, text="8").grid(row=9, column=0)
        self.devLabel9 = Label(f2, font=myFont, width=2, text="9").grid(row=10, column=0)
        self.devLabel10 = Label(f2, font=myFont, width=2, text="10").grid(row=11, column=0)

        # placeholders for market weighting outputs
        self.bidWeightOne = Entry(f2, font=myFont, width=10).grid(row=2, column=1)
        self.bidWeightTwo = Entry(f2, font=myFont, width=10).grid(row=3, column=1)
        self.bidWeightThree = Entry(f2, font=myFont, width=10).grid(row=4, column=1)
        self.bidWeightFour = Entry(f2, font=myFont, width=10).grid(row=5, column=1)
        self.bidWeightFive = Entry(f2, font=myFont, width=10).grid(row=6, column=1)
        self.bidWeightSix = Entry(f2, font=myFont, width=10).grid(row=7, column=1)
        self.bidWeightSeven = Entry(f2, font=myFont, width=10).grid(row=8, column=1)
        self.bidWeightEight = Entry(f2, font=myFont, width=10).grid(row=9, column=1)
        self.bidWeightNine = Entry(f2, font=myFont, width=10).grid(row=10, column=1)
        self.bidWeightTen = Entry(f2, font=myFont, width=10).grid(row=11, column=1)

        self.askWeightOne = Entry(f2, font=myFont, width=10).grid(row=2, column=2)
        self.askWeightTwo = Entry(f2, font=myFont, width=10).grid(row=3, column=2)
        self.askWeightThree = Entry(f2, font=myFont, width=10).grid(row=4, column=2)
        self.askWeightFour = Entry(f2, font=myFont, width=10).grid(row=5, column=2)
        self.askWeightFive = Entry(f2, font=myFont, width=10).grid(row=6, column=2)
        self.askWeightSix = Entry(f2, font=myFont, width=10).grid(row=7, column=2)
        self.askWeightSeven = Entry(f2, font=myFont, width=10).grid(row=8, column=2)
        self.askWeightEight = Entry(f2, font=myFont, width=10).grid(row=9, column=2)
        self.askWeightNine = Entry(f2, font=myFont, width=10).grid(row=10, column=2)
        self.askWeightTen = Entry(f2, font=myFont, width=10).grid(row=11, column=2)


        # ************************************************ Graph ******************************************************

        # create tab for Graph to be displayed
        n = ttk.Notebook(root)
        f3 = ttk.Frame(n)  # frame with graph widgets gridded to it
        n.add(f3, text='Visualization')
        n.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=N)

        # create placeholder box for graph
        self.weightingGraph = Text(f3, font=myFont, width=120, height=10)
        self.weightingGraph.pack()
        self.weightingGraph.insert(END, graphPlaceholder)
        self.weightingGraph.grid(row=1, column=0, columnspan=2, pady=5, sticky=W)



    def connect_to_tws(self):
        self.tws_conn = Connection.create(port=self.port, clientId=self.client_id)
        self.tws_conn.connect()

    def disconnect_it(self):
        self.tws_conn.disconnect()




root = Tk() # declares root as the TKinter main window
root.title("Momentum Trading") # titles main window
root.geometry('1050x800') # sets size of of main window
root.attributes('-topmost', True) # forces main window to always be in front

EventLogMessagesPlaceholder = """To be populated with event log info"""
graphPlaceholder = """Placeholder for Graph"""

app = Application(root)

root.mainloop()

