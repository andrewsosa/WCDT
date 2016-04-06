import sys, os, praw, nltk, wikipedia

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import *

def extract_entities(sample):
    """
    Returns a set of proposed entities
    """
    sentences = nltk.sent_tokenize(sample)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    def extract_entity_names(t):
        entity_names = []

        if hasattr(t, 'label') and t.label:
            if t.label() == 'NE':
                entity_names.append(' '.join([child[0] for child in t]))
            else:
                for child in t:
                    entity_names.extend(extract_entity_names(child))

        return entity_names

    entity_names = []
    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)

        entity_names.extend(extract_entity_names(tree))

    # Print all entity names
    #print entity_names

    # Print unique entity names
    return set(entity_names)

def detect(headline):
    f = file("first.txt", "r")
    l = file("last.txt", "r")

    firsts = f.read().split()
    lasts = l.read().split()

    f.close()
    l.close()

    # Check with NLTK
    entities = extract_entities(headline)

    # Check with name list
    #for e in list(entities):
    #    for t in e.split():
    #        if (t.upper() not in firsts and t.upper() not in lasts) or len(e.split()) is not 2:
    #            entities.discard(e)

    # Check with Wikipedia
    for e in list(entities):
        try:
            page = wikipedia.page(str(e), auto_suggest=False)
            cats = page.categories

            flag = True
            for c in cats:
                if "deaths" in c or "births" in c:
                    flag = False
                    break
            if flag:
                #print "REJECTED", e
                entities.discard(e)

        except:
            #print "REJECTED", e
            entities.discard(e)
    return entities


def main():
    user_agent = "A headline crawler by /u/jezusosaku"
    r = praw.Reddit(user_agent=user_agent)
    #headlines = r.get_front_page()
    headlines = r.get_subreddit("news").get_hot()
    for t in [x.title for x in headlines]:
        s = detect(t)
        if len(s) == 1:
            print t, s

            hd = Headline(text=t, person=s.pop())
            hd.save()

            #if any(ext in t.lower() for ext in ["dead", "passed away", "died", "rip", "r.i.p."]):
            #    print  "dead"


if __name__ == "__main__":
    main()
