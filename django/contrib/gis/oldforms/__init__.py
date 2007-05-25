from django.oldforms import LargeTextField
from django.contrib.gis.geos import hex_to_wkt

class WKTField(LargeTextField):
    "An oldforms LargeTextField for editing WKT text in the admin."
    
    def render(self, data):
        # PostGIS uses EWKBHEX to store its values internally, converting
        # to WKT for the admin first -- unless there's no data, then just
        # pass None to LargeTextField's render.
        if not data:
            return super(WKTField, self).render(None)
        else:
            return super(WKTField, self).render(hex_to_wkt(data))
    
                                        
