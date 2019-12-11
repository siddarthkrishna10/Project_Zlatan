# The Curious Case of Zlatan Ibrahimović

While working on my [Football Transfers piece](https://github.com/siddarthkrishna10/Football_Transfers), I came across a quirk in the dataset. _Zlatan Ibrahimović_; the legendary Journeyman/Illeist/Scorer-of-great-goals/Pompous/Swedish Footballer, was undervalued throughout his career. You would think that one of the most decorated footballers in the modern era who has won over 31 career trophies and scored over 450+ goals would've been highly sought after in terms of money! But that doesn't seem to be the case with Zlatan. Just take a look at this graph,

![ZlatanValuation_Snap](https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Screengrabs/ZlatanValuation_Snap.PNG)

Across the nine clubs he's played in, only F.C. Barcelona splashed a huge amount of money(€69.5 million) to get him and ironically his time there turned out to be a nightmare...of the field atleast.

Here is the code snippet for the graph:
```python
#Reading the dataset into an object
c = pd.read_csv('C:/Users/Siddhardh/Desktop/ProjectZlatan/ZlatanStat_Sheet.csv')

#Plotting a bar graph for Market Value and Transfer Fee
c.plot(x='Club', y=['Market_Value', 'Transfer_Fee'], kind='bar')
plt.xlabel('Club')
plt.xticks(rotation=45)
plt.show()
```

Despite playing excellent football and banging in goals constantly at all the nine clubs he's played for, the market hasn't valued Ibrahimović highly. Even if you put aside the stats, his global superstar status and his bombastic attitude off the field didn't help. He's loved by millions for his eccentric and over-the-top attitude, helping him attain cult status in football but there is no clue as to why Zlatan is up there among the big money players.

The only layman's reason I or any other football fan could come up with is his **age**. As he grew old, clubs kept selling him for a bargain price and every single time he's proven himself the player he is. On some level, these clubs do regret not using him to his full potential. As mentioned in my other project, age is a big factor when it comes to the valuation of a player. Young players are usually valued higher than their older counterparts even if the said old player has proven himself. And that's been the case with Zlatan ever since his Barcelona exit. Even in 2012, when Paris Saint-Germain were drowning in newfound oil money, they got him below the market value price(€21 million). 

Another example is _Andrea Pirlo_; who played some of his best football when he moved from A.C. Milan to Juventus in 2011 on a free transfer at the age of 31. A.C. Milan didn't think that Pirlo could contribute anymore with him hitting the 30s and decided not to renew his contract. Juventus pounced on him and _il professore_ went on to play some scintillating, if not magical, football for _The Old Lady_.

I think this has been the case for Zlatan throughout his post-_Inter_ career. Every club he's been to, he's scored goals, won them acclodes and yet every future club decides he isn't worth the big bucks. Like I mentioned earlier, it could be his age, or the fact that he is a bit of a character to deal with in the dressing room...we may never know.

Therefore this simple project of mine is just me trying to analyse Zlatan Ibrahimović's club career with some charts and see how he has performed in each club he's played in.

_Just a small note before you proceed any further. His stats for Malmo are very inaccurate and lot of sources contradict each other on this. So I've decided to exclude Malmo from majority of my analysis. I'll point it out if I include them._

Before I go any further, here is a table summarising Zlatan's club career:

Club | Period(Months) | Market Value | Transfer Fee | Appearances | Minutes Played | Goals | Assists
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
Malmö FF | 30 | €0 | €0 | 47 | NA | 18 | 3
Ajax | 37 | €0 | €7,800,000 | 110 | 7193 | 48 | 15
Juventus | 23 |  €0 | €16,000,000 | 92 | 6867 | 26 | 7
Internazionale | 36 | €25,000,000 | €24,800,000 | 117 | 9712 | 66 | 29
Barcelona | 13 |  €45,000,000 | €69,500,000 | 46 | 3334 | 22 | 13
A.C. Milan(Loan) | 10 |  €35,000,000 | €0 | 41 | 3394 | 21 | 12
A.C. Milan | 12 | €35,000,000 | €24,000,000 | 44 | 3807 | 35 | 12
Paris Saint-Germain | 48 | €37,000,000 | €21,000,000 | 180 | 15090 | 156 | 60
Manchester United | 21 |  €15,000,000 | €0 | 53 | 4034 | 29 | 10
LA Galaxy | 21 | €5,000,000 | €0 | 58 | 4933 | 53 | 15
