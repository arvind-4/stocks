"""URL configuration for the stocks app."""

from django.urls import path

from .views import (
    about_view,
    crypto_list_view,
    crypto_view,
    error_view,
    home_page_view,
    redirect_page_stocks,
    redirect_price_view,
    stocks_details,
)

urlpatterns = [
    path("", home_page_view),
    path("cryto/", crypto_view),
    path("cryto/list/", crypto_list_view),
    path("stocks/details/", stocks_details),
    path("about/", about_view),
    path("error/", error_view),
    path("<stock_name>/", redirect_page_stocks),
    path("stockdata/<stock_code>/", redirect_price_view),
]
