#!python
# ChristmasTime.py
# An Interactive Fiction game by Christopher "avarisclari" Weigle
# IFID = B25D3DDC-238D-4D68-8AE7-956ACFF9110E

import textwrap
import sys
import string
import os

sys.stdout.write("\x1b]2;Christmas Time\x07")

scenes = {
    "title": {
        "description": "\n"
                       "      * ***      *\n"
                       "    *  ****  * **                       *                    *\n"
                       "   *  *  ****  **                      ***                  **\n"
                       "  *  **   **   **                       *                   **\n"
                       " *  ***        **        ***  ****               ****     ********                                ****\n"
                       "**   **        **  ***    **** **** * ***       * **** * ********  *** **** ****       ****      * **** *\n"
                       "**   **        ** * ***    **   ****   ***     **  ****     **      *** **** ***  *   * ***  *  **  ****\n"
                       "**   **        ***   ***   **           **    ****          **       **  **** ****   *   ****  ****\n"
                       "**   **        **     **   **           **      ***         **       **   **   **   **    **     ***\n"
                       "**   **        **     **   **           **        ***       **       **   **   **   **    **       ***\n"
                       " **  **        **     **   **           **          ***     **       **   **   **   **    **         ***\n"
                       "  ** *      *  **     **   **           **     ****  **     **       **   **   **   **    **    ****  **\n"
                       "   ***     *   **     **   ***          **    * **** *      **       **   **   **   **    **   * **** *\n"
                       "    *******    **     **    ***         *** *    ****        **      ***  ***  ***   ***** **     ****\n"
                       "      ***       **    **                 ***                          ***  ***  ***   ***   **\n"
                       "  ****           *    *\n"
                       " *  *************    *\n"
                       "*     *********     ***\n"
                       "*     *  *         * *\n"
                       " **  *  **\n"
                       "    *  ***         ***     *** **** ****       ***\n"
                       "   **   **          ***     *** **** ***  *   * ***\n"
                       "   **   **           **      **  **** ****   *   ***\n"
                       "   **   **           **      **   **   **   **    ***\n"
                       "   **   **           **      **   **   **   ********\n"
                       "    **  **           **      **   **   **   *******\n"
                       "     ** *      *     **      **   **   **   **\n"
                       "      ***     *      **      **   **   **   ****    *\n"
                       "       *******       *** *   ***  ***  ***   *******\n"
                       "         ***          ***     ***  ***  ***   *****",
        "paths": [
            { "go_to": "opening", "phrase": "It was a crisp, snowy night..." },
            { "go_to": "about", "phrase": "About" }
            ]
        },
    "opening": {
        "description": "I was standing on my front porch, watching the snow drift"
                       " down. The light from my study shone outside. I took a sip"
                       " of my cocoa, and my glasses fogged up from the steam. "
                       "I was wearing a light brown fleece sweater, and blue "
                       "jeans. I recall this because of what happened that day."
                       " I stood there lost in thought for the better part of "
                       "an hour.",
        "paths": [
            { "go_to": "the_letter_arrives", "phrase": "Earlier that day..." }
            ]
        },
    "the_letter_arrives": {
        "description":    "I received a letter. It was from my father. It wished"
                          " me a Merry Christmas. Nothing more. The letter was a"
                          " shock for many reasons, the main one being my father"
                          " had passed three months prior. I opted to call my "
                          "mother.\n\"Hey, honey!\"\n\"Hi, mom. Have you checked"
                          " your mail today?\"\n\"No, I haven't.\"\n I paused "
                          "and took a deep breath. I looked at the paper in my "
                          "hand.\n\"I'm calling about Dad.\"\nA moment of silence."
                          "\n\"What about him?\"\n\"I received a letter.\"\n I "
                          "heard a faint gasp, like she tried covering her mouth"
                          " before the noise could escape her lips.",
        "paths": [
            { "go_to": "the_second_letter", "phrase": "I asked her to check her mail." },
            { "go_to": "the_meeting", "phrase": "I asked her if we could meet downtown." }
            ]
        },
    "the_meeting": {
        "description": "The downtown tree is surrounded by tourists, passersby,"
                       " and \"traditional\" carolers. I see my mother across "
                       "the street, and wave her over. We started walking down "
                       "the sidewalk.\n\"I got one too, honey.\"\n I looked at "
                       "her. I looked ahead and kept walking.\n\"I'm, sorry. "
                       "I know you miss him.\"\nI ignored her and kept walking."
                       " We turned into a small restaurant, and sat at a table.",
        "paths": [
            { "go_to": "the_second_letter1", "phrase": "Mom started reading..." }
            ]
        },
    "the_second_letter1": {
        "description": "\"Dearest,\n    I know this letter will come as a shock"
                       " to you. I wrote this to wish you and all our family a "
                       "Merry Christmas. Did you put up decorations? It must "
                       "have been painful for you, as it was my favorite time "
                       "of year. Did you give the mailman something for his "
                       "trouble?\n    I know you and our children must miss me."
                       " Please, take care of them. And don't refuse them help."
                       " We are all family after all.\n\nWith love, \nMerry "
                       "Christmas\"",
        "paths": [
            { "go_to": "silence", "phrase": "She sat there silent." }
            ]
        },
    "silence": {
        "description": "I sat there looking down at the table. Mom was staying "
                       "silent the whole time. I didn't know how to respond after"
                       " hearing my father's letter to her. The waiter started "
                       "approaching, and then continued away after seeing we "
                       "weren't ready at all. \n\"Oh... Quentin...\"\nIf it "
                       "wasn't so quiet, I wouldn't have heard her. I apologized"
                       "and we decided to leave without ordering anything.",
        "paths": [
            { "go_to": "home_again", "phrase": "I unlocked my house and went"
                                                 " inside." }
            ]
        },
    "the_second_letter": {
        "description": "A few minutes pass. I sit there waiting for my mother to"
                       " get back to her phone. I hear a shuffling noise, as "
                       "the phone is picked back up.\n\"Honey? I...\"\nI could "
                       "hear the muffled sound of a small cry and something hitting"
                       " paper.\n\"Mom, what is it?\"\n\"I got one too.\"\nI "
                       "was pretty sure that noise was her tears hitting the "
                       "envelope.\n\"Mom? Are you alright?\"\nI heard the tear "
                       "of paper, and then she started reading it to me.",
        "paths": [
            { "go_to": "the_second_letter_read", "phrase": "It opened with..." }
            ]
        },
    "the_second_letter_read": {
        "description": "\"Dearest,\n    I know this letter will come as a shock"
                       " to you. I wrote this to wish you and all our family a "
                       "Merry Christmas. Did you put up decorations? It must "
                       "have been painful for you, as it was my favorite time "
                       "of year. Did you give the mailman something for his "
                       "trouble?\n    I know you and our children must miss me."
                       " Please, take care of them. And don't refuse them help."
                       " We are all family,1 after all.\n\nWith love, \nMerry "
                       "Christmas\"",
        "paths": [
            { "go_to": "my_sisters_letter", "phrase": "My phone said my sister was calling..." },
            { "go_to": "my_aunts_letter", "phrase": "Mother said my aunt was calling..." }
            ]
        },
    "my_aunts_letter":{
        "description": "\"Oh, alright.\"\nI looked at the time and sighed. I "
                       "said good bye and hung up. A few minutes later my phone"
                       " rang. I answered it and was surprised to hear both my "
                       "mother and aunt on it. Mom quickly explained that Alice"
                       " had received a letter as well, and we should see what "
                       "it said. I started, and sat back down. \"Are you okay "
                       "with that?\"\nI wanted to make sure Aunt Alice was "
                       "willing to share her letter with us. She took it hardest"
                       " after all.",
        "paths": [
            { "go_to": "my_aunts_letter_read", "phrase": "\"Yes,\" she said softly" }
            ]
        },
    "my_aunts_letter_read": {
        "description":  "Alice,\n    How are you doing, sis? Do you miss your "
                       "younger brother yet? I'm glad to know that you got "
                       "engaged. Tell James that I couldn't be happier for you"
                       " two.\n    Now... I need you to be strong. I know you "
                       "have been beating yourself up since all this began. I "
                       "know you think that you should have gotten it. You always"
                       " did try to protect me. I let you, probably a little too"
                       " much. \n    Alice... I'm glad you were my sister. I'm "
                       "only sorry Ricky didn't make it. I know it hurts to lose"
                       " two little brothers. But don't worry. I had a happy life."
                       " I had you for my sister, and Lucille for my wife. I had"
                       " two wonderful children with her. Don't lose sight of "
                       "them or James.\n\nLots of Love, Tinner.",
        "paths": [
            { "go_to": "my_letter1", "phrase": "So far the letters contained "
                                                    "more than mine."}
            ]
        },
    "home_again": {
        "description": "As I entered my house, I looked at the opened envelope "
                       "on my desk. I sighed. I looked over the envelope, searching"
                       " for any information I might have missed. I found nothing"
                       ", and put it to the side. I booted up my computer and "
                       " logged in. I looked through my social accounts, checking"
                       " for any news from anyone. A chat window opened on one,"
                       " blank at first as the site loaded it. \n\"Hey, you there"
                       "?\"",
        "paths": [
            { "go_to": "my_sister_chat", "phrase": "This was my first time "
                                                       "hearing from my sister"
                                                          " in a while." },
            { "go_to": "my_aunt_chat", "phrase": "It was rare for my aunt to "
                                                    "contact me." }
            ]
        },
    "my_sister_chat": {
        "description": "I replied, confirming I was actually at my computer. I "
                       "waited 5 minutes before asking if something was wrong. "
                       "\n\"I got something today.\"\nI looked at those words, "
                       "already sure I knew what it was. I paused a second and "
                       "responded, asking if it was a letter.\"Yes.\"\nI froze,"
                       " and looked at my letter, and thought back to my mother's"
                       ". I started asking who it was from, but got the answer "
                       "before I could finish. Dad sent one to her as well. I "
                       "sent a voice chat request, and asked if she could tell "
                       "me what he wrote.",
        "paths": [
            { "go_to": "my_sisters_note", "phrase": "She accepted and began reading" }
            ]
        },
    "my_sisters_note": {
        "description": "Dear Adrianna,\n    My lovely daughter, how do you fare?"
                       " How is your husband? I'm only kidding. I don't expect "
                       "you to wed anytime soon. Are you still seeing Alexander?"
                       " He was a nice man. \n    I know you are surprised to see"
                       " this letter. I suspect everyone will be. I don't know "
                       "how long I've been gone now. \n    Look, I'm not going "
                       "to tell you anything about living your life to the full"
                       "est. You live however makes you happy. I just wanted "
                       "you to know that I love you. You are a wonderful woman "
                       "who your mother and I raised to be true to herself."
                       "\n    Please, Adrianna, take care. I know you hate your"
                       "full first name, but I chose it for you because it was "
                       "as beautiful as you were when you were born. If Alexander"
                       " is still in your life, tell him I said Merry Christmas."
                       " Also, pass on the message that I said he can.\n\nAlways"
                       " in your heart,\nQuinten Favreau \n\n P.S. Merry Christmas"
                       ", Sweetheart.",
        "paths": [
            { "go_to": "my_letter", "phrase": "So far, the letters contained "
                                                "more than mine." }
            ]
        },
    "my_aunt_chat": {
        "description": "I asked her what was going on. She never messages me, "
                       "so I thought it strange she should now. The chat box "
                       "registered several times that she was typing, but then "
                       "would clear out as though she couldn't find the right "
                       "words. Finally she responded.\n\"Your father mailed me.\""
                       "\nI looked at the screen, making sure I saw that right."
                       " I asked what he said without thinking. A long pause. "
                       "Then a long period of typing showed on the screen. I "
                       "apologized for asking, but the typing continued.",
        "paths": [
            { "go_to": "aunt_letter", "phrase": "When the message finally "
                                                    "appeared, I had to scroll"
                                                        "to read it." }
            ]
        },
    "aunt_letter": {
        "description": "Alice,\n    How are you doing, sis? Do you miss your "
                       "younger brother yet? I'm glad to know that you got "
                       "engaged. Tell James that I couldn't be happier for you"
                       " two.\n    Now... I need you to be strong. I know you "
                       "have been beating yourself up since all this began. I "
                       "know you think that you should have gotten it. You always"
                       " did try to protect me. I let you, probably a little too"
                       " much. \n    Alice... I'm glad you were my sister. I'm "
                       "only sorry Ricky didn't make it. I know it hurts to lose"
                       " two little brothers. But don't worry. I had a happy life."
                       " I had you for my sister, and Lucille for my wife. I had"
                       " two wonderful children with her. Don't lose sight of "
                       "them or James.\n\nLots of Love, Tinner.",
        "paths": [
            { "go_to": "my_letter1", "phrase": "So far, the letters contained "
                                                 "more than mine." }
            ]
        },
    "my_sisters_letter": {
        "description": "I told my mother that my sister was calling and I'd talk"
                       " to her later. I switched over to my sister. She sounded "
                       "like she had been crying.\n\"I just got a l-l\"\nShe was"
                       " stuttering. I knew where she was going.\n\"Dad?\"\n"
                       "\"Yeah.\"\nI looked at the letter in my hand. I was "
                       "getting a strange feeling in my gut. I looked at my "
                       "letter and told her everything was going to be alright."
                       " I told her about mom's letter, and she calmed down a bit"
                       ". I then told her about mine.",
        "paths": [
            { "go_to": "my_sisters_letter_read", "phrase": "Her letter said more..."
                                                            " much more." }
            ]
        },
    "my_sisters_letter_read": {
        "description": "Dear Adrianna,\n    My lovely daughter, how do you fare?"
                       " How is your husband? I'm only kidding. I don't expect "
                       "you to wed anytime soon. Are you still seeing Alexander?"
                       " He was a nice man. \n    I know you are surprised to see"
                       " this letter. I suspect everyone will be. I don't know "
                       "how long I've been gone now. \n    Look, I'm not going "
                       "to tell you anything about living your life to the full"
                       "est. You live however makes you happy. I just wanted "
                       "you to know that I love you. You are a wonderful woman "
                       "who your mother and I raised to be true to herself."
                       "\n    Please, Adrianna, take care. I know you hate your"
                       " full first name, but I chose it for you because it was "
                       "as beautiful as you were when you were born. If Alexander"
                       " is still in your life, tell him I said Merry Christmas."
                       " Also, pass on the message that I said he can.\n\nAlways"
                       " in your heart,\nQuinten Favreau \n\n P.S. Merry Christmas"
                       ", Sweetheart.",
        "paths": [
            { "go_to": "my_letter", "phrase": "So far, the letters contained "
                                                             "more than mine." },
            { "go_to": "family_meeting", "phrase": "I needed to call the family"
                                                        " and see who all "
                                                          "recieved a letter." }
            ]
        },
    "my_letter": {
        "description": "I sat down at my desk and looked over my letter once "
                       "more. All that was on it was those few words. \n\"Merry"
                       " Christmas. \n\nLove, \nQuinten Favreau\" \n\nI looked at"
                       " my envelope, and sighed. Other than my name and address"
                       " there was nothing to go by. I tapped my fingers on the"
                       " desk, lost in thought. \n\"Why would Father send me a "
                       "short note, when going into detail with my mother and "
                       "sister? Did he have nothing to say to me?\" \nI sighed,"
                       "and looked out the window, seeing clouds start rolling "
                       "in. My father and I were very close. We had the same "
                       "sense of humor, and I was by his side when he passed. "
                       "I looked at my phone, and saw it was only 14:30.",
        "paths": [
            { "go_to": "family_meeting", "phrase": "I decided to call everyone "
                                                        "and see if anyone else"
                                                             " knew about this." }
            ]
        },
    "my_letter1": {
        "description": "I sat down at my desk and looked over my letter once "
                       "more. All that was on it was those few words. \n\"Merry"
                       " Christmas. \n\n Love, \nQuinten Favreau\" \n\nI looked at"
                       " my envelope, and sighed. Other than my name and address"
                       " there was nothing to go by. I tapped my fingers on the"
                       " desk, lost in thought. \n\"Why would Father send me a "
                       "short note, when going into detail with my mother and "
                       "sister? Did he have nothing to say to me?\" \nI sighed,"
                       "and looked out the window, seeing clouds start rolling "
                       "in. My father and I were very close. We had the same "
                       "sense of humor, and I was by his side when he passed. "
                       "I looked at my phone, and saw it was only 14:30.",
        "paths": [
            { "go_to": "family_meeting1", "phrase": "I decided to call everyone "
                                                        "and see if anyone else"
                                                             " knew about this." }
            ]
        },
    "family_meeting": {
        "description": "The first to arrive at the restaurant was my grandmother."
                       " She was always prepunctual, and today was no exception."
                       " She sat across from me at the table. We didn't utter a"
                       " single word. We were waiting on the others. The waiter"
                       " took our drink orders and left us. My sister arrived "
                       "next. She stood there looking around, until I waved her"
                       " over. She sat next to me, and ordered a drink. She "
                       "greeted our grandmother, and then sat there quietly. "
                       "Finally, our mother and aunt arrived. As they sat down,"
                       " I started speaking. My mother quickly hushed me. \n\""
                       "We're still waiting on one more.\"\nI looked at her and"
                       " blinked. I wasn't sure who she was talking about. Ten"
                       " minutes passed, then Frank appeared. I gulped. My "
                       "mother glared at me. Frank sat next to my grandmother, "
                       "and placed an envelope on the table, addressed to him."
                       " My mother followed suit, then my sister and my "
                       "grandmother. \n\"So...\" I began. \"Who wants to start?",
        "paths": [
            { "go_to": "franks_letter", "phrase": "Frank nodded almost imperceptibly",},
            { "go_to": "grandmas_letter", "phrase": "Our grandmother picked up"
                                                        "her letter." },
            { "go_to": "aunts_letter", "phrase": "Aunt Alice pulled her letter"
                                                    "from her purse."}
            ]
        },
        "grandmas_letter": {
        "description": "Hello Mom.\n    How long has it been since I last wrote"
                       " you a letter? I know this is hard on you. No one wants"
                       " to lose their child before they go. I'm sorry I didn't"
                       " visit or call as often as you would have liked. You did"
                       " a terrific job of raising me, just ask your daughter-in"
                       "-law.\n    Mom, I love you. I know I rarely said it to "
                       "you. Did you know... Well... When your time is almost "
                       "up you can hear the most beautiful song. I'm sure even "
                       "Beethoven heard it before he left this world. He could "
                       "have made it so all could hear it, but even he disappeared"
                       " before it could be written.\n    I digress. I'm sorry."
                       " I want you to know that no one else could have raised me"
                       " like you and Pop did. I'll give him your love in the "
                       "next world. Merry Christmas, Mom. \n\nYour loving son,"
                       "\nQuinten Favreau \n\nP.S. Lucille said she'll do her"
                       " best to help you when you need it.",
        "paths": [
            { "go_to": "grandmaa", "phrase": "She sat there smiling." }
            ]
        },
    "grandmaa": {
        "description": "I haven't seen her that happy since before Grandpa died."
                       " I reached across the table and squeezed her hand. She "
                       "had tears going down her cheeks as well, but hers seemed"
                       " to not stem from sadness, but gratitude. Father wrote her"
                       " to comfort her. What surprised me was hearing about the"
                       " song. He never mentioned it when I was by his side. He "
                       "just looked at the ceiling, smiled and closed his eyes."
                       " He accepted his fate, when we were still pleading with"
                       " the doctors. \nI got shaken out of my memories by my "
                       "aunt clearing her throat. We all looked at her, and I "
                       "nodded.",
        "paths": [
            { "go_to": "alice_letter1", "phrase": "She pulled her letter out of"
                                                    "her purse and cleared"
                                                        " her throat." }
            ]
        },
    "family_meeting1": {
        "description": "The first to arrive at the restaurant was my grandmother."
                       " She was always prepunctual, and today was no exception."
                       " She sat across from me at the table. We didn't utter a"
                       " single word. We were waiting on the others. The waiter"
                       " took our drink orders and left us. My sister arrived "
                       "next. She stood there looking around, until I waved her"
                       " over. She sat next to me, and ordered a drink. She "
                       "greeted our grandmother, and then sat there quietly. "
                       "Finally, our mother and aunt arrived. As they sat down,"
                       " I started speaking. My mother quickly hushed me. \n\""
                       "We're still waiting on one more.\"\nI looked at her and"
                       " blinked. I wasn't sure who she was talking about. Ten"
                       " minutes passed and then Frank appeared. I gulped. My "
                       "mother glared at me. Frank sat next to my grandmother, "
                       "and placed an envelope on the table, addressed to him."
                       " My mother followed suit, then my sister and my "
                       "grandmother. \n\"So...\" I began. \"Who wants to start?",
        "paths": [
            { "go_to": "franks_letter1", "phrase": "Frank nodded almost imperceptibly" },
            { "go_to": "grandmas_letter1", "phrase": "Our grandmother picked up"
                                                        "her letter." },
            { "go_to": "adriannas_letter", "phrase": "Adrianna pulled her letter"
                                                    "from the envelope."}
            ]
        },
    "franks_letter": {
        "description": "Frank,\n    How are you, my old friend? I trust you are "
                       "doing fine. I know we haven't talked in awhile. I'm "
                       "sorry for everything. You were my best friend. Did you"
                       " attend my funeral? If you didn't, I would understand. "
                       "\n    I want you to know something. After all this time"
                       ", I still regret it. However, I also know that you "
                       "deserve a better friend than me. Please, take care of "
                       "yourself. I only wish you the best. \n    One more thing"
                       ", Frank. Please, don't hate my family for my mistake. "
                       "I wanted to say all this to you before I pass on, but..."
                       " well I don't have much time left. I want you to have "
                       "a Merry Christmas.\n\nMay We Be Friends Again,\nQuinten"
                       " Favreau",
        "paths": [
            { "go_to": "tears", "phrase": "Frank could barely manage to say"
                                            " my father's name by the end." }
            ]
        },
    "tears": {
        "description": "The letter was already wet. Frank was crushing the edges"
                       " in his hands as tears poured down his face. I didn't "
                       "know what had happened between them, as my father didn't"
                       " like to talk about it. The letter meant nothing to me,"
                       " nor my sister, but we could hear our father's cries "
                       "for forgiveness as though he were right there.\nOur"
                       " mother hugged Frank. Tears rolled down her cheeks as "
                       "well. Grandma gently pulled the letter from Frank's hands"
                       " and sighed.\n\"Sorry, Myrtle. Please... What did Quinten"
                       " say to you?\"",
    "paths": [
        { "go_to": "grandmas_lettera", "phrase": "Grandma took a sip of her drink, "
                                                    "and began reading." }
        ]
        },
    "franks_letter1": {
        "description": "Frank,\n    How are you, my old friend? I trust you are "
                       "doing fine. I know we haven't talked in awhile. I'm "
                       "sorry for everything. You were my best friend. Did you"
                       " attend my funeral? If you didn't, I would understand. "
                       "\n    I want you to know something. After all this time"
                       ", I still regret it. However, I also know that you "
                       "deserve a better friend than me. Please, take care of "
                       "yourself. I only wish you the best. \n    One more thing"
                       ", Frank. Please, don't hate my family for my mistake. "
                       "I wanted to say all this to you before I pass on, but..."
                       " well I don't have much time left. I want you to have "
                       "a Merry Christmas.\n\nMay We Be Friends Again,\nQuinten"
                       " Favreau",
        "paths": [
            { "go_to": "tears1", "phrase": "Frank could barely manage to say"
                                            " my father's name by the end." }
            ]
        },
    "tears1": {
        "description": "The letter was already wet. Frank was crushing the edges"
                       " in his hands as tears poured down his face. I didn't "
                       "know what had happened between them, as my father didn't"
                       " like to talk about it. The letter meant nothing to me,"
                       " nor my sister, but we could hear our father's cries "
                       "for forgiveness as though he were right there.\nOur"
                       " mother hugged Frank. Tears rolled down her cheeks as "
                       "well. Grandma gently pulled the letter from Frank's hands"
                       " and sighed.\n\"Sorry, Myrtle. Please... What did Quinten"
                       " say to you?\"",
    "paths": [
        { "go_to": "grandmas_letterb", "phrase": "Grandma took a sip of her drink, "
                                                    "and began reading." }
        ]
        },
    "franks_letter2": {
        "description": "Frank,\n    How are you, my old friend? I trust you are "
                       "doing fine. I know we haven't talked in awhile. I'm "
                       "sorry for everything. You were my best friend. Did you"
                       " attend my funeral? If you didn't, I would understand. "
                       "\n    I want you to know something. After all this time"
                       ", I still regret it. However, I also know that you "
                       "deserve a better friend than me. Please, take care of "
                       "yourself. I only wish you the best. \n    One more thing"
                       ", Frank. Please, don't hate my family for my mistake. "
                       "I wanted to say all this to you before I pass on, but..."
                       " well I don't have much time left. I want you to have "
                       "a Merry Christmas.\n\nMay We Be Friends Again,\nQuinten"
                       " Favreau",
        "paths": [
            { "go_to": "tears2", "phrase": "Frank could barely manage to say"
                                            " my father's name by the end." }
            ]
        },
    "tears2": {
        "description": "The letter was already wet. Frank was crushing the edges"
                       " in his hands as tears poured down his face. I didn't "
                       "know what had happened between them, as my father didn't"
                       " like to talk about it. The letter meant nothing to me,"
                       " nor my sister, but we could hear our father's cries "
                       "for forgiveness as though he were right there.\nOur"
                       " mother hugged Frank. Tears rolled down her cheeks as "
                       "well. Grandma gently pulled the letter from Frank's hands"
                       " and sighed.",
    "paths": [
        {  "go_to": "afterwards", "phrase": "It was quiet." }
        ]
        },
    "franks_letter3": {
        "description": "Frank,\n    How are you, my old friend? I trust you are "
                       "doing fine. I know we haven't talked in awhile. I'm "
                       "sorry for everything. You were my best friend. Did you"
                       " attend my funeral? If you didn't, I would understand. "
                       "\n    I want you to know something. After all this time"
                       ", I still regret it. However, I also know that you "
                       "deserve a better friend than me. Please, take care of "
                       "yourself. I only wish you the best. \n    One more thing"
                       ", Frank. Please, don't hate my family for my mistake. "
                       "I wanted to say all this to you before I pass on, but..."
                       " well I don't have much time left. I want you to have "
                       "a Merry Christmas.\n\nMay We Be Friends Again,\nQuinten"
                       " Favreau",
        "paths": [
            { "go_to": "tears3", "phrase": "Frank could barely manage to say"
                                            " my father's name by the end." }
            ]
        },
    "tears3": {
        "description": "The letter was already wet. Frank was crushing the edges"
                       " in his hands as tears poured down his face. I didn't "
                       "know what had happened between them, as my father didn't"
                       " like to talk about it. The letter meant nothing to me,"
                       " nor my sister, but we could hear our father's cries "
                       "for forgiveness as though he were right there.\nOur"
                       " mother hugged Frank. Tears rolled down her cheeks as "
                       "well. Grandma gently pulled the letter from Frank's hands"
                       " and sighed.\n\"Sorry, Myrtle. Please... What did Quinten"
                       " say to you?\"",
    "paths": [
        { "go_to": "grandmas_letter2", "phrase": "Grandma took a sip of her drink, "
                                                    "and began reading." }
        ]
        },
    "grandmas_lettera": {
        "description": "Hello Mom.\n    How long has it been since I last wrote"
                       " you a letter? I know this is hard on you. No one wants"
                       " to lose their child before they go. I'm sorry I didn't"
                       " visit or call as often as you would have liked. You did"
                       " a terrific job of raising me, just ask your daughter-in"
                       "-law.\n    Mom, I love you. I know I rarely said it to "
                       "you. Did you know... Well... When your time is almost "
                       "up you can hear the most beautiful song. I'm sure even "
                       "Beethoven heard it before he left this world. He could "
                       "have made it so all could hear it, but even he disappeared"
                       " before it could be written.\n    I digress. I'm sorry."
                       " I want you to know that no one else could have raised me"
                       " like you and Pop did. I'll give him your love in the "
                       "next world. Merry Christmas, Mom. \n\nYour loving son,"
                       "\nQuinten Favreau \n\nP.S. Lucille said she'll do her"
                       " best to help you when you need it.",
        "paths": [
            { "go_to": "grandma", "phrase": "She sat there smiling." }
            ]
        },
    "grandma": {
        "description": "I haven't seen her that happy since before Grandpa died."
                       " I reached across the table and squeezed her hand. She "
                       "had tears going down her cheeks as well, but hers seemed"
                       " to not stem from sadness, but gratitude. Father wrote her"
                       " to comfort her. What surprised me was hearing about the"
                       " song. He never mentioned it when I was by his side. He "
                       "just looked at the ceiling, smiled and closed his eyes."
                       " He accepted his fate, when we were still pleading with"
                       " the doctors. \nI got shaken out of my memories by my "
                       "aunt clearing her throat. We all looked at her, and I "
                       "nodded.",
        "paths": [
            { "go_to": "alice_letter", "phrase": "She pulled her letter out of"
                                                    "her purse and cleared"
                                                        " her throat." }
            ]
        },
    "grandmas_letterb": {
        "description": "Hello Mom.\n    How long has it been since I last wrote"
                       " you a letter? I know this is hard on you. No one wants"
                       " to lose their child before they go. I'm sorry I didn't"
                       " visit or call as often as you would have liked. You did"
                       " a terrific job of raising me, just ask your daughter-in"
                       "-law.\n    Mom, I love you. I know I rarely said it to "
                       "you. Did you know... Well... When your time is almost "
                       "up you can hear the most beautiful song. I'm sure even "
                       "Beethoven heard it before he left this world. He could "
                       "have made it so all could hear it, but even he disappeared"
                       " before it could be written.\n    I digress. I'm sorry."
                       " I want you to know that no one else could have raised me"
                       " like you and Pop did. I'll give him your love in the "
                       "next world. Merry Christmas, Mom. \n\nYour loving son,"
                       "\nQuinten Favreau \n\nP.S. Lucille said she'll do her"
                       " best to help you when you need it.",
        "paths": [
            { "go_to": "grandmab", "phrase": "She sat there smiling." }
            ]
        },
    "grandmab": {
        "description": "I haven't seen her that happy since before Grandpa died."
                       " I reached across the table and squeezed her hand. She "
                       "had tears going down her cheeks as well, but hers seemed"
                       " to not stem from sadness, but gratitude. Father wrote her"
                       " to comfort her. What surprised me was hearing about the"
                       " song. He never mentioned it when I was by his side. He "
                       "just looked at the ceiling, smiled and closed his eyes."
                       " He accepted his fate, when we were still pleading with"
                       " the doctors. \nI got shaken out of my memories by my "
                       "sister clearing her throat. We all looked at her, and I "
                       "nodded.",
        "paths": [
            { "go_to": "adrianna_letter", "phrase": "She pulled her letter out of"
                                                    "the envelope and cleared"
                                                        " her throat." }
            ]
        },
    "grandmas_letter1": {
        "description": "Hello Mom.\n    How long has it been since I last wrote"
                       " you a letter? I know this is hard on you. No one wants"
                       " to lose their child before they go. I'm sorry I didn't"
                       " visit or call as often as you would have liked. You did"
                       " a terrific job of raising me, just ask your daughter-in"
                       "-law.\n    Mom, I love you. I know I rarely said it to "
                       "you. Did you know... Well... When your time is almost "
                       "up you can hear the most beautiful song. I'm sure even "
                       "Beethoven heard it before he left this world. He could "
                       "have made it so all could hear it, but even he disappeared"
                       " before it could be written.\n    I digress. I'm sorry."
                       " I want you to know that no one else could have raised me"
                       " like you and Pop did. I'll give him your love in the "
                       "next world. Merry Christmas, Mom. \n\nYour loving son,"
                       "\nQuinten Favreau \n\nP.S. Lucille said she'll do her"
                       " best to help you when you need it.",
        "paths": [
            { "go_to": "grandma1", "phrase": "She sat there smiling." }
            ]
        },
    "grandma1": {
        "description": "I haven't seen her that happy since before Grandpa died."
                       " I reached across the table and squeezed her hand. She "
                       "had tears going down her cheeks as well, but hers seemed"
                       " to not stem from sadness, but gratitude. Father wrote her"
                       " to comfort her. What surprised me was hearing about the"
                       " song. He never mentioned it when I was by his side. He "
                       "just looked at the ceiling, smiled and closed his eyes."
                       " He accepted his fate, when we were still pleading with"
                       " the doctors. \nI got shaken out of my memories by my "
                       "sister clearing her throat. We all looked at her, and I "
                       "nodded.",
        "paths": [
            { "go_to": "adrianna_letter1", "phrase": "She pulled her letter out of"
                                                    "her purse and cleared"
                                                        " her throat." }
            ]
        },
    "grandmas_letter2": {
        "description": "Hello Mom.\n    How long has it been since I last wrote"
                       " you a letter? I know this is hard on you. No one wants"
                       " to lose their child before they go. I'm sorry I didn't"
                       " visit or call as often as you would have liked. You did"
                       " a terrific job of raising me, just ask your daughter-in"
                       "-law.\n    Mom, I love you. I know I rarely said it to "
                       "you. Did you know... Well... When your time is almost "
                       "up you can hear the most beautiful song. I'm sure even "
                       "Beethoven heard it before he left this world. He could "
                       "have made it so all could hear it, but even he disappeared"
                       " before it could be written.\n    I digress. I'm sorry."
                       " I want you to know that no one else could have raised me"
                       " like you and Pop did. I'll give him your love in the "
                       "next world. Merry Christmas, Mom. \n\nYour loving son,"
                       "\nQuinten Favreau \n\nP.S. Lucille said she'll do her"
                       " best to help you when you need it.",
        "paths": [
            { "go_to": "grandma2", "phrase": "She sat there smiling." }
            ]
        },
    "grandma2": {
        "description": "I haven't seen her that happy since before Grandpa died."
                       " I reached across the table and squeezed her hand. She "
                       "had tears going down her cheeks as well, but hers seemed"
                       " to not stem from sadness, but gratitude. Father wrote her"
                       " to comfort her. What surprised me was hearing about the"
                       " song. He never mentioned it when I was by his side. He "
                       "just looked at the ceiling, smiled and closed his eyes."
                       " He accepted his fate, when we were still pleading with"
                       " the doctors.",
        "paths": [
            {  "go_to": "afterwards", "phrase": "It was quiet." }
            ]
        },
    "adrianna_letter": {
        "description": "Dear Adrianna,\n    My lovely daughter, how do you fare?"
                       " How is your husband? I'm only kidding. I don't expect "
                       "you to wed anytime soon. Are you still seeing Alexander?"
                       " He was a nice man. \n    I know you are surprised to see"
                       " this letter. I suspect everyone will be. I don't know "
                       "how long I've been gone now. \n    Look, I'm not going "
                       "to tell you anything about living your life to the full"
                       "est. You live however makes you happy. I just wanted "
                       "you to know that I love you. You are a wonderful woman "
                       "who your mother and I raised to be true to herself."
                       "\n    Please, Adrianna, take care. I know you hate your"
                       "full first name, but I chose it for you because it was "
                       "as beautiful as you were when you were born. If Alexander"
                       " is still in your life, tell him I said Merry Christmas."
                       " Also, pass on the message that I said he can.\n\nAlways"
                       " in your heart,\nQuinten Favreau \n\n P.S. Merry Christmas"
                       ", Sweetheart.",
        "paths": [
            {  "go_to": "afterwards", "phrase": "It was quiet." }
            ]
        },
    "adrianna_letter1": {
        "description": "Dear Adrianna,\n    My lovely daughter, how do you fare?"
                       " How is your husband? I'm only kidding. I don't expect "
                       "you to wed anytime soon. Are you still seeing Alexander?"
                       " He was a nice man. \n    I know you are surprised to see"
                       " this letter. I suspect everyone will be. I don't know "
                       "how long I've been gone now. \n    Look, I'm not going "
                       "to tell you anything about living your life to the full"
                       "est. You live however makes you happy. I just wanted "
                       "you to know that I love you. You are a wonderful woman "
                       "who your mother and I raised to be true to herself."
                       "\n    Please, Adrianna, take care. I know you hate your"
                       "full first name, but I chose it for you because it was "
                       "as beautiful as you were when you were born. If Alexander"
                       " is still in your life, tell him I said Merry Christmas."
                       " Also, pass on the message that I said he can.\n\nAlways"
                       " in your heart,\nQuinten Favreau \n\n P.S. Merry Christmas"
                       ", Sweetheart.",
        "paths": [
            { "go_to": "franks_letter2", "phrase": "Frank placed his hand on "
                                                        "her shoulder, and "
                                                            "picked up his"
                                                                "letter." }
            ]
        },
    "adriannas_letter": {
        "description": "Dear Adrianna,\n    My lovely daughter, how do you fare?"
                       " How is your husband? I'm only kidding. I don't expect "
                       "you to wed anytime soon. Are you still seeing Alexander?"
                       " He was a nice man. \n    I know you are surprised to see"
                       " this letter. I suspect everyone will be. I don't know "
                       "how long I've been gone now. \n    Look, I'm not going "
                       "to tell you anything about living your life to the full"
                       "est. You live however makes you happy. I just wanted "
                       "you to know that I love you. You are a wonderful woman "
                       "who your mother and I raised to be true to herself."
                       "\n    Please, Adrianna, take care. I know you hate your"
                       "full first name, but I chose it for you because it was "
                       "as beautiful as you were when you were born. If Alexander"
                       " is still in your life, tell him I said Merry Christmas."
                       " Also, pass on the message that I said he can.\n\nAlways"
                       " in your heart,\nQuinten Favreau \n\n P.S. Merry Christmas"
                       ", Sweetheart.",
        "paths": [
            { "go_to": "franks_letter3", "phrase": "Frank placed his hand on "
                                                        "her shoulder, and "
                                                            "picked up his"
                                                                "letter." }
            ]
        },
    "aunts_letter": {
        "description": "Alice,\n    How are you doing, sis? Do you miss your "
                       "younger brother yet? I'm glad to know that you got "
                       "engaged. Tell James that I couldn't be happier for you"
                       " two.\n    Now... I need you to be strong. I know you "
                       "have been beating yourself up since all this began. I "
                       "know you think that you should have gotten it. You always"
                       " did try to protect me. I let you, probably a little too"
                       " much. \n    Alice... I'm glad you were my sister. I'm "
                       "only sorry Ricky didn't make it. I know it hurts to lose"
                       " two little brothers, but don't worry, I had a happy life."
                       " I had you for my sister, and Lucille for my wife. I had"
                       " two wonderful children with her. Don't lose sight of "
                       "them or James.\n\nLots of Love,\nTinner",
        "paths": [
            { "go_to": "alice", "phrase": "Aunt Alice was biting her lip, "
                                            "trying to hold back tears." }
            ]
        },
    "alice": {
        "description": "She folded the letter up and put it away. She sat there"
                       " gasping for breath, trying not to cry. I used to laugh"
                       " when she called our father Tinner, because he hated it"
                       ". But right now, hearing her pet name for him was only "
                       "stirring up old memories for her.",
        "paths": [
            { "go_to": "franks_letter3", "phrase": "Frank placed his hand on "
                                                        "her shoulder, and "
                                                            "picked up his"
                                                                "letter." }
            ]
        },
    "alice_letter": {
        "description": "Alice,\n    How are you doing, sis? Do you miss your "
                       "younger brother yet? I'm glad to know that you got "
                       "engaged. Tell James that I couldn't be happier for you"
                       " two.\n    Now... I need you to be strong. I know you "
                       "have been beating yourself up since all this began. I "
                       "know you think that you should have gotten it. You always"
                       " did try to protect me. I let you, probably a little too"
                       " much. \n    Alice... I'm glad you were my sister. I'm "
                       "only sorry Ricky didn't make it. I know it hurts to lose"
                       " two little brothers, but don't worry, I had a happy life."
                       " I had you for my sister, and Lucille for my wife. I had"
                       " two wonderful children with her. Don't lose sight of "
                       "them or James.\n\nLots of Love,\nTinner",
        "paths": [
            { "go_to": "alice", "phrase": "Aunt Alice was biting her lip, "
                                            "trying to hold back tears." }
            ]
        },
    "alice": {
        "description": "She folded the letter up and put it away. She sat there"
                       " gasping for breath, trying not to cry. I used to laugh"
                       " when she called our father Tinner, because he hated it"
                       ". But right now, hearing her pet name for him was only "
                       "stirring up old memories for her.",
        "paths": [
            { "go_to": "afterwards", "phrase": "It was quiet." }
            ]
        },
    "alice_letter1": {
        "description": "Alice,\n    How are you doing, sis? Do you miss your "
                       "younger brother yet? I'm glad to know that you got "
                       "engaged. Tell James that I couldn't be happier for you"
                       " two.\n    Now... I need you to be strong. I know you "
                       "have been beating yourself up since all this began. I "
                       "know you think that you should have gotten it. You always"
                       " did try to protect me. I let you, probably a little too"
                       " much. \n    Alice... I'm glad you were my sister. I'm "
                       "only sorry Ricky didn't make it. I know it hurts to lose"
                       " two little brothers, but don't worry, I had a happy life."
                       " I had you for my sister, and Lucille for my wife. I had"
                       " two wonderful children with her. Don't lose sight of "
                       "them or James.\n\nLots of Love,\nTinner",
        "paths": [
            { "go_to": "alice1", "phrase": "Aunt Alice was biting her lip, "
                                            "trying to hold back tears." }
            ]
        },
    "alice1": {
        "description": "She folded the letter up and put it away. She sat there"
                       " gasping for breath, trying not to cry. I used to laugh"
                       " when she called our father Tinner, because he hated it"
                       ". But right now, hearing her pet name for him was only "
                       "stirring up old memories for her.",
        "paths": [
            { "go_to": "franks_letter2", "phrase": "Frank placed his hand on "
                                                        "her shoulder, and "
                                                            "picked up his"
                                                                "letter." }
            ]
        },
    "aunts_letter": {
        "description": "Alice,\n    How are you doing, sis? Do you miss your "
                       "younger brother yet? I'm glad to know that you got "
                       "engaged. Tell James that I couldn't be happier for you"
                       " two.\n    Now... I need you to be strong. I know you "
                       "have been beating yourself up since all this began. I "
                       "know you think that you should have gotten it. You always"
                       " did try to protect me. I let you, probably a little too"
                       " much. \n    Alice... I'm glad you were my sister. I'm "
                       "only sorry Ricky didn't make it. I know it hurts to lose"
                       " two little brothers, but don't worry, I had a happy life."
                       " I had you for my sister, and Lucille for my wife. I had"
                       " two wonderful children with her. Don't lose sight of "
                       "them or James.\n\nLots of Love,\nTinner",
        "paths": [
            { "go_to": "alice2", "phrase": "Aunt Alice was biting her lip, "
                                            "trying to hold back tears." }
            ]
        },
    "alice2": {
        "description": "She folded the letter up and put it away. She sat there"
                       " gasping for breath, trying not to cry. I used to laugh"
                       " when she called our father Tinner, because he hated it"
                       ". But right now, hearing her pet name for him was only "
                       "stirring up old memories for her.",
        "paths": [
            { "go_to": "franks_letter3", "phrase": "Frank placed his hand on "
                                                        "her shoulder, and "
                                                            "picked up his"
                                                                "letter." }
            ]
        },
    "afterwards": {
        "description": "I sat there, watching water droplets run down the side"
                       "of my glass. I didn't know what to say. I felt hurt that"
                       " I was the only who didn't have a real message from my "
                       "dad. He tried to bring closure to everyone, it seemed, "
                       "but for me, I just felt hollow. I paid for everyone's "
                       "drinks, and we parted.",
        "paths": [
            { "go_to": "catching_up", "phrase": "I noticed my cocoa had gotten "
                                                    "cold." }
            ]
        },
    "catching_up": {
        "description": "I went inside and set my mug down. I was still hurting,"
                       " but I couldn't brood. I'm sure he had his reasons. He "
                       "was always saying he does what he feels is necessary.\n"
                       "My phone started ringing. The number was unknown to me."
                       "\n\"Hello?\"\n\"Hi... I wasn't sure if I should call you"
                       ".\"\n\"Who is this?\"\n\"Um, well... My name is Mel. I"
                       "... I'm your uncle.\"\nI didn't have time for this. My "
                       "mother was an only child, and my father's only brother "
                       "died when he was a child.\n\"Do you think this is a joke"
                       "?\" I screamed into the phone. \"Where do you get off "
                       "calling a stranger and saying your their uncle?\"\n"
                       "\"He didn't say much in your letter did he?\" \nI paused"
                       ".\n\"How... did you know that?\"\n\"I know lots. I gots"
                       " one too.",
        "paths": [
            { "go_to": "the_final_letter", "phrase": "\"Strange, being disowned"
                                                        " gettin' a letter after"
                                                            "all these years.\"" }
            ]
        },
    "the_final_letter": {
        "description": "Um...\n\n    I know we aren't supposed to talk. Mom is "
                       "still upset over what happened. I thought you should "
                       "at least know though. By the time you receive this "
                       "I won't be in this world anymore. Now, don't think that"
                       " I let the guilt from that accident push me to suicide."
                       " Heavens, no. Mel, I'm sick. Very sick.\n    Mel. Don't"
                       " be mad at Mom for what happened. She misses you. She "
                       "won't say it, but she does. We all do. I'm writing a "
                       "letter to everyone. I'm giving you a number to contact."
                       " It's one of my kids. Oh, yeah, you're an Uncle. You'd be"
                       " proud of these kids too.\n    This is the final letter"
                       " I'm writing. I didn't want to write yours first and "
                       "change everything I say so often I couldn't write the"
                       " others. Mel, please come home for Christmas.\n\nYour"
                       " Loving Brother, Tinner",
        "paths": [
            { "go_to": "christmasinvite", "phrase": "I choked." }
            ]
        },
    "christmasinvite": {
        "description": "There was a knot in my throat. I couldn't speak. I got "
                       "it. I understood why my letter didn't have any special "
                       "words for me. Father had no regrets with me. He knew I "
                       "would be fine.\n\"Mel?\" I said hoarsely. \"Will you..."
                       "\" My voice got stuck in my throat. \n\"Will you come "
                       "home, and join the family?\"\nI heard a muffled yes. I "
                       "could tell he was crying too. I realized then that we "
                       "only had a few days left to get everything ready. No "
                       "one had discussed Christmas at all this year. I gave "
                       "him my address and said that we'll celebrate at my house"
                       ". It wasn't much, but the family would truly be together"
                       " for the first time in a long time.",
        "paths": [
            { "go_to": "thefamily", "phrase": "I looked around the house and "
                                                "smiled." }
            ]
        },
    "thefamily": {
        "description": "Mel was the first to arrive. He didn't look anything like"
                       " my father, so I had a hard time believing it was him. "
                       "He showed me a picture of himself when he was a toddler "
                       "with Grandpa . Mel is the spitting image of Grandpa, "
                       "so I smiled and welcomed him. I apologized for my rudeness"
                       " and offered him a drink. Mom arrived next. She froze "
                       "when she saw Mel, and walked in slowly. \n\"Mom, this is"
                       "--\"\n\"Mel, I know sweet heart. I know you said he'd be "
                       "here, but it's just been so long.\"\n At that moment "
                       "Grandma arrived. She stood in the doorway for a good 5 "
                       "minutes before coming in. Mel immediately put his drink"
                       " down and hugged her. Grandma smiled and held him. \n"
                       "\"My baby boy's come home...\"\n\"Yes, Mom, I'm finally"
                       " home.\"\nFinally, Adrianna, Alice and Frank showed up "
                       "at about the same time. They had their arms full of wrapped"
                       " boxes. We rushed to help them carry them in. I then set "
                       "them all under the tree, and smiled. I turned to my family"
                       "and looked at each of their faces. \nSoftly, I said to them"
                       " \"Merry Christmas, everyone!\"",
        "paths": [
            { "go_to": "credits", "phrase": "Merry Christmas to all." }
            ]
        },
    "credits": {
        "description": "Programming, Story, and ASCII Art by: \n\n    Christopher"
                       " \"avarisclari\" Weigle \n\n\n\n        Thank you for "
                       "playing. Merry Christmas.",
        "paths": [
            { "go_to": "title", "phrase": "The End." }
            ]
        },
    "ashley": {
        "description": "Merry Christmas, Ashley. I wanted to dedicate this game"
                       " to you this year. :) You have brought a lot of happiness"
                       " in my life and I'm glad we met. You are one of the nicest"
                       " people I know, and it's a real pleasure knowing you.",
    "paths": [
        { "go_to": "title", "phrase": "I hope you enjoyed it." }
        ]
        },
    "about": {
        "description": "I started writing this with a completely different story"
                       " in mind. I originally wanted to do something about a man"
                       " who hasn't seen his family in years coming home, but as"
                       " I started writing, the words slowly shifted to what you"
                       " have here. I want to thank all of you for playing this."
                       "\n\n            Have a Merry Christmas. \n--avarisclari",
        "paths": [
            { "go_to": "title", "phrase": "Return to Title" }
            ]
        }
}

scene = scenes["title"]

while 1 == 1:
    next_choice = None
    paths = scene["paths"]
    description = scene["description"]
    lines = string.split("\n")

    for line in lines:
        if len(line > 55):
            w = textwrap.TextWrapper(width=45, break_long_words=False)
            line = '\n'.join(w.wrap(line))
        decription += line +"\n"
    print description



    #Shows the choices
    for i in range(0, len(paths)):
        path = paths[i]
        menu_item = i + 1
        print "\t", menu_item, path["phrase"]

    print "\t0 Quit"

    #Get user selection

    prompt = "Make a selection (0 - %i): \n" % len(paths)

    while next_choice == None:
        try:
            choice = raw_input(prompt)
            menu_selection = int(choice)
            if menu_selection == 0:
                print "Merry Christmas!"
                sys.exit()
            if menu_selection == 7:
                next_choice = "ashley"
                if sys.platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")
            else:
                index = menu_selection -1
                next_choice = paths[ index ]

        except(IndexError, ValueError):
                print choice, "is not a valid selection"

    if next_choice == "quit":
        print "Merry Christmas!"
        sys.exit()
    if next_choice == "ashley":
        scene = scenes["ashley"]
    else:
        scene = scenes[ next_choice["go_to"] ]
        print next_choice["phrase"], "\n"
        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")
