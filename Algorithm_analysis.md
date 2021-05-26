# Analiza algorytmu

## Założenia

Algorytm Bellmana-Forda służy do wyszukiwania najkrótszych ścieżek w grafie ważonym z wierzchołka źródłowego do wszystkich pozostałych wierzchołków.

## Przykłady wykorzystania

Najpopularniejszym rozwiązaniem wykorzystującym algorytm Bellmana-Forda jest [protokół routingu RIP](https://pl.wikipedia.org/wiki/Routing_Information_Protocol) używany w sieciach komputerowych:

1.  Każdy węzeł (router) oblicza odległości między sobą a wszystkimi innymi węzłami w systemie autonomicznym i przechowuje te informacje w tabeli.
2.  Każdy węzeł wysyła swoją tabelę do wszystkich sąsiednich węzłów.
3.  Gdy węzeł otrzymuje tabele odległości od swoich sąsiadów, oblicza najkrótsze trasy do wszystkich innych węzłów i aktualizuje własną tabelę, aby odzwierciedlić wszelkie zmiany.

Algorytm jest również wykorzystywany do sprawdzania występowania w grafie ujemnych cykli osiągalnych ze źródła.