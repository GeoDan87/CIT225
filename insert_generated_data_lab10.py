from db_connect import *
from generate_newsletters_podcasts import *

PODCAST_BASE_URL = 'https://www.habitatforhugemanatees.org/podcasts/'
NEWSLETTER_BASE_URL = 'https://www.habitatforhugemanatees.org/newsletters/'

con = connect_db_engine()

podcast_names = [{'podcast_name': "This Manatee Life"
                  ,'podcast_description': "A weekly public radio show that documents extraordinary tales from ordinary manatees. Host Ira Grassbed brings you stories of love, loss, and seagrass from the gentle giants of coastal waters."}
                 ,{'podcast_name': "The Joe Dugong Experience"
                   ,'podcast_description': "The internet's most controversial three-hour conversations with manatee experts, conservationists, and that one guy who swears manatees can communicate telepathically. Hosted by former Fear Factor host turned passionate manatee advocate."}
                 ,{'podcast_name':"Serial Swimmer"
                  ,'podcast_description':"A podcast that investigates one mysterious manatee migration pattern over the course of an entire season. Did Marvin the Manatee really travel to Bermuda and back? Host Sarah Koenig-Flipper dives deep to uncover the truth."}
                 ,{'podcast_name':"Freakonomanatees"
                  ,'podcast_description':"Exploring the hidden side of manatee behavior through the lens of economics. Why do manatees cluster in power plant discharge areas? Is there a manatee mating economy? Stephen Dubner and Steven Levitt examine the incentives that drive our favorite sea cows."}
                 ,{'podcast_name':"The Daily Sea Cow"
                  ,'podcast_description':"Twenty minutes a day, five days a week, hosted by Michael Barbaro with his signature thoughtful pauses, bringing you the biggest stories in the manatee world right now, from conservation efforts to manatee celebrity gossip."}]

newsletter_names = [
    {
        "newsletter_name": "The Sea Cow Gazette",
        "newsletter_description": "A bi-weekly publication reporting on all the breaking news from the manatee world at a leisurely pace. Features in-depth interviews with marine biologists, conservation updates, and the popular 'Seagrass Connoisseur' column ranking the tastiest underwater meadows."
    },
    {
        "newsletter_name": "Manatee Business (Slow News Day)",
        "newsletter_description": "The premier financial newsletter for the discerning marine mammal investor. Covers the latest trends in thermal spring real estate, analysis of seagrass futures, and special features on work-life balance (spoiler: it's mostly floating and eating)."
    },
    {
        "newsletter_name": "The Chubby Mermaid Monthly",
        "newsletter_description": "A glossy lifestyle magazine celebrating the rotund beauty of manatees. Each issue includes fashion tips for the full-figured sea mammal, blubber-positive affirmations, and mythbusting articles about the mermaid-manatee confusion throughout history."
    },
    {
        "newsletter_name": "Flippers & Giggles",
        "newsletter_description": "The comedy newsletter that proves manatees have a sense of humor. Packed with marine mammal memes, underwater puns, and hilarious first-person accounts of awkward human encounters. The 'Photobombs' section features manatees sneaking into tourist pictures."
    },
    {
        "newsletter_name": "Lettuce Entertain You (Manatee Edition)",
        "newsletter_description": "The ultimate culinary guide for herbivorous sea mammals. Each issue features recipes using different aquatic plants, reviews of feeding grounds around the world, and celebrity chef manatees sharing their secret techniques for efficient grazing."
    },
    {
        "newsletter_name": "The Snout & About",
        "newsletter_description": "A travel and adventure newsletter for the curious manatee. Highlights unexplored coves, warm-water getaways, and boat-free zones perfect for a peaceful vacation. Includes a safety section on propeller avoidance and the annual 'Best Springs' destination guide."
    }
]

podcasts = generate_podcast_info(podcast_names)

newsletters = generate_newsletter_info(newsletter_names)

#Insert the podcast info data
insert_data(con, 'podcast_info', 'hfh', podcasts)

#Insert the newsletter info data
insert_data(con, 'newsletter_info', 'hfh', newsletters)

podcasts = select_data(con, 'podcast_info', 'hfh')

newsletters = select_data(con, 'newsletter_info', 'hfh')

supporters = select_data(con, 'supporter', 'hfh')

emails = select_data(con, 'email_address', 'hfh')

#Add a URL to newsletters
for n in newsletters:
    n.update({'newsletter_url': NEWSLETTER_BASE_URL + n.get('newsletter_name').lower().replace(' ','-').replace('(', '').replace(')', '').replace('&', 'and')})

podcast_subs = generate_podcast_subs(supporters, podcasts)

newsletter_subs = generate_newsletter_subs(emails, newsletters)

#Insert the podcast subscriptions data
insert_data(con, 'podcast_subscription', 'hfh', podcast_subs)

#Insert the newsletter subscriptions data
insert_data(con, 'newsletter_subscription', 'hfh', newsletter_subs)