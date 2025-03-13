import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))

def test_view_daily_standup(page: Page):
    """User story:
    [U1] Som en användare, vill jag kunna se hur en daily scrum går till, så att jag kan lära mig göra på rätt sätt

    Acceptanskriterier:
    [A1.1] Det går att klicka på knappen "somewhere in the middle"
    [A1.2] Det går att klicka på knappen "Daily standup"
    [A1.3] Rubriken "Daily standup" ska vara synlig på webbsidan.

    Scenario:
    1. Klicka på knappen "somewhere in the middle"
    2. klicka på knappen vars text innehåller "daily standup"
    3. kontrollera att man ser en rubrik med texten "Daily standup"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")

    button_locator = page.get_by_role("button")
    middle_button = button_locator.get_by_text( re.compile("Somewhere in the middle") )
    middle_button.click(timeout=100)

    daily_button = page.get_by_role("button").get_by_text( re.compile("Daily standup") )
    expect(daily_button).to_have_count(1, timeout=100)  # Locator assertion
    daily_button.click()

    heading = page.get_by_role("heading").get_by_text( re.compile("Daily standup") )
    expect(heading).to_be_visible(timeout=100)
