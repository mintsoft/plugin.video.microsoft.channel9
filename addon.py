##############################################################################
#
# Microsoft Channel 9 - Video addon for XBMC
# http://channel9.msdn.com
#
# Version 1.0
# 
# Coding by Dan Dar3 
# http://dandar3.blogspot.com
#
#
# Credits:
#   * Team XBMC                                                         [http://xbmc.org/]
#   * The Channel 9 Team @ Microsoft                                    [http://channel9.msdn.com/About]
#   * Leonard Richardson <leonardr@segfault.org> - BeautifulSoup 3.0.7a [http://www.crummy.com/software/BeautifulSoup/]
#

# 
# Constants
#
__addon__   = "Microsoft Channel 9"
__author__  = "Dan Dar3"
__url__     = "http://dandar3.blogspot.com"
__date__    = "22 May 2011"
__version__ = "1.0"

#
# Imports
#
import os
import sys
import xbmcaddon

__settings__ = xbmcaddon.Addon()
rootDir = __settings__.getAddonInfo('path')
if rootDir[-1] == ';':
    rootDir = rootDir[0:-1]
rootDir = xbmc.translatePath(rootDir)

LIB_DIR = xbmc.translatePath( os.path.join( rootDir, 'resources', 'lib' ) )
sys.path.append (LIB_DIR)

#
# All (list)
#
if ( "action=list-all" in sys.argv[ 2 ] ):
    import ms_channel9_list_all as plugin
#
# Tags (browse)
#
elif ( "action=browse-tags" in sys.argv[ 2 ] ):
    import ms_channel9_browse_tags as plugin
#
# Tag (list)
#
elif ( "action=list-tag" in sys.argv[ 2 ] ):
    import ms_channel9_list_tag as plugin    
#
# Shows (browse)
#
elif ( "action=browse-shows" in sys.argv[ 2 ] ):
    import ms_channel9_browse_shows as plugin
#
# Show (list)
#
elif ( "action=list-show" in sys.argv[ 2 ] ):
    import ms_channel9_list_show as plugin
#
# Series (browse)
#
elif ( "action=browse-series" in sys.argv[ 2 ] ):
    import ms_channel9_browse_series as plugin
#
# Series (list)
#
elif ( "action=list-series" in sys.argv[ 2 ] ):
    import ms_channel9_list_series as plugin
#
# Play
#
elif ( "action=play" in sys.argv[ 2 ] ):
    import ms_channel9_play as plugin
#
# Main menu
#
else :
    xbmc.log( "[ADDON] %s v%s (%s)" % ( __addon__, __version__, __date__ ), xbmc.LOGNOTICE )
    import ms_channel9_main as plugin

plugin.Main()