import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
matplotlib.pyplot.plot( backLegSensorValues, linewidth=5, label='back leg')
matplotlib.pyplot.plot(frontLegSensorValues, linewidth=5, label='front leg')


matplotlib.pyplot.legend()

matplotlib.pyplot.show()