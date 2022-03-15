import numpy as numpy
import pyrosim.pyrosim as pyrosim
import os


class SOLUTION:


    def __init__(self):



        self.weights = numpy.random.rand(3, 2)


        # print(self.weights)


        self.weights = self.weights * 2 - 1


        # print(self.weights)



    def Evaluate(self):
        os.system("python3 simulate.py")



    def Create_World():


        pyrosim.Start_SDF("world.sdf")


        pyrosim.Send_Cube(name="Box", pos=[1, 1, .5], size=[1, 1, 1])


        pyrosim.End()




    def Create_Body():


        pyrosim.Start_URDF("body.urdf")


        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])



        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",


                        child="BackLeg", type="revolute", position=[1, 0, 1])



        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[1, 1, 1])



        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",


                        child="FrontLeg", type="revolute", position=[2, 0, 1])



        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])



        pyrosim.End()




    def Create_Brain():


        pyrosim.Start_NeuralNetwork("brain.nndf")



        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso"),


        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg"),


        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")



        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )


        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )


        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )


        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -1.0 )



        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg"),


        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")



        for currentRow in range(3):


            for currentColumn in range(2):
                pyrosim.Send_Synapse(


                    sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])



        pyrosim.End()


