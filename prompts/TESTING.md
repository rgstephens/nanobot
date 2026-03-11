# Testing

## Version & Model

What is your version and the name of the model configured in the Nanobot config.json

## Fargo

What is the fargo rating for chris melling

## Snooker

What is stan moody's snooker ranking

## cron

What cron jobs are scheduled

## heartbeat

What heartbeat tasks are running

## Headless HTML

give me a table of everyone in the ox-monday group with their rating and robustness. Generate an HTML string of your table then Use a "headless browser" or a library to take a screenshot of that HTML and send the resulting png/jpg to telegram

## Timed Snooker Player Updates

Go through my favorite snooker player list and once per minute, query the snooker skill for the next player in the list to determine when their next match will be played and save in memory. If you encounter an API error, pause for 90 seconds and continue.

## Daily Summary Email

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
- Add the name of the model configured in the Nanobot config.json in the footer along with the version "v0.3.0"

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset=3D"utf-8">
  <meta name=3D"viewport" content=3D"width=3Ddevice-width, initial-scale=3D=
1.0">
  <title>Daily Summary - March 8, 2026</title>
</head>
<body style=3D"margin: 0; padding: 20px; background-color: #f5f5f5; font-fa=
mily: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Ari=
al, sans-serif;">
  <div style=3D"max-width: 600px; margin: 0 auto; background-color: #ffffff=
; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0=
=2E1);">
   =20
    <!-- Header -->
    <div style=3D"background: linear-gradient(135deg, #667eea 0%, #764ba2 1=
00%); padding: 30px; text-align: center;">
      <h1 style=3D"margin: 0; color: #ffffff; font-size: 28px; font-weight:=
 600;">Daily Summary</h1>
      <p style=3D"margin: 8px 0 0 0; color: rgba(255,255,255,0.9); font-siz=
e: 16px;">Sunday, March 8, 2026 =E2=80=A2 Seattle, WA</p>
    </div>
   =20
    <div style=3D"padding: 25px;">
     =20
      <!-- Weather Section -->
      <div style=3D"margin-bottom: 25px;">
        <h2 style=3D"margin: 0 0 15px 0; color: #333; font-size: 18px; bord=
er-bottom: 2px solid #667eea; padding-bottom: 8px;">=F0=9F=8C=A4=EF=B8=8F W=
eather</h2>
        <table width=3D"100%" cellpadding=3D"0" cellspacing=3D"0" style=3D"=
border-collapse: collapse;">
          <tr>
            <td width=3D"50%" style=3D"vertical-align: top; padding-right: =
15px;">
              <div style=3D"background: linear-gradient(135deg, #74b9ff 0%,=
 #0984e3 100%); border-radius: 10px; padding: 15px; text-align: center;">
                <p style=3D"margin: 0 0 5px 0; color: rgba(255,255,255,0.9)=
; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">Seattle=
, WA</p>
                <p style=3D"margin: 0; color: #fff; font-size: 42px; font-w=
eight: 300;">=E2=98=81=EF=B8=8F 51=C2=B0F</p>
                <p style=3D"margin: 5px 0 0 0; color: rgba(255,255,255,0.9)=
; font-size: 13px;">High: 49=C2=B0F =E2=80=A2 Low: 39=C2=B0F</p>
                <p style=3D"margin: 3px 0 0 0; color: rgba(255,255,255,0.8)=
; font-size: 12px;">Humidity: 86% =E2=80=A2 Wind: =E2=86=97 7mph</p>
              </div>
            </td>
            <td width=3D"50%" style=3D"vertical-align: top; padding-left: 1=
5px;">
              <div style=3D"background: linear-gradient(135deg, #a29bfe 0%,=
 #6c5ce7 100%); border-radius: 10px; padding: 15px; text-align: center;">
                <p style=3D"margin: 0 0 5px 0; color: rgba(255,255,255,0.9)=
; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">Addingh=
am, UK</p>
                <p style=3D"margin: 0; color: #fff; font-size: 42px; font-w=
eight: 300;">=E2=9B=85=EF=B8=8F 49=C2=B0F</p>
                <p style=3D"margin: 5px 0 0 0; color: rgba(255,255,255,0.9)=
; font-size: 13px;">High: 47=C2=B0F =E2=80=A2 Low: 37=C2=B0F</p>
                <p style=3D"margin: 3px 0 0 0; color: rgba(255,255,255,0.8)=
; font-size: 12px;">Humidity: 93% =E2=80=A2 Wind: =E2=86=96 4mph</p>
              </div>
            </td>
          </tr>
        </table>
      </div>
     =20
      <!-- Calendar Section -->
      <div style=3D"margin-bottom: 25px;">
        <h2 style=3D"margin: 0 0 15px 0; color: #333; font-size: 18px; bord=
er-bottom: 2px solid #667eea; padding-bottom: 8px;">=F0=9F=93=85 Calendar</=
h2>
        <div style=3D"background-color: #f8f9fa; border-radius: 8px; paddin=
g: 15px;">
          <p style=3D"margin: 0 0 10px 0; color: #666; font-size: 13px; fon=
t-weight: 600; text-transform: uppercase;">Today</p>
          <div style=3D"background-color: #fff; border-left: 4px solid #667=
eea; padding: 10px 12px; margin-bottom: 15px; border-radius: 0 6px 6px 0;">
            <p style=3D"margin: 0; color: #333; font-weight: 600;">PCL Leag=
ue</p>
            <p style=3D"margin: 3px 0 0 0; color: #666; font-size: 13px;">2=
:00 PM - 6:00 PM PDT</p>
          </div>
          <p style=3D"margin: 0 0 10px 0; color: #666; font-size: 13px; fon=
t-weight: 600; text-transform: uppercase;">Tomorrow (Monday)</p>
          <div style=3D"background-color: #fff; border-left: 4px solid #10b=
981; padding: 10px 12px; margin-bottom: 10px; border-radius: 0 6px 6px 0;">
            <p style=3D"margin: 0; color: #333; font-weight: 600;">Lunch w/=
John</p>
            <p style=3D"margin: 3px 0 0 0; color: #666; font-size: 13px;">1=
2:00 PM - 1:00 PM PDT</p>
          </div>
          <div style=3D"background-color: #fff; border-left: 4px solid #f59=
e0b; padding: 10px 12px; border-radius: 0 6px 6px 0;">
            <p style=3D"margin: 0; color: #333; font-weight: 600;">Pool Lea=
gue (open play)</p>
            <p style=3D"margin: 3px 0 0 0; color: #666; font-size: 13px;">6=
:30 PM - 7:30 PM PDT</p>
          </div>
        </div>
      </div>
     =20
      <!-- FargoRate Section -->
      <div style=3D"margin-bottom: 25px;">
        <h2 style=3D"margin: 0 0 15px 0; color: #333; font-size: 18px; bord=
er-bottom: 2px solid #667eea; padding-bottom: 8px;">=F0=9F=8E=B1 FargoRate<=
/h2>
        <div style=3D"background: linear-gradient(135deg, #00b894 0%, #00ce=
c9 100%); border-radius: 10px; padding: 15px; text-align: center;">
          <p style=3D"margin: 0; color: #fff; font-size: 16px;">=E2=9C=93 N=
o changes</p>
          <p style=3D"margin: 5px 0 0 0; color: rgba(255,255,255,0.9); font=
-size: 13px;">Greg Stephens =E2=80=A2 Rating: 382 =E2=80=A2 Robustness: 222=
</p>
        </div>
      </div>
     =20
      <!-- Leeds United Section -->
      <div style=3D"margin-bottom: 25px;">
        <h2 style=3D"margin: 0 0 15px 0; color: #333; font-size: 18px; bord=
er-bottom: 2px solid #667eea; padding-bottom: 8px;">=E2=9A=BD Leeds United<=
/h2>
        <div style=3D"background-color: #1e3a5f; border-radius: 10px; paddi=
ng: 15px;">
          <p style=3D"margin: 0; color: #fff; font-size: 14px; font-weight:=
 600;">No match tomorrow</p>
          <p style=3D"margin: 8px 0 0 0; color: rgba(255,255,255,0.8); font=
-size: 13px;">Next: Crystal Palace vs Leeds United</p>
          <p style=3D"margin: 3px 0 0 0; color: rgba(255,255,255,0.7); font=
-size: 12px;">Sunday, March 15, 2026 =E2=80=A2 Leeds win odds: 29.5%</p>
        </div>
      </div>
     =20
      <!-- Snooker Section -->
      <div style=3D"margin-bottom: 25px;">
        <h2 style=3D"margin: 0 0 15px 0; color: #333; font-size: 18px; bord=
er-bottom: 2px solid #667eea; padding-bottom: 8px;">=F0=9F=8E=AF Snooker</h=
2>
        <div style=3D"background-color: #f8f9fa; border-radius: 8px; paddin=
g: 15px;">
          <p style=3D"margin: 0 0 8px 0; color: #666; font-size: 13px; font=
-weight: 600;">Tournaments</p>
          <p style=3D"margin: 0 0 12px 0; color: #333; font-size: 14px;">No=
 tournaments scheduled for today or tomorrow</p>
          <p style=3D"margin: 0 0 8px 0; color: #666; font-size: 13px; font=
-weight: 600;">Followed Players - Tomorrow's Matches</p>
          <p style=3D"margin: 0; color: #666; font-size: 14px; font-style: =
italic;">No matches scheduled for tomorrow</p>
          <p style=3D"margin: 8px 0 0 0; color: #888; font-size: 12px;">Nex=
t: Stan Moody vs TBD (World Open Rd 8) - March 17</p>
        </div>
      </div>
     =20
      <!-- TV Shows Section -->
      <div style=3D"margin-bottom: 25px;">
        <h2 style=3D"margin: 0 0 15px 0; color: #333; font-size: 18px; bord=
er-bottom: 2px solid #667eea; padding-bottom: 8px;">=F0=9F=93=BA TV Shows</=
h2>
        <div style=3D"background-color: #f8f9fa; border-radius: 8px; paddin=
g: 15px;">
          <p style=3D"margin: 0 0 10px 0; color: #666; font-size: 13px; fon=
t-weight: 600;">Today (Sunday)</p>
          <div style=3D"background-color: #fff; border-radius: 6px; padding=
: 12px; margin-bottom: 15px;">
            <p style=3D"margin: 0; color: #333; font-weight: 600;">The Grea=
t Pottery Throw Down</p>
            <p style=3D"margin: 3px 0 0 0; color: #666; font-size: 13px;">S=
9E10 "Mini Theatres and a Throwing Challenge" =E2=80=A2 Season Finale</p>
            <p style=3D"margin: 3px 0 0 0; color: #888; font-size: 12px;">8=
:00 PM GMT =E2=80=A2 BBC Two</p>
          </div>
          <p style=3D"margin: 0 0 10px 0; color: #666; font-size: 13px; fon=
t-weight: 600;">Tomorrow (Monday)</p>
          <div style=3D"background-color: #fff; border-radius: 6px; padding=
: 12px; margin-bottom: 10px;">
            <p style=3D"margin: 0; color: #333; font-weight: 600;">Paradise=
</p>
            <p style=3D"margin: 3px 0 0 0; color: #666; font-size: 13px;">S=
2E5 "The Mailman"</p>
            <p style=3D"margin: 3px 0 0 0; color: #888; font-size: 12px;">1=
2:00 AM EST =E2=80=A2 Hulu</p>
          </div>
          <div style=3D"background-color: #fff; border-radius: 6px; padding=
: 12px;">
            <p style=3D"margin: 0; color: #333; font-weight: 600;">Drops of=
 God</p>
            <p style=3D"margin: 3px 0 0 0; color: #666; font-size: 13px;">S=
2E7 "Break Free"</p>
            <p style=3D"margin: 3px 0 0 0; color: #888; font-size: 12px;">1=
2:00 AM CET =E2=80=A2 Apple TV+</p>
          </div>
        </div>
      </div>
     =20
      <!-- Spotify Section -->
      <div style=3D"margin-bottom: 25px;">
        <h2 style=3D"margin: 0 0 15px 0; color: #333; font-size: 18px; bord=
er-bottom: 2px solid #667eea; padding-bottom: 8px;">=F0=9F=8E=B5 New Music<=
/h2>
        <div style=3D"background: linear-gradient(135deg, #1db954 0%, #1914=
14 100%); border-radius: 10px; padding: 15px; text-align: center;">
          <p style=3D"margin: 0; color: #fff; font-size: 14px;">No new rele=
ases from your followed artists in the last 3 days</p>
        </div>
      </div>
     =20
    </div>
   =20
    <!-- Footer -->
    <div style=3D"background-color: #f8f9fa; padding: 20px; text-align: cen=
ter; border-top: 1px solid #e9ecef;">
      <p style=3D"margin: 0; color: #888; font-size: 12px;">Powered by <str=
ong>nanobot</strong> =F0=9F=90=88</p>
      <p style=3D"margin: 5px 0 0 0; color: #aaa; font-size: 11px;">Model: =
Claude 3.5 Sonnet (claude-3-5-sonnet)</p>
    </div>
   =20
  </div>
</body>
</html>
```

## Fargo Weekly Update

Send a summary email via mailgun to greg@udon.org from nanobot@triptrak.link with any fargo changes for the group named "ox-monday". 
Make the listing sharp and succinct using html follow the format below. 
For any players with a rating change in the last seven days list their name, id, new & old rating and robustness. Update the database with any new ratings.
Also, include a sorted table of all players in the league with their name, id and rating.
Add the name of the model configured in the Nanobot config.json in the footer along with "v0.2.0".

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset=3D"UTF-8">
    <meta name=3D"viewport" content=3D"width=3Ddevice-width, initial-scale=
=3D1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {=20
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Rob=
oto, 'Helvetica Neue', Arial, sans-serif;=20
            line-height: 1.5;=20
            color: #2d3748;=20
            background: #f7fafc;
            padding: 20px;
        }
        .container {=20
            max-width: 600px;=20
            margin: 0 auto;=20
            background: white;=20
            border-radius: 12px;=20
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }
        .header {=20
            background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
            color: white;=20
            padding: 24px;=20
            text-align: center;
        }
        .header h1 { font-size: 22px; font-weight: 700; margin-bottom: 4px;=
 }
        .header .group { font-size: 13px; opacity: 0.8; }
        .header .count { font-size: 12px; opacity: 0.6; margin-top: 4px; }
       =20
        .content { padding: 24px; }
       =20
        h2 {=20
            font-size: 12px;=20
            font-weight: 600;=20
            color: #1a202c;
            margin: 16px 0 10px 0;
            padding-bottom: 6px;
            border-bottom: 1px solid #e2e8f0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        h2:first-child { margin-top: 0; }
       =20
        .change-card {
            background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
            border-radius: 10px;
            padding: 16px;
            color: white;
            margin-bottom: 12px;
        }
        .change-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        .change-name {
            font-size: 16px;
            font-weight: 700;
        }
        .change-id {
            font-size: 11px;
            opacity: 0.8;
            font-family: monospace;
        }
        .change-rating {
            font-size: 28px;
            font-weight: 700;
            text-align: center;
            margin: 8px 0;
        }
        .change-arrow {
            opacity: 0.9;
        }
        .change-details {
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            opacity: 0.9;
            margin-top: 8px;
            padding-top: 8px;
            border-top: 1px solid rgba(255,255,255,0.2);
        }
       =20
        .no-changes {
            text-align: center;
            padding: 24px;
            color: #718096;
        }
        .no-changes-icon {
            font-size: 32px;
            margin-bottom: 8px;
        }
       =20
        .summary-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        .summary-table th {
            text-align: left;
            padding: 8px 6px;
            color: #718096;
            font-weight: 600;
            border-bottom: 1px solid #e2e8f0;
        }
        .summary-table td {
            padding: 8px 6px;
            border-bottom: 1px solid #f0f0f0;
        }
        .summary-table tr:last-child td {
            border-bottom: none;
        }
        .rating-col { text-align: right; font-weight: 600; }
        .id-col { font-family: monospace; color: #a0aec0; font-size: 10px; =
}
       =20
        .footer {
            background: #f7fafc;
            padding: 14px;
            text-align: center;
            font-size: 11px;
            color: #718096;
            border-top: 1px solid #e2e8f0;
        }
    </style>
</head>
<body>
    <div class=3D"container">
        <div class=3D"header">
            <h1>=F0=9F=8E=B1 FargoRate Changes</h1>
            <div class=3D"group">ox-monday Group</div>
            <div class=3D"count">1 of 24 players with rating changes</div>
        </div>
       =20
        <div class=3D"content">
            <h2>=E2=AC=86=EF=B8=8F Rating Changes</h2>
           =20
            <div class=3D"change-card">
                <div class=3D"change-header">
                    <span class=3D"change-name">Greg Stephens</span>
                    <span class=3D"change-id">ID: 1324244</span>
                </div>
                <div class=3D"change-rating">
                    380 <span class=3D"change-arrow">=E2=86=92</span> 382 <=
span style=3D"font-size: 14px; opacity: 0.9;">(+2)</span>
                </div>
                <div class=3D"change-details">
                    <span>Seattle WA</span>
                    <span>Robustness: 222</span>
                </div>
            </div>
           =20
            <h2>=F0=9F=93=8A All Members (24)</h2>
            <table class=3D"summary-table">
                <tr>
                    <th>Player</th>
                    <th class=3D"rating-col">Rating</th>
                    <th class=3D"id-col">ID</th>
                </tr>
                <tr><td>Marcello Girardi</td><td class=3D"rating-col">592</=
td><td class=3D"id-col">360492</td></tr>
                <tr><td>Michal Rybak</td><td class=3D"rating-col">567</td><=
td class=3D"id-col">1115327</td></tr>
                <tr><td>Alex Buzak</td><td class=3D"rating-col">544</td><td=
 class=3D"id-col">1119383</td></tr>
                <tr><td>Jonathan Ramalheira Tsu</td><td class=3D"rating-col=
">538</td><td class=3D"id-col">1341515</td></tr>
                <tr><td>Brian McEllin</td><td class=3D"rating-col">532</td>=
<td class=3D"id-col">1119367</td></tr>
                <tr><td>Zachary (Zak) Ross</td><td class=3D"rating-col">529=
</td><td class=3D"id-col">1119371</td></tr>
                <tr><td>Michael Jin</td><td class=3D"rating-col">516</td><t=
d class=3D"id-col">1132833</td></tr>
                <tr><td>Katrin Cheung</td><td class=3D"rating-col">500</td>=
<td class=3D"id-col">1324636</td></tr>
                <tr><td>Dani Casper</td><td class=3D"rating-col">491</td><t=
d class=3D"id-col">1137501</td></tr>
                <tr><td>Isaac Alexander</td><td class=3D"rating-col">480</t=
d><td class=3D"id-col">1341511</td></tr>
                <tr><td>Alexis Aguirre</td><td class=3D"rating-col">474</td=
><td class=3D"id-col">1207397</td></tr>
                <tr><td>Mason Drury</td><td class=3D"rating-col">473</td><t=
d class=3D"id-col">1119384</td></tr>
                <tr><td>Kyle Leck</td><td class=3D"rating-col">465</td><td =
class=3D"id-col">1209675</td></tr>
                <tr><td>Michael Dominguez</td><td class=3D"rating-col">463<=
/td><td class=3D"id-col">1119369</td></tr>
                <tr><td>Gregory Berns-Leone</td><td class=3D"rating-col">46=
0</td><td class=3D"id-col">1277009</td></tr>
                <tr><td>Alex Zuyok</td><td class=3D"rating-col">458</td><td=
 class=3D"id-col">1190373</td></tr>
                <tr><td>Niko Butt</td><td class=3D"rating-col">439</td><td =
class=3D"id-col">1191948</td></tr>
                <tr><td>Scott Crawford</td><td class=3D"rating-col">439</td=
><td class=3D"id-col">1337835</td></tr>
                <tr><td>David Saltzman</td><td class=3D"rating-col">432</td=
><td class=3D"id-col">1215491</td></tr>
                <tr><td>Mohammad Rammah</td><td class=3D"rating-col">416</t=
d><td class=3D"id-col">1179210</td></tr>
                <tr><td><strong>Greg Stephens</strong> =E2=AC=86=EF=B8=8F</=
td><td class=3D"rating-col"><strong>382</strong></td><td class=3D"id-col">1=
324244</td></tr>
                <tr><td>Dan McGuire</td><td class=3D"rating-col">393</td><t=
d class=3D"id-col">1327664</td></tr>
                <tr><td>Hector Mota</td><td class=3D"rating-col">371</td><t=
d class=3D"id-col">1367566</td></tr>
                <tr><td>Steve Leonard</td><td class=3D"rating-col">234</td>=
<td class=3D"id-col">1365659</td></tr>
            </table>
        </div>
       =20
        <div class=3D"footer">
            =F0=9F=90=88 nanobot@triptrak.link =E2=80=A2 March 6, 2026
        </div>
    </div>
</body>
</html>
```
