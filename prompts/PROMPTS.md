# Prompts

## Email Formatting

- **qwen3.5-397b-a17b**: Nice formatting, had trakt & spotify API issues
- **glm-5**: formatting poor except for March 8, instruction following good
- **gpt-5-mini**: poor at everything

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

## Test Fargo Summary Prompt

Send a summary email via mailgun to greg@udon.org from nanobot@triptrak.link with any fargo changes for the group named "ox-monday". Make the listing sharp and succinct using html follow the format below. For any players with a rating change in the last seven days list their name, id, new & old rating and robustness. Update the database with any new ratings. Also, include a sorted table of all players in the league with their name, id and rating. Add the name of the model configured in the Nanobot config.json in the footer along with "v0.2.0".

## Weekly Fargo for Monday League

Every Monday at 4am pacific time, send a summary email via mailgun to greg@udon.org and Niko.butt@gmail.com from nanobot@triptrak.link with any fargo changes for the group named "ox-monday". Make the listing sharp and succinct. For any players with changes list their name, id, new & old rating and robustness. It should only include changes in the last 7 days and make sure you update the database with any new ratings. Also, include a sorted table of all players in the league with their name, id and rating.

## Weekly Planner Prompt

- Send a summary email via mailgun to greg@udon.org. Use the calendar to determine my location and timezone, by default use Seattle, WA unless there is another location on my upcoming calendar for the week. The email should contain the following:
  - Weather forecast for the week
  - Release of new track or record by one of my spotify followed artists in the next week
  - Future snooker matches in the coming week from followed players in my trello list lookup using the snooker skill


## Nicely formatted image

```txt
give me a table of everyone in the ox-monday group with their rating and robustness. Generate an HTML string of your table then Use a "headless browser" or a library to take a screenshot of that HTML and send the resulting png/jpg to telegram
```