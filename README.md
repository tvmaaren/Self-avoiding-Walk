<h1>Self avoiding-walk</h1>

Groepsopdracht voor programmeren in de wiskunde over self avoiding waks


<h2>Overzicht van functies</h2>

<h3>__init__(self,template="2dsquare",direction_vectors=None)</h3>
<table>
<tr><th>template<th>Het template rooster dat gebruikt wordt. Mogelijke waarden zijn: "2dsquare", "3dcubic", "4dcubic", "2dtriangle", None. Als er niet gebruik gemaakt word van een template moet dit gelijk zijn aan None<th><tr>
<tr><th>direction_vectors<th>Lijst richtingsvectoren van het rooster. Als er een template gebruikt  wordt moet dit gelijk zijn aan None.<th><tr>
</table>
Initialiseert de klasse

<h3>pop(self,n=1)</h3>
<table>
    <tr><th>n<th>Hoeveelheid punten dat van wandeling verwijderd moet worden.<th></tr>
</table>
Haalt punten weg van het einde van de wandeling
<h3>go_direction(self,direction)</h3>
<table>
    <tr><th>direction<th>Is een index van <b>direction_vectors</b>. Het geeft de richting aan van de stap.
</table>
Zet een stap in een gegeven richting.
<h3>possible_walks(self,N)</h3>
<table>
<tr><th>N</th><th>De lengte van de wandelingen</th></tr>
</table>
Telt alle mogelijke wandelingen met lengte N vanuit de oorsprong die gecreërt kunnen worden.
<h3>possible_walks_faster(self,N)</h3>
<table>
  <tr><th>N<th>De lengte van de wandelingen<th><tr>
</table>
Telt alle mogelijke wandelingen met lengte N vanuit de oorsprong die gecreërt kunnen worden op een snellere manier dan dat <b>possible_walks</b> dat doet. Werkt alleen maar als het uiteinde van de wandeling op de oorsprong ligt.
<h3>plot(self)</h3>
Geeft een grafische weergave van de SAW. Dit werkt alleen als de template gelijk is aan "2dsquare" of "2dtriangle".

<h2>Richtingsvectoren voor de templates</h2>

In figuur \ref{fig:kub_rich},\ref{fig:vier_rich} en \ref{fig:drie_rich} ziet u voor de verschillende templates de indices van de richtingsvectoren.

\begin{figure}[h]
\begin{minipage}{0.3\textwidth}
    \includesvg[width=\columnwidth]{3dkubisch_richtingen.svg}
    \caption{3dcubic}
    \label{fig:kub_rich}
\end{minipage}
\begin{minipage}{0.3\textwidth}
    \includesvg[width=\columnwidth]{vierkantsrooster_richtingen.svg}
    \caption{2dsquare}
    \label{fig:vier_rich}
\end{minipage}
\begin{minipage}{0.3\textwidth}
    \includesvg[width=\columnwidth]{driehoeksrooster_richtingen}
    \caption{2dtriangle}
    \label{fig:drie_rich}
\end{minipage}
\end{figure}

\subsection{Gebruik van de class}

\subsubsection{Standaard-template}

Wanneer de class geïnitialiseerd wordt moet er rekening gehouden worden met het rooster. Het is het makkelijkst wanneer er gebruik gemaakt word van een 2-dimensionaal vierhoekig rooster. In dat geval kan de gebruiker de SAW als volgt initialiseren:
\begin{python}
s = SAW()
\end{python}
Zoals u ziet hoeven er geen parameters aan toegevoegd te worden. Stel nu dat we een trap willen maken. We zien in figuur \ref{fig:vier_rich} dat naar boven gaan de index 1 heeft en naar rechts gaan de index 0 heeft. We kunnen dus een trap maken door telkens een stap omhoog te nemen en daarna een stap naar rechts.
\begin{python}
for i in range(10):
    s.go_direction(1)
    s.go_direction(0)
\end{python}
Dit kunnen we dan nu visualiseren met de functie plot:
\begin{python}
s.plot()
\end{python}

Onze SAW ziet er dan als volgt uit:
\begin{center}
    \includegraphics[scale=0.7]{Geplotte SAW.png}
\end{center}
Hierbij is het belangrijk dat de wandeling die op deze wijze gemaakt wordt zichzelf niet snijdt. Gebeurt dit wel dan komt er een error.

Dan nu nog een voorbeeld. We zijn nu benieuwd hoeveel zelfmijdende wandelingen van lengte 4 zijn op een tweedimensionaal vierkant rooster. Met de volgende code kunnen we dit bepalen:
\begin{python}
s = SAW()
print(s.possible_walks(4))
\end{python}
Wanneer dit uitgevoerd is 100 de output

\subsubsection{Andere templates}
Stel nu dat we een ander rooster willen gebruiken, dan moeten we dit specificeren. Voor ``2d vierkant roosters", ``3d kubische rooster", ``4d kubische rooster" en ``2d driehoeksrooster" is dit nog vrij gemakkelijk, want hier bestaat al een template voor. Deze roosters hebben als template respectievelijk: ``2dsquare",``3dcubic" en ``2dtriangle". Stel we willen een SAW initialiseren met een driehoeksrooster dan doen we:
\begin{python}
s = SAW(template="2dtriangle")
\end{python}
Hierop kan weer op dezelfde manier als bij de standaard-template gebruik gemaakt worden van de functies. De enige uitzondering hierbij is de functie ``plot", omdat deze alleen maar geïmplementeerd is voor de standaard template ``2dsquare"\ en ``2dtriangle". Voor alle ander templates zal er een error verschijnen wanneer de plot functie uitgevoerd wordt. Een voorbeeld van een geplotte SAW op het driehoeksrooster is:
\begin{center}
    \includegraphics[scale=0.7]{Geplotte SAW2.png}
\end{center}

\subsubsection{De class gebruiken zonder template}

Stel nu dat we een rooster willen maken waar nog geen template voor is. Een heel simpel voorbeeld is een 1-dimensionaal rooster van de gehele getallen. Hierbij kunnen we telkens maar twee richtingen op: Omhoog en omlaag. Omlaag komt hierbij overeen met de richtingsvector $-1$ en omhoog met de richtingsvector $1$. Wanneer de SAW-class geïnitialiseerd wordt moet er duidelijk gemaakt worden dat er geen gebruik wordt gemaakt van een template, dus moet de template gelijk zijn aan ``None". \code{direction\_vectors} is een lijst van tuples, die de richtingsvectoren voorstellen. In dit geval is dit dan [(-1,),(1,)]. We initialiseren de class als volgt:

\begin{python}
s = SAW(template=None, direction_vectors=[(-1,),(1,)]
\end{python}
We weten altijd dat er maar twee mogelijke wandelingen zijn voor willekeurige lengte n. We zien dus dat
\begin{python}
print(s.possible_walks(100))
\end{python}
een 2 geeft.
