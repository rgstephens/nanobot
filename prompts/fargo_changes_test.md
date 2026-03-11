# Fargo Weekly Update

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
