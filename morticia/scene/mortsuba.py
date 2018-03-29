__author__ = 'DGriffith'
"""
 *--------------------------------------------------------------------
 *
 * This file is part of MORTICIA.
 * Copyright (c) 2015-2018 by Derek Griffith
 *
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 *--------------------------------------------------------------------"""

"""
Class for Mitsuba support
"""
#import lxml
#import mitsuba

class Mitsuba(object):
    """ The Mitsuba class encapsulates the information provided in a Mitsuba scene file (.xml).
    This class contains the information in the scene file in an acesssible format for the purpose
    of manipulating Mitsuba scenes, writing the updated scene file and performing rendering
    in a multiprocessing environment.

    """
    import mitsuba
    def __init__(self, scenefile=None, paramMap=None, scenefolder=None):
        """

        :param scenefile: Name of file from which to load a scene (string). Must not include the path, but must have
        the extension .xml.
        :param paramMap: Dictionary of parameters which will get substituted when the scene is loaded.
        :param scenefolder: Path to the folder containing the scene if not in current directory. A list of folders in
        which to search for the scene can also be provided (string or list of strings).
        :return:
        """
        from mitsuba.core import *
        from mitsuba.render import SceneHandler
        # Set up the file resolver for this Mitsuba object
        # Get a reference to the threads file resolver
        self.fileResolver = Thread.getThread().getFileResolver()
        if scenefolder is not None:  # the user input something
            if scenefolder:  #  not blank
                if isinstance(scenefolder, basestring):
                    self.fileResolver.appendPath(scenefolder)
                else:  # assume a list of strings
                    for path in scenefolder:
                        self.fileResolver.appendPath(path)

        # Read in the scene file if requested
        if scenefile is not None:
            if not scenefile:
                # Open a dialog to get the filename
                import easygui
                filename = easygui.fileopenbox(msg='Please select a Mitsuba scene file.', filetypes=["*.xml"])
            # Load the scene
            self.scene = Scenehandler.loadScene(
                           self.fileResolver.resolve(scenefile), paramMap)

