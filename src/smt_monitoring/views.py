from django.db.models import Sum, F, FloatField
from django.db.models.functions import Coalesce
from django.shortcuts import render
from .models import Event

def dashboard(request):
    # zagregowane KPI per linia (ostatni pełny dzień lub całość – na start całość)
    agg = (
        Event.objects
        .values("lane")
        .annotate(
            pickup=Coalesce(Sum("pickup"), 0),
            pmiss=Coalesce(Sum("pmiss"), 0),
            rmiss=Coalesce(Sum("rmiss"), 0),
        )
        .order_by("lane")
    )

    rows = []
    for a in agg:
        errors = a["pmiss"] + a["rmiss"]
        pickup = a["pickup"] or 0
        success = (1 - (errors / pickup)) * 100 if pickup > 0 else 100.0
        rows.append({
            "lane": a["lane"],
            "pickup": pickup,
            "errors": errors,
            "success": round(success, 3),
        })

    context = {
        "rows": rows,
        "labels": [f"L{r['lane']}" for r in rows],
        "success_data": [r["success"] for r in rows],
        "error_data": [r["errors"] for r in rows],
    }
    return render(request, "dashboard.html", context)
