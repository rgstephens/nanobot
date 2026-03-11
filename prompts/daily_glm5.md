# Daily Summary Email

Send a summary email via mailgun to greg@udon.org from nanobot@triptrak.link. Use the calendar to determine my location and timezone, by default use Seattle, WA or the most recent location I was at.
"today" and "tomorrow" should be interpreted relative to my current timezone. All times should be presented in Pacific Time or the timezone my calendar shows that I am in.
Format the email using the html format example below. The email should contain the following:

- Weather forecast for today, include a nice graphic, the high and low temperature and expected precipitation. The presentation should be fairly small but visually attractive.
- The weather forecast for Addingham, UK
- Personal calendar items for today and tomorrow
- Did my fargo rate or robustness, id 1324244, change since the last update, if so provide the old and new rating and robustness values, if not the Fargo section should simple say "No changes".  The presentation should be fairly small but visually attractive.
- If there's a Leeds United game tomorrow send details - opponent, time, odds and TV channels using the polymarket-odds skill if possible
- Snooker tournaments scheduled for today and tomorrow using the snooker skill and try to find the TV channels for the UK and Ireland
- Snooker matches scheduled tomorrow from followed players trello list, use your memory for this instead of calling the snooker skill.
- From the list of trakt TV shows I'm watching, list episodes releasing today and tomorrow, do not show episodes released more than 3 days ago
- Release of new track or record by one of my Spotify followed artists today, do not show releases that are more than 3 days ago
- Add the name of the model configured in the Nanobot config.json in the footer along with the version "v0.2.0glm"

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset=3D"utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Robo=
to, Oxygen, Ubuntu, sans-serif; max-width: 700px; margin: 0 auto; padding: =
20px; background: #f5f5f5; }
    .container { background: white; border-radius: 12px; overflow: hidden; =
box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
    .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)=
; color: white; padding: 30px; text-align: center; }
    .header h1 { margin: 0; font-size: 28px; font-weight: 600; }
    .header .date { margin-top: 8px; opacity: 0.9; font-size: 16px; }
    .content { padding: 25px; }
    .section { margin-bottom: 30px; }
    .section-title { font-size: 18px; font-weight: 600; color: #333; margin=
-bottom: 15px; padding-bottom: 8px; border-bottom: 2px solid #667eea; displ=
ay: flex; align-items: center; gap: 10px; }
    .section-title .icon { font-size: 22px; }
   =20
    /* Weather cards */
    .weather-grid { display: flex; gap: 20px; flex-wrap: wrap; }
    .weather-card { flex: 1; min-width: 200px; background: linear-gradient(=
145deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 12px; padding: 20px; text=
-align: center; }
    .weather-card .location { font-weight: 600; color: #495057; margin-bott=
om: 10px; }
    .weather-card .weather-icon { font-size: 48px; margin: 10px 0; }
    .weather-card .temp { font-size: 36px; font-weight: 700; color: #212529=
; }
    .weather-card .temp-range { font-size: 14px; color: #6c757d; margin-top=
: 5px; }
    .weather-card .condition { font-size: 14px; color: #6c757d; margin-top:=
 8px; }
   =20
    /* Calendar */
    .calendar-item { background: #f8f9fa; border-left: 4px solid #667eea; p=
adding: 12px 15px; margin-bottom: 10px; border-radius: 0 8px 8px 0; }
    .calendar-item .time { font-size: 13px; color: #667eea; font-weight: 60=
0; }
    .calendar-item .title { font-size: 16px; font-weight: 500; color: #333;=
 margin-top: 4px; }
   =20
    /* Fargo */
    .fargo-box { background: linear-gradient(145deg, #d4edda 0%, #c3e6cb 10=
0%); border-radius: 10px; padding: 15px 20px; text-align: center; }
    .fargo-box .rating { font-size: 24px; font-weight: 700; color: #155724;=
 }
    .fargo-box .label { font-size: 13px; color: #155724; opacity: 0.8; }
   =20
    /* Snooker */
    .match-item { background: #fff3cd; border-left: 4px solid #ffc107; padd=
ing: 12px 15px; margin-bottom: 10px; border-radius: 0 8px 8px 0; }
    .match-item .tournament { font-size: 12px; color: #856404; font-weight:=
 600; text-transform: uppercase; }
    .match-item .players { font-size: 15px; font-weight: 500; color: #333; =
margin-top: 4px; }
    .match-item .time { font-size: 13px; color: #856404; margin-top: 4px; }
   =20
    /* TV Shows */
    .show-item { display: flex; justify-content: space-between; align-items=
: center; background: #e7f1ff; border-radius: 8px; padding: 12px 15px; marg=
in-bottom: 8px; }
    .show-item .show-name { font-weight: 600; color: #004085; }
    .show-item .episode { font-size: 14px; color: #004085; opacity: 0.8; }
    .show-item .air-time { font-size: 13px; color: #6c757d; }
   =20
    /* Leeds */
    .leeds-card { background: linear-gradient(145deg, #fff1f2 0%, #ffe4e6 1=
00%); border-radius: 12px; padding: 20px; text-align: center; }
    .leeds-card .matchup { font-size: 20px; font-weight: 700; color: #be123=
c; margin-bottom: 10px; }
    .leads-card .odds { font-size: 16px; color: #881337; }
   =20
    /* Footer */
    .footer { background: #f8f9fa; padding: 20px; text-align: center; color=
: #6c757d; font-size: 12px; border-top: 1px solid #e9ecef; }
    .footer .divider { margin: 0 10px; }
  </style>
</head>
<body>
  <div class=3D"container">
    <div class=3D"header">
      <h1>=F0=9F=8C=85 Daily Summary</h1>
      <div class=3D"date">Sunday, March 8, 2026 =E2=80=A2 Seattle, WA</div>
    </div>
   =20
    <div class=3D"content">
      <!-- Weather Section -->
      <div class=3D"section">
        <div class=3D"section-title"><span class=3D"icon">=F0=9F=8C=A4=EF=
=B8=8F</span> Weather</div>
        <div class=3D"weather-grid">
          <div class=3D"weather-card">
            <div class=3D"location">Seattle, WA</div>
            <div class=3D"weather-icon">=F0=9F=8C=AB=EF=B8=8F</div>
            <div class=3D"temp">51=C2=B0F</div>
            <div class=3D"temp-range">=E2=86=91 49=C2=B0F =E2=80=A2 =E2=86=
=93 39=C2=B0F</div>
            <div class=3D"condition">Mist =E2=80=A2 Humidity 86%</div>
          </div>
          <div class=3D"weather-card">
            <div class=3D"location">Addingham, UK</div>
            <div class=3D"weather-icon">=E2=9B=85</div>
            <div class=3D"temp">48=C2=B0F</div>
            <div class=3D"temp-range">=E2=86=91 47=C2=B0F =E2=80=A2 =E2=86=
=93 37=C2=B0F</div>
            <div class=3D"condition">Partly Cloudy =E2=80=A2 Humidity 93%</=
div>
          </div>
        </div>
      </div>
     =20
      <!-- Calendar Section -->
      <div class=3D"section">
        <div class=3D"section-title"><span class=3D"icon">=F0=9F=93=85</spa=
n> Calendar</div>
        <div style=3D"font-size: 14px; color: #667eea; font-weight: 600; ma=
rgin-bottom: 10px;">Today</div>
        <div class=3D"calendar-item">
          <div class=3D"time">2:00 PM - 6:00 PM</div>
          <div class=3D"title">PCL League</div>
        </div>
        <div style=3D"font-size: 14px; color: #667eea; font-weight: 600; ma=
rgin: 15px 0 10px;">Tomorrow</div>
        <div class=3D"calendar-item">
          <div class=3D"time">12:00 PM - 1:00 PM</div>
          <div class=3D"title">Lunch w/John</div>
        </div>
        <div class=3D"calendar-item">
          <div class=3D"time">6:30 PM - 7:30 PM</div>
          <div class=3D"title">Pool League (open play)</div>
        </div>
      </div>
     =20
      <!-- Fargo Section -->
      <div class=3D"section">
        <div class=3D"section-title"><span class=3D"icon">=F0=9F=8E=B1</spa=
n> FargoRate</div>
        <div class=3D"fargo-box">
          <div class=3D"label">Greg Stephens (ID: 1324244)</div>
          <div class=3D"rating">No changes</div>
          <div class=3D"label" style=3D"margin-top: 5px;">Current: 382 =E2=
=80=A2 Robustness: 222</div>
        </div>
      </div>
     =20
      <!-- Snooker Section -->
      <div class=3D"section">
        <div class=3D"section-title"><span class=3D"icon">=F0=9F=8E=AF</spa=
n> Snooker</div>
        <div style=3D"text-align: center; padding: 20px; background: #f8f9f=
a; border-radius: 10px; color: #6c757d;">
          <div style=3D"font-size: 16px; margin-bottom: 5px;">No tournament=
s scheduled</div>
          <div style=3D"font-size: 13px;">for today or tomorrow</div>
        </div>
        <div style=3D"margin-top: 15px;">
          <div style=3D"font-size: 13px; color: #666; margin-bottom: 8px;">=
Upcoming matches for followed players:</div>
          <div class=3D"match-item">
            <div class=3D"tournament">World Open =E2=80=A2 Rd 8</div>
            <div class=3D"players">TBD vs Stan Moody</div>
            <div class=3D"time">March 17, 2026 =E2=80=A2 6:30 AM PT</div>
          </div>
        </div>
      </div>
     =20
      <!-- TV Shows Section -->
      <div class=3D"section">
        <div class=3D"section-title"><span class=3D"icon">=F0=9F=93=BA</spa=
n> TV Episodes</div>
        <div class=3D"show-item">
          <div>
            <div class=3D"show-name">The Great Pottery Throw Down</div>
            <div class=3D"episode">S9E10: Mini Theatres and a Throwing Chal=
lenge</div>
          </div>
          <div class=3D"air-time">Today 1:00 PM</div>
        </div>
        <div class=3D"show-item">
          <div>
            <div class=3D"show-name">Paradise</div>
            <div class=3D"episode">S2E5: The Mailman</div>
          </div>
          <div class=3D"air-time">Tomorrow 9:00 PM</div>
        </div>
        <div class=3D"show-item">
          <div>
            <div class=3D"show-name">Drops of God</div>
            <div class=3D"episode">S2E8: Break Free</div>
          </div>
          <div class=3D"air-time">Tomorrow 4:00 PM</div>
        </div>
      </div>
     =20
      <!-- Spotify Section -->
      <div class=3D"section">
        <div class=3D"section-title"><span class=3D"icon">=F0=9F=8E=B5</spa=
n> New Music</div>
        <div style=3D"text-align: center; padding: 15px; background: #f8f9f=
a; border-radius: 10px; color: #6c757d; font-size: 14px;">
          No new releases from followed artists in the last 3 days
        </div>
      </div>
    </div>
   =20
    <div class=3D"footer">
      Powered by <strong>nanobot</strong> =E2=80=A2 Model: <strong>glm-5</s=
trong> =E2=80=A2 Generated in <strong>0.0s</strong>
    </div>
  </div>
</body>
</html>
```
