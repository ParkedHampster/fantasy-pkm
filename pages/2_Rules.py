import streamlit as st

st.title("Rules")

rule_1 = st.expander(" 1 - Levels")
rule_1.markdown("""
| Pokemon Form | **Lv** |
|     ---:     | :--: |
|   1st Form   | **100** |
|   2nd Form   | **85** |
|   3rd Form   | **75** |
|   Legends    | **75** |
|   Non-Evo    | **80** |
""")

rule_2 = st.expander(" 2 - Items")
rule_2.markdown("""
- Only one of any item per team
- You may switch items between battle days
- Mega Stones, Z Crystals, and Orbs are BANNED
    - No items ending in -ite or -Z
        - E.g. Alakazite, Firium Z, etc.
""")

rule_3 = st.expander(" 3 - Move/Ability Restrictions")
rule_3.markdown("""
- No Hidden Power of any type
- Once a move has been used in battle, it is locked in on that Pokemon
- You may change moves on Pokemon BEFORE battle day, provided a move HAS NOT already been used in a previous battle
- Abilities of Pokemon used in battle are considered locked in, regardless of moves being revealed and/or the Ability activating
    - A Pokemon not revealed during battle is considered BLANK for team-building.
"""
)

rule_4 = st.expander(" 4 - Free Agencies ")
rule_4.markdown("""
- There will be two types of Free Agency:
    - Priority and First Come First Served (FCFS)
        - Priority FA will open Saturdays at 12:00am after battle days, and close Monday nights at 11:59pm
        - FCFS will open on Tuesdays at 12:00am, and close Thursday nights at 11:59pm
- Priority FA order will be decided by your overall record at the end of battle day (most losses takes first priority)
        - Record ties will be decided by remainder (lower remainder = higher priority)
        - Remainder ties will be decided by draft number (lower draft number = higher priority)
- You are allowed ONE swap per week, whether it is during Priority or FCFS
- Pokemon coming from Free Agency have blank movesets; you may put whatever you like on them
- Drafted Pokemon returning to Free Agency will have locked-in moves and Abilities cleared, making them blank
- Pokemon returning to Free Agency cannot be picked up again until the following week
"""
)

rule_5 = st.expander(" 5 - Trades ")
rule_5.markdown("""
- Trades can be made any day of the week EXCEPT battle day
- All potential trades must go into the group chat NO LATER than Thursdays at 8pm
    - This is to ensure everyone has a chance to vote before battle day
- Trades must be approved by the group, majority rules
- If all votes are not in by battle day, a trade is automatically approved
- Traded Pokemon must keep any locked-in moves, but unrevealed moves are considered blank slots for the recipient
- Traded Pokemon keep the Abilities they had before the trade if a Pokemon was previously used in battle  
(Pokemon NOT used in battle YET are considered completely blank for trades)
- You are allowed to make ONE trade per week, but you may trade multiple Pokemon with the same Trainer (up to 3)
- Trades must be made within the same category (first forms for first forms, nons for nons, etc.)
"""
)

rule_6 = st.expander(" 6 - Team-Building")
rule_6.markdown("""
- Create your teams/boxes under the "National Dex" format
- If a move, item, or, Ability returns as "Illegal", but the Pokemon CAN learn it naturally, select it anyway.  
We will be battling in the Custom Game format; this overrides anything considered illegal by Showdown rules.
- REGIONAL VARIANTS ARE BANNED
- Alolan, Galarian, Hisuian, and Paldean forms are not eligible to be used this season
"""
)

rule_7 = st.expander(" 7 - Battling")
rule_7.markdown("""
- You must have a registered username in order to issue/receive challenges
- We will be battling under the Gen 9 Custom Game format
- Team Preview will be HIDDEN
    - Use the below command in the chat on Showdown after finding a user
    - DO NOT SELECT A FORMAT AFTER FINDING A USER
    - Insert the below code into the chat box on Showdown and send the message to issue the challenge  
/challenge gen9customgame @@@ Item Clause, ! Team Preview, Terastal Clause
    - You will not get to choose your lead at the start of battle
    - Ensure the Pokemon you want to lead with is at the top of the team
- If the code does not work and there is a Team preview, select the lead you want and play the battle out
    - DO NOT use the Terrastilize button underneath your moves during battle
"""
)

st.markdown("""
## DISCLAIMER

This is our first season playing strictly through
Showdown. Because of this, the above rules are subject
to change/be revised, and new rules may be added as the
season progresses. Everyone's patience is appreciated,
let's have a great season!
"""
)