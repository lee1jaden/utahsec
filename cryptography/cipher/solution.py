ciphertext = "Gur Pbzchgre Fpvrapr znwbe ng gur Havirefvgl bs Hgnu vf bar bs gur zbfg qlanzvp naq sbejneq-guvaxvat cebtenzf va gur fgngr, bssrevat fghqragf gur bccbeghavgl gb qvir vagb gur urneg bs gur grpu eribyhgvba. Jvgu n pbzcerurafvir pheevphyhz, unaqf-ba rkcrevraprf, naq n fgebat fhccbeg flfgrz, gur cebtenz cercnerf fghqragf gb or yrnqref va n encvqyl ribyivat svryq."
ciphertext2 = "Bar bs gur zbfg rkpvgvat nfcrpgf bs gur znwbe vf vgf irefngvyvgl. Pbzchgre fpvrapr vf gur onpxobar bs znal vaqhfgevrf, sebz ragregnvazrag naq urnygupner gb svanapr naq nrebfcnpr. Gur znwbe ng gur Havirefvgl bs Hgnu ersyrpgf guvf qvirefvgl, nyybjvat fghqragf gb rkcyber n jvqr neenl bs gbcvpf fhpu nf negvsvpvny vagryyvtrapr, qngn fpvrapr, fbsgjner ratvarrevat, plorefrphevgl, znpuvar yrneavat, naq uhzna-pbzchgre vagrenpgvba. Jurgure lbh'er vagrerfgrq va ohvyqvat zbovyr nccf, gur synt vf plorefrp{vfa'g_pf_fhcre_sha} qrfvtavat ynetr-fpnyr qngnonfrf, be perngvat vagryyvtrag flfgrzf, gur cebtenz rdhvcf lbh jvgu gur sbhaqngvbany xabjyrqtr naq cenpgvpny fxvyyf arrqrq gb fhpprrq."
ciphertext3 = "Gur snphygl ng gur Havirefvgl bs Hgnu ner abg bayl rqhpngbef ohg nyfb vaabingbef naq erfrnepuref jub ner npgviryl pbagevohgvat gb nqinaprzragf va gurve svryqf. Guvf perngrf n havdhr bccbeghavgl sbe fghqragf gb ratntr va phggvat-rqtr erfrnepu, bsgra jvgu erny-jbeyq nccyvpngvbaf. Snphygl zrzoref ner nccebnpunoyr naq rntre gb zragbe fghqragf, znxvat gur yrneavat rkcrevrapr uvtuyl crefbanyvmrq. Fghqragf pna pbyynobengr jvgu cebsrffbef ba erfrnepu ce"
# All are solved with a caesar cipher of shift 20

for i in range(26):
    encoded_words = ciphertext3.split()
    decoded_words = []
    for ew in encoded_words:
        dw = ""
        for letter in ew.lower():
            letterIndex = (ord(letter) + i) % 26 + 97
            dw = dw + chr(letterIndex)
        decoded_words.append(dw)
    print(str(i) + ". " + " ".join(decoded_words) + "\n")
