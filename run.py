from booking.booking import Booking
try:
    with Booking(teardown = True) as bot:
        bot.land_first_page()

        #bot.change_currency(currency='BRL')

        #bot.cookie()

        bot.select_place_to_go('viana')

        #bot.select_datas(check_in_date="2023-03-01", check_out_date="2023-03-03" )

        #bot.select_adults()

        #bot.booking_filtration()

        #bot.booking_find()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise





































