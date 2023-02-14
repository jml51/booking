from booking.booking import Booking

with Booking(teardown = True) as bot:
    bot.land_first_page()

    bot.change_currency(currency='BRL')

    bot.select_place_to_go('viana')
    

























