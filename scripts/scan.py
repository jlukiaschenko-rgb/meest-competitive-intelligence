#!/usr/bin/env python3
"""Monitor public pages for new relevant URLs. First run creates baseline."""
import json, re, hashlib
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

BASE=Path(__file__).resolve().parents[1]
DATA=BASE/"data"
TERMS=("promoc","rabat","discount","sale","news","blog","artyku","aktual","new","nowo","produkt","uslug","usług","przesyl","przesył","pacz","dostaw","kurier","kampan","cennik","kupon","shipping","delivery")
STOP=("login","privacy","polityka","cookie","koszyk","checkout","kontakt","register","account","regulamin")
class Links(HTMLParser):
    def __init__(self):
        super().__init__();self.items=[];self.in_a=False;self.href="";self.words=[]
    def handle_starttag(self,tag,attrs):
        if tag=="a":
            self.in_a=True;self.href=dict(attrs).get("href","");self.words=[]
    def handle_data(self,data):
        if self.in_a:self.words.append(data)
    def handle_endtag(self,tag):
        if tag=="a" and self.in_a:
            self.items.append((self.href," ".join(self.words).strip()));self.in_a=False

def load(path,default):
    try:return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError,json.JSONDecodeError):return default
def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def normalize(url):
    p=urlsplit(url)
    return urlunsplit((p.scheme,p.netloc.lower(),p.path.rstrip("/") or "/",p.query,""))
def category(hint,text):
    t=text.lower()
    if any(k in t for k in ("promoc","rab","kupon","discount","sale")):return "Promocje"
    if any(k in t for k in ("produkt","usług","uslug","integrac","nowo")):return "Produkty i usługi"
    if any(k in t for k in ("kampan","campaign")):return "Kampanie"
    return hint
def priority(c,cat):
    if cat in ("Promocje","Produkty i usługi"):return "high" if c["priority"]==1 else "medium"
    return "medium" if c["priority"]==1 else "low"
def crawl(source):
    req=Request(source["url"],headers={"User-Agent":"Mozilla/5.0 (compatible; MeestCI/1.0)"})
    with urlopen(req,timeout=15) as res:
        mime=res.headers.get("Content-Type","")
        if "html" not in mime.lower():raise ValueError("Not an HTML page")
        page=res.read(900000).decode("utf-8",errors="replace")
    parser=Links();parser.feed(page)
    origin=urlsplit(source["url"]).netloc.lower().removeprefix("www.")
    found={}
    for href,title in parser.items:
        try:
            u=normalize(urljoin(source["url"],href))
            p=urlsplit(u)
            if p.scheme not in ("https","http"):continue
            domain=p.netloc.lower().removeprefix("www.")
            if domain!=origin:continue
            if len(u)>350 or any(k in u.lower() for k in STOP):continue
            txt=(p.path+" "+title).lower()
            if not any(k in txt for k in TERMS):continue
            if u==normalize(source["url"]):continue
            found[u]=title[:180] or p.path.split("/")[-1].replace("-"," ").title()
        except ValueError:continue
    return dict(list(sorted(found.items()))[:250])

def main():
    config=load(BASE/"config"/"sources.json",{})
    state=load(DATA/"state.json",{})
    events=load(DATA/"events.json",[])
    history=load(DATA/"history.json",[])
    now=datetime.now(timezone.utc).isoformat(timespec="seconds")
    initial=not bool(state)
    ok=errors=added=0
    for c in config["competitors"]:
        for src in c["sources"]:
            key=c["name"]+"|"+src["url"]
            try:
                found=crawl(src);ok+=1
                previous=set(state.get(key,[]))
                if not initial and key in state:
                    for url in sorted(set(found)-previous):
                        title=found[url]
                        cat=category(src["category"],url+" "+title)
                        events.append({"id":hashlib.sha256((c["name"]+url).encode()).hexdigest()[:16],
                            "competitor":c["name"],"category":cat,"priority":priority(c,cat),
                            "title":title,"summary":"Nowy link wykryty na monitorowanej stronie. Wymaga weryfikacji treści oraz daty publikacji.",
                            "recommendation":"Sprawdź źródło i oceń znaczenie dla Meest Post.",
                            "url":url,"detected_at":now})
                        added+=1
                state[key]=sorted(found)
                print("OK",c["name"],src["url"],len(found))
            except Exception as ex:
                errors+=1;print("ERROR",c["name"],src["url"],str(ex)[:180])
    history.append({"checked_at":now,"successful_sources":ok,"failed_sources":errors,"new_events":added,"baseline":initial})
    save(DATA/"state.json",state)
    save(DATA/"events.json",events[-3000:])
    save(DATA/"history.json",history[-365:])
    print("SUMMARY",{"ok":ok,"errors":errors,"new":added,"baseline":initial})
if __name__=="__main__":main()
