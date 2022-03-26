import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
from PySide2.QtWidgets
commandName = 'hello'

class MyCommandClass( OpenMayaMPx.MPxCommand ):
    
    def __init__(self):
        ''' Constructor. '''
        OpenMayaMPx.MPxCommand.__init__(self)
    
    def doIt(self, args):
        ''' Command execution. '''
        
        print 'hello world!'

def cmdCreator():
    ''' Create an instance of our command. '''
    return OpenMayaMPx.asMPxPtr( MyCommandClass() )

def initializePlugin( mobject ):
    ''' Initialize the plug-in when Maya loads it. '''
    mplugin = OpenMayaMPx.MFnPlugin( mobject )
    try:
        mplugin.registerCommand( commandName, cmdCreator )
    except:
        sys.stderr.write( 'Failed to register command: ' + commandName )

def uninitializePlugin( mobject ):
    ''' Uninitialize the plug-in when Maya un-loads it. '''
    mplugin = OpenMayaMPx.MFnPlugin( mobject )
    try:
        mplugin.deregisterCommand( commandName )
    except:
        sys.stderr.write( 'Failed to unregister command: ' + commandName )