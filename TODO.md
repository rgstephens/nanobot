# Personal Agent with NanoBot

Features:

- add model identification to Version skill
- Connect to discord
- snooker - add /snooker setup feature like streaming buddy
- FargoRate change notification service: Telegram, Discord, Email, SMS (via iMessage, Twilio)
- Backup process, .env files, things in .gitignore, bot history
- Model testing setup
  - minimax, glm or kimi
- Reminders system & Timers
  - Notify me via SMS, iOS/watch
- Weekly planner
  - Release of new track or record by one of my followed artists
  - Snooker matches from followed players
- Daily planner
  - Send FargoRate update if there was a change
  - GHIN Hcp change
  - New TV show episodes
  - monitor Kevin's snooker site
  - Ox billiards calendar of events
- BMW climate control
- Tesla climate control
- Cache items to reduce cost & latency: snooker players from Trello, followed artists from Spotify
- Ask about my bands playing in cities on dates (Spotify API or access my local list of artists)

## Skills to Publish

- [ ] LangFuse Integration, [PR #1490](https://github.com/HKUDS/nanobot/pull/1490)
- [ ] GHIN
- [x] [FargoRate](https://clawhub.ai/rgstephens/fargo-skill)
- [x] [Snooker Skill](https://clawhub.ai/rgstephens/snooker-skill)

## Formatting for Telegram

Generate an HTML string of your table then Use a "headless browser" or a library to take a screenshot of that HTML and send the resulting png/jpg to telegram

## Daily Planner Prompt

Send a summary email via mailgun to greg@udon.org from nanobot@triptrak.link. Use the calendar to determine my location and timezone, by default use Seattle, WA or the most recent location I was at. "today" and "tomorrow" should be interpreted relative to my current timezone. All times should be presented in Pacific Time or the timezone my calendar shows that I am in. Also, format the email so it looks sharp. The email should contain the following:
  - Weather forecast for today, include a nice graphic, the high and low temperature and expected precipitation. The presentation should be fairly small but visually attractive.
  - The weather forecast for Addingham, UK
  - Personal calendar items for today and tomorrow
  - Did my fargo rate or robustness, id 1324244, change since the last update, if so provide the old and new rating and robustness values, if not the Fargo section should simple say "No changes".  The presentation should be fairly small but visually attractive.
  - If there's a Leeds United game tomorrow send details - opponent, time, odds and TV channels using the polymarket-odds skill if possible
  - Snooker tournaments scheduled for today and tomorrow using the snooker skill and try to find the TV channels for the UK and Ireland
  - Snooker matches scheduled tomorrow from followed players trello list, use your memory for this instead of calling the snooker skill.
  - From the list of trakt TV shows I'm watching, list episodes releasing today and tomorrow, do not show episodes released more than 3 days ago
  - Release of new track or record by one of my Spotify followed artists today, do not show releases that are more than 3 days ago
  - Add the name of the model configured in the Nanobot config.json in the footer

  - Cache snooker player info
  - Pottery show should check episodes on HBO not Channel 4
  - GHIN Hcp change
  - monitor Kevin's snooker site
  - Ox billiards calendar of events
  - Send FargoRate update if there was a change

## Daily Fargo Changes

Send a summary email via mailgun to greg@udon.org from nanobot@triptrak.link with all of any fargo changes for the group named "ox-monday". Make the listing sharp and succinct. For any players with changes list their name, id, new & old rating and robustness. It should only include changes in the last 24 hours and make sure you update the database with any new ratings.

## Weekly Fargo for Monday League

Every Monday at 4am pacific time, send a summary email via mailgun to greg@udon.org and Niko.butt@gmail.com from nanobot@triptrak.link with any fargo changes for the group named "ox-monday". Make the listing sharp and succinct. For any players with changes list their name, id, new & old rating and robustness. It should only include changes in the last 7 days and make sure you update the database with any new ratings. Also, include a sorted table of all players in the league with their name, id and rating.

## Weekly Planner Prompt

- Send a summary email via mailgun to greg@udon.org. Use the calendar to determine my location and timezone, by default use Seattle, WA unless there is another location on my upcoming calendar for the week. The email should contain the following:
  - Weather forecast for the week
  - Release of new track or record by one of my spotify followed artists in the next week
  - Future snooker matches in the coming week from followed players in my trello list lookup using the snooker skill

## Bot Context Prompt

My default timezone is Pacific time and my default location is Seattle, WA
r
## GHIN

```sh
curl 'https://api2.ghin.com/api/v1/golfer_login.json' \
  -X 'OPTIONS' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'access-control-request-headers: content-type' \
  -H 'access-control-request-method: POST' \
  -H 'origin: https://www.ghin.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.ghin.com/' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
curl 'https://api2.ghin.com/api/v1/golfer_login.json' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'origin: https://www.ghin.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.ghin.com/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  --data-raw $'{"user":{"password":"29P%40s\u0021Z","email_or_ghin":"3315181","remember_me":false},"token":"pp6FQn/vMpJiqxJHCL9jk6HgvB5MEsu+lSeyVTqtN7VlZ6E6sSGEz3Yb/Cl7UnnGp3AAmcmVR98WDox4YqAtLMOTtRPFww3oDyxSrqkhRu6Clwanw8h//TGovkHyYNhMj1q+hxOCjxwi9Ms396pobbSwWZamOV3aZDZ0KbC8m5VNPVDwVfl2uv7q95ZOWXSDXcvKCah3zyiIBtmgUctg/OoO2n0gunAv5QfXsAXnsvuH+ohPAcfAkho24jbVbhBYYlbg4H6v1lIyoeWoekoeuObKvI88f7s614mHp7gh+/SeHIj/6f681nrXeRf+8UoM+Vq8APjm59BWS88M4Zj3BhXQVPFV+M6bYso27xJ7/M6R2Q/yajVCJiKghOYiZFTkK3sOdQtPFoek8ywzZpenk2RCmddfixm4yVr02bw6viD4hTVAtW4SfHJaNHUmTermVLIu9Yrk4LEDU1f6qWwkWcxak/WiKb3CApimXF3AYByKfvRKS0EngM/kT0bMjqAzeMqKu/s/oUCXsDSxaC7kep8yRmz5xIg5ysz97tGwNId74nDRFYI4FM1JF/nGEH06udnNqUMehk+eyLGq3nBC9sh7qP9UZ01warzxB9eUjUBBZIQehTgiy7RPRvOgK1VqxKBKZSpaX/GgUTNTJ5EMp1SA9rZIPDfcNPaCHbwDvIg=","source":"GHINcom"}'
```

Lookup by State, First & Last Name

```sh
curl 'https://api2.ghin.com/api/v1/golfers.json?status=Active&from_ghin=true&per_page=25&sorting_criteria=full_name&order=asc&page=1&state=WA&last_name=Brannan&first_name=Randall&source=GHINcom' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1MTk0Iiwic2NwIjoidXNlciIsImF1ZCI6bnVsbCwiaWF0IjoxNzcyNTk1NjQ2LCJleHAiOjE3NzI2Mzg4NDYsImp0aSI6IjJlMGMzNDEzLTFhM2EtNGZiYy05MTk5LTNjN2RhODIxNzMxYSJ9.o5tn6tv4JL-crYET81_wL-pY2tsNknO9HXzbSWEBVgg' \
  -H 'origin: https://www.ghin.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.ghin.com/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
```

Lookup by GHIN id

```sh
curl 'https://api2.ghin.com/api/v1/golfers.json?status=Active&from_ghin=true&per_page=25&sorting_criteria=full_name&order=asc&page=1&state=WA&golfer_id=3315181&source=GHINcom' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1MTk0Iiwic2NwIjoidXNlciIsImF1ZCI6bnVsbCwiaWF0IjoxNzcyNTk1NjQ2LCJleHAiOjE3NzI2Mzg4NDYsImp0aSI6IjJlMGMzNDEzLTFhM2EtNGZiYy05MTk5LTNjN2RhODIxNzMxYSJ9.o5tn6tv4JL-crYET81_wL-pY2tsNknO9HXzbSWEBVgg' \
  -H 'origin: https://www.ghin.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.ghin.com/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
```

Get rounds for golfer

```sh
curl 'https://api2.ghin.com/api/v1/golfers/972030/scores.json?source=GHINcom' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1MTk0Iiwic2NwIjoidXNlciIsImF1ZCI6bnVsbCwiaWF0IjoxNzcyNTk1NjQ2LCJleHAiOjE3NzI2Mzg4NDYsImp0aSI6IjJlMGMzNDEzLTFhM2EtNGZiYy05MTk5LTNjN2RhODIxNzMxYSJ9.o5tn6tv4JL-crYET81_wL-pY2tsNknO9HXzbSWEBVgg' \
  -H 'origin: https://www.ghin.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.ghin.com/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
```
