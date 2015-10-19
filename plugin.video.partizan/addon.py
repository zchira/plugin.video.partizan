import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])


xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

YOUTUBE_PTN = 'plugin://plugin.video.youtube/play/?video_id=%s'
def youtube_url(videoid):
    return YOUTUBE_PTN % (videoid)

#print "mode"
my_addon = xbmcaddon.Addon('plugin.video.partizan')
iconImage = my_addon.getAddonInfo('icon')
fanart = my_addon.getAddonInfo('fanart')

title  = 'PartizanTV Live'
url = youtube_url('KSW-L-aZ_OY')
li = xbmcgui.ListItem(title, iconImage=iconImage)
#li.setArt({ 'poster': 'poster.png', 'banner' : 'banner.png' })
li.setProperty('isplayable','true')
li.setProperty('fanart_image', fanart)

xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
    
