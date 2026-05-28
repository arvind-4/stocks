"""Views for the stocks app."""

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from stocks.forms import StocksForm
from stocks.infrastructure.external_client.tingo_stock_client import (
    get_meta_data,
    get_price_information,
    get_search_data,
    get_stocks_fundementals,
    list_of_crypto_data,
)


def home_page_view(request: HttpRequest) -> HttpResponse:
    """Home page view for stock search."""
    form = StocksForm(request.POST or None)
    if form.is_valid():
        stock_name = form.cleaned_data["name"]
        if stock_name:
            return HttpResponseRedirect(stock_name)
    context = {
        "form": form,
    }
    return render(request, "stocks/home_page.html", context=context)


def redirect_page_stocks(request: HttpRequest, stock_name: str) -> HttpResponse:
    """Redirect to stock search results."""
    data = get_search_data(stock_name)
    if len(data) == 0:
        return redirect("/error")
    context = {
        "data": data,
    }
    return render(request, "stocks/ticker.html", context=context)


def redirect_price_view(request: HttpRequest, stock_code: str) -> HttpResponse:
    """Show price data for a stock."""
    data = get_price_information(stock_code)
    meta_data = get_meta_data(stock_code)
    context = {
        "data": data,
        "meta_data": meta_data,
        "stock_code": stock_code,
    }
    return render(request, "stocks/table.html", context=context)


def crypto_view(request: HttpRequest) -> HttpResponse:
    """Crypto currency view."""
    return render(request, "stocks/cryto_view.html", context={})


def crypto_list_view(request: HttpRequest) -> HttpResponse:
    """List crypto currencies."""
    data = list_of_crypto_data()
    context = {
        "data": data,
    }
    return render(request, "stocks/cryto_list_view.html", context=context)


def stocks_details(request: HttpRequest) -> HttpResponse:
    """Show stock fundamentals details."""
    data = get_stocks_fundementals()
    data = data[::-1]
    context = {
        "data": data,
    }
    return render(request, "stocks/stocks_details.html", context=context)


def error_view(request: HttpRequest) -> HttpResponse:
    """Error page view."""
    return render(request, "stocks/error.html", context={})


def about_view(request: HttpRequest) -> HttpResponse:
    """About page view."""
    return render(request, "stocks/about.html", context={})
