---
marp: true
theme: my_black_style
---

# računarske mreže

###### bebić / rač@petnica / jul 2021

---
<!-- footer: mreže / bebić / rač@petnica / jul 2021 -->
<!-- paginate: true -->

# šta je to internet ?

---

## kako izgleda internet ?

---

## šta znači reč *internet* ?

---

# vratimo se u 1980-te

* imamo računar
* kako da ga povežemo sa drugim?

---

## problemi sa kablovima

---

## problemi sa operaterom

---

## problemi sa fizikom

---

# modem

* 1/0 ------> neki signal *(modulator)*
* 1/0 <------ neki signal *(demodulator)*
* _**layer 1**: physical_

---

# kako da pričamo sa dva računara ?
* istovremeno ?

---

## *circuit switching*

![bg right fit invert](./mreze/c-switch.svg)

---

## *packet switching*

![bg right fit invert](./mreze/p-switch.svg)

---

## paketiranje

* *protocol service unit* + "koverta" = *protocol data unit*
* možemo ovo ponoviti više puta

---

# nazad na računare
* kako sada pričamo ?

---

## packet switched networking
* za koga + *podaci* --> **paketiranje**
* """ruter"""
* _**layer 2.5**: data link layer / logical link control_

---

## šta sve može biti *svič*
* poseban uređaj
* ostali računari
* ništa ?

---

### kontrola pristupa
* ko kad i kako priča
* može da se ukombinuje sa "za koga" delom
* _**layer 2**: data link layer / media access control_
* zapravo radi još svašta

---

# data link layer
* za koga + kontrola + _podaci_ --> **frejm**
* mac adresa: `18:5e:0f:c9:5c:cf`
* veličina frejma ograničena

---

## kako znamo **za koga** je paket ?
* kako da dođemo do tamo ?
* _moramo da "poznajemo" sve računare_ + put do njih
* radi za do par hiljada računara

---

# nazad na pošta analogiju

* kako radi pošta ?

---

## hierarhijska organizacija

srbija > valjevo > selo petnica > isp

---

# kako to funkcioniše na internetu

---

## primer adresa

- <font color=3366ff>01011011_10111011_1000</font><font color=ff2200>0000_1</font>1000111
* amres: 91.187.128.0/20 ...
* petnička mreža 91.187.128.128/25
* server: 91.187.128.199/24

<!--
ub-as `91.187.128.143` `91.187.128.0/20`
swiss-network `185.25.192.0/22`
-->

---

# internet

- _od koga_ + _za koga_ + podaci -> _**paket**_
- _**layer 3**: internet protocol_

---

# šta za sad imamo ?

---

## šta dalje ?

* više od ~1450 bajtova odjednom ?
* da li je sigurno stiglo ?
* bitan redosled ?

---

# šaljemo niz paketa (_stream_)

--> konekcija

---

## potvrda (_acknowledgement_)

---

## numeracija paketa

* preskakanje
* dupliranje
* izmena redosleda

---

# tcp

---

# a šta ako nam sve to ne treba ?

---

# udp

---

# a šta **sad** dalje

---

## sve

---

# http

```http
GET / HTTP/1.1
Host: www.google.com
Accept: */*

```

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 42069

<html>...</html>
```

- preneseni kao bajtovi kroz tcp stream

---

# ssl

- razmena ključeva
- enkripcija

---

# šta zapamtiti

* nivoi apstrakcije
* hierarhijska organizacija