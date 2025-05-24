example_msqa = {
    "example_1": {
        "example_context_msqa": """
            The theme song for the opening credits was Billy Joel 's `` My Life '' , although it was a re-recorded version with Gary Bennett as the vocalist . Some reruns shown in syndication ( such as when USA Network aired reruns , as well as its later runs on Me - TV ) and all home video and DVD releases use a vocal version of the show 's end credit instrumental theme , `` Shake Me Loose '' , performed by Stephanie Mills , for the opening credits , replacing `` My Life '' . Bosom Buddies reruns aired briefly on NBC in the summer of 1984 after Tom Hanks had become a major film star that summer with Splash and Bachelor Party . Reruns also aired on USA Network up until November 18 , 1995 as well as on TBS and TV Land up until the mid-2000s . More recently , Bosom Buddies began airing on Me - TV on October 2 , 2011 and again on Thursday nights beginning May 29 , 2014 , as part of the network 's `` Summer of Me '' promotion .
        """,
        "example_question_msqa": "who sang the theme song to bosom buddies",
        "example_clar_msqa": """
            1. Cognitive Cues: Bosom Buddies theme song vocalist; re-recorded version of "My Life"; Gary Bennett as the singer
            2. The question is asking for the identity of the person who sang the theme song to Bosom Buddies.
            3. Identify the person who sang the theme song to "Bosom Buddies."
            4. To identify the singer(s) of the theme song used in the opening credits of Bosom Buddies, including the re-recorded version and the version used in syndication.
        """,
        "example_know_msqa": """
            1. The theme song for Bosom Buddies was Billy Joel's "My Life."
            2. The re-recorded version of the theme song featured Gary Bennett as the vocalist.
            3. The version used in syndication replaced "My Life" with "Shake Me Loose," performed by Stephanie Mills.
        """,
        "example_logic_msqa": """
            1. The question is asking for the person who sang the theme song to Bosom Buddies.
            2. The context provides information about two versions of the theme song:
               - Gary Bennett's version of "My Life" for the re-recorded version.
               - Stephanie Mills' version of "Shake Me Loose" for the version used in syndication.
            3. The re-recorded version and the syndication version are directly related to the question, and both Gary Bennett and Stephanie Mills are involved in those versions.
        """,
        "example_number_msqa": 2,
        "example_locate_msqa": """
            1. although it was a re-recorded version with Gary Bennett as the vocalist.
            2. `` Shake Me Loose '' , performed by Stephanie Mills , for the opening credits , replacing `` My Life '' .
            """,
        "example_answer_msqa": "Gary Bennett; Stephanie Mills",
        "example_explanation_msqa": """
            The question is asking for the person who sang the theme song to "Bosom Buddies." Based on the context, two versions of the theme song are mentioned:
            1. Gary Bennett's version of "My Life" for the re-recorded version.
            2. Stephanie Mills' version of "Shake Me Loose" for the version used in syndication. Both of these singers are identified as performing the theme songs, making them the answers to the question.
            """
    },
    "example_2": {
        "example_context_msqa": """
            In Australia , the common law doctrine of Aboriginal title is referred to as native title , which is `` the recognition by Australian law that Indigenous people have rights and interests to their land that come from their traditional laws and customs '' . The concept recognises that in certain cases there was and is a continued beneficial legal interest in land held by local Indigenous Australians which survived the acquisition of radical title to the land by the Crown at the time of sovereignty . Native title can co-exist with non-Indigenous proprietary rights and in some cases different Indigenous groups can exercise their native title over the same land . The foundational case for native title in Australia was Mabo v Queensland ( No 2 ) ( 1992 ) . One year after the recognition of the legal concept of native title in Mabo , the Keating Government formalised the recognition by legislation with the enactment by the Australian Parliament of the Native Title Act 1993 . The Act attempted to clarify the legal position of landholders and the processes to be followed for native title to be claimed , protected and recognised through the courts . The Federal Court of Australia mediates claims made by Aboriginal and Torres Strait Islander peoples and hears applications for , and makes , native title determinations . Appeals against these determinations can be made to a full sitting of the Federal Court and then to the High Court of Australia . The National Native Title Tribunal ( NNTT ) , established under the Native Title Act 1993 , is a body that applies the ' registration test ' to all new native title claimant applications , and undertakes future act mediation and arbitral functions .
        """,
        "example_question_msqa": "key events in the development of law relating to native title in australia",
        "example_clar_msqa": """
            1. Cognitive Cues: native title in Australia; key legal events; Mabo case and Native Title Act
            2. The question asks for key events in the development of law relating to native title in Australia.
            3. The core details include significant legal cases, legislative actions, and milestones in the recognition and formalization of native title.
            4. The goal is to identify and list the major events that shaped the legal framework for native title in Australia.
        """,
        "example_know_msqa": """
            1. Native title in Australia is recognized as the rights of Indigenous people to their land based on traditional laws and customs.
            2. The Mabo v Queensland (No 2) case in 1992 is the foundational case for native title.
            3. The Native Title Act 1993 formalized the recognition of native title through legislation.
        """,
        "example_logic_msqa": """
            1. The question is asking for key events in the development of law relating to native title in Australia.
            2. The context mentions:
                - Mabo v Queensland (No 2) case in 1992 as the foundational case for native title.
                - The enactment of the Native Title Act 1993 by the Australian Parliament to formalize native title recognition.
            3. These are the distinct events that directly answer the question.
            4. There is no indication from the question that more than two events are expected.
        """,
        "example_number_msqa": 2,
        "example_locate_msqa": """
            1. The foundational case for native title in Australia was Mabo v Queensland ( No 2 ) ( 1992 ) .
            2. One year after the recognition of the legal concept of native title in Mabo , the Keating Government formalised the recognition by legislation with the enactment by the Australian Parliament of the Native Title Act 1993 .
            """,
        "example_answer_msqa": "Mabo v Queensland; Australian Parliament of the Native Title Act 1993",
        "example_explanation_msqa": """
            1. Mabo v Queensland, the case from 1992, which is the foundational case for native title in Australia.
            2. The Australian Parliament of the Native Title Act 1993, which formalized the recognition of native title through legislation.
        """
    },
    "example_3": {
        "example_context_msqa": """
            The Tennessean noted in October 2017 that 2017 was `` the bloodiest year for teens and children in more than a decade , '' many of whom were African Americans who lived in city - run housing projects . Nashville lies on the Cumberland River in the northwestern portion of the Nashville Basin . Nashville 's elevation ranges from its lowest point , 385 feet ( 117 m ) above sea level at the Cumberland River , to its highest point , 1,163 feet ( 354 m ) above sea level in the Radnor Lake State Natural Area . According to the United States Census Bureau , the city has a total area of 527.9 square miles ( 1,367 km ) , of which 504.0 square miles ( 1,305 km ) of it is land and 23.9 square miles ( 62 km ) of it ( 4.53 % ) is water .
        """,
        "example_question_msqa": "what is the sea level of nashville tn",
        "example_clar_msqa": """
            1. Cognitive Cues: sea level of Nashville; Nashville elevation; Cumberland River elevation
            2. The question is asking for the sea level of Nashville, TN.
            3. The central inquiry is focused on identifying the elevation of Nashville above sea level.
            4. The question refers to the geographical location of Nashville, Tennessee, and its altitude relative to sea level.
            5. The goal of the question is to find a specific sea level reference for Nashville, which vary depending on location.
        """,
        "example_know_msqa": """
            1. Nashville's elevation ranges from 385 feet (117 m) above sea level at the Cumberland River to 1,163 feet (354 m) above sea level in the Radnor Lake State Natural Area.
            2. The elevation of Nashville varies depending on the specific location within the city.
        """,
        "example_logic_msqa": """
            1. The question specifically asks for the sea level of Nashville, TN, which is related to its elevation above sea level.
            2. The context provides two different elevations within Nashville, one at the Cumberland River (385 feet) and one at the Radnor Lake State Natural Area (1,163 feet).
            3. The clarification emphasizes the varying elevation depending on location in the city.
            4. Since the question does not specify a particular location within Nashville, both the lowest and highest elevations can be considered valid answers.
        """,
        "example_number_msqa": 2,
        "example_locate_msqa": """
            1. Nashville 's elevation ranges from its lowest point , 385 feet ( 117 m ) above sea level at the Cumberland River , to its highest point , 1,163 feet ( 354 m ) above sea level in the Radnor Lake State Natural Area .
            """,
        "example_answer_msqa": "385 feet (117 m) above sea level at the Cumberland River; 1,163 feet (354 m) above sea level in the Radnor Lake State Natural Area",
        "example_explanation_msqa": """
            The question asks for the sea level of Nashville, TN, which is associated with its elevation above sea level. The context specifies two different elevations:
            1. 385 feet (117 m) above sea level at the Cumberland River, which is Nashville's lowest point
            2. 1,163 feet (354 m) above sea level in the Radnor Lake State Natural Area, which is Nashville's highest point.
        """
    },
    "example_4": {
        "example_context_msqa": """
            Basketball at the 1936 Summer Olympics was the first appearance of the sport as an official medal event . The tournament was played between 7 August and 14 August 1936 in Berlin , Germany . 23 nations entered the competition , making basketball the largest tournament of the team sports . The International Basketball Federation , and IOC which is the governing body of international basketball , used the 1936 tournament to experiment with outdoor basketball . Lawn tennis courts were used for the competition . This caused problems when the weather was adverse , especially during the final game .
        """,
        "example_question_msqa": "when and where was basketball introduced in olympics as a medal event",
        "example_clar_msqa": """
            1. Cognitive Cues: basketball in the Olympics; first official medal event; 1936 Summer Olympics in Berlin
            2. The question is asking for when and where basketball was introduced as a medal event in the Olympics.
            3. The central inquiry is focused on identifying the time (when) and place (where) of the first Olympic appearance of basketball as an official medal event.
            4. The question refers to basketball's debut as an Olympic medal event, which occurred at the 1936 Summer Olympics.
            5. The goal of the question is to retrieve both the exact year and location where basketball was first included as an Olympic medal event.
        """,
        "example_know_msqa": """
            1. Basketball at the 1936 Summer Olympics was the first appearance of the sport as an official medal event .
            2. The tournament was played between 7 August and 14 August 1936 in Berlin , Germany .
        """,
        "example_logic_msqa": """
            1. The question specifically asks for both the time ("when") and place ("where") basketball was introduced as a medal event in the Olympics.
            2. The context reveals that basketball's first Olympic medal appearance occurred during the 1936 Summer Olympics.
            3. The location of this event is identified as Berlin, Germany.
            4. The knowledge evidence confirms these key details: the year and the location.
        """,
        "example_number_msqa": 2,
        "example_locate_msqa": """
            1. Basketball was introduced as an official medal event at the 1936 Summer Olympics.
            2. The tournament was held in Berlin, Germany.
            """,
        "example_answer_msqa": "1936 Summer Olympics; Berlin, Germany",
        "example_explanation_msqa": """
            The question asks for both the time ("when") and place ("where") basketball was introduced as a medal event in the Olympics. The context provides the following information:
            1. 1936 Summer Olympics was the event when basketball was first introduced as an official medal event.
            2. Berlin, Germany is identified as the location where the tournament took place. These are the key details answering the question.
        """
    },
    "example_5": {
        "example_context_msqa": """
            The Foreigner is a 2017 British - Chinese action thriller film directed by Martin Campbell and written by David Marconi , based on the 1992 novel The Chinaman by Stephen Leather . The British - Chinese co-production stars Jackie Chan , Pierce Brosnan , Michael McElhatton , Liu Tao , Charlie Murphy , Orla Brady and Katie Leung , and follows a businessman who seeks revenge for the death of his daughter . The Foreigner was released in China on 30 September 2017 and in the United States on 13 October 2017 , and has grossed $139 million worldwide . It received mixed to positive reviews , with critics praising the against - type performances of Chan and Brosnan while calling the film itself cliché and a shadow of the post-Taken era . Ngoc Minh Quan is a retired Vietnam War special operations forces soldier who now runs a Chinese restaurant in London . When his teenage daughter Fan is killed in a department store bombing claimed by a group calling themselves the `` Authentic IRA '' , a distraught Quan seeks revenge . He first attempts to bribe Scotland Yard officer Richard Bromley for the names of the bombers , but Bromley refuses to accept the bribe nor reveal any information . Quan next focuses on Irish deputy minister Liam Hennessy , who speaks publicly about his status as a former leader of the IRA forces while condemning the bombing . Keyi Lam , Quan 's co-worker and personal friend , attempts to console and convince him to move on , but he refuses to be swayed and eventually leaves for Belfast to meet Hennessy . Hennessy claims to have no knowledge of the bombing or its perpetrators , but Quan does not believe him . His queries escalate until he becomes fixated on Hennessy , setting off a homemade bomb in his office and threatening more unless he gets the bombers ' names .
        """,
        "example_question_msqa": "when does the new jackie chan movie the foreigner come out",
        "example_clar_msqa": """
            1. Cognitive Cues: Jackie Chan movie; release date; The Foreigner
            2. The question is asking for the release date of the movie The Foreigner.
            3. The central inquiry is focused on identifying the specific time when the movie was released.
            4. The question refers to the movie The Foreigner, which starred Jackie Chan and was released in multiple countries.
            5. The goal of the question is to retrieve the exact dates for when the movie The Foreigner came out in different regions (China and the US).
        """,
        "example_know_msqa": """
            1. The Foreigner was released in China on 30 September 2017.
            2. The Foreigner was released in the United States on 13 October 2017.
            3. The Foreigner is a 2017 British-Chinese action thriller film starring Jackie Chan.
        """,
        "example_logic_msqa": """
            1. The question asks about the release dates of the movie The Foreigner starring Jackie Chan.
            2. The context provides release dates in multiple countries: China and the United States.
            3. Based on the context and knowledge evidence, the movie was released in China on 30 September 2017 and in the United States on 13 October 2017.
            4. These are the only distinct answers related to the question.
        """,
        "example_number_msqa": 2,
        "example_locate_msqa": """
            1. The Foreigner was released in China on 30 September 2017 and in the United States on 13 October 2017 , and has grossed $139 million worldwide .
            """,
        "example_answer_msqa": "in China on 30 September 2017; in the United States on 13 October 2017",
        "example_explanation_msqa": """
            The context specifies that the movie The Foreigner was released in China on 30 September 2017 and in the United States on 13 October 2017. These are the exact release details provided in the context in response to the question regarding when and where the movie was released.
        """
    },
    "example_6": {
        "example_context_msqa": """
            `` I Say a Little Prayer '' is a song written by Burt Bacharach and Hal David for Dionne Warwick , originally peaking at number four on the U.S. Billboard Hot 100 pop singles chart in December 1967 . On the R&B Singles chart it peaked at number eight . Intended by lyricist Hal David to convey a woman 's concern for her man who 's serving in the Vietnam War , `` I Say a Little Prayer '' was recorded by Dionne Warwick in a 9 April 1966 session . Although Bacharach 's recordings with Warwick typically took no more than three takes ( often only taking one ) , Bacharach did ten takes on `` I Say a Little Prayer '' and still disliked the completed track , feeling it rushed .
        """,
        "example_question_msqa": "who wrote i say a little prayer for you",
        "example_clar_msqa": """
            1. Cognitive Cues: songwriters of \"I Say a Little Prayer\"; Burt Bacharach and Hal David; original composition for Dionne Warwick
            2. The central inquiry is asking for the identity of the individuals who wrote the song \"I Say a Little Prayer.\"
            3. The core concepts include the song title \"I Say a Little Prayer\" and the individuals responsible for its creation.
            4. The goal is to identify the songwriters of \"I Say a Little Prayer,\" specifically Burt Bacharach and Hal David.
        """,
        "example_know_msqa": """
            1. \"I Say a Little Prayer\" was written by Burt Bacharach and Hal David.
            2. The song was originally composed for Dionne Warwick.
        """,
        "example_logic_msqa": """
            1. The question is asking for the individuals who wrote the song \"I Say a Little Prayer.\"
            2. The context explicitly states that the song was written by Burt Bacharach and Hal David.
            3. Both Burt Bacharach and Hal David are credited as the songwriters, and they are mentioned together as a pair in the context.
            4. There is no indication that the songwriters should be treated as separate answers. Therefore, there are two correct answers.
        """,
        "example_number_msqa": 2,
        "example_locate_msqa": """
            1. `` I Say a Little Prayer '' is a song written by Burt Bacharach and Hal David for Dionne Warwick , originally peaking at number four on the U.S. Billboard Hot 100 pop singles chart in December 1967 .
        """,
        "example_answer_msqa": "in China on 30 September 2017; in the United States on 13 October 2017",
        "example_explanation_msqa": """
            The song "I Say a Little Prayer" was written by Burt Bacharach and Hal David for Dionne Warwick. The context confirms that both Bacharach and David were responsible for writing the song.
        """
    },
    "example_7": {
        "example_context_msqa": """
        The Broncos began their 2008 campaign on the road against their AFC West rival, the Oakland Raiders, in the second game of ESPN's Monday Night Football doubleheader.  In the first quarter, Denver ran out of the gates early as QB Jay Cutler completed a 26-yard TD pass to rookie WR Eddie Royal (who was filling in for WR Brandon Marshall, due to his 1-game suspension).  In the second quarter, the Broncos continued their domination as kicker Matt Prater got a 26-yard field goal, while FB Michael Pittman got a 3-yard TD run.  In the third quarter, Denver ran away with the game as Cutler completed a 48-yard TD pass to WR Darrell Jackson, while Prater nailed a 43-yard field goal.  In the fourth quarter, the Raiders spoiled the Broncos' bid for a shutout as QB JaMarcus Russell completed an 8-yard TD pass to WR Ashley Lelie.  Denver ended its domination with RB Selvin Young's 5-yard TD run and Pittman's 1-yard TD run.  Oakland ended the scoring with Russell completing a 4-yard TD pass to WR Ronald Curry. With the dominating win, the Broncos began their season at 1-0; with the rest of the division suffering losses, Denver, in Week 1, is in sole possession of 1st place. Eddie Royal, in his NFL debut, had the best Week 1 stats of any wide receiver, getting 9 receptions for 146 yards and a touchdown.
    """,
        "example_question_msqa": "How many touchdowns did JaMarcus Russell have?",
        "example_clar_msqa": """
        1. Cognitive Cues: JaMarcus Russell; number of touchdowns; completed touchdown passes
        2. The central inquiry is asking how many touchdowns JaMarcus Russell had in the game described.
        3. The core concepts include JaMarcus Russell as the player, a 2008 football game between the Denver Broncos and Oakland Raiders as the event, and the number of touchdowns he threw as the key detail.
        4. The goal is to determine the total number of touchdown passes that JaMarcus Russell threw in this specific game based on the context provided.
    """,
        "example_know_msqa": """
        1. JaMarcus Russell completed an 8-yard TD pass to WR Ashley Lelie in the fourth quarter.
        2. JaMarcus Russell completed a 4-yard TD pass to WR Ronald Curry later in the fourth quarter.
    """,
        "example_logic_msqa": """
        1. The question asks for the number of touchdowns JaMarcus Russell had, which refers specifically to touchdowns attributed to him, typically as the passing quarterback.
        2. In the context, JaMarcus Russell is mentioned in two distinct touchdown plays:
        - One 8-yard TD pass to Ashley Lelie.
        - One 4-yard TD pass to Ronald Curry.
        3. Each of these is a separate completed touchdown pass, and both are credited to JaMarcus Russell.
        4. However, the question is asking how many touchdowns he had—which may be interpreted as a total count, not a list of distinct types or recipients.
        5. Since both plays are touchdowns he was responsible for (via passing), and no other type of touchdown (e.g., rushing) is mentioned, we count them as a single type of answer: the total number of touchdowns he had.
    """,
        "example_number_msqa": 1,
        "example_locate_msqa": """
        1. In the fourth quarter, the Raiders spoiled the Broncos' bid for a shutout as QB JaMarcus Russell completed an 8-yard TD pass to WR Ashley Lelie.
        2. Oakland ended the scoring with Russell completing a 4-yard TD pass to WR Ronald Curry.
    """,
        "example_answer_msqa": "2",
        "example_explanation_msqa": """
        1. The question asks for the number of touchdowns JaMarcus Russell had in the game.
        2. The context states that JaMarcus Russell threw two touchdown passes:
        - One 8-yard TD pass to WR Ashley Lelie.
        - One 4-yard TD pass to WR Ronald Curry.
        3. These are two separate and clearly stated touchdown passes credited to JaMarcus Russell. No other touchdowns involving him are mentioned in the context.
        4. Therefore, the total number of touchdowns JaMarcus Russell had in the game is two.
    """
    },
    "example_8": {
        "example_context_msqa": """
        After winning at home, the Bengals traveled down south to take on the Jaguars.  The Jags scored first in the first quarter when Josh Lambo kicked a 32-yard field goal to make it 3-0.  They would make it 10-0 in the second quarter when Blake Bortles found Marqise Lee on a 3-yard pass.  The Bengals got on the board coming within 3 as Joe Mixon ran for a 7-yard touchdown making the score 10-7.  However, the Jags pulled away with Lambo's 56-yard field goal to make it 13-7 at halftime.  In the second half it was all Jags as they scored in the third quarter with Lambo hitting his third field goal of the day from 25 yards out to make it 16-7.  In the fourth quarter, they would wrap up the scoring of the game with Jaydon Mickens 63-yard punt return for a touchdown and the final score 23-7. The game was notable seeing  A.J. Green getting ejected in the second quarter after fighting with Jacksonville's Jalen Ramsey, who was also ejected.
    """,
        "example_question_msqa": "Who was removed first",
        "example_clar_msqa": """
        1. Cognitive Cues: order of ejections; A.J. Green and Jalen Ramsey fight; who left the game first
        2. The central inquiry is asking which player—A.J. Green or Jalen Ramsey—was removed from the game first as a result of their ejection.
        3. The core concepts include A.J. Green and Jalen Ramsey as the individuals involved, their ejection due to an on-field fight during the Bengals vs. Jaguars game, and the sequence or timing of their removal from the game.
        4. The goal is to determine which of the two players (Green or Ramsey) was the first to be removed from the game following the ejection incident.
    """,
        "example_know_msqa": """
        1. A.J. Green was ejected in the second quarter.
        2. Jalen Ramsey was also ejected after the fight with A.J. Green.
        3. The game was notable for their ejections following the altercation.
    """,
        "example_logic_msqa": """
        1. The question is asking who was removed first during the game between the Bengals and the Jaguars.
        2. The context mentions that both A.J. Green and Jalen Ramsey were ejected after a fight in the second quarter.
        3. The context specifically states that A.J. Green was ejected in the second quarter, while Jalen Ramsey was also ejected after fighting with A.J. Green.
        4. Based on the provided context, it can be inferred that A.J. Green was likely the first to be removed due to the sequence of events.
    """,
        "example_number_msqa": 1,
        "example_locate_msqa": """
        1. The game was notable seeing  A.J. Green getting ejected in the second quarter after fighting with Jacksonville's Jalen Ramsey, who was also ejected.
    """,
        "example_answer_msqa": "A.J. Green",
        "example_explanation_msqa": """
        1. The question is asking who was removed first during the game between the Bengals and the Jaguars.
        2. The context states that both A.J. Green and Jalen Ramsey were ejected after a fight in the second quarter:
        - A.J. Green was ejected for fighting with Jalen Ramsey.
        - Jalen Ramsey was also ejected after the altercation with A.J. Green.
        3. Although the context does not explicitly state who was removed first, the fact that A.J. Green's ejection is mentioned first suggests he was likely the first player to be removed.
        4. Therefore, based on the order of the events and typical reporting, A.J. Green was removed first.
    """
    },
    "example_9": {
        "example_context_msqa": """
        After Culloden, government forces spent the next few weeks searching for rebels, confiscating cattle and burning Non-Juring Episcopalian and Catholic meeting houses; many of those who participated in the Rebellion came from this element of Scottish society. Prisoners from regiments in the French service were treated as POWs and exchanged, but 3,500 captured Jacobites were indicted for treason. 650 of these died awaiting trial, 120 were executed , 900 were pardoned and the rest transported. The Jacobite lords Kilmarnock, Balmerino and Lovat were beheaded on Tower Hill in April 1747, but these were among the last executions. Public sympathies had shifted and Cumberland's insistence on severity earned him the nickname 'Butcher' from a City of London alderman. The last Jacobite to be executed was Doctor Archibald Cameron, younger brother of Lochiel. Convicted of treason for his part in the 45, he escaped into exile; when he returned to Scotland in March 1753, he was allegedly betrayed by members of his own clan and executed in London on 7 June.
    """,
        "example_question_msqa": "Of the 3,500 Jacobites that were captured and indited for treason how many lived?",
        "example_clar_msqa": """
        1. Cognitive Cues: JaMarcus Russell; number of touchdowns; completed touchdown passes
        2. The central inquiry is asking how many touchdowns JaMarcus Russell had in the game described.
        3. The core concepts include JaMarcus Russell as the player, a 2008 football game between the Denver Broncos and Oakland Raiders as the event, and the number of touchdowns he threw as the key detail.
        4. The goal is to determine the total number of touchdown passes that JaMarcus Russell threw in this specific game based on the context provided.
    """,
        "example_know_msqa": """
        1. 3,500 Jacobites were captured and indicted for treason.
        2. 650 died awaiting trial.
        3. 120 were executed.
        4. 900 were pardoned.
        5. The rest were transported.
    """,
        "example_logic_msqa": """
        1. The question is asking how many of the 3,500 captured and indicted Jacobites lived.
        2. The context provides the following breakdown of the 3,500 Jacobites:
            - 650 died awaiting trial.
            - 120 were executed.
            - 900 were pardoned.
            - The rest were transported.
        3. To determine how many lived, we need to exclude those who died (650 + 120 = 770) from the total (3,500).
        4. The number of Jacobites who lived is therefore 3,500 - 770 = 2,730.
        5. However, the question may also be interpreted as asking for the distinct categories of those who lived (pardoned and transported). 
            - Pardoned: 900
            - Transported: 3,500 - (650 + 120 + 900) = 1,830
        6. If the question is interpreted as asking for the distinct groups that lived (pardoned and transported), then there are 2 answers. If it is asking for the total number who lived, then the answer is 1 (2,730).Given the phrasing \"how many lived,\" it is more likely asking for the total number who lived, not the distinct categories.
    """,
        "example_number_msqa": 1,
        "example_locate_msqa": """
        1. Prisoners from regiments in the French service were treated as POWs and exchanged, but 3,500 captured Jacobites were indicted for treason.
        2. 650 of these died awaiting trial, 120 were executed , 900 were pardoned and the rest transported.
    """,
        "example_answer_msqa": "2,730",
        "example_explanation_msqa": """
        1. The question asks how many of the 3,500 captured and indicted Jacobites lived.
        2. The context states that 650 died awaiting trial and 120 were executed, totaling 770 deaths.
        3. Subtracting the deaths (770) from the total (3,500) gives the number who lived: 3,500 - 770 = 2,730.
        4. The answer is the total number who lived, not the breakdown of pardoned or transported individuals.
    """
    },
    "example_10": {
        "example_context_msqa": """
        In the city, the age distribution of the population shows 21.8% under the age of 18, 13.1% from 18 to 24, 31.7% from 25 to 44, 20.1% from 45 to 64, and 13.2% who were 65 years of age or older. The median age was 34 years. For every 100 females, there were 87.1 males. For every 100 females age 18 and over, there were 83.5 males.
    """,
        "example_question_msqa": "Which age groups had a bigger population than those 65 years of age or older but lower than those 25 to 44?",
        "example_clar_msqa": """
        1. Cognitive Cues: Age groups; Population comparison; Groups larger than those 65 and older but smaller than those 25 to 44
        2. The central inquiry is asking to identify which age groups had a larger population than those who are 65 years or older but had a smaller population than those between the ages of 25 to 44.
        3. The core concepts include the age groups 65 years or older (13.2% of the population), 25 to 44 years (31.7% of the population), and the groups to compare: Under 18, 18 to 24, and 45 to 64.
        4. The goal is to identify the age groups whose population percentage is higher than 13.2% (those 65 or older) but lower than 31.7% (those 25 to 44).
    """,
        "example_know_msqa": """
        1. The age group 25 to 44 had a population of 31.7%.
        2. The age group 45 to 64 had a population of 20.1%.
        3. The age group 65 years or older had a population of 13.2%.
    """,
        "example_logic_msqa": """
        1. The question is asking for age groups that had a population percentage greater than 13.2% (65 years or older) but less than 31.7% (25 to 44).
        2. From the context, the population percentages for the age groups are:
            - Under 18: 21.8%
            - 18 to 24: 13.1%
            - 25 to 44: 31.7%
            - 45 to 64: 20.1%
            - 65 or older: 13.2%
        3. The age groups that meet the criteria (greater than 13.2% and less than 31.7%) are:
            - Under 18: 21.8%
            - 45 to 64: 20.1%
        4. The age group 18 to 24 (13.1%) does not meet the criteria as it is not greater than 13.2%.
    """,
        "example_number_msqa": 2,
        "example_locate_msqa": """
        1. In the city, the age distribution of the population shows 21.8% under the age of 18, 13.1% from 18 to 24, 31.7% from 25 to 44, 20.1% from 45 to 64, and 13.2% who were 65 years of age or older.
    """,
        "example_answer_msqa": "45 to 64; under the age of 18",
        "example_explanation_msqa": """
        1. The question asks for age groups with a population percentage greater than 13.2% (65 or older) but less than 31.7% (25 to 44).
        2. The context provides the following population percentages:
            - Under 18: 21.8% (greater than 13.2% and less than 31.7%)
            - 45 to 64: 20.1% (greater than 13.2% and less than 31.7%)
            - 18 to 24: 13.1% (does not meet the criteria as it is not greater than 13.2%).
        3. Thus, the qualifying age groups are \"under the age of 18\" and \"45 to 64,\" with their respective percentages.
    """
    },
}

example_drop = {
    "example_7": {
        "example_context_msqa": """
            The Broncos began their 2008 campaign on the road against their AFC West rival, the Oakland Raiders, in the second game of ESPN's Monday Night Football doubleheader.  In the first quarter, Denver ran out of the gates early as QB Jay Cutler completed a 26-yard TD pass to rookie WR Eddie Royal (who was filling in for WR Brandon Marshall, due to his 1-game suspension).  In the second quarter, the Broncos continued their domination as kicker Matt Prater got a 26-yard field goal, while FB Michael Pittman got a 3-yard TD run.  In the third quarter, Denver ran away with the game as Cutler completed a 48-yard TD pass to WR Darrell Jackson, while Prater nailed a 43-yard field goal.  In the fourth quarter, the Raiders spoiled the Broncos' bid for a shutout as QB JaMarcus Russell completed an 8-yard TD pass to WR Ashley Lelie.  Denver ended its domination with RB Selvin Young's 5-yard TD run and Pittman's 1-yard TD run.  Oakland ended the scoring with Russell completing a 4-yard TD pass to WR Ronald Curry. With the dominating win, the Broncos began their season at 1-0; with the rest of the division suffering losses, Denver, in Week 1, is in sole possession of 1st place. Eddie Royal, in his NFL debut, had the best Week 1 stats of any wide receiver, getting 9 receptions for 146 yards and a touchdown.
        """,
        "example_question_msqa": "How many touchdowns did JaMarcus Russell have?",
        "example_clar_msqa": """
            1. Cognitive Cues: JaMarcus Russell; number of touchdowns; completed touchdown passes
            2. The central inquiry is asking how many touchdowns JaMarcus Russell had in the game described.
            3. The core concepts include JaMarcus Russell as the player, a 2008 football game between the Denver Broncos and Oakland Raiders as the event, and the number of touchdowns he threw as the key detail.
            4. The goal is to determine the total number of touchdown passes that JaMarcus Russell threw in this specific game based on the context provided.
        """,
        "example_know_msqa": """
            1. JaMarcus Russell completed an 8-yard TD pass to WR Ashley Lelie in the fourth quarter.
            2. JaMarcus Russell completed a 4-yard TD pass to WR Ronald Curry later in the fourth quarter.
        """,
        "example_logic_msqa": """
            1. The question asks for the number of touchdowns JaMarcus Russell had, which refers specifically to touchdowns attributed to him, typically as the passing quarterback.
            2. In the context, JaMarcus Russell is mentioned in two distinct touchdown plays:
            - One 8-yard TD pass to Ashley Lelie.
            - One 4-yard TD pass to Ronald Curry.
            3. Each of these is a separate completed touchdown pass, and both are credited to JaMarcus Russell.
            4. However, the question is asking how many touchdowns he had—which may be interpreted as a total count, not a list of distinct types or recipients.
            5. Since both plays are touchdowns he was responsible for (via passing), and no other type of touchdown (e.g., rushing) is mentioned, we count them as a single type of answer: the total number of touchdowns he had.
        """,
        "example_number_msqa": 1,
        "example_locate_drop": """
            1. In the fourth quarter, the Raiders spoiled the Broncos' bid for a shutout as QB JaMarcus Russell completed an 8-yard TD pass to WR Ashley Lelie.
            2. Oakland ended the scoring with Russell completing a 4-yard TD pass to WR Ronald Curry.
        """,
        "example_answer_msqa": "2",
        "example_explanation_msqa": """
            1. The question asks for the number of touchdowns JaMarcus Russell had in the game.
            2. The context states that JaMarcus Russell threw two touchdown passes:
            - One 8-yard TD pass to WR Ashley Lelie.
            - One 4-yard TD pass to WR Ronald Curry.
            3. These are two separate and clearly stated touchdown passes credited to JaMarcus Russell. No other touchdowns involving him are mentioned in the context.
            4. Therefore, the total number of touchdowns JaMarcus Russell had in the game is two.
        """
    },
    "example_8": {
        "example_context_msqa": """
            After winning at home, the Bengals traveled down south to take on the Jaguars.  The Jags scored first in the first quarter when Josh Lambo kicked a 32-yard field goal to make it 3-0.  They would make it 10-0 in the second quarter when Blake Bortles found Marqise Lee on a 3-yard pass.  The Bengals got on the board coming within 3 as Joe Mixon ran for a 7-yard touchdown making the score 10-7.  However, the Jags pulled away with Lambo's 56-yard field goal to make it 13-7 at halftime.  In the second half it was all Jags as they scored in the third quarter with Lambo hitting his third field goal of the day from 25 yards out to make it 16-7.  In the fourth quarter, they would wrap up the scoring of the game with Jaydon Mickens 63-yard punt return for a touchdown and the final score 23-7. The game was notable seeing  A.J. Green getting ejected in the second quarter after fighting with Jacksonville's Jalen Ramsey, who was also ejected.
        """,
        "example_question_msqa": "Who was removed first",
        "example_clar_msqa": """
            1. Cognitive Cues: order of ejections; A.J. Green and Jalen Ramsey fight; who left the game first
            2. The central inquiry is asking which player—A.J. Green or Jalen Ramsey—was removed from the game first as a result of their ejection.
            3. The core concepts include A.J. Green and Jalen Ramsey as the individuals involved, their ejection due to an on-field fight during the Bengals vs. Jaguars game, and the sequence or timing of their removal from the game.
            4. The goal is to determine which of the two players (Green or Ramsey) was the first to be removed from the game following the ejection incident.
        """,
        "example_know_msqa": """
            1. A.J. Green was ejected in the second quarter.
            2. Jalen Ramsey was also ejected after the fight with A.J. Green.
            3. The game was notable for their ejections following the altercation.
        """,
        "example_logic_msqa": """
            1. The question is asking who was removed first during the game between the Bengals and the Jaguars.
            2. The context mentions that both A.J. Green and Jalen Ramsey were ejected after a fight in the second quarter.
            3. The context specifically states that A.J. Green was ejected in the second quarter, while Jalen Ramsey was also ejected after fighting with A.J. Green.
            4. Based on the provided context, it can be inferred that A.J. Green was likely the first to be removed due to the sequence of events.
        """,
        "example_number_msqa": 1,
        "example_locate_msqa": """
            1. The game was notable seeing  A.J. Green getting ejected in the second quarter after fighting with Jacksonville's Jalen Ramsey, who was also ejected.
        """,
        "example_answer_msqa": "A.J. Green",
        "example_explanation_msqa": """
            1. The question is asking who was removed first during the game between the Bengals and the Jaguars.
            2. The context states that both A.J. Green and Jalen Ramsey were ejected after a fight in the second quarter:
            - A.J. Green was ejected for fighting with Jalen Ramsey.
            - Jalen Ramsey was also ejected after the altercation with A.J. Green.
            3. Although the context does not explicitly state who was removed first, the fact that A.J. Green's ejection is mentioned first suggests he was likely the first player to be removed.
            4. Therefore, based on the order of the events and typical reporting, A.J. Green was removed first.
        """
    },
    "example_9": {
        "example_context_msqa": """
            After Culloden, government forces spent the next few weeks searching for rebels, confiscating cattle and burning Non-Juring Episcopalian and Catholic meeting houses; many of those who participated in the Rebellion came from this element of Scottish society. Prisoners from regiments in the French service were treated as POWs and exchanged, but 3,500 captured Jacobites were indicted for treason. 650 of these died awaiting trial, 120 were executed , 900 were pardoned and the rest transported. The Jacobite lords Kilmarnock, Balmerino and Lovat were beheaded on Tower Hill in April 1747, but these were among the last executions. Public sympathies had shifted and Cumberland's insistence on severity earned him the nickname 'Butcher' from a City of London alderman. The last Jacobite to be executed was Doctor Archibald Cameron, younger brother of Lochiel. Convicted of treason for his part in the 45, he escaped into exile; when he returned to Scotland in March 1753, he was allegedly betrayed by members of his own clan and executed in London on 7 June.
        """,
        "example_question_msqa": "Of the 3,500 Jacobites that were captured and indited for treason how many lived?",
        "example_clar_msqa": """
            1. Cognitive Cues: JaMarcus Russell; number of touchdowns; completed touchdown passes
            2. The central inquiry is asking how many touchdowns JaMarcus Russell had in the game described.
            3. The core concepts include JaMarcus Russell as the player, a 2008 football game between the Denver Broncos and Oakland Raiders as the event, and the number of touchdowns he threw as the key detail.
            4. The goal is to determine the total number of touchdown passes that JaMarcus Russell threw in this specific game based on the context provided.
        """,
        "example_know_msqa": """
            1. 3,500 Jacobites were captured and indicted for treason.
            2. 650 died awaiting trial.
            3. 120 were executed.
            4. 900 were pardoned.
            5. The rest were transported.
        """,
        "example_logic_msqa": """
            1. The question is asking how many of the 3,500 captured and indicted Jacobites lived.
            2. The context provides the following breakdown of the 3,500 Jacobites:
                - 650 died awaiting trial.
                - 120 were executed.
                - 900 were pardoned.
                - The rest were transported.
            3. To determine how many lived, we need to exclude those who died (650 + 120 = 770) from the total (3,500).
            4. The number of Jacobites who lived is therefore 3,500 - 770 = 2,730.
            5. However, the question may also be interpreted as asking for the distinct categories of those who lived (pardoned and transported). 
                - Pardoned: 900
                - Transported: 3,500 - (650 + 120 + 900) = 1,830
            6. If the question is interpreted as asking for the distinct groups that lived (pardoned and transported), then there are 2 answers. If it is asking for the total number who lived, then the answer is 1 (2,730).Given the phrasing \"how many lived,\" it is more likely asking for the total number who lived, not the distinct categories.
        """,
        "example_number_msqa": 1,
        "example_locate_msqa": """
            1. Prisoners from regiments in the French service were treated as POWs and exchanged, but 3,500 captured Jacobites were indicted for treason.
            2. 650 of these died awaiting trial, 120 were executed , 900 were pardoned and the rest transported.
        """,
        "example_answer_msqa": "2,730",
        "example_explanation_msqa": """
            1. The question asks how many of the 3,500 captured and indicted Jacobites lived.
            2. The context states that 650 died awaiting trial and 120 were executed, totaling 770 deaths.
            3. Subtracting the deaths (770) from the total (3,500) gives the number who lived: 3,500 - 770 = 2,730.
            4. The answer is the total number who lived, not the breakdown of pardoned or transported individuals.
        """
    },
}
