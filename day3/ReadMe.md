## Maya Libraries
1. OpenMaya
2. OpenMayaUI
3. OpenMayaAnim
   1. deformers
   2. inverse kinematics
4. OpenMayaFX
   1. classes for AutoDesk Dynamics
5. OpenMayaRender
6. OpenMayaMPx
   1. classes for proxy objects, no C++
7. OpenMayaCloth
## Class Categories
1. Proxy Classes: MPx**.
   1. MPxCommand, MPxNode
2. Function Set Classes:
3. MObject
4. Iterator Classes: MIt
   1. MItDag, MItMeshEdge
5. Wrapper Classes
   1. for simple classes such as MPoint, MVector
   2. Fully implemented python class

## API Command Utilities
### MGlobal

### Error Handling & Debugging

### DAG hierarchy (Directed Acyclic Graph)
1. A MDagPath is a handle describing a path to a node.
2. MObject is a wrapper around a pointer to determine what it is and what you can do with it.