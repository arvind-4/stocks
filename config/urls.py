"""config URL Configuration."""

from django.urls import path

from stocks.views import (
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
    path("", home_page_view, name="home"),
    path("cryto/", crypto_view, name="crypto"),
    path("cryto/list/", crypto_list_view, name="crypto_list"),
    path("stocks/details/", stocks_details, name="stocks_details"),
    path("about/", about_view, name="about"),
    path("error/", error_view, name="error"),
    path("<stock_name>/", redirect_page_stocks, name="redirect_stock"),
    path("stockdata/<stock_code>/", redirect_price_view, name="redirect_price"),
]
