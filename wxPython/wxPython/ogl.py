## This file reverse renames symbols in the wx package to give
## them their wx prefix again, for backwards compatibility.
##
## Generated by ./distrib/build_renamers.py

# This silly stuff here is so the wxPython.wx module doesn't conflict
# with the wx package.  We need to import modules from the wx package
# here, then we'll put the wxPython.wx entry back in sys.modules.
import sys
_wx = None
if sys.modules.has_key('wxPython.wx'):
    _wx = sys.modules['wxPython.wx']
    del sys.modules['wxPython.wx']

import wx.ogl

sys.modules['wxPython.wx'] = _wx
del sys, _wx


# Now assign all the reverse-renamed names:
wxShapeRegion = wx.ogl.ShapeRegion
wxPyShapeEvtHandler = wx.ogl.PyShapeEvtHandler
wxPyShape = wx.ogl.PyShape
oglMETAFLAGS_OUTLINE = wx.ogl.oglMETAFLAGS_OUTLINE
oglMETAFLAGS_ATTACHMENTS = wx.ogl.oglMETAFLAGS_ATTACHMENTS
wxPseudoMetaFile = wx.ogl.PseudoMetaFile
wxPyRectangleShape = wx.ogl.PyRectangleShape
wxPyControlPoint = wx.ogl.PyControlPoint
wxPyBitmapShape = wx.ogl.PyBitmapShape
wxPyDrawnShape = wx.ogl.PyDrawnShape
wxOGLConstraint = wx.ogl.OGLConstraint
wxPyCompositeShape = wx.ogl.PyCompositeShape
wxPyDividedShape = wx.ogl.PyDividedShape
wxPyDivisionShape = wx.ogl.PyDivisionShape
wxPyEllipseShape = wx.ogl.PyEllipseShape
wxPyCircleShape = wx.ogl.PyCircleShape
wxArrowHead = wx.ogl.ArrowHead
wxPyLineShape = wx.ogl.PyLineShape
wxPyPolygonShape = wx.ogl.PyPolygonShape
wxPyTextShape = wx.ogl.PyTextShape
wxDiagram = wx.ogl.Diagram
wxPyShapeCanvas = wx.ogl.PyShapeCanvas
KEY_SHIFT = wx.ogl.KEY_SHIFT
KEY_CTRL = wx.ogl.KEY_CTRL
ARROW_NONE = wx.ogl.ARROW_NONE
ARROW_END = wx.ogl.ARROW_END
ARROW_BOTH = wx.ogl.ARROW_BOTH
ARROW_MIDDLE = wx.ogl.ARROW_MIDDLE
ARROW_START = wx.ogl.ARROW_START
ARROW_HOLLOW_CIRCLE = wx.ogl.ARROW_HOLLOW_CIRCLE
ARROW_FILLED_CIRCLE = wx.ogl.ARROW_FILLED_CIRCLE
ARROW_ARROW = wx.ogl.ARROW_ARROW
ARROW_SINGLE_OBLIQUE = wx.ogl.ARROW_SINGLE_OBLIQUE
ARROW_DOUBLE_OBLIQUE = wx.ogl.ARROW_DOUBLE_OBLIQUE
ARROW_METAFILE = wx.ogl.ARROW_METAFILE
ARROW_POSITION_END = wx.ogl.ARROW_POSITION_END
ARROW_POSITION_START = wx.ogl.ARROW_POSITION_START
CONTROL_POINT_VERTICAL = wx.ogl.CONTROL_POINT_VERTICAL
CONTROL_POINT_HORIZONTAL = wx.ogl.CONTROL_POINT_HORIZONTAL
CONTROL_POINT_DIAGONAL = wx.ogl.CONTROL_POINT_DIAGONAL
CONTROL_POINT_ENDPOINT_TO = wx.ogl.CONTROL_POINT_ENDPOINT_TO
CONTROL_POINT_ENDPOINT_FROM = wx.ogl.CONTROL_POINT_ENDPOINT_FROM
CONTROL_POINT_LINE = wx.ogl.CONTROL_POINT_LINE
FORMAT_NONE = wx.ogl.FORMAT_NONE
FORMAT_CENTRE_HORIZ = wx.ogl.FORMAT_CENTRE_HORIZ
FORMAT_CENTRE_VERT = wx.ogl.FORMAT_CENTRE_VERT
FORMAT_SIZE_TO_CONTENTS = wx.ogl.FORMAT_SIZE_TO_CONTENTS
LINE_ALIGNMENT_HORIZ = wx.ogl.LINE_ALIGNMENT_HORIZ
LINE_ALIGNMENT_VERT = wx.ogl.LINE_ALIGNMENT_VERT
LINE_ALIGNMENT_TO_NEXT_HANDLE = wx.ogl.LINE_ALIGNMENT_TO_NEXT_HANDLE
LINE_ALIGNMENT_NONE = wx.ogl.LINE_ALIGNMENT_NONE
SHADOW_NONE = wx.ogl.SHADOW_NONE
SHADOW_LEFT = wx.ogl.SHADOW_LEFT
SHADOW_RIGHT = wx.ogl.SHADOW_RIGHT
OP_CLICK_LEFT = wx.ogl.OP_CLICK_LEFT
OP_CLICK_RIGHT = wx.ogl.OP_CLICK_RIGHT
OP_DRAG_LEFT = wx.ogl.OP_DRAG_LEFT
OP_DRAG_RIGHT = wx.ogl.OP_DRAG_RIGHT
OP_ALL = wx.ogl.OP_ALL
ATTACHMENT_MODE_NONE = wx.ogl.ATTACHMENT_MODE_NONE
ATTACHMENT_MODE_EDGE = wx.ogl.ATTACHMENT_MODE_EDGE
ATTACHMENT_MODE_BRANCHING = wx.ogl.ATTACHMENT_MODE_BRANCHING
BRANCHING_ATTACHMENT_NORMAL = wx.ogl.BRANCHING_ATTACHMENT_NORMAL
BRANCHING_ATTACHMENT_BLOB = wx.ogl.BRANCHING_ATTACHMENT_BLOB
gyCONSTRAINT_CENTRED_VERTICALLY = wx.ogl.gyCONSTRAINT_CENTRED_VERTICALLY
gyCONSTRAINT_CENTRED_HORIZONTALLY = wx.ogl.gyCONSTRAINT_CENTRED_HORIZONTALLY
gyCONSTRAINT_CENTRED_BOTH = wx.ogl.gyCONSTRAINT_CENTRED_BOTH
gyCONSTRAINT_LEFT_OF = wx.ogl.gyCONSTRAINT_LEFT_OF
gyCONSTRAINT_RIGHT_OF = wx.ogl.gyCONSTRAINT_RIGHT_OF
gyCONSTRAINT_ABOVE = wx.ogl.gyCONSTRAINT_ABOVE
gyCONSTRAINT_BELOW = wx.ogl.gyCONSTRAINT_BELOW
gyCONSTRAINT_ALIGNED_TOP = wx.ogl.gyCONSTRAINT_ALIGNED_TOP
gyCONSTRAINT_ALIGNED_BOTTOM = wx.ogl.gyCONSTRAINT_ALIGNED_BOTTOM
gyCONSTRAINT_ALIGNED_LEFT = wx.ogl.gyCONSTRAINT_ALIGNED_LEFT
gyCONSTRAINT_ALIGNED_RIGHT = wx.ogl.gyCONSTRAINT_ALIGNED_RIGHT
gyCONSTRAINT_MIDALIGNED_TOP = wx.ogl.gyCONSTRAINT_MIDALIGNED_TOP
gyCONSTRAINT_MIDALIGNED_BOTTOM = wx.ogl.gyCONSTRAINT_MIDALIGNED_BOTTOM
gyCONSTRAINT_MIDALIGNED_LEFT = wx.ogl.gyCONSTRAINT_MIDALIGNED_LEFT
gyCONSTRAINT_MIDALIGNED_RIGHT = wx.ogl.gyCONSTRAINT_MIDALIGNED_RIGHT
DIVISION_SIDE_NONE = wx.ogl.DIVISION_SIDE_NONE
DIVISION_SIDE_LEFT = wx.ogl.DIVISION_SIDE_LEFT
DIVISION_SIDE_TOP = wx.ogl.DIVISION_SIDE_TOP
DIVISION_SIDE_RIGHT = wx.ogl.DIVISION_SIDE_RIGHT
DIVISION_SIDE_BOTTOM = wx.ogl.DIVISION_SIDE_BOTTOM
wxOGLInitialize = wx.ogl.OGLInitialize
wxOGLCleanUp = wx.ogl.OGLCleanUp
wxShapeCanvas = wx.ogl.ShapeCanvas
wxShapeEvtHandler = wx.ogl.ShapeEvtHandler
wxShape = wx.ogl.Shape
wxRectangleShape = wx.ogl.RectangleShape
wxBitmapShape = wx.ogl.BitmapShape
wxDrawnShape = wx.ogl.DrawnShape
wxCompositeShape = wx.ogl.CompositeShape
wxDividedShape = wx.ogl.DividedShape
wxDivisionShape = wx.ogl.DivisionShape
wxEllipseShape = wx.ogl.EllipseShape
wxCircleShape = wx.ogl.CircleShape
wxLineShape = wx.ogl.LineShape
wxPolygonShape = wx.ogl.PolygonShape
wxTextShape = wx.ogl.TextShape
wxControlPoint = wx.ogl.ControlPoint


