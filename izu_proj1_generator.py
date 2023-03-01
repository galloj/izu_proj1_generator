latex_template = r"""
\documentclass{article}

\usepackage[czech]{babel}

\usepackage[a4paper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}

% Useful packages
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{tabularx}

\setlength{\parindent}{0cm}
\setlength{\parskip}{\baselineskip}%

\title{\textbf{Zadání 1. úkolu do předmětu IZU}}
\date{\vspace{-5ex}}

\begin{document}
\maketitle

Jméno: !NAME!

Login: !LOGIN!


Pomocí metody A* najděte nejkratší cestu v mapě složené z pravidelných buněk, kde cena přechodu mezi
dvěma stavy (buňkami) je dána číslem, uvedeným v Tabulce 1 (a je stejná pro všechny přechody ze sousedních
míst do příslušné buňky). Nepřekročitelné buňky mají hodnotu "Z" (jako "zeď" ). Po každém kroku vypište nové
hodnoty seznamů Open a Closed. Do pomocné tabulky s ohodnocením uzlů zapisujte aktuálně zkoumaný uzel,
cenu cesty do aktuálního uzlu „g“, heuristiku „h“ a celkovou cenu cesty „f“. Heuristiku počítejte jako přímou
vzdálenost středů dvou buněk, kde velikost strany jedné buňky je rovna jedné. Uzly generujte v pořadí zleva
doprava a shora dolů, uvažujte 8-okolí buňky
(tzn. operátory $\nwarrow,\uparrow,\nearrow,\leftarrow, \rightarrow,\swarrow,\downarrow,\searrow)$. Výslednou cestu zapište
do tabulky Výsledná cesta. Uzel se skládá ze souřadnic, z ohodnocení f a souřadnic uzlu, ze kterého byl vyge-
nerován nebo z operátoru, který byl použit (aby bylo možné nalézt cestu od startu k cíli).



Uzly zapisujte: ([sloupec, řádek], celkové ohodnocení f, [souřadnice otcovského uzlu nebo operátor])

Start: !START!

Cíl: !END!

Výsledná cesta: !VYSLEDNACESTA!

\begin{center}
\begin{tabular}{|c||c|c|c|c|c|c|c|c|c|c|} 
 \hline
 y/x & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
 \hline\hline
 !MAPA!
\end{tabular}
\end{center}

Tabulka 1: Mapa přechodů. Např. cena přechodu do cílové buňky je rovna 2 pro všechny buňky s cílovou buňkou sousedící.

Pomocná tabulka:

\begin{center}
\begin{tabularx}{\textwidth}{l X X X X l X X X X } 
  & Uzel & g & h & f &   & Uzel & g & h & f \\
  !POMOCNATABULKA!
\end{tabularx}
\end{center}

!ITERACE!

\end{document}
"""

# "Příjmení Jméno"
name = None
# "xlogin00"
login = None
# (x, y)
start = None
# int or float
initial_cost = None
# (x, y)
end = None
# 2D array of strings
mapa = None
# [(uzel, g, h, f), ...]
pomocna_tabulka = []
# [(open, closed), ...]
iterace = []
# [(x, y), ...]
vysledna_cesta = []

def get_latex():
    assert name is not None
    assert login is not None
    assert start is not None
    assert initial_cost is not None
    assert end is not None
    assert mapa is not None
    ret = latex_template
    ret = ret.replace('!NAME!', name)
    ret = ret.replace('!LOGIN!', login)
    ret = ret.replace('!START!', f"({[*start]}, {initial_cost}, [null])")
    ret = ret.replace('!END!', f"({[*end]}, X, [?, ?])")
    ret = ret.replace('!MAPA!', " \\\\\n\\hline\n".join([str(i) + " & " + " & ".join(x) for i, x in enumerate(mapa)])+" \\\\\n\\hline\n")
    pomocna_tmp = (pomocna_tabulka + [["","","",""] for x in range(30)])[:30]
    a=["01.", "02.", "03.", "04.", "05.", "06.", "07.", "08.", "09.", "10.", "11.", "12.", "13.", "14.", "15."]
    b=["16.", "17.", "18.", "19.", "20.", "21.", "22.", "23.", "24.", "25.", "26.", "27.", "28.", "29.", "30."]
    pomocna_tmp = zip(a, pomocna_tmp[:15], b, pomocna_tmp[15:])
    pomocna_tmp = [[f"{y: .2f}" if type(y) == float else str(y) for y in [x[0], *x[1], x[2], *x[3]]] for x in pomocna_tmp]
    ret = ret.replace('!POMOCNATABULKA!', " \\\\\n".join([" & ".join(x) for x in pomocna_tmp])+" \\\\\n")
    its = ""
    for x in range(16):
        s = r"""% https://tex.stackexchange.com/a/186191
\noindent\rule{\textwidth}{2pt}
\textbf{N. iterace}

Open: OPEN

Closed: CLOSED

"""
        if x < len(iterace):
            s = s.replace('OPEN', str(iterace[x][0]))
            s = s.replace('CLOSED', str(iterace[x][1]))
        else:
            s = s.replace('OPEN', '')
            s = s.replace('CLOSED', '')
        s = s.replace('N', str(x+1))
        its += s
    ret = ret.replace('!ITERACE!', its)
    ret = ret.replace('!VYSLEDNACESTA!', str(vysledna_cesta))

    return ret