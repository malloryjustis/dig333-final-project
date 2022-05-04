# dig333-final-project
Final Project Log

Project Proposal: [Proposal Slides - Including Schematics](https://docs.google.com/presentation/d/1VCNRhh4Yt2g6CyYGfm-fvS7Go773UuG2uuAi2unPjNQ/edit?usp=sharing)

## Milestone 1: Getting Weather Data From Internet to Raspberry Pi

National Weather Service API: https://api.weather.gov/

Davidson Weather: https://api.weather.gov/points/35.499302,-80.848686

GET Davidson Weather request: https://api.weather.gov/gridpoints/GSP/116,76/forecast/hourly

Installed [JSON](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=en-US) Chrome browser extension and [Postman](https://web.postman.co/onboarding/user) onto computer to read data.

[Python Code that turns weather data into readable file](https://github.com/malloryjustis/dig333-final-project/blob/main/weatherdatafromapi.py)

[Python Code that narrows down weather data to current weather](https://github.com/malloryjustis/dig333-final-project/blob/main/currentweatherdataonly.py)

## Milestone 2: Create Python Code that Will Connect Weather Data to GPIO for Output

The following screenshot shows the general code outline for turning the weather data dictionary into GPIO output:

<img src="photos/gpiocodebeforegpiosettings.jpg" alt="code outline" style="float: left; margin-right: 10px;" />

Here is the [GPIO Code](https://github.com/malloryjustis/dig333-final-project/blob/main/python_codes/weather_to_gpio.py) that turns the data in the Python code into an output for the hardware.

## Milestone 3: Create Hardware System that Works with Python Code

Hardware setup:

<img src="photos/hardware_setup.jpg" alt="hardware setup" style="float: left; margin-right: 10px;" />

Running code manually to figure out bugs:

<img src="photos/codinghardware.jpg" alt="coding hardware" style="float: left; margin-right: 10px;" />

Porch light turning on at midnight when the code is run:

<img src="photos/porchlight.jpg" alt="porch light on" style="float: left; margin-right: 10px;" />

Using [Crontab](https://crontab.guru/#@hourly) to make code run hourly:

<img src="photos/crontabrunning.jpg" alt="setting up crontab" style="float: left; margin-right: 10px;" />

## Fixes

The Weather API that I was using was unreliable; servers kept going down. So I decided to use a different [API](https://api.weatherusa.net/v1/forecast?q=35.227085,-80.843124&daily=0&units=e&maxtime=7d). The codes are still the same, just with a different link. All new python files have the same names at the previous ones, just with a 2 at the end.

## Milestone 4: Designing the House

Found Adobe Illustrator vector file for download from an [Etsy shop](https://www.etsy.com/listing/786887665/16-miniature-cabin-type-02vector-file?click_key=8ff4772b4ab388e8ccdbe30313a731a55b073fed%3A786887665&click_sum=9d484603&ref=shop_home_active_37) to laser engrave a tiny house.

<img src="photos/tinyhouse_floorplans.jpg" alt="Floor Plan" style="float: left; margin-right: 10px;" />

Laser cutting the file in the makerspace:

<img src="photos/laserengraver.jpg" alt="Laser Engraving" style="float: left; margin-right: 10px;" />

