from django.contrib import admin
from .models import Event

admin.site.site_header = "SMT Monitoring — Admin"
admin.site.site_title = "SMT Monitoring"
admin.site.index_title = "Dashboard administracyjny"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "timestamp", "lane", "mc", "fadd", "fsadd",
        "pn", "feeder_serial", "pickup", "pmiss", "rmiss"
    )
    # filtry: PN, linia, maszyna (możesz łączyć je jednocześnie)
    list_filter = ("pn", "lane", "mc")
    # wyszukiwanie tylko po PN (bez feeder_serial)
    search_fields = ("pn",)
    ordering = ("-timestamp",)