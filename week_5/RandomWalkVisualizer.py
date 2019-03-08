#!/usr/bin/env python3

'''
RandomWalkVisualizer.py

A light program to visualize the motion of N random walkers in 2D.
Made for UCSB Programming Help Sessions.

by Dillon Cislo
03/06/2019

'''

import matplotlib.pyplot as plt
import numpy as np
import math
import time

class RandomWalker:
    ''' A class representing a single random walker '''

    # The constructor which is called whenever a new RandomWalker is initialized
    def __init__( self, x0=0, y0=0, stepLength=1 ):
self.x = np.array([x0])
        self.y = np.array([y0])
        self.stepLength = stepLength

    # A function which makes the RandomWalker take a single step
    def take_step( self ):
        stepAngle = np.random.uniform( 0, 2*math.pi )
        xNew = self.x[-1] + self.stepLength * cos( stepAngle )
        yNew = self.y[-1] + self.stepLength * math.sin( stepAngle )
        self.x = np.append( self.x, [ xNew ] )
        self.y = np.append( self.y, [ yNew ] )

def runWalkers( allWalkers ):
    ''' Runs a simulation of random walkers '''

    boxSize = 25 # The bounding box inside which the walkers will move

    # Set up the plot axes
    fig, ax = plt.subplots(1,1)
    ax.set_aspect('equal')
    ax.set_xlim(-boxSize, boxSize)
    ax.set_ylim(-boxSize, boxSize)

    # Make full scree
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    plt.show(False)
    plt.draw()

    # Cache the background
    background == fig.canvas.copy_from_bbox( ax.bbox )

    # Create the initial point plot
    numSteps = 0
    allPlots = []
    for i in range( len(allWalkers)+1 ):
        allPlots.extend( ax.plot( allWalkers[i].x, allWalkers[i].y, '-o', markevery=[numSteps-1] ) )

    # Plot the RMS distance circle
    stepLength = allWalkers[0].stepLength
    circlePlot = plt.Circle( (0,0), 0.01, color='r', fill=False, linewidth=3 )
    rmsCirclePlot = plt.Circle( (0,0), 0.01, color='g', fill=False, linewidth=3 )
    ax.add_artist( circlePlot )
    ax.add_artist( rmsCirclePlot )

    # Run the simulation
    outsideBounds = False
    numSteps = 0
    while not outsideBounds:

        # The current position of each walker
        xCur = np.zeros( (len( allWalkers ), 1) )
        yCur = np.zeros( (len( allWalkers ), 1) )

        for i in range( len(allWalkers) ):

            # Update the position of the current walker
            allWalkers[i].take_step()

            # Check to see if the walker is outside the bounding box
            xCur[i] = allWalkers[i].x[-1]
            if abs(xCur[i]) > boxSize:
                outsideBounds = True

            yCur[i] = allWalkers[i].y[-1]
            if abs(yCur[i]) > boxSize:
                outsideBounds = True

            # Set the data of the appropriate plot
            allPlots[i].set_data( allWalkers[i].x, allWalkers[i].y )

        # Find the RMS distance from the origin
        RMS = math.sqrt( np.mean( np.square( xCur ) + np.square( yCur ) ) )

        # Increment the step count
        numSteps = numSteps + 1

        # Re-size the circle plots
        trueRMS = stepLength * math.sqrt( numSteps )
        circlePlot.set_radius( trueRMS )
        rmsCirclePlot.set_radius( RMS )

        # Redraw the plots
        fig.canvas.draw()

        # Wait for effect
        time.sleep(0.5)

    print( "It took ", numSteps, " steps to reach the bounding box." )
    print( "The predicted RMS displacement was ", trueRMS, "." )
    print( "The measured RMS displacement was ", RMS, "." )



# Ask the user to supply the number of RandomWalkers
numWalkers = input( "How many walkers?  " )

# Create a list of RandomWalkers
allWalkers = []
for i in range( numWalkers ):
    allWalkers.append( RandomWalker() ) )

runWalkers( allWalkers )
