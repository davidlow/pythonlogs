dt = DAQ_Transport(instruments, -1, 1, Rbias=1, rate = 10, numpts = 100)
dt.run()