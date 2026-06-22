import csv
from datetime import date

today = date.today().strftime("%Y-%m-%d")

# === AP+TS ===
ap_ts = [
    ("aadabhyderabad", "https://epaper.aadabhyderabad.in/"),
    ("akshratimes", "https://epaper.akshratimes.com/"),
    ("andhrajyothy", "https://epapp.andhrajyothy.com/"),
    ("dishadaily", "https://epaper.dishadaily.com/"),
    ("eenadu", "https://epaper.eenadu.net/"),
    ("jyothidaily", "https://epaper.jyothidaily.com/"),
    ("kothaswaram", "https://epaper.kothaswaram.com/"),
    ("mahaadaily", "https://epaper.mahaadaily.com/"),
    ("maname", "https://www.manamepaper.com/"),
    ("manasarkar", "https://epaper.manasarkar.com/"),
    ("naadesam", "https://epaper.naadesam.com/"),
    ("navabhoomi", "https://www.navabhoomi.com/"),
    ("netishubhodaya", "https://epaper.netishubhodaya.com/"),
    ("nijamnews", "https://epaper.nijamnews.in/"),
    ("ninadam", "https://epaper.ninadam.in/"),
    ("nyayamnews", "https://epaper.nyayamnews.com/"),
    ("penpower", "https://epaper.penpower.in/index.php?date={YYYY-MM-DD}"),
    ("prabhanews", "https://epaper.prabhanews.com/"),
    ("prajagonthuka", "https://epaper.prajagonthuka.in/"),
    ("prajajyothinews", "https://epaper.prajajyothinews.com/"),
    ("prajaprashna", "https://epaper.prajaprashna.com/"),
    ("prajasakti", "https://epaper.prajasakti.com/"),
    ("sakshi", "https://epaper.sakshi.com/"),
    ("subhodayamdaily", "https://www.subhodayamdaily.in/"),
    ("surya", "https://www.suryaepaper.com/"),
    ("suryavelugu", "https://www.suryavelugu.com/"),
    ("teluguprabha", "https://epaper.teluguprabha.net/"),
    ("telugurekha", "https://epaper.telugurekhamedia.com/"),
    ("tolivelugu", "https://www.tolivelugu.com/"),
    ("vaartha", "https://epaper.vaartha.com/"),
    ("visalaandhra", "https://epaper.visalaandhra.com/"),
    ("Yuvatharam", "https://epaper.yuvatharamnews.com/"),
]

# === TS ===
ts = [
    ("95newspaper", "https://www.95newspaper.com/"),
    ("adugunews", "https://epaper.adugunews.com/"),
    ("agnidharanews", "https://epaper.agnidharanews.com/"),
    ("aksharagalam", "https://epaper.aksharagalam.com/"),
    ("aksharam", "https://epaper.aksharamtelugudaily.com/"),
    ("bigtvlive", "https://epaper.bigtvlive.com/"),
    ("churakalu", "https://epaper.churakalu.com/"),
    ("citytimesdaily", "https://epaper.citytimesdaily.com/"),
    ("iyyalatelangana", "https://epaper.iyyalatelangana.com/"),
    ("janampowerdaily", "https://janampowerdaily.in/"),
    ("janamsakshi", "https://epaper.janamsakshi.org/"),
    ("janasamudram", "https://epaper.janasamudram.com/"),
    ("keratamnews", "https://keratamnews.in/"),
    ("manasakshi", "https://epaper.manasakshi.in/"),
    ("manatelangana", "https://epaper.manatelangana.news/"),
    ("mediatodaydaily", "https://epaper.mediatodaydaily.in/"),
    ("metroevenings", "https://epaper.metroevenings.com/"),
    ("nagaranijam", "https://epaper.nagaranijam.com/"),
    ("namasthehyderabad", "https://www.namasthehyderabad.com/"),
    ("navatelangana", "https://epaper.navatelangana.com/"),
    ("netisakshi", "https://epaper.netisakshi.com/"),
    ("netivartha", "https://epaper.netivarthaspeednews.com/"),
    ("newslinetelugu", "https://epaper.newslinetelugu.com/"),
    ("ntnews", "https://epaper.ntnews.com/"),
    ("padmakranthi", "https://www.padmakranthi.com/"),
    ("pcwnews", "https://epaper.pcwnews.in/"),
    ("prabhathaudayam", "https://www.prabhathaudayam.com/"),
    ("prajaasakshi", "https://prajaasakshi.com/"),
    ("prajajwalanews", "https://epaper.prajajwalanews.com/"),
    ("prajapaksham", "https://epaper.prajapaksham.in/"),
    ("prajashankaravam", "https://epaper.prajashankaravam.com/"),
    ("prajaspoorthi", "https://www.prajaspoorthi.com/"),
    ("prajatantranews", "https://epaper.prajatantranews.com/"),
    ("prajavinikidi", "https://www.prajavinikidi.com/"),
    ("prathipaksham", "https://epaper.prathipaksham.in/"),
    ("roamingnews", "https://epaper.roamingnews.in/"),
    ("siridaily", "https://epaper.siridaily.com/"),
    ("sooryasena", "https://www.sooryasena.com/"),
    ("telanganadisha", "https://www.telanganadishaepaper.com/"),
    ("telanganagalam", "https://telanganagalam.com/"),
    ("telanganakanuka", "https://epaper.telanganakanuka.com/"),
    ("telanganamuchatlu", "https://epaper.telanganamuchatlu.in/"),
    ("telanganapatrika", "https://epaper.telanganapatrika.in/"),
    ("tholikranthi", "https://www.tholikranthidaily.com/"),
    ("tholisamayam", "https://epaper.tholisamayam.in/"),
    ("thovvanews", "https://epaper.thovvanews.com/"),
    ("v6velugu", "https://epaper.v6velugu.com/"),
    ("vaarthalu", "https://www.vaarthalu.in/"),
    ("vasthavam", "https://www.vasthavam.com/"),
    ("vedhanews", "https://epaper.vedhanews.in/"),
    ("vijayakranthi", "https://epaper.vijayakranthinews.com/"),
    ("vishalabharati", "https://epaper.vishalabharati.com/"),
    ("vishvambhara", "https://epaper.vishvambhara.com/"),
    ("visionandhra", "https://epaper.visionandhra.in/archive/date/{DD-Mon-YYYY}"),
    ("voicetoday", "https://epaper.voicetodaynews.com/"),
    ("voodayam", "https://epaper.voodayam.com/"),
]

# === AP ===
ap = [
    ("andhrapatrikaa", "https://www.andhrapatrikaa.com/"),
    ("andhrapragathi", "https://www.andhrapragathi.com/"),
    ("Chaitanyavaradhi", "https://www.cvdaily.in/"),
    ("kadilinchevaartha", "https://epaper.kadilinchevaartha.com/"),
    ("telugudesam", "https://www.telugudesam.org/e-paper/"),
    ("todaypallesakshi", "https://www.todaypallesakshi.in/"),
    ("viswamvoice", "https://epaper.viswamvoice.com/"),
]

# === ENGLISH ===
english = [
    ("dailypioneer", "https://dailypioneer.com/"),
    ("deccanchronicle", "http://epaper.deccanchronicle.com/"),
    ("financialexpress", "https://epaper.financialexpress.com/"),
    ("penpower", "https://epaper.penpower.in/paper.php?date={YYYY-MM-DD}&edition=2"),
    ("sundayguardianlive", "https://epaper.sundayguardianlive.com/"),
    ("telanganatoday", "https://epaper.telanganatoday.com/Hyderabad?eid=1&edate={DD/MM/YYYY}"),
    ("thehansindia", "https://epaper.thehansindia.com/"),
    ("thestatesman", "https://epaper.thestatesman.com/"),
    ("wakeuptelangana", "https://epaper.wakeuptelangana.com/"),
]

def write_csv(filename, data, start_id, category):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "url", "category", "date_dynamic"])
        for i, (name, url) in enumerate(data):
            uid = start_id + i
            is_dynamic = "{" in url
            writer.writerow([uid, name, url, category, "yes" if is_dynamic else "no"])
    print(f"Created {filename} with {len(data)} entries")

write_csv("ap_ts.csv", ap_ts, 100, "AP+TS")
write_csv("ts.csv", ts, 200, "TS")
write_csv("ap.csv", ap, 300, "AP")
write_csv("english.csv", english, 400, "English")
print("All CSV files created!")
