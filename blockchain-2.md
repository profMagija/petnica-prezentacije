---
marp: true
theme: my_black_style
author: nikola bebić
math: katex
---

# decentralizovani sistemi
bebić / rač @ petnica / februar 2026

---

<!-- footer: dse / bebić / rač@petnica / februar 2026 -->
<!-- paginate: true -->

# centralizovan sistem

---

# decentralizovan sistem

* $\not=$ **distribuiran** sistem

---

# problemi centralizacije

* single point of failure
* količina komunikacije
* kontrola i poverenje

---

# peer-to-peer komunikacija

* adresiranje
* prosleđivanje i rutiranje

---

# anonimna komunikacija

* enkripcija
* onion routing

---

# broadcast komunikacija

* flooding
* gossip
* anti-entropy

---

# pretraga podataka

* nestruktuirana pretraga
  * bubble storm
* strukturirana pretraga
  * dht

---

# distribucija podataka

* replicated storage
* opportunistic caching
* bittorrent

---

# validacija podataka

* kriptografski potpisi
* reputacioni sistemi

---

# koncenzus

* problem: kako da se svi složimo oko istih podataka

---

# koncenzus u centralizovanom sistemu

* centralni autoritet

---

# koncenzus u decentralizovanom sistemu

* konzistentnost
* 2PC
* Paxos, Raft

---

# CAP teorema

* konzistentnost
* dostupnost
* tolerancija na particije

---

# problem: byzantine fault tolerance

---

# koncenzus pod BFT modelom

* PBFT
* leader-based protokoli
  * Tendermint
  * HotStuff

---

# blockchain

* nepromenljivi registar transakcija

---

# block<font color="#555">chain</font>

* spisak transakcija = redosled

---

# <font color="#555">block</font>chain

* blokovi su kriptografski povezani = nepromenljivi

---

# problemi koje moramo da rešimo

* koncenzus oko najnovijeg bloka
* razglasavanje novih transakcija
* pretraga i skladištenje podataka

---

# koncenzus - eventualna konzistentnost

* nakon nekog vremena $t$ dostižemo konzistentnost
  * anti-entropy
  * reconciliation

---

# problem: sybil napad

---

# Satošianski koncenzus

* probabilistički eventualni koncenzus
  * Proof-of-X
* klasični koncenzus

---

# razglasavanje novih transakcija

- flooding / gossip

---

# pretraga i skladištenje podataka

- nestruktuirana pretraga

---

# sažetak

* decentralizovani sistemi
* p2p algoritmi
* koncenzus
* blockchain