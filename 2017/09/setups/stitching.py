from datetime import datetime
import types

numx = 2
numy = 2
step_size = 100 # Step 100 attosteps
scans = []
tds = []
movements = []
res_readouts = []

foldername = datetime.now().strftime("%Y-%m-%d_%H%M%S_scan_series")

for y in range(numy):
    for x in range(numx):
        if y % 2:
            movements.append((step_size, 0))
        else:
            movements.append((-1 * step_size, 0))
    movements.append((0, step_size))
    
def start():
    for move in movements:
        if move[0] != 0:
            print("sweeping down")
            pz.z.sweep(pz.z.V, -400, sweep_rate=100)
            print("moving")
            atto.x.step(move[0])
        if move[1] != 0:
            print("sweeping down")
            pz.z.sweep(pz.z.V, -400, sweep_rate=100)
            print("moving")
            atto.y.step(move[1])
        scan = Scanplane(instruments, plane=plane, numpts=[1000,25],
                         scanheight=15, scan_rate=150)
        print("scanning", scan.filename)
        saveinfolder(foldername, scan)
        scan.run()
        scans.append(scan)
        res_readouts.append((atto.x.pos, atto.y.pos))
        plt.close("all")

    


def saveinfolder(foldername, obj):
    def newsave(self, **kwargs):
        return super(type(obj), obj).save(appendedpath=foldername,
                                              **kwargs)
    obj.save = types.MethodType(newsave, obj)

