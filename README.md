# Automatizācijas projekts "YouTube"
Ilgi domājot par ideju projektam nevarēju izdomāt, kāda automatizācija varētu noderēt manā ikdienā. Ņemot vērā to, ka esmu pilna laika students un sportists mana prioritāte nebija izveidot projektu, kas palīdzēs darboties ar exceli vai epastu, jo ar to nenodarbojos ikdienā un tas man personīgi nepalīdzēs! 
Tāpēc nonācu pie secinājuma, ka laikam vajadzētu automatizēt kādu lietu, ar ko nodarbojos savā brīvajā laikā, un padarīt to effektīvu un izbaudāmāku. Un platforma pie kā nonācu ir - YouTube!

Mans projekta mērķis ir izveidot skriptu, kas automātiski saglabās jebkuru YouTube video manā datorā. Šādā veidā vietās, kur man nav pieejams internets man būs saglabājušies video, kurus varēšu izmantot jebkurā laikā un vietā, piemēram, lidojot/ceļojot. 
Un papildus ar šo projektu neesmu spiests maksāt par YouTube Premium abonamentu katru mēnesi, lai saglabātu video un skatītos šos video bez reklāmām.

Rakstot skriptu izmantoju divas biblotēkas. Pytube un tkinter. 
pytube - ir biblotēka, kas ir priekš darbošanās ar Youtube platformu un video saglabāšanu, un tkinter ir jau iepriekš iebūvēta biblotēka python, kas ir standarta graphical user interface darbarīks, kas ļauj saglabāt šo video failu vieglāk izvēloties un uzklikšķinot uz savas vēlamās lokācijas datorā.

Programma tiek izmantota šādi - Iedarbinu kodu, tas man prasīs ievadīt YT video URL, kad to ievadu, tas izmetīs ekrānu, kur būs jāzivēlas saglabāšanās lokācija datorā. Kad tas tiek izdarīts Video sāk lādēties, kas nenotiek uzreiz, bet gan var paņemt pāris minūtes atkarībā no video garuma un interneta ātruma. Kad terminālī parādās "video ir veiksmīgi ielādējies" var droši doties uz mapīti, kur esi saglabājis video un to skatīties. Kad vajadzīgie video ir ielādēti, tas tos var skatīt pilnīgi bez inerneta jebkurā vietā un laikā.
