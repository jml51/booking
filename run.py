from booking.booking import Booking

with Booking(teardown = True) as bot:
    bot.land_first_page()

    #bot.change_currency(currency='BRL')

    #bot.cookie()

    #bot.select_place_to_go('viana')

    #bot.select_datas(check_in_date="2023-03-01", check_out_date="2023-03-03" )

    #bot.select_adults()

    bot.booking_filtration()






































