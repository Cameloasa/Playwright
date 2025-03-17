import re
from asyncio import timeout

from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"), timeout= 2000)

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
    expect(page).to_have_title(re.compile("Agile helper"), timeout=2000)

    button_locator = page.get_by_role("button")
    middle_button = button_locator.get_by_text( re.compile("Somewhere in the middle") )
    middle_button.click(timeout=100)

    daily_button = page.get_by_role("button").get_by_text( re.compile("Daily standup") )
    expect(daily_button).to_have_count(1, timeout=100)  # Locator assertion
    daily_button.click()

    heading = page.get_by_role("heading").get_by_text( re.compile("Daily standup") )
    expect(heading).to_be_visible(timeout=100)

def test_view_sprint_planning(page: Page):
    """User story:
       [U2] Som en användare, vill jag kunna se Sprint planning
       för att förstå hur planeringen av en sprint går till och vilka steg som ingår.

       Acceptanskriterier:
       [A2.1] Det går att klicka på knappen "First"
       [A2.2] Det går att hitta knappen "Sprint Planning"
       [A2.3] Det går att klicka på knappen "Sprint Planning"
       [A2.4] Rubriken "Sprint Planning" ska vara synlig på webbsidan.

       Scenario:
       1. Klicka på knappen "First"
       2. Hitta button med texten "Sprint planning"
       3. klicka på knappen "Sprint planning"
       4. kontrollera att man ser en rubrik med texten "Sprint planning"

        Testscenario în Punktlista:
        1. Navigera till sidan https://lejonmanen.github.io/agile-helper/.
        2. Kontrollera att sidan har rätt titel "Agile helper" (implicit testning av sidans laddning).
        3. Hitta knappen "First" och kontrollera att den är synlig.
        4. Klicka på "First" och verifiera att knappen "Sprint Planning" blir synlig.
        5. Hitta knappen "Sprint Planning" och klicka på den.
        6. Kontrollera att rubriken "Sprint Planning" syns på sidan.
       """
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")
    expect(page).to_have_title(re.compile("Agile helper"), timeout=2000)

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click(timeout=100)

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()

    # Klicka på den
    sp_button.click(timeout=100)

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()

def test_view_sprint_retrospective(page: Page):
    """User story:
        [U3] Som en användare, vill jag kunna se Sprint retrospective

        Acceptanskriterier:
        [A3.1] Det går att klicka på knappen "Last"
        [A3.2] Det går att hitta knappen "Sprint retrospective"
        [A3.3] Det går att klicka på knappen "Sprint retrospective"
        [A3.4] Rubriken "Sprint retrospective" ska vara synlig på webbsidan.

        Scenario:
        1. Klicka på knappen "Last"
        2. Hitta knappen med texten "Sprint retrospective"
        3. Klicka på knappen vars text innehåller "sprint retrospective"
        4. kontrollera att man ser en rubrik med texten "Sprint retrospective"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    expect(page).to_have_title(re.compile("Agile helper"), timeout=2000)

    # Klicka på knappen "Last"
    locator = page.get_by_role("button")
    last_button = locator.get_by_text("Last")
    last_button.click(timeout=100)

    # Hitta knappen med texten "Sprint retrospective"
    retrospective_button = page.get_by_role("button").get_by_text(re.compile("Sprint retrospective"))
    expect(retrospective_button).to_be_visible()

    # klicka på knappen vars text innehåller "sprint retrospective"
    retrospective_button.click(timeout=100)

    # kontrollera att man ser en rubrik med texten "Sprint review"
    retrospective_heading = page.get_by_role("heading").get_by_text("Sprint retrospective")
    expect(retrospective_heading).to_be_visible()

def test_sprint_planning_start(page: Page):
    """User Story:
        [U4]Som en användare, vill jag kunna förstå stegen i sprint planning genom
        att läsa listan och se mer information genom att hovra över varje punkt,
        samt avsluta genom att starta sprinten.

        Scenario:
        1. Navigera till webbsidan: https://lejonmanen.github.io/agile-helper/
        2. Klicka på knappen "First".
        3. Klicka på knappen "Sprint planning".
        4. Klicka på knappen "Ok, we are done. Start the sprint.".
        5. Kontrollera att dialogrutan stängs.
    """
    """Testar detaljerad interaktion inom Sprint Planning-dialogen"""

    # Steg 1: Navigera till sidan
    page.goto("https://lejonmanen.github.io/agile-helper/")
    expect(page).to_have_title(re.compile("Agile helper"), timeout=2000)

    # Steg 2: Klicka på "First"
    first_button = page.get_by_role("button", name="First")
    first_button.click(timeout= 100)

    # Steg 3: Klicka på "Sprint planning"
    sprint_planning_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    sprint_planning_button.click(timeout= 100)

    # Steg 4: Klicka på "Ok, we are done. Start the sprint."
    start_sprint_button = page.get_by_role("button", name=re.compile("Start the sprint"))
    start_sprint_button.click(timeout= 100)

    # Steg 5: Kontrollera att dialogrutan är stängd
    dialog = page.locator("dialog")
    expect(dialog).not_to_be_visible()



