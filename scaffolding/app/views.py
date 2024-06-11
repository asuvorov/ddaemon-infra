"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

import json
import mimetypes

from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponse,
    HttpResponseBadRequest)
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_http_methods

from .management.commands import clear_cache


# =============================================================================
# ===
# === HANDLERS
# ===
# =============================================================================
def handler400(request, exception=None):
    """400 Handler."""
    return render(request, "error-pages/400.html", status=404)


def handler403(request, exception=None):
    """403 Handler."""
    return render(request, "error-pages/403.html", status=404)


def handler404(request, exception=None):
    """404 Handler."""
    return render(request, "error-pages/404.html", status=404)


def handler500(request, exception=None):
    """500 Handler."""
    try:
        clear_cache.Command().handle()

        # ---------------------------------------------------------------------
        # --- Save the Log

    except Exception as exc:
        print(f"### EXCEPTION : {type(exc).__name__} : {str(exc)}")

    return render(request, "error-pages/500.html", status=500)
